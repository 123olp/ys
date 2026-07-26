#!/usr/bin/env bash
set -euo pipefail

portal_url="${PORTAL_PAGES_URL:-https://human-infra.pages.dev}"
wiki_url="${WIKI_PAGES_URL:-https://human-infra-wiki.pages.dev}"
tech_tree_url="${TECH_TREE_PAGES_URL:-https://human-infra-tech-tree.pages.dev}"

portal="$(curl -fsSL "$portal_url/")"
grep -Fq 'id="www-wikipedia-org"' <<<"$portal"
grep -Fq 'Human Infra' <<<"$portal"
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
    --data-urlencode 'title=有效永生与主体持续性')"
grep -Fq '有效永生与主体持续性' <<<"$article"

search="$(curl -fsSL --get "$wiki_url/index.php" \
    --data-urlencode 'title=Special:Search' \
    --data-urlencode 'search=长寿')"
grep -Fq '只读快照中的标题搜索结果' <<<"$search"

tech_tree="$(curl -fsSL "$tech_tree_url/")"
grep -Fq '<title>Historical Tech Tree</title>' <<<"$tech_tree"
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
