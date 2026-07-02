#!/usr/bin/env python3
"""Validate synthetic NHATS survey-design plan envelopes."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_survey_design_protocol.json"
)
DEFAULT_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_survey_design_test_cases.json"
)
DEFAULT_OUT = REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-survey-design-validation.json"

REQUIRED_COMPONENT_IDS = {
    "analysis_weight",
    "strata",
    "psu_or_cluster",
    "variance_method",
    "domain_subpopulation_rule",
    "missingness_and_route_rule",
    "round_linkage_rule",
    "finite_population_boundary",
}
REQUIRED_GATE_IDS = {
    "technical-paper-confirmed",
    "colectica-design-fields-confirmed",
    "round-specific-weight-selected",
    "strata-psu-fields-confirmed",
    "variance-method-selected",
    "domain-subpopulation-rule-selected",
    "missingness-route-map-ready",
    "disclosure-validation-passed",
    "weighted-estimator-script-reviewed",
}
ALLOWED_VARIANCE_METHODS = {
    "Taylor linearization",
    "replicate weights",
    "survey-package-compatible-plan",
}


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


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


def status_set(rows: Any, id_key: str) -> set[str]:
    if not isinstance(rows, list):
        return set()
    result: set[str] = set()
    for row in rows:
        if isinstance(row, dict) and isinstance(row.get(id_key), str):
            result.add(row[id_key])
    return result


def has_confirmed_field(plan: dict[str, Any], field_name: str) -> bool:
    field = plan.get(field_name)
    return (
        isinstance(field, dict)
        and isinstance(field.get("name"), str)
        and bool(field["name"].strip())
        and field.get("status") == "synthetic-confirmed"
    )


def validate_protocol(protocol: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if protocol.get("schemaVersion") != "human-infra.life-path-nhats-survey-design-protocol.v1":
        reasons.append("protocol schemaVersion mismatch")
    if protocol.get("sourceId") != "nhats":
        reasons.append("protocol sourceId must be nhats")
    if protocol.get("protocolId") != "nhats-r13-r14-survey-design-protocol-draft":
        reasons.append("protocolId mismatch")

    decision = protocol.get("currentDecision")
    required_false = {
        "surveyDesignReady",
        "weightedCountsAllowed",
        "weightedCurvesAllowed",
        "varianceEstimationAllowed",
        "populationInferenceAllowed",
        "publicExportAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    }
    if not isinstance(decision, dict):
        reasons.append("protocol currentDecision must be an object")
    else:
        for field in sorted(required_false):
            if decision.get(field) is not False:
                reasons.append(f"protocol currentDecision.{field} must be false")

    component_ids = status_set(protocol.get("requiredDesignComponents"), "id")
    missing_components = sorted(REQUIRED_COMPONENT_IDS - component_ids)
    if missing_components:
        reasons.append(f"protocol missing design components: {missing_components}")
    for component in protocol.get("requiredDesignComponents", []):
        if not isinstance(component, dict):
            reasons.append("protocol design component must be an object")
            continue
        if component.get("status") != "missing" or component.get("blocksWeightedEstimate") is not True:
            reasons.append(f"design component {component.get('id')!r} must be missing and blocking")

    gate_ids = status_set(protocol.get("readinessGates"), "id")
    missing_gates = sorted(REQUIRED_GATE_IDS - gate_ids)
    if missing_gates:
        reasons.append(f"protocol missing readiness gates: {missing_gates}")
    for gate in protocol.get("readinessGates", []):
        if not isinstance(gate, dict):
            reasons.append("protocol readiness gate must be an object")
            continue
        if gate.get("status") != "missing" or gate.get("blocksWeightedEstimate") is not True:
            reasons.append(f"readiness gate {gate.get('id')!r} must be missing and blocking")

    candidates = protocol.get("candidateFieldFamilies")
    if not isinstance(candidates, list) or len(candidates) < 3:
        reasons.append("protocol candidateFieldFamilies must include weight, strata and PSU candidates")
    else:
        for candidate in candidates:
            if not isinstance(candidate, dict):
                reasons.append("candidate field family must be an object")
                continue
            if candidate.get("status") != "candidate-pattern-only":
                reasons.append(f"candidate field {candidate.get('id')!r} must stay candidate-pattern-only")

    summary = protocol.get("gateSummary")
    if not (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_GATE_IDS)
    ):
        reasons.append("protocol gateSummary must keep every survey-design gate missing and blocking")

    source_trace = protocol.get("sourceTrace")
    if not (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and any("conditions-of-use" in url for url in source_trace)
        and any("cross-year-search" in url for url in source_trace)
        and any("NHATSUserGuideR14" in url for url in source_trace)
        and any("NHATSTechnicalPaper55" in url for url in source_trace)
    ):
        reasons.append("protocol sourceTrace must include official NHATS conditions, Cross-Year Search, User Guide and Technical Paper 55")

    return reasons


def validate_design_plan(plan: dict[str, Any], protocol: dict[str, Any]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if plan.get("schemaVersion") != "human-infra.synthetic-nhats-survey-design-plan.v1":
        reasons.append("design plan schemaVersion mismatch")
    if plan.get("sourceId") != protocol.get("sourceId"):
        reasons.append("sourceId does not match protocol")
    if plan.get("containsRealNhatsData") is not False:
        reasons.append("containsRealNhatsData must be false")
    if plan.get("containsRowLevelData") is not False:
        reasons.append("containsRowLevelData must be false")
    if plan.get("calibrationRequested") is not False:
        reasons.append("calibrationRequested must be false")
    if plan.get("individualPredictionRequested") is not False:
        reasons.append("individualPredictionRequested must be false")

    required_fields = {
        "weightField": "analysis weight",
        "strataField": "strata field",
        "psuOrClusterField": "PSU / variance-unit / cluster field",
    }
    for field_name, label in required_fields.items():
        if not has_confirmed_field(plan, field_name):
            reasons.append(f"missing confirmed {label}")

    variance_method = plan.get("varianceMethod")
    if variance_method not in ALLOWED_VARIANCE_METHODS:
        reasons.append(f"varianceMethod must be one of {sorted(ALLOWED_VARIANCE_METHODS)}")

    for field_name, label in (
        ("domainSubpopulationRule", "domain/subpopulation rule"),
        ("missingnessRouteRule", "missingness and route rule"),
        ("roundLinkageRule", "round linkage rule"),
    ):
        if not isinstance(plan.get(field_name), str) or not plan[field_name].strip():
            reasons.append(f"missing {label}")

    if plan.get("publicExportRequested") is True:
        reasons.append("publicExportRequested must be false for synthetic survey-design validation")
    if plan.get("populationInferenceRequested") is True:
        reasons.append("populationInferenceRequested must be false until real design and disclosure gates pass")
    if plan.get("disclosureValidationStatus") != "synthetic-pass":
        reasons.append("disclosureValidationStatus must be synthetic-pass for synthetic weighted diagnostics")

    decision = "allow-weighted-diagnostics" if not reasons else "block-weighted-estimate"
    return decision, reasons


def build_report(
    protocol_path: Path,
    test_cases_path: Path,
    protocol: dict[str, Any],
    test_cases: dict[str, Any],
) -> dict[str, Any]:
    protocol_reasons = validate_protocol(protocol)
    boundary = test_cases.get("currentBoundary")
    boundary_reasons: list[str] = []
    if test_cases.get("schemaVersion") != "human-infra.life-path-nhats-survey-design-test-cases.v1":
        boundary_reasons.append("test cases schemaVersion mismatch")
    if test_cases.get("sourceId") != protocol.get("sourceId"):
        boundary_reasons.append("test cases sourceId must match protocol")
    if test_cases.get("protocolId") != protocol.get("protocolId"):
        boundary_reasons.append("test cases protocolId must match protocol")
    if not isinstance(boundary, dict):
        boundary_reasons.append("test cases currentBoundary must be an object")
    else:
        if boundary.get("containsRealNhatsData") is not False:
            boundary_reasons.append("test cases must not contain real NHATS data")
        if boundary.get("containsSyntheticOnly") is not True:
            boundary_reasons.append("test cases must be synthetic only")
        if boundary.get("calibrationAllowed") is not False:
            boundary_reasons.append("test cases must keep calibration disallowed")
        if boundary.get("individualPredictionAllowed") is not False:
            boundary_reasons.append("test cases must keep individual prediction disallowed")

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
                        "expectedDecision": "block-weighted-estimate",
                        "observedDecision": "block-weighted-estimate",
                        "status": "FAIL",
                        "reasons": ["case must be an object"],
                    }
                )
                continue
            design_plan = case.get("designPlan")
            expected = case.get("expectedDecision")
            if not isinstance(design_plan, dict):
                observed, reasons = "block-weighted-estimate", ["case designPlan must be an object"]
            else:
                observed, reasons = validate_design_plan(design_plan, protocol)
            if protocol_reasons:
                observed = "block-weighted-estimate"
                reasons = [*reasons, *protocol_reasons]
            if boundary_reasons:
                observed = "block-weighted-estimate"
                reasons = [*reasons, *boundary_reasons]
            status = "PASS" if observed == expected else "FAIL"
            if status == "FAIL":
                case_failures += 1
            if observed == "allow-weighted-diagnostics":
                allowed_count += 1
            if observed == "block-weighted-estimate":
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
        if not protocol_reasons
        and not boundary_reasons
        and case_count > 0
        and case_failures == 0
        and allowed_count > 0
        and blocked_count > 0
        else "FAIL"
    )
    return {
        "schemaVersion": "human-infra.life-path-nhats-survey-design-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "testCasesPath": repo_rel(test_cases_path),
        "testCasesSha256": sha256_file(test_cases_path),
        "overallStatus": overall,
        "boundary": {
            "containsRealNhatsData": False,
            "containsSyntheticOnly": True,
            "surveyDesignProofOnly": True,
            "publicInferenceProofOnly": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "note": "This report validates synthetic survey-design envelopes only; it does not validate real NHATS extraction, design-weighted estimation, population inference, calibration, clinical use or individual prediction."
        },
        "summary": {
            "caseCount": case_count,
            "pass": sum(1 for row in case_rows if row["status"] == "PASS"),
            "fail": case_failures,
            "allowedCount": allowed_count,
            "blockedCount": blocked_count,
            "protocolIssueCount": len(protocol_reasons),
            "boundaryIssueCount": len(boundary_reasons)
        },
        "cases": case_rows
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    protocol_path = args.protocol.resolve()
    test_cases_path = args.test_cases.resolve()
    out_path = args.out.resolve()
    protocol = load_json(protocol_path)
    test_cases = load_json(test_cases_path)
    report = build_report(protocol_path, test_cases_path, protocol, test_cases)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
