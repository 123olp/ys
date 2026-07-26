#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
runtime_dir="$wiki_dir/runtime/pages"
commit_hash="$(git -C "$wiki_dir" rev-parse HEAD)"

ensure_project() {
    local project="$1"
    local projects
    projects="$(
        timeout 20s wrangler pages project list 2>&1 \
            | sed $'s/\033\\[[0-9;]*[mK]//g' \
            || true
    )"
    if ! grep -Eq "│[[:space:]]*${project}[[:space:]]*│" <<<"$projects"; then
        wrangler pages project create "$project" --production-branch main
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

wrangler pages deploy "$runtime_dir/portal" \
    --project-name human-infra \
    --branch main \
    --commit-hash "$commit_hash" \
    --commit-message "Deploy Human Infra language portal"
wrangler pages deploy "$runtime_dir/wiki" \
    --project-name human-infra-wiki \
    --branch main \
    --commit-hash "$commit_hash" \
    --commit-message "Deploy Human Infra Wiki read-only snapshot"
