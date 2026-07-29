#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="${MAIN_DOMAIN_OUTPUT_DIR:-$wiki_dir/runtime/pages/main-domain}"
portal_url="${MAIN_DOMAIN_URL:-https://tradecatlabs.com/}"
wiki_url="${WIKI_PUBLIC_URL:-https://human-infra-wiki.pages.dev/}"
technology_tree_url="${TECH_TREE_PUBLIC_URL:-https://human-infra-tech-tree.pages.dev/}"

python3 "$wiki_dir/scripts/build-portal-release.py" \
    --output "$output_dir" \
    --portal-url "$portal_url" \
    --wiki-url "$wiki_url" \
    --technology-tree-url "$technology_tree_url"

printf 'window.HUMAN_INFRA_PORTAL={wikiPort:"",wikiBase:"%s"};\n' \
    "$wiki_url" >"$output_dir/runtime-config.js"
printf 'ok\n' >"$output_dir/healthz"
cat >"$output_dir/_headers" <<'EOF'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/portal/*
  Cache-Control: public, max-age=31536000, immutable
/runtime-config.js
  Cache-Control: public, max-age=300
EOF

python3 "$wiki_dir/scripts/check-main-domain-release.py" \
    --directory "$output_dir" \
    --portal-url "$portal_url" \
    --wiki-url "$wiki_url" \
    --technology-tree-url "$technology_tree_url"

printf '主域名静态门户发布物完成: %s\n' "$output_dir"
