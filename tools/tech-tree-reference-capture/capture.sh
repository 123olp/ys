#!/usr/bin/env bash
set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MANIFEST="${ROOT_DIR}/docs/reference/tech-tree-web-candidates/candidates.json"
CAPTURE_RUN_ID="${CAPTURE_RUN_ID:-$(date -u +%Y%m%dT%H%M%SZ)}"
OUTPUT_ROOT="${ROOT_DIR}/build/reference-captures/tech-tree/${CAPTURE_RUN_ID}"
CAPTURE_BROWSER="${CAPTURE_BROWSER:-1}"
CAPTURE_ONLY="${CAPTURE_ONLY:-}"
CAPTURE_PROXY="${CAPTURE_PROXY:-}"
TIMEOUT_SECONDS="${TIMEOUT_SECONDS:-45}"

mkdir -p "${OUTPUT_ROOT}"
SUMMARY="${OUTPUT_ROOT}/capture-summary.tsv"
printf 'id\turl\thttp_capture\tbrowser_capture\tstatus\n' > "${SUMMARY}"

if [[ ! -f "${MANIFEST}" ]]; then
  printf 'manifest not found: %s\n' "${MANIFEST}" >&2
  exit 2
fi

mapfile -t ROWS < <(
  python3 - "${MANIFEST}" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    data = json.load(handle)
for item in data["candidates"]:
    print(f'{item["id"]}\t{item["url"]}')
PY
)

WGET_PROXY_ARGS=()
CHROME_PROXY_ARGS=()
if [[ -n "${CAPTURE_PROXY}" ]]; then
  WGET_PROXY_ARGS+=("-e" "use_proxy=yes" "-e" "https_proxy=${CAPTURE_PROXY}" "-e" "http_proxy=${CAPTURE_PROXY}")
  CHROME_PROXY_ARGS+=("--proxy-server=${CAPTURE_PROXY}")
fi

CHROME_BIN=""
for candidate in google-chrome chromium chromium-browser; do
  if command -v "${candidate}" >/dev/null 2>&1; then
    CHROME_BIN="$(command -v "${candidate}")"
    break
  fi
done

for row in "${ROWS[@]}"; do
  IFS=$'\t' read -r id url <<< "${row}"
  if [[ -n "${CAPTURE_ONLY}" && "${id}" != "${CAPTURE_ONLY}" ]]; then
    continue
  fi

  candidate_dir="${OUTPUT_ROOT}/${id}"
  mirror_dir="${candidate_dir}/mirror"
  mkdir -p "${mirror_dir}"
  log_file="${candidate_dir}/capture.log"
  : > "${log_file}"
  http_status="failed"
  browser_status="skipped"
  printf '[%s] HTTP capture: %s\n' "${id}" "${url}" | tee -a "${log_file}"
  if timeout "${TIMEOUT_SECONDS}s" wget \
    --no-verbose \
    --timeout=20 \
    --tries=2 \
    --waitretry=2 \
    --page-requisites \
    --convert-links \
    --adjust-extension \
    --span-hosts \
    --directory-prefix="${mirror_dir}" \
    --warc-file="${candidate_dir}/network" \
    "${WGET_PROXY_ARGS[@]}" \
    "${url}" >> "${log_file}" 2>&1; then
    http_status="complete"
  fi

  if [[ "${CAPTURE_BROWSER}" == "1" && -n "${CHROME_BIN}" ]]; then
    browser_status="failed"
    profile_dir="${candidate_dir}/chrome-profile"
    mkdir -p "${profile_dir}"
    printf '[%s] Browser capture\n' "${id}" | tee -a "${log_file}"
    chrome_args=(
      --headless=new
      --no-sandbox
      --disable-gpu
      --disable-dev-shm-usage
      --disable-breakpad
      --disable-crash-reporter
      --no-first-run
      --hide-scrollbars
      --window-size=1600,10000
      --virtual-time-budget=10000
      --user-data-dir="${profile_dir}"
      "${CHROME_PROXY_ARGS[@]}"
    )
    if timeout "${TIMEOUT_SECONDS}s" "${CHROME_BIN}" "${chrome_args[@]}" \
      --dump-dom "${url}" > "${candidate_dir}/rendered.html" 2>> "${log_file}" \
      && timeout "${TIMEOUT_SECONDS}s" "${CHROME_BIN}" "${chrome_args[@]}" \
      --screenshot="${candidate_dir}/screenshot.png" "${url}" >> "${log_file}" 2>&1; then
      browser_status="complete"
    fi
    rm -rf "${profile_dir}"
  fi

  status="blocked"
  if [[ "${http_status}" == "complete" && "${browser_status}" == "complete" ]]; then
    status="complete"
  elif [[ "${http_status}" == "complete" || "${browser_status}" == "complete" ]]; then
    status="partial"
  fi

  (
    cd "${candidate_dir}" || exit 1
    find . -type f ! -name SHA256SUMS -print0 \
      | sort -z \
      | xargs -0 -r sha256sum > SHA256SUMS
  )
  printf '%s\t%s\t%s\t%s\t%s\n' "${id}" "${url}" "${http_status}" "${browser_status}" "${status}" >> "${SUMMARY}"
done

python3 - "${SUMMARY}" <<'PY'
import csv
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle, delimiter="\t"))
counts = {}
for row in rows:
    counts[row["status"]] = counts.get(row["status"], 0) + 1
print("capture summary:", ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))
PY
