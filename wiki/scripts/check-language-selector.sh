#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

mkdir -p runtime

docker run --rm \
    --network host \
    --volume "$wiki_dir/scripts/check-language-selector.js:/work/check-language-selector.js:ro" \
    --volume "$wiki_dir/runtime:/work" \
    --env WIKI_TEST_URL="${WIKI_TEST_URL:-http://127.0.0.1:18782/}" \
    --entrypoint node \
    backstopjs/backstopjs:6.3.25 \
    /work/check-language-selector.js
