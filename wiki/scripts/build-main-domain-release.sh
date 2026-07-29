#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output_dir="${MAIN_DOMAIN_OUTPUT_DIR:-$wiki_dir/runtime/pages/main-domain}"
source_wiki_dir="${WIKI_RELEASE_DIR:-$wiki_dir/runtime/pages/wiki}"
portal_url="${MAIN_DOMAIN_URL:-https://tradecatlabs.com/}"
wiki_url="${WIKI_PUBLIC_URL:-https://human-infra-wiki.pages.dev/}"
technology_tree_url="${TECH_TREE_PUBLIC_URL:-https://human-infra-tech-tree.pages.dev/}"

python3 "$wiki_dir/scripts/build-mediawiki-main-domain-release.py" \
    --source-wiki "$source_wiki_dir" \
    --output "$output_dir" \
    --portal-url "$portal_url" \
    --wiki-url "$wiki_url" \
    --technology-tree-url "$technology_tree_url"

printf 'ok\n' >"$output_dir/healthz"
cat >"$output_dir/_headers" <<'EOF'
/
  Cache-Control: public, max-age=0, must-revalidate, no-transform
/404.html
  Cache-Control: public, max-age=0, must-revalidate, no-transform
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/images/*
  Cache-Control: public, max-age=31536000, immutable
/resources/*
  Cache-Control: public, max-age=31536000, immutable
EOF
cat >"$output_dir/robots.txt" <<EOF
User-agent: *
Allow: /

Sitemap: ${portal_url%/}/sitemap.xml
EOF
cat >"$output_dir/sitemap.xml" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>${portal_url%/}/</loc></url>
</urlset>
EOF
cat >"$output_dir/llms.txt" <<EOF
# Human Infra

> 研究主体持续性、有效永生及其技术、证据与治理条件的知识基础设施。

- [Human Infra Wiki](${wiki_url%/}/): MediaWiki 研究知识库
- [Human Infra Technology Tree](${technology_tree_url%/}/): 目标导向科技树
- [Source repository](https://github.com/tradecatlabs/human_infra): 研究域、证据与治理契约
EOF
python3 - "$output_dir/entity.jsonld" "$portal_url" "$wiki_url" "$technology_tree_url" <<'PY'
import json
import sys
from pathlib import Path

target, portal_url, wiki_url, tree_url = sys.argv[1:]
payload = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Human Infra",
    "url": portal_url.rstrip("/") + "/",
    "publisher": {
        "@type": "Organization",
        "name": "tradecatlabs",
        "url": "https://github.com/tradecatlabs",
    },
    "sameAs": [
        wiki_url.rstrip("/") + "/",
        tree_url.rstrip("/") + "/",
        "https://github.com/tradecatlabs/human_infra",
    ],
}
Path(target).write_text(
    json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
PY

python3 "$wiki_dir/scripts/check-main-domain-release.py" \
    --directory "$output_dir" \
    --source-wiki "$source_wiki_dir" \
    --portal-url "$portal_url" \
    --wiki-url "$wiki_url" \
    --technology-tree-url "$technology_tree_url"

printf '主域名 MediaWiki 发布物完成: %s\n' "$output_dir"
