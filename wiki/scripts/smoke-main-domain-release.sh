#!/usr/bin/env bash
set -euo pipefail

main_url="${MAIN_DOMAIN_URL:-https://tradecatlabs.com}"
wiki_url="${WIKI_PUBLIC_URL:-https://human-infra-wiki.pages.dev}"
technology_tree_url="${TECH_TREE_PUBLIC_URL:-https://human-infra-tech-tree.pages.dev}"
legacy_portal_url="${LEGACY_PORTAL_URL:-https://human-infra.pages.dev}"

fetch() {
    curl \
        --fail \
        --silent \
        --show-error \
        --location \
        --max-time 30 \
        --retry 5 \
        --retry-all-errors \
        --retry-delay 2 \
        "$1"
}

head_check() {
    curl \
        --fail \
        --silent \
        --show-error \
        --head \
        --max-time 30 \
        --retry 5 \
        --retry-all-errors \
        --retry-delay 2 \
        "$1" >/dev/null
}

main_html="$(fetch "$main_url/")"
grep -Fq "<link href=\"$main_url/\" rel=\"canonical\"" <<<"$main_html"
grep -Fq "action=\"$wiki_url/search/\"" <<<"$main_html"
grep -Fq "href=\"$technology_tree_url/\"" <<<"$main_html"
grep -Fq 'content="MediaWiki ' <<<"$main_html"
grep -Fq 'skin-vector-2022' <<<"$main_html"
grep -Fq 'href="/assets/mediawiki.css"' <<<"$main_html"
if grep -Eq 'adapter\\.js|runtime-config\\.js|_worker\\.js|cloudflareinsights|data-cf-beacon' <<<"$main_html"; then
    printf '主域名包含禁止的自写前端、运行时入口或边缘注入脚本。\n' >&2
    exit 1
fi

for asset in \
    assets/mediawiki.css \
    resources/assets/human-infra-mark.svg \
    resources/assets/mediawiki_compact.svg; do
    head_check "$main_url/$asset"
done

for url in "$legacy_portal_url/" "$wiki_url/" "$technology_tree_url/"; do
    head_check "$url"
done

printf '主域名与三个 pages.dev 入口 smoke 通过。\n'
