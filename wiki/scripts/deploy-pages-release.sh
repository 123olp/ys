#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
runtime_dir="$wiki_dir/runtime/pages"
commit_hash="$(git -C "$wiki_dir" rev-parse HEAD)"

list_projects() {
    timeout -k 5s 20s wrangler pages project list 2>&1 \
        | sed $'s/\033\\[[0-9;]*[mK]//g' \
        || [[ "${PIPESTATUS[0]}" -eq 124 ]]
}

project_exists() {
    local project="$1"
    list_projects | grep -Eq "│[[:space:]]*${project}[[:space:]]*│"
}

ensure_project() {
    local project="$1"
    if ! project_exists "$project"; then
        local status=0
        timeout -k 5s 60s wrangler pages project create \
            "$project" \
            --production-branch main \
            || status=$?
        if [[ "$status" -ne 0 && "$status" -ne 124 ]]; then
            return "$status"
        fi
        project_exists "$project" || {
            printf 'Pages 项目创建后无法确认: %s\n' "$project" >&2
            return 1
        }
    fi
}

deploy_project() {
    local directory="$1"
    local project="$2"
    local message="$3"
    local status=0
    timeout -k 5s 900s wrangler pages deploy "$directory" \
        --project-name "$project" \
        --branch main \
        --commit-hash "$commit_hash" \
        --commit-message "$message" \
        || status=$?
    if [[ "$status" -ne 0 && "$status" -ne 124 ]]; then
        return "$status"
    fi
}

[[ -s "$runtime_dir/portal/index.html" ]] || {
    printf '缺少门户发布产物，请先运行 make pages-build。\n' >&2
    exit 1
}
[[ -s "$runtime_dir/wiki/snapshot/index.json" ]] || {
    printf '缺少 Wiki 发布产物，请先运行 make pages-build。\n' >&2
    exit 1
}

ensure_project human-infra
ensure_project human-infra-wiki

deploy_project \
    "$runtime_dir/portal" \
    human-infra \
    "Deploy Human Infra language portal"
deploy_project \
    "$runtime_dir/wiki" \
    human-infra-wiki \
    "Deploy Human Infra Wiki read-only snapshot"
