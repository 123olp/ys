#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

set -a
# shellcheck disable=SC1091
source .env
set +a

base_url="${WIKI_SERVER%/}"

printf '等待 Wiki HTTP 就绪'
for _ in $(seq 1 60); do
    if curl -fsS "$base_url/api.php?action=query&meta=siteinfo&format=json" >/dev/null 2>&1; then
        printf '\n'
        break
    fi
    printf '.'
    sleep 2
done

siteinfo="$(curl -fsS "$base_url/api.php?action=query&meta=siteinfo&format=json")"
grep -Fq '"sitename":"Human Infra Wiki"' <<<"$siteinfo"

extensions="$(curl -fsS "$base_url/api.php?action=query&meta=siteinfo&siprop=extensions&format=json")"
for extension in Cite ParserFunctions VisualEditor PageForms; do
    grep -Fq "\"name\":\"$extension\"" <<<"$extensions" || {
        printf '缺少扩展: %s\n' "$extension" >&2
        exit 1
    }
done

pages="$(curl -fsS --get "$base_url/api.php" \
    --data-urlencode 'action=query' \
    --data-urlencode 'titles=首页|Form:研究域|Form:技术节点|Form:证据来源' \
    --data-urlencode 'format=json')"
if grep -Fq '"missing":true' <<<"$pages"; then
    printf '关键种子页面缺失。\n' >&2
    exit 1
fi

main_page="$(curl -fsS --get "$base_url/index.php" \
    --data-urlencode 'title=首页' \
    --data-urlencode 'action=raw')"
grep -Fq '标准录入' <<<"$main_page" || {
    printf '首页未加载 Human Infra 种子内容。\n' >&2
    exit 1
}

for form in 研究域 技术节点 证据来源; do
    form_source="$(curl -fsS --get "$base_url/index.php" \
        --data-urlencode "title=Form:$form" \
        --data-urlencode 'action=raw')"
    grep -Fq 'for template' <<<"$form_source" || {
        printf '表单定义不可用: %s\n' "$form" >&2
        exit 1
    }
done

docker compose --env-file .env exec -T db healthcheck.sh --connect --innodb_initialized >/dev/null
printf 'Wiki smoke test: PASS\n'
