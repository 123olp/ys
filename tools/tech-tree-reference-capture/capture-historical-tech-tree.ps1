[CmdletBinding()]
param(
    [string]$OutputRoot = 'D:\.projects\human-infra-reference-captures\historical-tech-tree',
    [string]$RunId = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ'),
    [ValidateRange(1, 8)]
    [int]$Concurrency = 4,
    [ValidateRange(1024, 65535)]
    [int]$Port = 18791
)

$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$baseUrl = 'https://www.historicaltechtree.com'
$runDir = Join-Path $OutputRoot $RunId
$rawDir = Join-Path $runDir 'raw'
$mirrorDir = Join-Path $runDir 'mirror'
$browserDir = Join-Path $runDir 'browser'
$evidenceDir = Join-Path $runDir 'evidence'
$tempDir = Join-Path $runDir 'runtime'
$downloadList = Join-Path $tempDir 'aria2-assets.txt'
$scriptRoot = $PSScriptRoot
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$sourceRepo = 'https://github.com/etiennefd/hhr-tech-tree.git'

if (Test-Path -LiteralPath $runDir) {
    throw "拒绝覆盖既有批次：$runDir"
}
New-Item -ItemType Directory -Force -Path $rawDir, $mirrorDir, $browserDir, $evidenceDir, $tempDir | Out-Null

$aria2 = Get-Command aria2c -ErrorAction SilentlyContinue
$node = Get-Command node -ErrorAction SilentlyContinue
$python = Get-Command python -ErrorAction SilentlyContinue
$git = Get-Command git -ErrorAction SilentlyContinue
if (-not $aria2) { throw '未找到 aria2c。请先执行 winget install aria2.aria2。' }
if (-not $node) { throw '未找到 Node.js。' }
if (-not $python) { throw '未找到 Python。' }
if (-not $git) { throw '未找到 Git。' }

function Save-Response {
    param(
        [string]$Url,
        [string]$RelativePath,
        [switch]$Optional
    )
    $target = Join-Path $rawDir $RelativePath
    $headerTarget = "$target.headers.json"
    New-Item -ItemType Directory -Force -Path (Split-Path $target -Parent) | Out-Null
    try {
        $response = Invoke-WebRequest -UseBasicParsing -Uri $Url -OutFile $target -PassThru -TimeoutSec 90
        $headerRecord = [ordered]@{
            url = $Url
            status = [int]$response.StatusCode
            content_type = [string]$response.Headers['Content-Type']
            etag = [string]$response.Headers['ETag']
            last_modified = [string]$response.Headers['Last-Modified']
            bytes = (Get-Item -LiteralPath $target).Length
        }
        [IO.File]::WriteAllText(
            $headerTarget,
            ($headerRecord | ConvertTo-Json -Depth 5),
            $utf8NoBom
        )
        return $true
    } catch {
        if ($Optional) {
            [IO.File]::WriteAllText(
                "$target.error.txt",
                $_.Exception.ToString(),
                $utf8NoBom
            )
            return $false
        }
        throw
    }
}

function Get-MirrorRelativePath {
    param([uri]$Uri)
    $decoded = [uri]::UnescapeDataString($Uri.AbsolutePath).TrimStart('/')
    if (-not $decoded) { return 'index.html' }
    if ($Uri.AbsolutePath.EndsWith('/')) { return ($decoded.TrimEnd('/') + '/index.html') }
    return $decoded
}

function Add-Asset {
    param(
        [System.Collections.Generic.Dictionary[string, string]]$Assets,
        [string]$Url,
        [switch]$AllowExternal
    )
    if (-not $Url) { return }
    $uri = [uri]$Url
    if ($uri.Scheme -notin @('http', 'https')) { return }
    if ($uri.Host -ne 'www.historicaltechtree.com' -and -not $AllowExternal) { return }
    $relative = Get-MirrorRelativePath $uri
    if ($uri.Host -ne 'www.historicaltechtree.com') {
        $relative = "external-assets/$($uri.Host)/$relative"
    }
    $Assets[$uri.GetLeftPart([System.UriPartial]::Path)] = $relative
}

try {
    # ==================== 保存原始核心响应 ====================
    $coreRoutes = @(
        @{ Url = "$baseUrl/"; Path = 'pages/index.html'; Mirror = 'index.html'; Optional = $false },
        @{ Url = "$baseUrl/about"; Path = 'pages/about.html'; Mirror = 'about/index.html'; Optional = $false },
        @{ Url = "$baseUrl/changelog"; Path = 'pages/changelog.html'; Mirror = 'changelog/index.html'; Optional = $false },
        @{ Url = "$baseUrl/image-credits"; Path = 'pages/image-credits.html'; Mirror = 'image-credits/index.html'; Optional = $true },
        @{ Url = "$baseUrl/mini-tree"; Path = 'pages/mini-tree.html'; Mirror = 'mini-tree/index.html'; Optional = $false },
        @{ Url = "$baseUrl/api/inventions"; Path = 'api/inventions.json'; Mirror = 'api/inventions'; Optional = $false },
        @{ Url = "$baseUrl/api/inventions?detail=true"; Path = 'api/inventions.detail.json'; Mirror = ''; Optional = $false },
        @{ Url = "$baseUrl/robots.txt"; Path = 'meta/robots.txt'; Mirror = 'robots.txt'; Optional = $true },
        @{ Url = "$baseUrl/sitemap.xml"; Path = 'meta/sitemap.xml'; Mirror = 'sitemap.xml'; Optional = $true },
        @{ Url = "$baseUrl/site.webmanifest"; Path = 'meta/site.webmanifest'; Mirror = 'site.webmanifest'; Optional = $false }
    )
    foreach ($route in $coreRoutes) {
        $saved = Save-Response -Url $route.Url -RelativePath $route.Path -Optional:$route.Optional
        if ($saved -and $route.Mirror) {
            $target = Join-Path $mirrorDir $route.Mirror
            New-Item -ItemType Directory -Force -Path (Split-Path $target -Parent) | Out-Null
            Copy-Item -LiteralPath (Join-Path $rawDir $route.Path) -Destination $target -Force
        }
    }

    # ==================== 用真实浏览器发现运行时资产 ====================
    & $node.Source `
        (Join-Path $scriptRoot 'historical-tech-tree-browser.mjs') `
        --mode discover `
        --url "$baseUrl/" `
        --output $browserDir
    if ($LASTEXITCODE -ne 0) { throw '在线 Chrome 资源发现或交互门禁失败。' }

    $api = Get-Content (Join-Path $rawDir 'api/inventions.json') -Raw -Encoding utf8 | ConvertFrom-Json
    $nodes = @($api.nodes)
    $links = @($api.links)
    if ($nodes.Count -lt 2400 -or $links.Count -lt 3700) {
        throw "图数据计数异常：nodes=$($nodes.Count), links=$($links.Count)"
    }
    $sampleNodeId = [string]$nodes[0].id
    if ($sampleNodeId) {
        $sampleSaved = Save-Response `
            -Url "$baseUrl/api/inventions/$sampleNodeId" `
            -RelativePath "api/samples/$sampleNodeId.json" `
            -Optional
        if ($sampleSaved) {
            $sampleTarget = Join-Path $mirrorDir "api/inventions/$sampleNodeId"
            New-Item -ItemType Directory -Force -Path (Split-Path $sampleTarget -Parent) | Out-Null
            Copy-Item `
                -LiteralPath (Join-Path $rawDir "api/samples/$sampleNodeId.json") `
                -Destination $sampleTarget `
                -Force
        }
    }

    # ==================== 生成确定性 aria2 清单 ====================
    $assets = [System.Collections.Generic.Dictionary[string, string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )
    $discover = Get-Content (Join-Path $browserDir 'discover-report.json') -Raw -Encoding utf8 | ConvertFrom-Json
    foreach ($resource in $discover.resources) {
        Add-Asset -Assets $assets -Url ([string]$resource.url)
    }
    foreach ($nodeItem in $nodes) {
        if ($nodeItem.localImage) {
            $imageUri = [uri]::new([uri]"$baseUrl/", [string]$nodeItem.localImage)
            Add-Asset -Assets $assets -Url $imageUri.AbsoluteUri -AllowExternal
        }
    }
    foreach ($route in $coreRoutes) {
        if ($route.Mirror) {
            $routeUri = [uri]$route.Url
            $assets[$routeUri.GetLeftPart([System.UriPartial]::Path)] = $route.Mirror
        }
    }
    foreach ($fixedAsset in @(
        '/placeholder-invention.jpg',
        '/tool-in-situ-being-unearthed-at-excavation_3_edit.jpg',
        '/favicon.ico',
        '/favicon.svg',
        '/favicon-16x16.png',
        '/favicon-32x32.png',
        '/apple-touch-icon.png',
        '/android-chrome-192x192.png',
        '/android-chrome-512x512.png',
        '/og-image.png'
    )) {
        $assetUri = [uri]::new([uri]"$baseUrl/", $fixedAsset)
        Add-Asset -Assets $assets -Url $assetUri.AbsoluteUri
    }

    $ariaLines = [System.Collections.Generic.List[string]]::new()
    foreach ($entry in $assets.GetEnumerator() | Sort-Object Key) {
        $target = Join-Path $mirrorDir $entry.Value
        New-Item -ItemType Directory -Force -Path (Split-Path $target -Parent) | Out-Null
        $ariaLines.Add($entry.Key)
        $ariaLines.Add("  dir=$(Split-Path $target -Parent)")
        $ariaLines.Add("  out=$(Split-Path $target -Leaf)")
    }
    [IO.File]::WriteAllLines($downloadList, $ariaLines, $utf8NoBom)

    & $aria2.Source `
        --input-file=$downloadList `
        --max-concurrent-downloads=$Concurrency `
        --split=1 `
        --max-tries=4 `
        --retry-wait=3 `
        --connect-timeout=30 `
        --timeout=90 `
        --allow-overwrite=true `
        --auto-file-renaming=false `
        --console-log-level=warn `
        --summary-interval=0 `
        --file-allocation=none
    if ($LASTEXITCODE -ne 0) { throw "aria2c 下载失败，退出码：$LASTEXITCODE。" }

    # 核心 API 必须保留无扩展名路径，避免本地运行时请求失配。
    Copy-Item (Join-Path $rawDir 'api/inventions.json') (Join-Path $mirrorDir 'api/inventions') -Force

    # API 中偶尔存在伪装为 localImage 的外部绝对 URL；镜像副本必须改写为本地闭合路径。
    $externalAssetMap = [ordered]@{}
    foreach ($nodeItem in $nodes) {
        if (-not $nodeItem.localImage) { continue }
        $imageUri = [uri]::new([uri]"$baseUrl/", [string]$nodeItem.localImage)
        if ($imageUri.Host -eq 'www.historicaltechtree.com') { continue }
        $relative = "external-assets/$($imageUri.Host)/$(Get-MirrorRelativePath $imageUri)"
        $externalAssetMap[$imageUri.AbsoluteUri] = "/$relative"
        $nodeItem.localImage = "/$relative"
    }
    if ($externalAssetMap.Count -gt 0) {
        [IO.File]::WriteAllText(
            (Join-Path $mirrorDir 'api/inventions'),
            (@{ nodes = $nodes; links = $links } | ConvertTo-Json -Depth 20 -Compress),
            $utf8NoBom
        )
        [IO.File]::WriteAllText(
            (Join-Path $evidenceDir 'external-asset-map.json'),
            ($externalAssetMap | ConvertTo-Json -Depth 5),
            $utf8NoBom
        )
    }

    # ==================== 保存公开源码与许可边界 ====================
    $sourceCodeDir = Join-Path $runDir 'source-code'
    & $git.Source clone --depth 1 $sourceRepo $sourceCodeDir
    if ($LASTEXITCODE -ne 0) { throw '公开源码仓库克隆失败。' }
    $sourceCommit = (& $git.Source -C $sourceCodeDir rev-parse HEAD).Trim()
    Remove-Item -LiteralPath (Join-Path $sourceCodeDir '.git') -Recurse -Force
    $licenseBoundary = [ordered]@{
        source_repository = $sourceRepo
        source_commit = $sourceCommit
        code_license = 'MIT, subject to the repository LICENSE'
        dataset_license = 'Not covered by the MIT license; upstream reserves rights'
        image_license = 'Per-image review required through /image-credits and original source'
        local_snapshot_use = 'Research and comparison only; do not redistribute as an open dataset'
    }
    [IO.File]::WriteAllText(
        (Join-Path $evidenceDir 'license-boundary.json'),
        ($licenseBoundary | ConvertTo-Json -Depth 5),
        $utf8NoBom
    )

    # ==================== 本地重放和浏览器门禁 ====================
    $serverLog = Join-Path $tempDir 'http-server.log'
    $serverError = Join-Path $tempDir 'http-server.error.log'
    $server = Start-Process `
        -FilePath $python.Source `
        -ArgumentList '-m', 'http.server', "$Port", '--bind', '127.0.0.1', '--directory', $mirrorDir `
        -PassThru `
        -WindowStyle Hidden `
        -RedirectStandardOutput $serverLog `
        -RedirectStandardError $serverError
    try {
        $ready = $false
        for ($attempt = 0; $attempt -lt 40; $attempt++) {
            try {
                $probe = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:$Port/" -TimeoutSec 2
                if ($probe.StatusCode -eq 200) { $ready = $true; break }
            } catch {
                Start-Sleep -Milliseconds 250
            }
        }
        if (-not $ready) { throw "本地 HTTP 服务未就绪，日志：$serverError" }

        $offlineBrowserDir = Join-Path $browserDir 'offline'
        & $node.Source `
            (Join-Path $scriptRoot 'historical-tech-tree-browser.mjs') `
            --mode verify `
            --url "http://127.0.0.1:$Port/" `
            --output $offlineBrowserDir
        if ($LASTEXITCODE -ne 0) { throw '离线 Chrome 交互门禁失败。' }
    } finally {
        if ($server -and -not $server.HasExited) {
            Stop-Process -Id $server.Id -Force
            $server.WaitForExit()
        }
    }

    # ==================== 数据、资源闭合和哈希审计 ====================
    & $python.Source `
        (Join-Path $scriptRoot 'verify_historical_capture.py') `
        --run-dir $runDir
    if ($LASTEXITCODE -ne 0) { throw 'Historical Tech Tree 完整性审计失败。' }

    $archivePath = Join-Path $OutputRoot "historical-tech-tree-$RunId.zip"
    $archiveEvidencePath = "$archivePath.sha256.json"
    $result = [ordered]@{
        verdict = 'PASS'
        run_id = $RunId
        run_dir = $runDir
        archive = $archivePath
        archive_hash_record = $archiveEvidencePath
        graph = [ordered]@{
            nodes = $nodes.Count
            links = $links.Count
        }
        requested_assets = $assets.Count
        source_commit = $sourceCommit
    }
    [IO.File]::WriteAllText(
        (Join-Path $evidenceDir 'capture-result.json'),
        ($result | ConvertTo-Json -Depth 8),
        $utf8NoBom
    )
    Compress-Archive -Path $runDir -DestinationPath $archivePath -CompressionLevel Optimal
    $archiveEvidence = [ordered]@{
        archive = $archivePath
        archive_bytes = (Get-Item -LiteralPath $archivePath).Length
        archive_sha256 = (Get-FileHash -LiteralPath $archivePath -Algorithm SHA256).Hash.ToLowerInvariant()
    }
    [IO.File]::WriteAllText(
        $archiveEvidencePath,
        ($archiveEvidence | ConvertTo-Json -Depth 5),
        $utf8NoBom
    )
    [ordered]@{
        capture = $result
        archive_evidence = $archiveEvidence
    } | ConvertTo-Json -Depth 8
} catch {
    $failure = [ordered]@{
        verdict = 'BLOCK'
        run_id = $RunId
        run_dir = $runDir
        error = $_.Exception.ToString()
    }
    [IO.File]::WriteAllText(
        (Join-Path $evidenceDir 'capture-result.json'),
        ($failure | ConvertTo-Json -Depth 8),
        $utf8NoBom
    )
    throw
}
