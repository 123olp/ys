#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

[[ -f .env ]] || {
    printf '缺少 wiki/.env，请先执行 scripts/bootstrap.sh。\n' >&2
    exit 1
}

set -a
# shellcheck disable=SC1091
source .env
set +a

docker compose --env-file .env exec -T wiki \
    php maintenance/run.php importImages \
    --extensions=svg \
    --overwrite \
    --user="$WIKI_ADMIN_USER" \
    --comment="同步 Human Infra 受治理品牌资源" \
    /opt/human-infra-wiki/seed-assets >/dev/null
printf '已导入: File:Human-Infra-mark.svg\n'

while IFS=$'\t' read -r title file; do
    [[ -n "$title" && "${title:0:1}" != "#" ]] || continue
    source_file="$wiki_dir/content/$file"
    [[ -f "$source_file" ]] || {
        printf 'manifest 引用的文件不存在: %s\n' "$source_file" >&2
        exit 1
    }

    docker compose --env-file .env exec -T wiki \
        php maintenance/run.php edit \
        --user="$WIKI_ADMIN_USER" \
        --summary="同步 Human Infra 受治理种子内容" \
        "$title" < "$source_file" >/dev/null
    printf '已导入: %s\n' "$title"
done < content/manifest.tsv

docker compose --env-file .env exec -T wiki php maintenance/run.php runJobs --maxjobs=100 >/dev/null
printf '%s\n' 'Human Infra:首页' | docker compose --env-file .env exec -T wiki \
    php maintenance/run.php purgePage >/dev/null
printf '已刷新: Human Infra:首页\n'
