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
    PAGES-PUBLISHING-CONTRACT.md
    homepage-upstream/UPSTREAM.md
    homepage-upstream/snapshot/metadata.json
    homepage-upstream/snapshot/Wikipedia_Home.wiki
    homepage-upstream/snapshot/Wikipedia_Home_banner.wiki
    homepage-upstream/snapshot/Wikipedia_Home_styles.css
    homepage-upstream/snapshot/Wikipedia_Home_rendered.html
    homepage-upstream/snapshot/Wikipedia_Home_language_links.json
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
    portal/assets/human-infra-tech-tree.png
    scripts/refresh-wikipedia-portal.py
    scripts/refresh-wikipedia-homepage.py
    scripts/build-wikipedia-homepage.py
    scripts/export-pages-snapshot.py
    scripts/build-pages-release.sh
    scripts/deploy-pages-release.sh
    scripts/smoke-pages-release.sh
    pages/wiki-worker.js
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

python3 - <<'PY'
from pathlib import Path

source = Path("content/Template_Home_Related_Projects.wiki").read_text(
    encoding="utf-8"
)
if 'class="plainlinks noresize"' not in source:
    raise SystemExit("首页关联项目未复用 Wikipediasister 表格契约")
if source.count("[[File:Human-Infra-mark.svg") < 9:
    raise SystemExit("首页关联项目缺少顶部标志或八个入口标志")

templates = {
    "research_map": Path("content/Template_Home_Research_Map.wiki").read_text(
        encoding="utf-8"
    ),
    "current_focus": Path("content/Template_Home_Current_Focus.wiki").read_text(
        encoding="utf-8"
    ),
    "participate": Path("content/Template_Home_Participate.wiki").read_text(
        encoding="utf-8"
    ),
    "reminder": Path("content/Template_Home_Reminder.wiki").read_text(
        encoding="utf-8"
    ),
    "site_links": Path("content/Template_Home_Site_Links.wiki").read_text(
        encoding="utf-8"
    ),
}
if "[[File:Human-Infra-tech-tree.png" not in templates["research_map"]:
    raise SystemExit("首页研究图谱未提供原生 MediaWiki 图片内容")
if sum(
    line.startswith("* ")
    for line in templates["current_focus"].splitlines()
) < 8:
    raise SystemExit("首页当前重点内容密度不足")
for name in ("participate", "reminder"):
    if "[[File:Human-Infra-mark.svg|70px|right" not in templates[name]:
        raise SystemExit(f"首页 {name} 未复用上游右侧 70px 图片结构")
if sum(
    line.startswith("* ")
    for line in templates["site_links"].splitlines()
) < 15:
    raise SystemExit("首页站点链接未达到上游三列十五项结构")
PY

grep -Fq 'resources/assets/licenses/cc-by-sa.png' config/HumanInfraSettings.php || {
    printf '站点未配置 MediaWiki 内置 CC BY-SA 许可证图标。\n' >&2
    exit 1
}
grep -Fq 'resources/assets/human-infra-mark.svg' config/HumanInfraSettings.php || {
    printf '站点未配置本地 Human Infra 品牌资源。\n' >&2
    exit 1
}
grep -Fq "wfLoadExtension( 'UniversalLanguageSelector' );" config/HumanInfraSettings.php || {
    printf '站点未启用 MediaWiki 官方 UniversalLanguageSelector 扩展。\n' >&2
    exit 1
}
grep -Fq "\$wgULSPosition = 'interlanguage';" config/HumanInfraSettings.php || {
    printf 'UniversalLanguageSelector 未使用官方 interlanguage 入口。\n' >&2
    exit 1
}
grep -Fq 'UniversalLanguageSelector/archive/${ULS_COMMIT}.tar.gz' Dockerfile || {
    printf 'Wiki 镜像未固定安装官方 UniversalLanguageSelector。\n' >&2
    exit 1
}
grep -Fq 'maintenance/run.php populateInterwiki' scripts/bootstrap.sh || {
    printf '启动流程未使用 MediaWiki 核心 populateInterwiki 建立语言前缀。\n' >&2
    exit 1
}
grep -Fq 'human-infra-mark.svg:/var/www/html/resources/assets/human-infra-mark.svg:ro' compose.yaml || {
    printf 'Wiki 服务未只读挂载 Human Infra 品牌资源。\n' >&2
    exit 1
}
grep -Fq 'seed-assets/Human-Infra-mark.svg:ro' compose.yaml || {
    printf 'Wiki 服务未挂载可复现的 MediaWiki 品牌种子文件。\n' >&2
    exit 1
}
grep -Fq 'seed-assets/Human-Infra-tech-tree.png:ro' compose.yaml || {
    printf 'Wiki 服务未挂载可复现的科技树图片种子文件。\n' >&2
    exit 1
}
grep -Fq "printf '%s\\n' 'Human Infra:首页'" scripts/import-content.sh || {
    printf '内容导入流程未按 MediaWiki 1.46 契约刷新首页解析缓存。\n' >&2
    exit 1
}

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
    'Category:Human Infra Wiki' \
    'Category:模板' \
    'Category:信息框模板' \
    'Category:首页模板' \
    'Category:隐藏分类' \
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

python3 - <<'PY'
import re
from pathlib import Path

content_dir = Path("content")
manifest_entries = {
    title: filename
    for title, filename in (
        line.split("\t", 1)
        for line in (content_dir / "manifest.tsv").read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    )
}
manifest_titles = set(manifest_entries)

category_parents = {}
for title, filename in manifest_entries.items():
    if not title.startswith("Category:"):
        continue
    source = (content_dir / filename).read_text(encoding="utf-8")
    if re.search(r"(?m)^=\s*Category:", source):
        raise SystemExit(f"分类页不得在正文重复页面标题: {filename}")
    category_parents[title] = {
        f"Category:{parent.strip()}"
        for parent in re.findall(r"\[\[Category:([^\]|]+)", source)
    }

root_category = "Category:Human Infra Wiki"
def verify_category_path(title, trail):
    if title == root_category:
        return
    if title in trail:
        cycle = " -> ".join((*trail, title))
        raise SystemExit(f"分类层级存在循环: {cycle}")
    parents = category_parents.get(title, set())
    if not parents:
        raise SystemExit(f"分类无法追溯到顶级分类: {title}")
    unknown = sorted(parent for parent in parents if parent not in category_parents)
    if unknown:
        raise SystemExit(f"分类引用未治理父分类 {title}: {unknown}")
    for parent in parents:
        verify_category_path(parent, (*trail, title))


for title in category_parents:
    verify_category_path(title, ())

base_categories = (
    "Category_Evidence_source.wiki",
    "Category_Fiction_reference.wiki",
    "Category_Portals.wiki",
    "Category_Research_domain.wiki",
    "Category_Technology_node.wiki",
    "Category_Topic.wiki",
)
for filename in base_categories:
    source = (content_dir / filename).read_text(encoding="utf-8")
    if "[[Category:Human Infra Wiki]]" not in source:
        raise SystemExit(f"基础分类未接入单一顶级分类: {filename}")

for filename in (
    "Template_Research_domain.wiki",
    "Template_Technology_node.wiki",
    "Template_Evidence_source.wiki",
):
    source = (content_dir / filename).read_text(encoding="utf-8")
    noinclude = source.partition("<noinclude>")[2]
    if "[[Category:信息框模板]]" not in noinclude:
        raise SystemExit(f"信息框模板缺少模板页维护分类: {filename}")

common_css = (content_dir / "MediaWiki_Common_css.wiki").read_text(encoding="utf-8")
if ".hi-portal" in common_css:
    raise SystemExit("Portal 禁止使用项目私有平行布局 CSS。")

required_sections = {
    "Portal_Immortality.wiki": ("概览", "精选条目", "研究路线", "证据与反证", "参与建设", "相关门户"),
    "Portal_Aging_Longevity.wiki": ("概览", "精选研究", "技术路线", "证据与边界", "开放问题", "参与建设", "相关门户"),
    "Portal_Body_Augmentation.wiki": ("概览", "精选研究", "功能替代", "证据与边界", "开放问题", "参与建设", "相关门户"),
    "Portal_Brain_Memory.wiki": ("概览", "精选研究", "技术与测量", "证据与边界", "开放问题", "参与建设", "相关门户"),
    "Portal_AI_Science.wiki": ("概览", "精选研究", "能力阶梯", "证据与边界", "开放问题", "参与建设", "相关门户"),
    "Portal_Future_Waiting.wiki": ("概览", "精选研究", "候选路径", "证据与边界", "开放问题", "参与建设", "相关门户"),
    "Portal_Governance.wiki": ("概览", "精选研究", "治理对象", "内容与证据治理", "开放问题", "参与建设", "相关门户"),
}
for filename, sections in required_sections.items():
    source = (content_dir / filename).read_text(encoding="utf-8")
    if "hi-portal" in source:
        raise SystemExit(f"Portal 仍依赖项目私有布局类: {filename}")
    if re.search(r"(?m)^=\s+[^=].*\s+=$", source):
        raise SystemExit(f"Portal 不得在正文重复页面标题: {filename}")
    for section in sections:
        if f"== {section} ==" not in source:
            raise SystemExit(f"Portal 缺少标准内容槽 {section}: {filename}")
    links = {
        match.strip()
        for match in re.findall(r"\[\[([^\]|#]+)", source)
        if not match.startswith(("File:", "Category:"))
    }
    if len(links) < 10:
        raise SystemExit(f"Portal 内部导航密度不足: {filename}")
    missing = sorted(link for link in links if link not in manifest_titles)
    if missing:
        raise SystemExit(f"Portal 存在未治理内部链接 {filename}: {missing}")
PY

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

language_links = json.loads(
    Path(
        "homepage-upstream/snapshot/Wikipedia_Home_language_links.json"
    ).read_text(encoding="utf-8")
)
metadata = json.loads(
    Path("homepage-upstream/snapshot/metadata.json").read_text(encoding="utf-8")
)
expected = metadata["language_links"]["count"]
if len(language_links) != expected:
    raise SystemExit(
        f"首页官方语言链接快照不完整: expected={expected}, "
        f"actual={len(language_links)}"
    )
codes = [item["lang"] for item in language_links]
if len(codes) != len(set(codes)):
    raise SystemExit("首页官方语言链接快照存在重复语言代码")
PY

if [[ -f .env ]]; then
    docker compose --env-file .env config --quiet
else
    cp env.example .env.validation
    trap 'rm -f .env.validation' EXIT
    docker compose --env-file .env.validation config --quiet
fi

printf 'Wiki source contract: PASS\n'
