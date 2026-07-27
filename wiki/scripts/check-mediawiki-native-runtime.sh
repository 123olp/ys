#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

MEDIAWIKI_TEST_URL="${MEDIAWIKI_TEST_URL:-http://127.0.0.1:18782/wiki/Wikipedia:%E9%A6%96%E9%A1%B5}"
curl --fail --silent --show-error \
    --output /dev/null \
    "$MEDIAWIKI_TEST_URL"

docker_args=(
    run
    --rm
    --network host
    --volume
    "$wiki_dir/scripts/check-mediawiki-native-runtime.js:/work/check-mediawiki-native-runtime.js:ro"
    --volume
    "$wiki_dir/runtime:/work"
    --env
    "MEDIAWIKI_TEST_URL=$MEDIAWIKI_TEST_URL"
)
for proxy_variable in \
    HTTP_PROXY HTTPS_PROXY NO_PROXY \
    http_proxy https_proxy no_proxy; do
    if [[ -n "${!proxy_variable:-}" ]]; then
        docker_args+=(--env "$proxy_variable=${!proxy_variable}")
    fi
done

docker "${docker_args[@]}" \
    --entrypoint node \
    backstopjs/backstopjs:6.3.25 \
    /work/check-mediawiki-native-runtime.js
