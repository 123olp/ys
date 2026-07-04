#!/usr/bin/env python3
"""验证本地 NHANES public-use LMF weighted-domain 输出报告边界。"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhanes-public-lmf-weighted-domain-output-local"
    / "validation.json"
)

FORBIDDEN_KEYS = {
    "SEQN",
    "RIDAGEYR",
    "RIAGENDR",
    "recordCount",
    "deathCount",
    "unweightedCount",
    "unweightedRecords",
    "unweightedDeaths",
    "weightSum",
    "weightedDeaths",
    "rawRows",
    "individualRiskScore",
    "deathDate",
    "publicAiPrompt",
    "publicAiResponse",
}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, nested in value.items():
            keys.add(str(key))
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_bool(data: dict[str, Any], key: str, expected: bool, errors: list[str], prefix: str) -> None:
    if data.get(key) is not expected:
        fail(errors, f"{prefix}.{key} must be {expected}")


def validate_output_path(path: Path, data: dict[str, Any], errors: list[str]) -> None:
    relative = repo_rel(path)
    if not relative.startswith("build/reports/"):
        fail(errors, "local weighted-domain output must stay under build/reports/")
    if relative.startswith("web/src/data/"):
        fail(errors, "local weighted-domain output must never be written under web/src/data/")
    scope = data.get("outputScope")
    if not isinstance(scope, dict):
        fail(errors, "outputScope must be an object")
        return
    if scope.get("storageClass") != "ignored-local-build-report":
        fail(errors, "outputScope.storageClass mismatch")
    if scope.get("actualPath") != relative:
        fail(errors, "outputScope.actualPath must match the validated input path")
    for key in (
        "publicExportAllowed",
        "webDataWritten",
        "trackedArtifactAllowed",
        "rawRowsPersistedAfterRun",
        "temporaryAnalysisCsvPersistedAfterRun",
    ):
        require_bool(scope, key, False, errors, "outputScope")


def validate_runtime(data: dict[str, Any], errors: list[str]) -> None:
    runtime = data.get("runtime")
    if not isinstance(runtime, dict):
        fail(errors, "runtime must be an object")
        return
    expected = {
        "estimatorBackend": "R survey",
        "designFunction": "svydesign",
        "domainSubsettingFunction": "survey::subset",
        "varianceMethod": "Taylor linearization",
        "domainIndicatorTiming": "post-design subset via survey::subset",
    }
    for key, value in expected.items():
        if runtime.get(key) != value:
            fail(errors, f"runtime.{key} mismatch")
    require_bool(runtime, "rowDropBeforeDesign", False, errors, "runtime")
    if not runtime.get("rVersion"):
        fail(errors, "runtime.rVersion must be present")
    if not runtime.get("surveyVersion"):
        fail(errors, "runtime.surveyVersion must be present")


def validate_boundary(data: dict[str, Any], errors: list[str]) -> None:
    boundary = data.get("modelUseBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "modelUseBoundary must be an object")
        return
    for key in (
        "containsRealNhanesPublicUseData",
        "containsRealWeightedRates",
        "containsRealDesignBasedIntervals",
    ):
        require_bool(boundary, key, True, errors, "modelUseBoundary")
    for key in (
        "containsRowLevelData",
        "containsIdentifiers",
        "containsExactDomainCountsInOutput",
        "publicOutputDisclosureReviewComplete",
        "realPublicationReliabilityReviewComplete",
        "publicWeightedDomainOutputAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
        "medicalAdviceAllowed",
    ):
        require_bool(boundary, key, False, errors, "modelUseBoundary")

    blocked = set(boundary.get("blockedUses", []))
    for item in (
        "public weighted-domain mortality publication",
        "public design-based confidence interval release",
        "calibrated Human Infra prediction",
        "individual prediction",
        "individual death-date output",
        "medical advice",
    ):
        if item not in blocked:
            fail(errors, f"modelUseBoundary.blockedUses missing {item!r}")


def validate_cells(data: dict[str, Any], errors: list[str]) -> tuple[int, int, int]:
    output = data.get("weightedDomainOutput")
    if not isinstance(output, dict):
        fail(errors, "weightedDomainOutput must be an object")
        return 0, 0, 0
    cells = output.get("cells")
    if not isinstance(cells, list):
        fail(errors, "weightedDomainOutput.cells must be a list")
        return 0, 0, 0
    if output.get("cellCount") != 8 or len(cells) != 8:
        fail(errors, "weightedDomainOutput must contain exactly 8 sex x ageBand cells")

    expected_pairs = {(sex, band) for sex in ("female", "male") for band in ("18-39", "40-59", "60-79", "80+")}
    observed_pairs: set[tuple[str, str]] = set()
    min_dof = 10**9
    release_blocked = 0
    quality_pass = 0
    for index, cell in enumerate(cells):
        if not isinstance(cell, dict):
            fail(errors, f"cell {index} must be an object")
            continue
        pair = (str(cell.get("sex")), str(cell.get("ageBand")))
        observed_pairs.add(pair)
        rate = cell.get("weightedMortalityRate")
        standard_error = cell.get("standardError")
        interval = cell.get("confidenceInterval95")
        dof = cell.get("domainDof")
        if not isinstance(rate, (int, float)) or not 0 <= float(rate) <= 1:
            fail(errors, f"cell {pair} weightedMortalityRate must be between 0 and 1")
        if not isinstance(standard_error, (int, float)) or float(standard_error) < 0:
            fail(errors, f"cell {pair} standardError must be non-negative")
        if not isinstance(interval, dict):
            fail(errors, f"cell {pair} confidenceInterval95 must be an object")
        else:
            lower = interval.get("lower")
            upper = interval.get("upper")
            if not isinstance(lower, (int, float)) or not isinstance(upper, (int, float)):
                fail(errors, f"cell {pair} confidence interval bounds must be numeric")
            elif float(lower) > float(rate) or float(upper) < float(rate) or float(lower) > float(upper):
                fail(errors, f"cell {pair} confidence interval must contain the point estimate")
            if interval.get("method") != "R survey svymean normal confint; interval is not bounded to [0, 1]":
                fail(errors, f"cell {pair} confidence interval method mismatch")
        if not isinstance(dof, int) or dof < 1:
            fail(errors, f"cell {pair} domainDof must be a positive integer")
        else:
            min_dof = min(min_dof, dof)
        flags = cell.get("localQualityFlags")
        if not isinstance(flags, dict):
            fail(errors, f"cell {pair} localQualityFlags must be an object")
        elif flags.get("minimumUnweightedCellRuleMet") is True:
            quality_pass += 1
        if cell.get("publicReleaseStatus") == "blocked-local-only-not-disclosure-reviewed":
            release_blocked += 1
        else:
            fail(errors, f"cell {pair} publicReleaseStatus must remain blocked")

    if observed_pairs != expected_pairs:
        fail(errors, f"weightedDomainOutput cells mismatch: {sorted(observed_pairs ^ expected_pairs)}")
    return len(cells), min_dof if min_dof != 10**9 else 0, quality_pass if release_blocked == len(cells) else quality_pass


def validate_report(path: Path, data: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    if data.get("schemaVersion") != "human-infra.nhanes-public-lmf-weighted-domain-output-local-run.v1":
        fail(errors, "schemaVersion mismatch")
    if data.get("status") != "local-real-weighted-domain-output-generated-not-public-not-reviewed":
        fail(errors, "status mismatch")
    if data.get("sourceId") != "nhanes-public-lmf-2017-2018":
        fail(errors, "sourceId mismatch")

    validate_output_path(path, data, errors)
    validate_runtime(data, errors)
    validate_boundary(data, errors)
    cell_count, min_dof, quality_pass = validate_cells(data, errors)

    keys = collect_keys(data)
    leaked = sorted(keys & FORBIDDEN_KEYS)
    if leaked:
        fail(errors, f"forbidden row/count-like keys present in local report: {leaked}")

    diagnostics = data.get("temporaryInputDiagnostics")
    if not isinstance(diagnostics, dict):
        fail(errors, "temporaryInputDiagnostics must be an object")
    else:
        if diagnostics.get("temporaryAnalysisCsvPersistedAfterRun") is not False:
            fail(errors, "temporary input CSV persistence flag must be false")

    summary = {
        "cellCount": cell_count,
        "minimumDomainDof": min_dof,
        "qualityPassCellCount": quality_pass,
        "containsRealWeightedRates": data.get("modelUseBoundary", {}).get("containsRealWeightedRates"),
        "containsRealDesignBasedIntervals": data.get("modelUseBoundary", {}).get("containsRealDesignBasedIntervals"),
        "publicWeightedDomainOutputAllowed": data.get("modelUseBoundary", {}).get("publicWeightedDomainOutputAllowed"),
        "webDataWritten": data.get("outputScope", {}).get("webDataWritten"),
    }
    return errors, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    data = load_json(input_path)
    errors, summary = validate_report(input_path, data)
    result = {
        "schemaVersion": "human-infra.nhanes-public-lmf-weighted-domain-output-local-run-validation.v1",
        "status": "pass" if not errors else "fail",
        "validatedAt": datetime.now(timezone.utc).isoformat(),
        "inputPath": repo_rel(input_path),
        "inputSha256": sha256_file(input_path),
        "summary": summary,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
