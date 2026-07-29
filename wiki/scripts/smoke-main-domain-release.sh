#!/usr/bin/env bash
set -euo pipefail

main_url="${MAIN_DOMAIN_URL:-https://tradecatlabs.com}"
wiki_url="${WIKI_PUBLIC_URL:-https://human-infra-wiki.pages.dev}"
technology_tree_url="${TECH_TREE_PUBLIC_URL:-https://human-infra-tech-tree.pages.dev}"
legacy_portal_url="${LEGACY_PORTAL_URL:-https://human-infra.pages.dev}"

fetch() {
    curl --fail --silent --show-error --location --max-time 30 "$1"
}

main_html="$(fetch "$main_url/")"
grep -Fq "<link href=\"$main_url/\" rel=\"canonical\"" <<<"$main_html"
grep -Fq "action=\"$wiki_url/search/\"" <<<"$main_html"
grep -Fq "href=\"$technology_tree_url/\"" <<<"$main_html"
grep -Fq 'content="MediaWiki ' <<<"$main_html"
grep -Fq 'skin-vector-2022' <<<"$main_html"
grep -Fq 'href="/assets/mediawiki.css"' <<<"$main_html"
if grep -Eq 'adapter\\.js|runtime-config\\.js|_worker\\.js' <<<"$main_html"; then
    printf '主域名包含禁止的自写前端或运行时入口。\n' >&2
    exit 1
fi

for asset in \
    assets/mediawiki.css \
    resources/assets/human-infra-mark.svg \
    resources/assets/mediawiki_compact.svg; do
    curl --fail --silent --show-error --head --max-time 30 \
        "$main_url/$asset" >/dev/null
done

for url in "$legacy_portal_url/" "$wiki_url/" "$technology_tree_url/"; do
    curl --fail --silent --show-error --head --max-time 30 "$url" >/dev/null
done

printf '主域名与三个 pages.dev 入口 smoke 通过。\n'
