#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
runtime_dir="$wiki_dir/runtime/pages"
portal_dir="$runtime_dir/portal"
wiki_output_dir="$runtime_dir/wiki"
wiki_public_url="${WIKI_PAGES_URL:-https://human-infra-wiki.pages.dev}"
wiki_local_url="${WIKI_LOCAL_URL:-http://127.0.0.1:18782}"

python3 "$wiki_dir/scripts/build-portal-release.py" \
    --output "$portal_dir"
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

for file in \
    index.html \
    404.html \
    compat/index.html \
    search/index.html \
    random/index.html \
    wiki/长寿逃逸速度/index.html \
    snapshot/index.json \
    resources/assets/licenses/cc-by-sa.png \
    resources/assets/poweredby_mediawiki.svg \
    resources/assets/mediawiki_compact.svg; do
    [[ -s "$wiki_output_dir/$file" ]] || {
        printf 'Wiki Pages 发布产物缺失: %s\n' "$file" >&2
        exit 1
    }
done
for forbidden in _worker.js _routes.json functions; do
    if [[ -e "$wiki_output_dir/$forbidden" ]]; then
        printf 'Wiki Pages 发布物禁止包含函数入口: %s\n' \
            "$forbidden" >&2
        exit 1
    fi
done
python3 "$wiki_dir/scripts/audit-geo-publication.py" \
    --portal-dir "$portal_dir" \
    --wiki-dir "$wiki_output_dir"
if grep -Fq 'id="vector-toc-pinned-container"' \
    "$wiki_output_dir/index.html"; then
    printf 'Wiki Pages 首页外壳错误继承普通文章目录。\n' >&2
    exit 1
fi
appearance_control_count="$(
    grep -o 'id="skin-client-pref-[^"]*-value-[^"]*"' \
        "$wiki_output_dir/index.html" \
        | sort -u \
        | wc -l
)"
[[ "$appearance_control_count" -eq 8 ]] || {
    printf 'Wiki Pages 外观面板控件不完整，实际为 %s/8。\n' \
        "$appearance_control_count" >&2
    exit 1
}
grep -Fq 'src="/assets/vector-client-preferences.js"' \
    "$wiki_output_dir/index.html" || {
    printf 'Wiki Pages 缺少 Vector 静态偏好适配器。\n' >&2
    exit 1
}

printf 'Pages 发布产物完成:\n'
printf '  portal: %s\n' "$portal_dir"
printf '  wiki:   %s\n' "$wiki_output_dir"
