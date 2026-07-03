#!/usr/bin/env python3
"""Validate the NHATS route-classifier readiness gate."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
MANUAL_DIR = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
)
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
DEFAULT_ROUTE_FIELD_REGISTER = MANUAL_DIR / "life_path_nhats_route_field_discovery_register.json"
DEFAULT_VALUE_LABEL_EXECUTION = (
    MANUAL_DIR / "life_path_nhats_colectica_value_label_review_execution_register.json"
)
DEFAULT_AUTHENTICATED_CAPTURE_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_MISSINGNESS_ROUTE_PROTOCOL = MANUAL_DIR / "life_path_nhats_missingness_route_protocol.json"
DEFAULT_PREOUTCOME_AGGREGATION_PROTOCOL = (
    MANUAL_DIR / "life_path_nhats_preoutcome_aggregation_protocol.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-classifier-readiness-validation.json"
)

REQUIRED_INPUT_FAMILIES = {
    "identity_join_key",
    "round13_baseline_eligibility",
    "round14_interview_status",
    "proxy_status",
    "facility_residential_status",
    "death_decedent_indicator",
    "nonresponse_missing_code",
    "design_weight_linkage",
    "disclosure_cell_count",
}
REQUIRED_PROMOTION_GATES = {
    "real-data-access-approved",
    "controlled-colectica-login-recorded",
    "authenticated-variable-pages-captured",
    "value-labels-confirmed",
    "question-text-universe-skip-logic-confirmed",
    "route-value-crosswalk-confirmed",
    "variable-specific-missing-code-map-confirmed",
    "sensitive-death-boundary-exclusion-reviewed",
    "second-reviewer-signoff",
    "survey-design-ready",
    "disclosure-review-before-public-output",
    "route-classifier-code-review",
}
REQUIRED_FALSE_DECISIONS = {
    "colecticaValueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkConfirmed",
    "variableSpecificMissingCodeMapConfirmed",
    "secondReviewerSignoff",
    "controlledColecticaCaptureComplete",
    "realDataAccessApproved",
    "routeClassifierReady",
    "classifierCodeAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "routeFieldCandidatesKnown",
    "standardNegativeCodeFamilyKnown",
}
ALLOWED_INPUT_FAMILY_STATUSES = {
    "crosswalk-candidate-only",
    "boundary-only-sensitive-fields-excluded",
    "standard-family-only-variable-specific-map-blocked",
    "computed-output-only",
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


def row_ids(rows: Any, key: str = "id") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append(
        {
            "id": check_id,
            "status": "PASS" if passed else "FAIL",
            "detail": detail,
        }
    )


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_register(
    register: dict[str, Any],
    route_field_register: dict[str, Any],
    value_label_execution: dict[str, Any],
    authenticated_capture_template: dict[str, Any],
    missingness_route_protocol: dict[str, Any],
    preoutcome_aggregation_protocol: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-route-classifier-readiness.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("readinessId") == "nhats-r13-r14-route-classifier-readiness-2026-07-03"
        and register.get("status") == "blocked-colectica-and-real-data-required"
        and register.get("routeFieldDiscoveryRegisterId") == route_field_register.get("registerId")
        and register.get("valueLabelExecutionRegisterId")
        == value_label_execution.get("executionRegisterId")
        and register.get("authenticatedCaptureTemplateId")
        == authenticated_capture_template.get("templateId")
        and register.get("missingnessRouteProtocolId")
        == missingness_route_protocol.get("protocolId")
        and register.get("preOutcomeAggregationProtocolId")
        == preoutcome_aggregation_protocol.get("protocolId")
    )
    add_check(
        checks,
        "readiness-identity-and-upstream-bindings",
        identity_ok,
        "readiness gate must bind route-field, value-label execution, authenticated capture, missingness-route and pre-outcome aggregation upstreams",
    )

    decision = register.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if isinstance(decision, dict):
        for key in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is True
        for key in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(key) is False
    add_check(
        checks,
        "decision-boundary",
        decision_ok,
        "only route-field candidates and standard negative-code family may be known; every classifier, extraction, export, calibration and individual-prediction decision must remain false",
    )

    input_families = register.get("classifierInputFamilies")
    family_ids = row_ids(input_families)
    family_shape_ok = isinstance(input_families, list) and all(
        isinstance(row, dict)
        and isinstance(row.get("requires"), list)
        and len(row["requires"]) >= 2
        and row.get("promotionAllowed") is False
        and row.get("candidateStatus") in ALLOWED_INPUT_FAMILY_STATUSES
        for row in input_families or []
    )
    add_check(
        checks,
        "classifier-input-families",
        REQUIRED_INPUT_FAMILIES.issubset(family_ids) and family_shape_ok,
        f"missing={sorted(REQUIRED_INPUT_FAMILIES - family_ids)}",
    )

    promotion_gates = register.get("promotionGates")
    gate_ids = row_ids(promotion_gates)
    gates_blocked = isinstance(promotion_gates, list) and all(
        isinstance(gate, dict)
        and gate.get("blocksRouteClassifier") is True
        and gate.get("status") in {"blocked", "prepared-but-not-sufficient"}
        for gate in promotion_gates
    )
    add_check(
        checks,
        "promotion-gates-block-classifier",
        REQUIRED_PROMOTION_GATES.issubset(gate_ids) and gates_blocked,
        f"missing={sorted(REQUIRED_PROMOTION_GATES - gate_ids)}",
    )

    source_trace = register.get("sourceTrace")
    source_paths = {
        str(row.get("path", ""))
        for row in source_trace
        if isinstance(row, dict)
    } if isinstance(source_trace, list) else set()
    source_trace_ok = {
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_field_discovery_register.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_execution_register.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_authenticated_capture_template.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_protocol.json",
        "domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_preoutcome_aggregation_protocol.json",
    }.issubset(source_paths)
    add_check(
        checks,
        "source-trace-paths",
        source_trace_ok,
        "source trace must point to the five upstream NHATS route/classifier readiness records",
    )

    prohibited = register.get("prohibitedActions")
    prohibited_ok = (
        isinstance(prohibited, list)
        and has_text(prohibited, "candidate variable names")
        and has_text(prohibited, "crosswalk field names")
        and has_text(prohibited, "aggregate real NHATS rows")
        and has_text(prohibited, "public systems")
        and has_text(prohibited, "individual prediction")
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "readiness gate must prohibit candidate-name routing, real aggregation, public export, calibration and individual prediction",
    )

    next_evidence = register.get("nextEvidenceRequired")
    next_evidence_ok = (
        isinstance(next_evidence, list)
        and has_text(next_evidence, "governed NHATS data access")
        and has_text(next_evidence, "Colectica")
        and has_text(next_evidence, "value labels")
        and has_text(next_evidence, "missing-code map")
        and has_text(next_evidence, "survey design")
        and has_text(next_evidence, "second reviewer")
    )
    add_check(
        checks,
        "next-evidence-required",
        next_evidence_ok,
        "next evidence must require governed data access, Colectica capture, labels, missing-code map, survey design and second review",
    )

    upstream_blockers_ok = (
        route_field_register.get("status") == "crosswalk-confirmed-colectica-pending-cannot-route"
        and value_label_execution.get("currentDecision", {}).get("routeClassifierAllowed") is False
        and value_label_execution.get("routeValueCrosswalkDraft", {}).get("promotionAllowed") is False
        and value_label_execution.get("negativeMissingCodeMap", {}).get(
            "variableSpecificMapReady"
        )
        is False
        and authenticated_capture_template.get("currentDecision", {}).get(
            "routeClassifierAllowed"
        )
        is False
        and missingness_route_protocol.get("status") == "protocol-only-cannot-route-yet"
        and preoutcome_aggregation_protocol.get("status")
        == "protocol-only-preoutcome-rules-frozen-l4-blocked"
    )
    add_check(
        checks,
        "upstream-blockers-inherited",
        upstream_blockers_ok,
        "readiness gate must inherit route-field, Colectica, missingness-route and pre-outcome aggregation blockers",
    )

    return checks


def build_report(
    register_path: Path,
    route_field_register_path: Path,
    value_label_execution_path: Path,
    authenticated_capture_template_path: Path,
    missingness_route_protocol_path: Path,
    preoutcome_aggregation_protocol_path: Path,
) -> dict[str, Any]:
    register = load_json(register_path)
    route_field_register = load_json(route_field_register_path)
    value_label_execution = load_json(value_label_execution_path)
    authenticated_capture_template = load_json(authenticated_capture_template_path)
    missingness_route_protocol = load_json(missingness_route_protocol_path)
    preoutcome_aggregation_protocol = load_json(preoutcome_aggregation_protocol_path)

    checks = validate_register(
        register,
        route_field_register,
        value_label_execution,
        authenticated_capture_template,
        missingness_route_protocol,
        preoutcome_aggregation_protocol,
    )
    summary = summarize(checks)
    decision = register.get("currentDecision", {})
    return {
        "schemaVersion": "human-infra.life-path-nhats-route-classifier-readiness-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "routeFieldDiscoveryRegisterPath": repo_rel(route_field_register_path),
        "routeFieldDiscoveryRegisterSha256": sha256_file(route_field_register_path),
        "valueLabelExecutionRegisterPath": repo_rel(value_label_execution_path),
        "valueLabelExecutionRegisterSha256": sha256_file(value_label_execution_path),
        "authenticatedCaptureTemplatePath": repo_rel(authenticated_capture_template_path),
        "authenticatedCaptureTemplateSha256": sha256_file(authenticated_capture_template_path),
        "missingnessRouteProtocolPath": repo_rel(missingness_route_protocol_path),
        "missingnessRouteProtocolSha256": sha256_file(missingness_route_protocol_path),
        "preOutcomeAggregationProtocolPath": repo_rel(preoutcome_aggregation_protocol_path),
        "preOutcomeAggregationProtocolSha256": sha256_file(preoutcome_aggregation_protocol_path),
        "readinessId": register.get("readinessId"),
        "status": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "classifierInputFamilyCount": len(register.get("classifierInputFamilies", [])),
        "promotionGateCount": len(register.get("promotionGates", [])),
        "boundary": {
            "routeClassifierReady": decision.get("routeClassifierReady"),
            "classifierCodeAllowed": decision.get("classifierCodeAllowed"),
            "realExtractionAllowed": decision.get("realExtractionAllowed"),
            "aggregateCohortFlowAllowed": decision.get("aggregateCohortFlowAllowed"),
            "weightedRouteCountsAllowed": decision.get("weightedRouteCountsAllowed"),
            "publicExportAllowed": decision.get("publicExportAllowed"),
            "calibrationAllowed": decision.get("calibrationAllowed"),
            "individualPredictionAllowed": decision.get("individualPredictionAllowed"),
        },
        "checks": checks,
        "note": "This validation proves only that a blocked NHATS route-classifier readiness gate exists and inherits upstream blockers. It does not prove real data access, Colectica capture, value-label confirmation, route-value crosswalk readiness, survey-design readiness, extraction readiness, calibration or individual prediction readiness.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--route-field-register", type=Path, default=DEFAULT_ROUTE_FIELD_REGISTER)
    parser.add_argument("--value-label-execution", type=Path, default=DEFAULT_VALUE_LABEL_EXECUTION)
    parser.add_argument(
        "--authenticated-capture-template",
        type=Path,
        default=DEFAULT_AUTHENTICATED_CAPTURE_TEMPLATE,
    )
    parser.add_argument(
        "--missingness-route-protocol",
        type=Path,
        default=DEFAULT_MISSINGNESS_ROUTE_PROTOCOL,
    )
    parser.add_argument(
        "--preoutcome-aggregation-protocol",
        type=Path,
        default=DEFAULT_PREOUTCOME_AGGREGATION_PROTOCOL,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    report = build_report(
        args.register.resolve(),
        args.route_field_register.resolve(),
        args.value_label_execution.resolve(),
        args.authenticated_capture_template.resolve(),
        args.missingness_route_protocol.resolve(),
        args.preoutcome_aggregation_protocol.resolve(),
    )
    out_path = args.out.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={report['status']} checks={report['summary']}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
