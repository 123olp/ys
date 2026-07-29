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

for url in "$legacy_portal_url/" "$wiki_url/" "$technology_tree_url/"; do
    curl --fail --silent --show-error --head --max-time 30 "$url" >/dev/null
done

printf '主域名与三个 pages.dev 入口 smoke 通过。\n'
