#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

required=(
    AGENTS.md
    README.md
    CONTENT-STANDARD.md
    ROUTING-CONTRACT.md
    LANGUAGE-EDITION-CONTRACT.md
    HOMEPAGE-PORTAL-CONTRACT.md
    homepage-upstream/UPSTREAM.md
    homepage-upstream/snapshot/metadata.json
    homepage-upstream/snapshot/Wikipedia_Home.wiki
    homepage-upstream/snapshot/Wikipedia_Home_banner.wiki
    homepage-upstream/snapshot/Wikipedia_Home_styles.css
    homepage-upstream/snapshot/Wikipedia_Home_rendered.html
    Dockerfile
    compose.yaml
    env.example
    config/HumanInfraSettings.php
    docker/entrypoint.sh
    portal/index.html
    portal/adapter.js
    portal/UPSTREAM.md
    portal/LICENSE.wikimedia-portals
    portal/languages.json
    portal/default.conf.template
    portal/assets/human-infra-mark.svg
    portal/assets/human-infra-wordmark.svg
    scripts/refresh-wikipedia-portal.py
    scripts/refresh-wikipedia-homepage.py
    scripts/build-wikipedia-homepage.py
    scripts/run-backstop.sh
    visual-regression/backstop.contract.json
    visual-regression/backstop.wikipedia.json
    visual-regression/engine_scripts/onReady.js
    visual-regression/engine_scripts/onReadyContract.js
    content/manifest.tsv
)

for file in "${required[@]}"; do
    [[ -s "$file" ]] || {
        printf '缺失或为空: %s\n' "$file" >&2
        exit 1
    }
done

python3 - <<'PY'
import json
from pathlib import Path

for filename in ("backstop.contract.json", "backstop.wikipedia.json"):
    config = json.loads(
        Path("visual-regression", filename).read_text(encoding="utf-8")
    )
    if config.get("engine") != "playwright":
        raise SystemExit(f"{filename}: BackstopJS 必须使用 Playwright 引擎")
    if config.get("report") != ["browser", "CI"]:
        raise SystemExit(f"{filename}: 必须同时生成浏览器与 CI 报告")
    if not config.get("scenarios"):
        raise SystemExit(f"{filename}: 缺少视觉回归场景")
    for scenario in config["scenarios"]:
        if scenario.get("misMatchThreshold") != 0:
            raise SystemExit(
                f"{filename}: 场景未使用零像素差异阈值: {scenario.get('label')}"
            )
        if scenario.get("requireSameDimensions") is not True:
            raise SystemExit(
                f"{filename}: 场景未要求相同尺寸: {scenario.get('label')}"
            )

contract = json.loads(
    Path("visual-regression/backstop.contract.json").read_text(encoding="utf-8")
)
reference_path = contract.get("paths", {}).get("bitmaps_reference")
if reference_path != "visual-regression/bitmaps_reference":
    raise SystemExit("模板契约参考图必须保存在受版本控制的 visual-regression 目录")

expected_references = len(contract["viewports"]) * sum(
    len(scenario["selectors"]) for scenario in contract["scenarios"]
)
actual_references = len(list(Path(reference_path).glob("*.png")))
if actual_references != expected_references:
    raise SystemExit(
        f"模板契约参考图不完整: expected={expected_references}, "
        f"actual={actual_references}"
    )
PY

python3 scripts/build-wikipedia-homepage.py --check

grep -Fq 'class="central-featured"' portal/index.html || {
    printf '语言门户缺少 Wikimedia central-featured DOM 契约。\n' >&2
    exit 1
}
grep -Fq 'class="search-container"' portal/index.html || {
    printf '语言门户缺少 Wikimedia search-container DOM 契约。\n' >&2
    exit 1
}
grep -Fq 'data-hi-language="zh"' portal/index.html || {
    printf '语言门户缺少中文路由锚点。\n' >&2
    exit 1
}
[[ ! -e portal/styles.css ]] || {
    printf '禁止用本地 styles.css 覆盖 Wikimedia 官方门户视觉层。\n' >&2
    exit 1
}
python3 - <<'PY'
import re
from pathlib import Path

manifest_titles = {
    line.split("\t", 1)[0]
    for line in Path("content/manifest.tsv").read_text(encoding="utf-8").splitlines()
    if line and not line.startswith("#")
}
portal_html = Path("portal/index.html").read_text(encoding="utf-8")
portal_titles = set(re.findall(r'data-hi-title="([^"]+)"', portal_html))
missing_titles = sorted(portal_titles - manifest_titles)
if missing_titles:
    raise SystemExit(f"语言门户存在未入库的 Wiki 目标: {missing_titles}")

local_assets = set(
    re.findall(r'(?:src|href)="(assets/[^"]+)"', portal_html)
    + re.findall(r'url\((assets/[^)]+)\)', portal_html)
)
missing_assets = sorted(
    asset for asset in local_assets if not Path("portal", asset).is_file()
)
if missing_assets:
    raise SystemExit(f"语言门户缺少本地化上游资源: {missing_assets}")
PY

declare -A titles=()
while IFS=$'\t' read -r title file; do
    [[ -n "$title" && "${title:0:1}" != "#" ]] || continue
    [[ -f "content/$file" ]] || {
        printf 'manifest 文件缺失: %s\n' "$file" >&2
        exit 1
    }
    [[ -z "${titles[$title]:-}" ]] || {
        printf 'manifest 标题重复: %s\n' "$title" >&2
        exit 1
    }
    titles["$title"]=1
done < content/manifest.tsv

for title in \
    'MediaWiki:Mainpage' \
    'MediaWiki:Common.css' \
    'Human Infra:首页' \
    'Template:首页/styles.css' \
    'Portal:永生与主体持续性' \
    'Portal:衰老机制与长寿科学' \
    'Portal:身体替代与人体增强' \
    'Portal:脑、记忆与主体连续性' \
    'Portal:AI与自动化科学' \
    'Portal:未来等待' \
    'Portal:治理、风险与公平'; do
    [[ -n "${titles[$title]:-}" ]] || {
        printf '缺少受治理关键页面: %s\n' "$title" >&2
        exit 1
    }
done

grep -Fq '<div id="mp-2012">' content/Human_Infra_Main_Page.wiki || {
    printf '中文首页缺少中文维基百科 mp-2012 根 DOM 契约。\n' >&2
    exit 1
}
for contract in mp-2012-banner mp-2012-column-left mp-2012-column-right mp-2012-links; do
    grep -Fq "id=\"$contract\"" content/Human_Infra_Main_Page.wiki content/Template_Home_Header.wiki || {
        printf '中文首页缺少上游 DOM 契约: %s\n' "$contract" >&2
        exit 1
    }
done
for contract in column-feature column-dyk column-good column-itn column-otd column-uptrends column-participate column-tips; do
    grep -Fq "id=\"$contract\"" content/Human_Infra_Main_Page.wiki || {
        printf '中文首页缺少官方内容容器契约: %s\n' "$contract" >&2
        exit 1
    }
done

python3 - <<'PY'
import json
from pathlib import Path

registry = json.loads(Path("portal/languages.json").read_text(encoding="utf-8"))
languages = registry.get("languages", [])
codes = [item.get("code") for item in languages]
if len(codes) != len(set(codes)):
    raise SystemExit("语言注册表存在重复 code")

available = [item for item in languages if item.get("status") == "available"]
if not any(item.get("code") == "zh" for item in available):
    raise SystemExit("中文语言版本必须保持 available")

for item in languages:
    if item.get("status") not in {"available", "planned"}:
        raise SystemExit(f"无效语言状态: {item.get('status')}")
    if item.get("status") == "planned" and item.get("origin"):
        raise SystemExit(f"筹备语言不得提供可用 origin: {item.get('code')}")
PY

if [[ -f .env ]]; then
    docker compose --env-file .env config --quiet
else
    cp env.example .env.validation
    trap 'rm -f .env.validation' EXIT
    docker compose --env-file .env.validation config --quiet
fi

printf 'Wiki source contract: PASS\n'
