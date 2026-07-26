#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
runtime_dir="$wiki_dir/runtime/pages"
portal_dir="$runtime_dir/portal"
wiki_output_dir="$runtime_dir/wiki"
wiki_public_url="${WIKI_PAGES_URL:-https://human-infra-wiki.pages.dev}"
wiki_local_url="${WIKI_LOCAL_URL:-http://127.0.0.1:18782}"

rm -rf "$portal_dir"
mkdir -p "$portal_dir"

cp "$wiki_dir/portal/index.html" "$portal_dir/"
cp "$wiki_dir/portal/adapter.js" "$portal_dir/"
cp "$wiki_dir/portal/languages.json" "$portal_dir/"
cp "$wiki_dir/portal/LICENSE.wikimedia-portals" "$portal_dir/"
cp -R "$wiki_dir/portal/assets" "$portal_dir/"
printf 'window.HUMAN_INFRA_PORTAL={wikiPort:"",wikiBase:"%s"};\n' \
    "$wiki_public_url" >"$portal_dir/runtime-config.js"
printf 'ok\n' >"$portal_dir/healthz"
cat >"$portal_dir/_headers" <<'EOF'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/runtime-config.js
  Cache-Control: public, max-age=300
EOF

python3 "$wiki_dir/scripts/export-pages-snapshot.py" \
    --base-url "$wiki_local_url" \
    --output "$wiki_output_dir"

printf 'Pages 发布产物完成:\n'
printf '  portal: %s\n' "$portal_dir"
printf '  wiki:   %s\n' "$wiki_output_dir"
