# 科技树候选采集工具

该工具组合成熟能力完成候选参考采集：

- `wget --warc-file` 保存 HTTP 响应与 WARC。
- `wget --page-requisites` 保存公开页面及直接依赖。
- Headless Chrome 保存 JavaScript 渲染后的 DOM 和长截图。
- `sha256sum` 生成完整性清单。

选定的 Historical Tech Tree 使用更严格的 Windows 固定资源工作流：公开 API 抽取、Chrome/CDP 动态资源发现、aria2 清单抓取、离线依赖闭合和 Chrome 交互门禁。完整契约见 `CAPTURE-CONTRACT.md`。

## 使用

```bash
bash tools/tech-tree-reference-capture/capture.sh
```

指定代理、单个候选或跳过浏览器：

```bash
CAPTURE_PROXY=http://host:7890 CAPTURE_ONLY=calitree \
  bash tools/tech-tree-reference-capture/capture.sh

CAPTURE_BROWSER=0 bash tools/tech-tree-reference-capture/capture.sh
```

输出进入 `build/reference-captures/tech-tree/<run-id>/<candidate-id>/`，包括 `mirror/`、`rendered.html`、`screenshot.png`、`network.warc.gz`、`capture.log` 和 `SHA256SUMS`。每次运行使用新的 UTC 批次目录，不覆盖旧证据。原始网页只供本地比较研究，不进入 Git，也不授予复用第三方资产的权利。

## 候选浏览器

```bash
python3 -m http.server 18779 --bind 0.0.0.0
```

打开 `http://localhost:18779/tools/tech-tree-reference-capture/viewer/`。左侧切换全部候选，中间加载原站，右侧显示适配度与复用边界。若外站通过 CSP 或 `X-Frame-Options` 禁止内嵌，使用“新窗口打开”。

受限环境不能监听端口时，可生成并直接打开自包含页面：

```bash
python3 tools/tech-tree-reference-capture/build_standalone_viewer.py
```

输出为 `build/reference-captures/tech-tree/viewer/index.html`。

## Historical Tech Tree 完整镜像

在 Windows PowerShell 中执行：

```powershell
powershell -ExecutionPolicy Bypass -File `
  "<wsl-home>\.projects\human_infra\tools\tech-tree-reference-capture\capture-historical-tech-tree.ps1"
```

默认输出：

```text
D:\.projects\human-infra-reference-captures\historical-tech-tree\<run-id>\
```

命令会抓取真实站点页面、公开图数据、API 声明的全部本地技术图片和浏览器发现的运行时资产，随后执行结构审计、本地 HTTP 重放、Chrome 交互门禁、逐文件 SHA-256 和 ZIP 打包。可用 `-OutputRoot`、`-RunId`、`-Concurrency` 和 `-Port` 调整运行参数。

哲学知识图谱的旧快照仅用于证明 Windows 抓取工作流可用，不属于 Historical Tech Tree 内容。需要归档该参考批次时执行：

```bash
python3 tools/tech-tree-reference-capture/import_workflow_reference.py
```
