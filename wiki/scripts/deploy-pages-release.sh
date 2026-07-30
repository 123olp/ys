#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
runtime_dir="$wiki_dir/runtime/pages"
commit_hash="$(git -C "$wiki_dir" rev-parse HEAD)"

run_until_marker() {
    local marker="$1"
    local timeout_seconds="$2"
    shift 2
    local log_file
    local pid
    local deadline
    local status=0
    log_file="$(mktemp)"
    "$@" >"$log_file" 2>&1 &
    pid=$!
    deadline=$((SECONDS + timeout_seconds))

    while kill -0 "$pid" 2>/dev/null; do
        if grep -Fq "$marker" "$log_file"; then
            kill "$pid" 2>/dev/null || true
            wait "$pid" 2>/dev/null || true
            cat "$log_file"
            find "$log_file" -delete
            return 0
        fi
        if (( SECONDS >= deadline )); then
            kill "$pid" 2>/dev/null || true
            wait "$pid" 2>/dev/null || true
            cat "$log_file" >&2
            find "$log_file" -delete
            return 124
        fi
        sleep 1
    done

    wait "$pid" || status=$?
    cat "$log_file"
    if grep -Fq "$marker" "$log_file"; then
        status=0
    fi
    find "$log_file" -delete
    return "$status"
}

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
        run_until_marker "Successfully created" 90 \
            wrangler pages project create \
            "$project" \
            --production-branch main
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
    run_until_marker "Deployment complete!" 900 \
        wrangler pages deploy "$directory" \
        --project-name "$project" \
        --branch main \
        --commit-hash "$commit_hash" \
        --commit-message "$message"
}

[[ -s "$runtime_dir/wiki/snapshot/index.json" ]] || {
    printf '缺少 Wiki 发布产物，请先运行 make pages-build。\n' >&2
    exit 1
}

python3 "$wiki_dir/scripts/check-mediawiki-native-ui.py"
"$wiki_dir/scripts/check-mediawiki-native-runtime.sh"

wiki_project="${WIKI_PAGES_PROJECT:-human-infra-wiki-public}"
ensure_project "$wiki_project"

deploy_project \
    "$runtime_dir/wiki" \
    "$wiki_project" \
    "Deploy Human Infra Wiki read-only snapshot"
