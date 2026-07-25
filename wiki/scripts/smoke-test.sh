#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

set -a
# shellcheck disable=SC1091
source .env
set +a

base_url="${WIKI_SERVER%/}"
portal_url="${WIKI_PORTAL_URL:-http://localhost:18784}"
portal_url="${portal_url%/}"

curl -fsS "$portal_url/healthz" | grep -Fq 'ok'
portal_html="$(curl -fsS "$portal_url/")"
grep -Fq 'Human Infra' <<<"$portal_html"
grep -Fq 'class="central-featured"' <<<"$portal_html"
grep -Fq 'class="search-container"' <<<"$portal_html"
grep -Fq 'data-hi-language="zh"' <<<"$portal_html"
curl -fsS "$portal_url/adapter.js" | grep -Fq 'HUMAN_INFRA_PORTAL'
curl -fsS "$portal_url/UPSTREAM.md" | grep -Fq 'wikimedia/portals'

printf '等待 Wiki HTTP 就绪'
for _ in $(seq 1 60); do
    if curl -fsS "$base_url/api.php?action=query&meta=siteinfo&format=json" >/dev/null 2>&1; then
        printf '\n'
        break
    fi
    printf '.'
    sleep 2
done

siteinfo="$(curl -fsS "$base_url/api.php?action=query&meta=siteinfo&format=json")"
python3 -c '
import json
import sys

general = json.load(sys.stdin)["query"]["general"]
assert general["sitename"] == "Human Infra Wiki"
assert general["mainpage"] == "Human Infra:首页"
' <<<"$siteinfo"

namespaces="$(curl -fsS "$base_url/api.php?action=query&meta=siteinfo&siprop=namespaces&format=json")"
grep -Fq '"100":{"id":100,"case":"first-letter","canonical":"Portal"' <<<"$namespaces" || {
    printf 'Portal 命名空间不可用。\n' >&2
    exit 1
}

extensions="$(curl -fsS "$base_url/api.php?action=query&meta=siteinfo&siprop=extensions&format=json")"
for extension in Cite ParserFunctions TemplateStyles VisualEditor PageForms; do
    grep -Fq "\"name\":\"$extension\"" <<<"$extensions" || {
        printf '缺少扩展: %s\n' "$extension" >&2
        exit 1
    }
done

pages="$(curl -fsS --get "$base_url/api.php" \
    --data-urlencode 'action=query' \
    --data-urlencode 'titles=Human Infra:首页|Portal:永生与主体持续性|Form:研究域|Form:技术节点|Form:证据来源' \
    --data-urlencode 'format=json')"
if grep -Fq '"missing":true' <<<"$pages"; then
    printf '关键种子页面缺失。\n' >&2
    exit 1
fi

main_page="$(curl -fsS --get "$base_url/index.php" \
    --data-urlencode 'title=Human Infra:首页' \
    --data-urlencode 'action=raw')"
grep -Fq '<div id="mp-2012">' <<<"$main_page" || {
    printf '首页未加载 Human Infra 种子内容。\n' >&2
    exit 1
}

rendered_main_page="$(curl -fsS "$base_url/")"
for contract in 'id="mp-2012-banner"' 'id="mp-2012-column-left"' 'id="mp-2012-column-right"' 'id="mp-2012-links"'; do
    grep -Fq "$contract" <<<"$rendered_main_page" || {
        printf '中文项目首页缺少上游 DOM 契约: %s\n' "$contract" >&2
        exit 1
    }
done
python3 -c '
import re
import sys

page = sys.stdin.read()
match = re.search(
    r"<div id=\"mp-2012-sisters\"[^>]*>(.*?)</table>",
    page,
    re.DOTALL,
)
if not match:
    raise SystemExit("中文项目首页缺少完整关联项目表格。")
fragment = match.group(1)
if "plainlinks noresize" not in fragment or fragment.count("<a ") < 16:
    raise SystemExit("中文项目首页关联项目组件内容密度不足。")
' <<<"$rendered_main_page"
grep -Fq '典范研究' <<<"$rendered_main_page" || {
    printf '中文项目首页内容未渲染。\n' >&2
    exit 1
}
if grep -Eq '<img[^>]+src=""' <<<"$rendered_main_page"; then
    printf '中文项目首页存在空图片地址。\n' >&2
    exit 1
fi
if grep -Fq 'MediaWiki_logo_reworked' <<<"$rendered_main_page"; then
    printf '中文项目首页仍引用外部 MediaWiki 占位品牌。\n' >&2
    exit 1
fi
grep -Fq '/resources/assets/human-infra-mark.svg' <<<"$rendered_main_page" || {
    printf '中文项目首页未使用本地 Human Infra 品牌资源。\n' >&2
    exit 1
}
grep -Fq 'Human-Infra-mark.svg' <<<"$rendered_main_page" || {
    printf '中文项目首页横幅未使用 MediaWiki 本地文件仓库中的品牌资源。\n' >&2
    exit 1
}
brand_media_path="$(
    grep -oE 'src="[^"]*Human-Infra-mark\.svg"' <<<"$rendered_main_page" \
        | head -n 1 \
        | cut -d '"' -f 2
)"
[[ -n "$brand_media_path" ]] && curl -fsS -o /dev/null \
    "${base_url}${brand_media_path}" || {
    printf 'MediaWiki 本地文件仓库中的 Human Infra 品牌资源不可用。\n' >&2
    exit 1
}
curl -fsS -o /dev/null \
    "$base_url/resources/assets/human-infra-mark.svg" || {
    printf 'Human Infra 品牌资源不可用。\n' >&2
    exit 1
}
curl -fsS -o /dev/null \
    "$base_url/resources/assets/licenses/cc-by-sa.png" || {
    printf 'CC BY-SA 许可证图标不可用。\n' >&2
    exit 1
}

for form in 研究域 技术节点 证据来源; do
    form_source="$(curl -fsS --get "$base_url/index.php" \
        --data-urlencode "title=Form:$form" \
        --data-urlencode 'action=raw')"
    grep -Fq 'for template' <<<"$form_source" || {
        printf '表单定义不可用: %s\n' "$form" >&2
        exit 1
    }
done

docker compose --env-file .env exec -T db healthcheck.sh --connect --innodb_initialized >/dev/null
printf 'Wiki smoke test: PASS\n'
