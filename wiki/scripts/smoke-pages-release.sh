#!/usr/bin/env bash
set -euo pipefail

portal_url="${PORTAL_PAGES_URL:-https://human-infra.pages.dev}"
wiki_url="${WIKI_PAGES_URL:-https://human-infra-wiki.pages.dev}"
tech_tree_url="${TECH_TREE_PAGES_URL:-https://human-infra-tech-tree.pages.dev}"

portal="$(curl -fsSL "$portal_url/")"
grep -Fq 'id="www-wikipedia-org"' <<<"$portal"
grep -Fq 'Human Infra' <<<"$portal"
grep -Fq 'class="banner banner-bottom' <<<"$portal"
portal_missing_status="$(
    curl -sS -o /dev/null -w '%{http_code}' \
        "$portal_url/__human_infra_missing_route__"
)"
[[ "$portal_missing_status" == "404" ]] || {
    printf '门户未知路径必须返回 404，实际为 %s。\n' \
        "$portal_missing_status" >&2
    exit 1
}
curl -fsSL "$portal_url/runtime-config.js" \
    | grep -Fq 'https://human-infra-wiki.pages.dev'

wiki="$(curl -fsSL "$wiki_url/")"
grep -Fq 'Human Infra Wiki' <<<"$wiki"
grep -Fq 'id="mp-2012"' <<<"$wiki"
grep -Fq '只读公开快照' <<<"$wiki"
grep -Fq 'page-Main_Page' <<<"$wiki"
if grep -Fq 'id="vector-toc-pinned-container"' <<<"$wiki"; then
    printf 'Wiki 首页错误继承了普通文章目录外壳。\n' >&2
    exit 1
fi
for asset in \
    /resources/assets/licenses/cc-by-sa.png \
    /resources/assets/poweredby_mediawiki.svg \
    /resources/assets/mediawiki_compact.svg; do
    curl -fsSL "$wiki_url$asset" >/dev/null
done

article="$(curl -fsSL --get "$wiki_url/index.php" \
    --data-urlencode 'title=长寿逃逸速度')"
grep -Fq '长寿逃逸速度' <<<"$article"
grep -Fq 'page-长寿逃逸速度 rootpage-长寿逃逸速度' <<<"$article"
grep -Fq 'returnto=%E9%95%BF%E5%AF%BF%E9%80%83%E9%80%B8%E9%80%9F%E5%BA%A6' <<<"$article"
grep -Fq 'title=%E9%95%BF%E5%AF%BF%E9%80%83%E9%80%B8%E9%80%9F%E5%BA%A6&amp;oldid=' <<<"$article"
grep -Fq 'href="#稳定对象、阶段与状态"' <<<"$article"
if grep -Fq 'href="#研究对象与作用边界"' <<<"$article"; then
    printf 'Wiki 普通词条错误继承了模板文章目录。\n' >&2
    exit 1
fi

search="$(curl -fsSL --get "$wiki_url/index.php" \
    --data-urlencode 'title=Special:Search' \
    --data-urlencode 'search=长寿')"
grep -Fq '只读快照中的标题搜索结果' <<<"$search"

tech_tree="$(curl -fsSL "$tech_tree_url/")"
grep -Fq '<title>Human Infra Tech Tree</title>' <<<"$tech_tree"
if grep -Fq '/_vercel/insights/' <<<"$tech_tree"; then
    printf '科技树公开页面仍包含 Vercel 专属遥测。\n' >&2
    exit 1
fi
tech_tree_chunk="$(
    grep -oE 'src="[^"]*app/page-[^"]+\.js"' <<<"$tech_tree" \
        | head -1 \
        | cut -d'"' -f2
)"
[[ -n "$tech_tree_chunk" ]]
curl -fsSL "$tech_tree_url$tech_tree_chunk" \
    | grep -Fq 'HUMAN INFRA TECH TREE'

printf 'Pages 公开入口验证通过:\n'
printf '  %s\n  %s\n  %s\n' "$portal_url" "$wiki_url" "$tech_tree_url"
