#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$wiki_dir"

mkdir -p runtime

server_pid=""
cleanup() {
    if [[ -n "$server_pid" ]]; then
        kill "$server_pid" 2>/dev/null || true
        wait "$server_pid" 2>/dev/null || true
    fi
}
trap cleanup EXIT

if [[ -z "${WIKI_TEST_URL:-}" ]]; then
    [[ -s "$wiki_dir/runtime/pages/wiki/index.html" ]] || {
        printf '缺少 Wiki 静态发布物，请先运行 make pages-build。\n' >&2
        exit 1
    }
    test_port="$(
        python3 -c \
            'import socket; s = socket.socket(); s.bind(("127.0.0.1", 0)); print(s.getsockname()[1]); s.close()'
    )"
    WIKI_TEST_URL="http://127.0.0.1:${test_port}/"
    python3 -m http.server \
        "$test_port" \
        --bind 127.0.0.1 \
        --directory "$wiki_dir/runtime/pages/wiki" \
        >"$wiki_dir/runtime/vector-appearance-server.log" 2>&1 &
    server_pid=$!

    for _ in $(seq 1 50); do
        if curl --fail --silent \
            --output /dev/null \
            "$WIKI_TEST_URL"; then
            break
        fi
        if ! kill -0 "$server_pid" 2>/dev/null; then
            cat "$wiki_dir/runtime/vector-appearance-server.log" >&2
            exit 1
        fi
        sleep 0.1
    done
    curl --fail --silent --show-error \
        --output /dev/null \
        "$WIKI_TEST_URL"
fi

docker_args=(
    run
    --rm
    --network host
    --volume
    "$wiki_dir/scripts/check-vector-appearance.js:/work/check-vector-appearance.js:ro"
    --volume
    "$wiki_dir/runtime:/work"
    --env
    "WIKI_TEST_URL=$WIKI_TEST_URL"
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
    /work/check-vector-appearance.js
