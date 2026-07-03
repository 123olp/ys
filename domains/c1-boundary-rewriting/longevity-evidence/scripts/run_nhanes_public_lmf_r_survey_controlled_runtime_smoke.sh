#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../../../.." && pwd)"
ENV_FILE="${REPO_ROOT}/domains/c1-boundary-rewriting/longevity-evidence/runtime/nhanes-public-lmf-r-survey-conda.yml"
ENV_PREFIX="${HUMAN_INFRA_R_SURVEY_ENV_PREFIX:-${REPO_ROOT}/.runtime/nhanes-r-survey}"
OUT_PATH="${HUMAN_INFRA_R_SURVEY_SMOKE_OUT:-${REPO_ROOT}/web/src/data/life-path-nhanes-public-lmf-r-survey-controlled-runtime-smoke-validation.json}"
VALIDATOR="${REPO_ROOT}/domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhanes_public_lmf_r_survey_runtime_smoke.py"

if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: conda is required to provision the controlled R survey runtime." >&2
  exit 1
fi

if [[ ! -x "${ENV_PREFIX}/bin/Rscript" ]]; then
  conda env create -p "${ENV_PREFIX}" -f "${ENV_FILE}"
else
  if ! "${ENV_PREFIX}/bin/Rscript" -e 'suppressPackageStartupMessages(library(survey))' >/dev/null 2>&1; then
    conda env update -p "${ENV_PREFIX}" -f "${ENV_FILE}" --prune
  fi
fi

PATH="${ENV_PREFIX}/bin:${PATH}" python3 "${VALIDATOR}" --out "${OUT_PATH}"
