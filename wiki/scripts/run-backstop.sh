#!/usr/bin/env bash
set -euo pipefail

wiki_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
action="${1:-test}"
suite="${2:-contract}"

case "$action" in
    reference|test)
        ;;
    *)
        printf '用法: %s {reference|test}\n' "$0" >&2
        exit 2
        ;;
esac

case "$suite" in
    contract)
        config="visual-regression/backstop.contract.json"
        ;;
    audit)
        config="visual-regression/backstop.wikipedia.json"
        ;;
    *)
        printf '未知视觉套件: %s；允许 contract 或 audit。\n' "$suite" >&2
        exit 2
        ;;
esac

docker run --rm \
    --network host \
    --user "$(id -u):$(id -g)" \
    --env HTTP_PROXY \
    --env HTTPS_PROXY \
    --env NO_PROXY \
    --env http_proxy \
    --env https_proxy \
    --env no_proxy \
    --mount "type=bind,source=$wiki_dir,target=/src" \
    --workdir /src \
    backstopjs/backstopjs:6.3.25 \
    "$action" \
    "--config=$config"
