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
    --data-urlencode 'titles=Human Infra:首页|Portal:永生与主体持续性|Category:Human Infra Wiki|Category:首页模板|Form:研究域|Form:技术节点|Form:证据来源' \
    --data-urlencode 'format=json')"
if grep -Fq '"missing":true' <<<"$pages"; then
    printf '关键种子页面缺失。\n' >&2
    exit 1
fi

for query_page in Wantedpages Wantedtemplates Wantedcategories; do
    query_result="$(curl -fsS --get "$base_url/api.php" \
        --data-urlencode 'action=query' \
        --data-urlencode 'list=querypage' \
        --data-urlencode "qppage=$query_page" \
        --data-urlencode 'qplimit=max' \
        --data-urlencode 'format=json')"
    python3 -c '
import json
import sys

page_name = sys.argv[1]
results = json.load(sys.stdin)["query"]["querypage"]["results"]
if results:
    titles = [result.get("title", result.get("value")) for result in results]
    raise SystemExit(f"{page_name} 仍有缺失项: {titles}")
' "$query_page" <<<"$query_result"
done

for portal in \
    '永生与主体持续性' \
    '衰老机制与长寿科学' \
    '身体替代与人体增强' \
    '脑、记忆与主体连续性' \
    'AI与自动化科学' \
    '未来等待' \
    '治理、风险与公平'; do
    rendered_portal="$(curl -fsS --get "$base_url/index.php" \
        --data-urlencode "title=Portal:$portal")"
    grep -Fq '参与建设' <<<"$rendered_portal" || {
        printf '专题门户缺少参与建设内容槽: %s\n' "$portal" >&2
        exit 1
    }
    grep -Fq '相关门户' <<<"$rendered_portal" || {
        printf '专题门户缺少相关门户内容槽: %s\n' "$portal" >&2
        exit 1
    }
    if grep -Fq 'hi-portal' <<<"$rendered_portal"; then
        printf '专题门户仍依赖项目私有平行布局: %s\n' "$portal" >&2
        exit 1
    fi
done

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
from html.parser import HTMLParser
import sys

requirements = dict((
    ("mp-2012-column-featurepic-block", 4),
    ("mp-2012-column-right-block-b", 5),
    ("mp-2012-column-right-block-c", 3),
    ("mp-2012-links", 15),
    ("mp-2012-sisters", 16),
))


class HomepageContractParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.void_tags = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }
        self.stack = []
        self.links = {key: 0 for key in requirements}
        self.classes = {key: set() for key in requirements}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        parent_contract = self.stack[-1][1] if self.stack else None
        contract = attributes.get("id")
        active = contract if contract in requirements else parent_contract
        if active:
            self.classes[active].update(attributes.get("class", "").split())
            if tag == "a":
                self.links[active] += 1
        if tag not in self.void_tags:
            self.stack.append((tag, active))

    def handle_startendtag(self, tag, attrs):
        attributes = dict(attrs)
        active = self.stack[-1][1] if self.stack else None
        if active:
            self.classes[active].update(attributes.get("class", "").split())
            if tag == "a":
                self.links[active] += 1

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break


page = sys.stdin.read()
parser = HomepageContractParser()
parser.feed(page)
for contract, minimum_links in requirements.items():
    if parser.links[contract] < minimum_links:
        raise SystemExit(f"中文项目首页组件内容不足: {contract}")
if not {"plainlinks", "noresize"}.issubset(parser.classes["mp-2012-sisters"]):
    raise SystemExit("中文项目首页关联项目未复用 Wikipediasister 表格契约。")
if "Human-Infra-tech-tree.png" not in page:
    raise SystemExit("中文项目首页未渲染本地科技树图片。")
' <<<"$rendered_main_page"
grep -Fq '典范研究' <<<"$rendered_main_page" || {
    printf '中文项目首页内容未渲染。\n' >&2
    exit 1
}
grep -Fq '请按' <<<"$rendered_main_page" || {
    printf '中文项目首页仍在使用过期模板解析缓存。\n' >&2
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
tech_tree_media_path="$(
    grep -oE 'src="[^"]*Human-Infra-tech-tree\.png[^"]*"' <<<"$rendered_main_page" \
        | head -n 1 \
        | cut -d '"' -f 2
)"
[[ -n "$tech_tree_media_path" ]] && curl -fsS -o /dev/null \
    "${base_url}${tech_tree_media_path}" || {
    printf 'MediaWiki 本地文件仓库中的 Human Infra 科技树图片不可用。\n' >&2
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
