#!/usr/bin/env bash
set -euo pipefail

portal_url="${PORTAL_PAGES_URL:-https://human-infra.pages.dev}"
wiki_url="${WIKI_PAGES_URL:-https://human-infra-wiki.pages.dev}"
tech_tree_url="${TECH_TREE_PAGES_URL:-https://human-infra-tech-tree.pages.dev}"
temp_dir="$(mktemp -d)"
trap 'rm -rf "$temp_dir"' EXIT

fetch_contains() {
    local url="$1"
    local pattern="$2"
    local output="$temp_dir/response"
    curl -fsSL "$url" -o "$output"
    grep -Fq "$pattern" "$output"
}

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
fetch_contains \
    "$portal_url/runtime-config.js" \
    'https://human-infra-wiki.pages.dev'
portal_robots="$(curl -fsSL "$portal_url/robots.txt")"
grep -Fq "Sitemap: $portal_url/sitemap.xml" <<<"$portal_robots"
fetch_contains "$portal_url/sitemap.xml" "<loc>$portal_url/</loc>"
fetch_contains "$portal_url/llms.txt" 'Human Infra Wiki'
grep -Fq '<link href="https://human-infra.pages.dev/" rel="canonical"' <<<"$portal"
grep -Fq 'property="og:title"' <<<"$portal"
grep -Fq 'application/ld+json' <<<"$portal"

wiki="$(curl -fsSL "$wiki_url/")"
grep -Fq 'Human Infra Wiki' <<<"$wiki"
grep -Fq 'id="mp-2012"' <<<"$wiki"
grep -Fq '只读公开快照' <<<"$wiki"
grep -Fq 'page-Main_Page' <<<"$wiki"
grep -Fq 'name="description"' <<<"$wiki"
grep -Fq 'property="og:title"' <<<"$wiki"
grep -Fq 'application/ld+json' <<<"$wiki"
appearance_control_count="$(
    grep -o 'id="skin-client-pref-[^"]*-value-[^"]*"' <<<"$wiki" \
        | sort -u \
        | wc -l
)"
[[ "$appearance_control_count" -eq 8 ]] || {
    printf 'Wiki 公开首页外观面板控件不完整，实际为 %s/8。\n' \
        "$appearance_control_count" >&2
    exit 1
}
grep -Fq 'src="/assets/vector-client-preferences.js"' <<<"$wiki"
fetch_contains \
    "$wiki_url/assets/vector-client-preferences.js" \
    'vector-feature-custom-font-size'
for forbidden_id in \
    ca-talk \
    ca-viewsource \
    n-recentchanges \
    n-specialpages \
    p-variants \
    pt-login-2 \
    t-info \
    t-permalink \
    vector-sticky-header \
    vector-user-links-dropdown-checkbox; do
    if grep -Fq "id=\"$forbidden_id\"" <<<"$wiki"; then
        printf 'Wiki 公开首页保留不可用操作控件: %s。\n' \
            "$forbidden_id" >&2
        exit 1
    fi
done
if grep -Fq 'href="#"' <<<"$wiki"; then
    printf 'Wiki 公开首页仍包含无目标链接。\n' >&2
    exit 1
fi
main_page_alias="$(
    curl -fsSL "$wiki_url/wiki/Main_Page/"
)"
if grep -Fq 'action="/index.php/' <<<"$main_page_alias"; then
    printf 'Wiki 首页别名仍包含依赖 MediaWiki 后端的表单。\n' >&2
    exit 1
fi
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
wiki_robots="$(curl -fsSL "$wiki_url/robots.txt")"
grep -Fq "Sitemap: $wiki_url/sitemap.xml" <<<"$wiki_robots"
fetch_contains "$wiki_url/sitemap.xml" '<urlset'
fetch_contains "$wiki_url/llms.txt" 'Machine discovery'
fetch_contains "$wiki_url/geo/entity.jsonld" '"Human Infra Wiki"'
curl -fsSL "$wiki_url/geo/pages.ndjson" -o "$temp_dir/pages.ndjson"
geo_first_line="$(sed -n '1p' "$temp_dir/pages.ndjson")"
grep -Fq '"description"' <<<"$geo_first_line"

article="$(curl -fsSL "$wiki_url/wiki/%E9%95%BF%E5%AF%BF%E9%80%83%E9%80%B8%E9%80%9F%E5%BA%A6/")"
grep -Fq '长寿逃逸速度' <<<"$article"
grep -Fq 'page-长寿逃逸速度 rootpage-长寿逃逸速度' <<<"$article"
grep -Fq 'href="#稳定对象、阶段与状态"' <<<"$article"
grep -Fq 'name="description"' <<<"$article"
grep -Fq 'property="og:type"' <<<"$article"
grep -Fq 'content="article"' <<<"$article"
grep -Fq 'application/ld+json' <<<"$article"
if grep -Fq 'class="mw-editsection"' <<<"$article"; then
    printf 'Wiki 公开词条仍暴露不可用编辑入口。\n' >&2
    exit 1
fi
if grep -Fq 'href="#研究对象与作用边界"' <<<"$article"; then
    printf 'Wiki 普通词条错误继承了模板文章目录。\n' >&2
    exit 1
fi

historical="$(
    curl -fsSL \
        "$wiki_url/wiki/%E5%8E%86%E5%8F%B2%E6%8A%80%E6%9C%AF%E8%B0%B1%E7%B3%BB/"
)"
if grep -Eq 'class="[^"]*\\bsortable\\b' <<<"$historical"; then
    printf 'Wiki 公开词条仍声明不存在的表格排序能力。\n' >&2
    exit 1
fi

search="$(curl -fsSL "$wiki_url/search/?q=%E9%95%BF%E5%AF%BF")"
grep -Fq 'id="hi-static-search"' <<<"$search"
fetch_contains "$wiki_url/assets/wiki-search.js" 'snapshot/index.json'

legacy_status="$(
    curl -sS -o /dev/null -w '%{http_code}' \
        "$wiki_url/index.php/%E9%95%BF%E5%AF%BF%E9%80%83%E9%80%B8%E9%80%9F%E5%BA%A6"
)"
[[ "$legacy_status" == "301" || "$legacy_status" == "302" ]] || {
    printf 'Wiki 旧词条路径应重定向，实际为 %s。\n' \
        "$legacy_status" >&2
    exit 1
}

compat="$(curl -fsSL --get "$wiki_url/index.php" \
    --data-urlencode 'title=长寿逃逸速度')"
grep -Fq '正在转向静态词条' <<<"$compat"

wiki_missing_status="$(
    curl -sS -o /dev/null -w '%{http_code}' \
        "$wiki_url/wiki/__human_infra_missing_route__/"
)"
[[ "$wiki_missing_status" == "404" ]] || {
    printf 'Wiki 未知词条必须返回 404，实际为 %s。\n' \
        "$wiki_missing_status" >&2
    exit 1
}

tech_tree="$(curl -fsSL "$tech_tree_url/")"
grep -Fq '<title>Human Infra Tech Tree</title>' <<<"$tech_tree"
if grep -Fq '/_vercel/insights/' <<<"$tech_tree"; then
    printf '科技树公开页面仍包含 Vercel 专属遥测。\n' >&2
    exit 1
fi
tech_tree_chunk="$(
    grep -oEm1 'src="[^"]*app/page-[^"]+\.js"' <<<"$tech_tree" \
        | cut -d'"' -f2
)"
[[ -n "$tech_tree_chunk" ]]
fetch_contains "$tech_tree_url$tech_tree_chunk" 'HUMAN INFRA TECH TREE'

printf 'Pages 公开入口验证通过:\n'
printf '  %s\n  %s\n  %s\n' "$portal_url" "$wiki_url" "$tech_tree_url"
