#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
proxy_env=()
for variable in \
    HTTP_PROXY HTTPS_PROXY NO_PROXY \
    http_proxy https_proxy no_proxy; do
    if [[ -n "${!variable:-}" ]]; then
        proxy_env+=(--env "$variable")
    fi
done

docker run --rm \
    --network host \
    --volume "$wiki_dir/scripts/check-portal-search.js:/work/check-portal-search.js:ro" \
    "${proxy_env[@]}" \
    --env PORTAL_TEST_URL="${PORTAL_TEST_URL:-https://human-infra.pages.dev/}" \
    --env WIKI_TEST_URL="${WIKI_TEST_URL:-https://wiki.tradecatlabs.com/}" \
    --entrypoint node \
    backstopjs/backstopjs:6.3.25 \
    /work/check-portal-search.js
