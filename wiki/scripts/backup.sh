#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

[[ -f .env ]] || {
    printf '缺少 wiki/.env。\n' >&2
    exit 1
}

set -a
# shellcheck disable=SC1091
source .env
set +a

timestamp="$(date +%Y%m%dT%H%M%S)"
backup_dir="$wiki_dir/runtime/backups/$timestamp"
mkdir -p "$backup_dir"

docker compose --env-file .env exec -T db \
    mariadb-dump \
    --user=root \
    --password="$MARIADB_ROOT_PASSWORD" \
    --single-transaction \
    --routines \
    --events \
    "$MARIADB_DATABASE" | gzip -9 > "$backup_dir/database.sql.gz"

tar -czf "$backup_dir/images.tar.gz" -C runtime images
tar -czf "$backup_dir/config.tar.gz" -C runtime config
sha256sum "$backup_dir"/*.gz > "$backup_dir/SHA256SUMS"

printf '备份已创建: %s\n' "$backup_dir"
