#!/usr/bin/env python3
"""Validate synthetic NHATS disclosure-control output envelopes."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_POLICY = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_disclosure_control_policy.json"
)
DEFAULT_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_disclosure_control_test_cases.json"
)
DEFAULT_OUT = REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-disclosure-control-validation.json"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
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


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


def validate_policy(policy: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if policy.get("schemaVersion") != "human-infra.life-path-nhats-disclosure-control-policy.v1":
        reasons.append("policy schemaVersion mismatch")
    if policy.get("sourceId") != "nhats":
        reasons.append("policy sourceId must be nhats")

    decision = policy.get("currentDecision")
    required_false = {
        "publicExportAllowed",
        "rowLevelExportAllowed",
        "publicAiUploadAllowed",
        "smallCellExportAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    }
    if not isinstance(decision, dict):
        reasons.append("policy currentDecision must be an object")
    else:
        for field in sorted(required_false):
            if decision.get(field) is not False:
                reasons.append(f"policy currentDecision.{field} must be false")

    rules = policy.get("rules")
    if not isinstance(rules, dict):
        reasons.append("policy rules must be an object")
        return reasons
    if rules.get("aggregateOnly") is not True:
        reasons.append("policy rules.aggregateOnly must be true")
    if rules.get("smallCellThreshold") != 5:
        reasons.append("policy smallCellThreshold must be 5")

    allowed = as_set(rules.get("allowedOutputTypes"))
    required_allowed = {
        "cohort_flow_counts",
        "endpoint_route_counts",
        "missingness_table",
        "survey_design_plan",
        "disclosure_control_report",
        "aggregate_functional_survival_distribution",
    }
    missing_allowed = sorted(required_allowed - allowed)
    if missing_allowed:
        reasons.append(f"policy missing allowed output types: {missing_allowed}")

    required_fields = as_set(rules.get("requiredReportFields"))
    for field in (
        "schemaVersion",
        "sourceId",
        "outputId",
        "outputType",
        "containsRowLevelData",
        "publicExportRequested",
        "publicAiUploadRequested",
        "cells",
    ):
        if field not in required_fields:
            reasons.append(f"policy missing required report field: {field}")

    return reasons


def validate_case(output: dict[str, Any], policy: dict[str, Any]) -> tuple[str, list[str]]:
    rules = policy.get("rules", {})
    threshold = int(rules.get("smallCellThreshold", 5))
    allowed_output_types = as_set(rules.get("allowedOutputTypes"))
    forbidden_output_types = as_set(rules.get("forbiddenOutputTypes"))
    required_fields = as_set(rules.get("requiredReportFields"))
    required_cell_fields = as_set(rules.get("cellFields"))
    prohibited_keys = as_set(rules.get("prohibitedKeys"))

    reasons: list[str] = []
    missing_fields = sorted(field for field in required_fields if field not in output)
    if missing_fields:
        reasons.append(f"missing required fields: {missing_fields}")

    if output.get("sourceId") != policy.get("sourceId"):
        reasons.append("sourceId does not match policy sourceId")

    output_type = output.get("outputType")
    if output_type not in allowed_output_types:
        reasons.append(f"outputType {output_type!r} is not allowed")
    if output_type in forbidden_output_types:
        reasons.append(f"outputType {output_type!r} is explicitly forbidden")

    if output.get("containsRowLevelData") is not False:
        reasons.append("containsRowLevelData must be false")
    if output.get("publicAiUploadRequested") is not False:
        reasons.append("publicAiUploadRequested must be false")

    observed_prohibited_keys = sorted(collect_keys(output) & prohibited_keys)
    if observed_prohibited_keys:
        reasons.append(f"prohibited keys present: {observed_prohibited_keys}")

    cells = output.get("cells")
    if not isinstance(cells, list):
        reasons.append("cells must be a list")
    else:
        for index, cell in enumerate(cells):
            if not isinstance(cell, dict):
                reasons.append(f"cell[{index}] must be an object")
                continue
            missing_cell_fields = sorted(field for field in required_cell_fields if field not in cell)
            if missing_cell_fields:
                reasons.append(f"cell[{index}] missing fields: {missing_cell_fields}")
                continue
            count = cell.get("count")
            if not isinstance(count, int) or count < 0:
                reasons.append(f"cell[{index}].count must be a non-negative integer")
                continue
            if (
                output.get("publicExportRequested") is True
                and count < threshold
                and cell.get("suppressed") is not True
            ):
                reasons.append(f"cell[{index}] count below {threshold} is not suppressed")

    decision = "allow-export" if not reasons else "block-export"
    return decision, reasons


def build_report(
    policy_path: Path,
    test_cases_path: Path,
    policy: dict[str, Any],
    test_cases: dict[str, Any],
) -> dict[str, Any]:
    policy_reasons = validate_policy(policy)
    boundary = test_cases.get("currentBoundary")
    boundary_reasons: list[str] = []
    if test_cases.get("schemaVersion") != "human-infra.life-path-nhats-disclosure-control-test-cases.v1":
        boundary_reasons.append("test cases schemaVersion mismatch")
    if test_cases.get("sourceId") != policy.get("sourceId"):
        boundary_reasons.append("test cases sourceId must match policy")
    if not isinstance(boundary, dict):
        boundary_reasons.append("test cases currentBoundary must be an object")
    else:
        if boundary.get("containsRealNhatsData") is not False:
            boundary_reasons.append("test cases must not contain real NHATS data")
        if boundary.get("containsSyntheticOnly") is not True:
            boundary_reasons.append("test cases must be synthetic only")
        if boundary.get("calibrationAllowed") is not False:
            boundary_reasons.append("test cases must keep calibration disallowed")

    case_rows: list[dict[str, Any]] = []
    cases = test_cases.get("cases")
    case_failures = 0
    allowed_count = 0
    blocked_count = 0
    if isinstance(cases, list):
        for case in cases:
            if not isinstance(case, dict):
                case_failures += 1
                case_rows.append(
                    {
                        "id": "invalid-case",
                        "expectedDecision": "block-export",
                        "observedDecision": "block-export",
                        "status": "FAIL",
                        "reasons": ["case must be an object"],
                    }
                )
                continue
            output = case.get("output")
            expected = case.get("expectedDecision")
            if not isinstance(output, dict):
                observed, reasons = "block-export", ["case output must be an object"]
            else:
                observed, reasons = validate_case(output, policy)
            if policy_reasons:
                observed = "block-export"
                reasons = [*reasons, *policy_reasons]
            if boundary_reasons:
                observed = "block-export"
                reasons = [*reasons, *boundary_reasons]
            status = "PASS" if observed == expected else "FAIL"
            if status == "FAIL":
                case_failures += 1
            if observed == "allow-export":
                allowed_count += 1
            if observed == "block-export":
                blocked_count += 1
            case_rows.append(
                {
                    "id": case.get("id"),
                    "expectedDecision": expected,
                    "observedDecision": observed,
                    "status": status,
                    "reasons": reasons,
                }
            )
    else:
        case_failures += 1

    case_count = len(cases) if isinstance(cases, list) else 0
    overall = (
        "PASS"
        if not policy_reasons
        and not boundary_reasons
        and case_count > 0
        and case_failures == 0
        and allowed_count > 0
        and blocked_count > 0
        else "FAIL"
    )
    return {
        "schemaVersion": "human-infra.life-path-nhats-disclosure-control-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "policyPath": repo_rel(policy_path),
        "policySha256": sha256_file(policy_path),
        "testCasesPath": repo_rel(test_cases_path),
        "testCasesSha256": sha256_file(test_cases_path),
        "overallStatus": overall,
        "boundary": {
            "containsRealNhatsData": False,
            "containsSyntheticOnly": True,
            "publicExportProofOnly": True,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "note": "This report validates synthetic output envelopes only; it does not validate real NHATS extraction, calibration, causal inference, clinical use or individual prediction."
        },
        "summary": {
            "caseCount": case_count,
            "pass": sum(1 for row in case_rows if row["status"] == "PASS"),
            "fail": case_failures,
            "allowedCount": allowed_count,
            "blockedCount": blocked_count,
            "policyIssueCount": len(policy_reasons),
            "boundaryIssueCount": len(boundary_reasons)
        },
        "cases": case_rows
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy_path = args.policy.resolve()
    test_cases_path = args.test_cases.resolve()
    out_path = args.out.resolve()
    policy = load_json(policy_path)
    test_cases = load_json(test_cases_path)
    report = build_report(policy_path, test_cases_path, policy, test_cases)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
