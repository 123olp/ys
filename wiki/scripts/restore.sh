#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

backup_dir="${1:-}"
[[ "${RESTORE_CONFIRM:-}" == "restore" ]] || {
    printf '恢复会覆盖当前 Wiki。请设置 RESTORE_CONFIRM=restore。\n' >&2
    exit 1
}
[[ -d "$backup_dir" ]] || {
    printf '备份目录不存在: %s\n' "$backup_dir" >&2
    exit 1
}
[[ -f "$backup_dir/database.sql.gz" && -f "$backup_dir/images.tar.gz" && -f "$backup_dir/config.tar.gz" ]] || {
    printf '备份包不完整: %s\n' "$backup_dir" >&2
    exit 1
}

set -a
# shellcheck disable=SC1091
source .env
set +a

(cd "$backup_dir" && sha256sum -c SHA256SUMS)
docker compose --env-file .env stop wiki

gzip -dc "$backup_dir/database.sql.gz" | docker compose --env-file .env exec -T db \
    mariadb --user=root --password="$MARIADB_ROOT_PASSWORD" "$MARIADB_DATABASE"

rm -rf runtime/images runtime/config
tar -xzf "$backup_dir/images.tar.gz" -C runtime
tar -xzf "$backup_dir/config.tar.gz" -C runtime

docker compose --env-file .env up -d wiki
docker compose --env-file .env exec -T wiki php maintenance/run.php update --quick
"$wiki_dir/scripts/smoke-test.sh"
