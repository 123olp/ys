#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

for command in docker openssl curl; do
    command -v "$command" >/dev/null 2>&1 || {
        printf '缺少必需命令: %s\n' "$command" >&2
        exit 1
    }
done

docker compose version >/dev/null
mkdir -p runtime/config runtime/images runtime/db runtime/backups

if [[ ! -f .env ]]; then
    wiki_password="$(openssl rand -base64 30 | tr -d '\n')"
    db_password="$(openssl rand -base64 30 | tr -d '\n')"
    root_password="$(openssl rand -base64 30 | tr -d '\n')"
    {
        printf 'WIKI_PORT=18782\n'
        printf 'WIKI_SERVER=http://localhost:18782\n'
        printf "WIKI_SITE_NAME='Human Infra Wiki'\n"
        printf 'WIKI_ADMIN_USER=HumanInfraAdmin\n'
        printf 'WIKI_ADMIN_PASSWORD=%s\n' "$wiki_password"
        printf 'MARIADB_DATABASE=human_infra_wiki\n'
        printf 'MARIADB_USER=human_infra_wiki\n'
        printf 'MARIADB_PASSWORD=%s\n' "$db_password"
        printf 'MARIADB_ROOT_PASSWORD=%s\n' "$root_password"
    } > .env
    chmod 0600 .env
    printf '已生成本地密钥文件: %s/.env\n' "$wiki_dir"
fi

set -a
# shellcheck disable=SC1091
source .env
set +a

docker compose --env-file .env up -d db
printf '等待 MariaDB 就绪'
for _ in $(seq 1 60); do
    if docker compose --env-file .env exec -T db healthcheck.sh --connect --innodb_initialized >/dev/null 2>&1; then
        printf '\n'
        break
    fi
    printf '.'
    sleep 2
done

if ! docker compose --env-file .env exec -T db healthcheck.sh --connect --innodb_initialized >/dev/null 2>&1; then
    printf '\nMariaDB 未在预期时间内就绪。\n' >&2
    exit 1
fi

docker compose --env-file .env build wiki

if [[ ! -f runtime/config/LocalSettings.php ]]; then
    docker compose --env-file .env run --rm --no-deps wiki \
        php maintenance/run.php install \
        --dbtype=mysql \
        --dbserver=db \
        --dbname="$MARIADB_DATABASE" \
        --dbuser="$MARIADB_USER" \
        --dbpass="$MARIADB_PASSWORD" \
        --server="$WIKI_SERVER" \
        --scriptpath="" \
        --lang=zh \
        --pass="$WIKI_ADMIN_PASSWORD" \
        --confpath=/config \
        "$WIKI_SITE_NAME" \
        "$WIKI_ADMIN_USER"

fi

if ! grep -Fq "/opt/human-infra-wiki/HumanInfraSettings.php" runtime/config/LocalSettings.php; then
    docker compose --env-file .env run --rm --no-deps wiki \
        sh -c "printf \"\\nrequire_once '/opt/human-infra-wiki/HumanInfraSettings.php';\\n\" >> /config/LocalSettings.php"
fi

docker compose --env-file .env up -d wiki
docker compose --env-file .env exec -T wiki php maintenance/run.php update --quick
"$wiki_dir/scripts/import-content.sh"
"$wiki_dir/scripts/smoke-test.sh"

printf '\nHuman Infra Wiki 已就绪: %s\n' "$WIKI_SERVER"
