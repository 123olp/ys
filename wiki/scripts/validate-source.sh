#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

required=(
    AGENTS.md
    README.md
    CONTENT-STANDARD.md
    ROUTING-CONTRACT.md
    Dockerfile
    compose.yaml
    env.example
    config/HumanInfraSettings.php
    docker/entrypoint.sh
    content/manifest.tsv
)

for file in "${required[@]}"; do
    [[ -s "$file" ]] || {
        printf '缺失或为空: %s\n' "$file" >&2
        exit 1
    }
done

declare -A titles=()
while IFS=$'\t' read -r title file; do
    [[ -n "$title" && "${title:0:1}" != "#" ]] || continue
    [[ -f "content/$file" ]] || {
        printf 'manifest 文件缺失: %s\n' "$file" >&2
        exit 1
    }
    [[ -z "${titles[$title]:-}" ]] || {
        printf 'manifest 标题重复: %s\n' "$title" >&2
        exit 1
    }
    titles["$title"]=1
done < content/manifest.tsv

if [[ -f .env ]]; then
    docker compose --env-file .env config --quiet
else
    cp env.example .env.validation
    trap 'rm -f .env.validation' EXIT
    docker compose --env-file .env.validation config --quiet
fi

printf 'Wiki source contract: PASS\n'
