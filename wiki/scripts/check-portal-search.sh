#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

docker run --rm \
    --network host \
    --volume "$wiki_dir/scripts/check-portal-search.js:/work/check-portal-search.js:ro" \
    --env PORTAL_TEST_URL="${PORTAL_TEST_URL:-https://human-infra.pages.dev/}" \
    --env WIKI_TEST_URL="${WIKI_TEST_URL:-https://human-infra-wiki.pages.dev/}" \
    --entrypoint node \
    backstopjs/backstopjs:6.3.25 \
    /work/check-portal-search.js
