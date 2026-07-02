#!/usr/bin/env python3
"""Validate synthetic NHATS missingness and endpoint-route envelopes."""

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
    / "life_path_nhats_missingness_route_protocol.json"
)
DEFAULT_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_missingness_route_test_cases.json"
)
DEFAULT_OUT = REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-missingness-route-validation.json"

REQUIRED_ROUTE_CLASSES = {
    "alive_self_interview",
    "alive_proxy_interview",
    "alive_facility_or_residential_route",
    "alive_known_not_interviewed",
    "decedent_or_death_boundary",
    "missing_or_nonresponse",
    "not_classifiable",
    "excluded_sensitive_or_restricted_required",
    "suppressed_small_cell",
}
REQUIRED_ROUTE_FIELDS = {
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
REQUIRED_GATE_IDS = {
    "colectica-route-fields-confirmed",
    "baseline-eligibility-rule-confirmed",
    "followup-status-fields-confirmed",
    "death-boundary-fields-confirmed",
    "proxy-facility-route-fields-confirmed",
    "missing-code-crosswalk-ready",
    "survey-design-linkage-ready",
    "disclosure-control-ready",
    "route-classifier-script-reviewed",
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


def validate_protocol(protocol: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if protocol.get("schemaVersion") != "human-infra.life-path-nhats-missingness-route-protocol.v1":
        reasons.append("protocol schemaVersion mismatch")
    if protocol.get("sourceId") != "nhats":
        reasons.append("protocol sourceId must be nhats")
    if protocol.get("protocolId") != "nhats-r13-r14-missingness-route-protocol-draft":
        reasons.append("protocolId mismatch")
    if protocol.get("status") != "protocol-only-cannot-route-yet":
        reasons.append("protocol status must remain protocol-only-cannot-route-yet")

    decision = protocol.get("currentDecision")
    required_false = {
        "routeMapReady",
        "endpointClassificationAllowed",
        "missingnessRateAllowed",
        "weightedRouteCountsAllowed",
        "functionalSurvivalCurveAllowed",
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

    route_classes = protocol.get("requiredRouteClasses")
    missing_route_classes = sorted(REQUIRED_ROUTE_CLASSES - row_ids(route_classes))
    if missing_route_classes:
        reasons.append(f"protocol missing route classes: {missing_route_classes}")
    if isinstance(route_classes, list):
        for route_class in route_classes:
            if not isinstance(route_class, dict):
                reasons.append("route class must be an object")
                continue
            if route_class.get("status") != "unconfirmed":
                reasons.append(f"route class {route_class.get('id')!r} must remain unconfirmed")
            if route_class.get("blocksEndpointClassification") is not True:
                reasons.append(f"route class {route_class.get('id')!r} must block endpoint classification")
            if not str(route_class.get("minimumEvidence", "")).strip():
                reasons.append(f"route class {route_class.get('id')!r} missing minimum evidence")

    route_fields = protocol.get("requiredRouteFields")
    missing_route_fields = sorted(REQUIRED_ROUTE_FIELDS - row_ids(route_fields))
    if missing_route_fields:
        reasons.append(f"protocol missing route fields: {missing_route_fields}")
    if isinstance(route_fields, list):
        for route_field in route_fields:
            if not isinstance(route_field, dict):
                reasons.append("route field must be an object")
                continue
            if route_field.get("status") != "missing":
                reasons.append(f"route field {route_field.get('id')!r} must remain missing")
            if route_field.get("blocksEndpointClassification") is not True:
                reasons.append(f"route field {route_field.get('id')!r} must block endpoint classification")

    candidates = protocol.get("candidateFieldFamilies")
    if not isinstance(candidates, list) or len(candidates) < 5:
        reasons.append("protocol candidateFieldFamilies must include identity, status, proxy, facility, death and missing-code candidates")
    else:
        for candidate in candidates:
            if not isinstance(candidate, dict):
                reasons.append("candidate field family must be an object")
                continue
            if candidate.get("status") != "candidate-pattern-only":
                reasons.append(f"candidate field {candidate.get('id')!r} must stay candidate-pattern-only")

    rules = protocol.get("dominanceRules")
    if not (
        isinstance(rules, list)
        and has_text(rules, "death-boundary-dominates-functional-state")
        and has_text(rules, "missingness-is-not-outcome")
        and has_text(rules, "proxy-and-facility-stay-separate")
        and has_text(rules, "small-cell-suppression-before-public-export")
    ):
        reasons.append("protocol dominanceRules must register death, missingness, route-separation and small-cell rules")

    gates = protocol.get("readinessGates")
    missing_gates = sorted(REQUIRED_GATE_IDS - row_ids(gates))
    if missing_gates:
        reasons.append(f"protocol missing readiness gates: {missing_gates}")
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                reasons.append("readiness gate must be an object")
                continue
            if gate.get("status") != "missing" or gate.get("blocksEndpointClassification") is not True:
                reasons.append(f"readiness gate {gate.get('id')!r} must be missing and blocking")

    summary = protocol.get("gateSummary")
    if not (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_GATE_IDS)
    ):
        reasons.append("protocol gateSummary must keep every missingness-route gate missing and blocking")

    source_trace = protocol.get("sourceTrace")
    if not (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
    ):
        reasons.append("protocol sourceTrace must include official NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55")

    prohibited = protocol.get("prohibitedActions", [])
    if not (
        has_text(prohibited, "exact route fields")
        and has_text(prohibited, "missingness")
        and has_text(prohibited, "weighted route counts")
        and has_text(prohibited, "public AI")
        and has_text(prohibited, "individual death dates")
    ):
        reasons.append("protocol prohibitedActions must block premature routing, missingness-as-outcome, weighted counts, public AI and individual death-date outputs")

    return reasons


def validate_route_envelope(envelope: dict[str, Any], protocol: dict[str, Any]) -> tuple[str, str | None, list[str]]:
    reasons: list[str] = []
    if envelope.get("schemaVersion") != "human-infra.synthetic-nhats-route-envelope.v1":
        reasons.append("route envelope schemaVersion mismatch")
    if envelope.get("sourceId") != protocol.get("sourceId"):
        reasons.append("sourceId does not match protocol")
    if envelope.get("containsRealNhatsData") is not False:
        reasons.append("containsRealNhatsData must be false")
    if envelope.get("containsRowLevelData") is not False:
        reasons.append("containsRowLevelData must be false")
    if envelope.get("publicAiUploadRequested") is not False:
        reasons.append("publicAiUploadRequested must be false")
    if envelope.get("calibrationRequested") is not False:
        reasons.append("calibrationRequested must be false")
    if envelope.get("individualPredictionRequested") is not False:
        reasons.append("individualPredictionRequested must be false")

    signals = envelope.get("statusSignals")
    route_class: str | None = None
    if not isinstance(signals, dict):
        reasons.append("statusSignals must be an object")
    else:
        alive = signals.get("aliveStatus")
        death = signals.get("deathIndicator")
        missing = signals.get("missingOrNonresponse")
        restricted = signals.get("restrictedRequired")
        interview_route = signals.get("interviewRoute")
        proxy = signals.get("proxyStatus")
        facility = signals.get("facilityResidentialStatus")
        known_alive_not_interviewed = signals.get("knownAliveNotInterviewed")

        if alive is True and death is True:
            route_class = "not_classifiable"
            reasons.append("aliveStatus and deathIndicator conflict")
        elif restricted is True:
            route_class = "excluded_sensitive_or_restricted_required"
            reasons.append("route requires sensitive or restricted files")
        elif missing is True or envelope.get("missingCodeStatus") != "resolved":
            route_class = "missing_or_nonresponse"
            reasons.append("missing or nonresponse route cannot be endpoint-classified")
        elif death is True:
            route_class = "decedent_or_death_boundary"
        elif alive is True:
            if known_alive_not_interviewed is True:
                route_class = "alive_known_not_interviewed"
            elif facility is True or interview_route == "facility":
                route_class = "alive_facility_or_residential_route"
            elif proxy is True or interview_route == "proxy":
                route_class = "alive_proxy_interview"
            elif interview_route == "self":
                route_class = "alive_self_interview"
            else:
                route_class = "not_classifiable"
                reasons.append("alive route lacks self/proxy/facility/known-alive route evidence")
        else:
            route_class = "not_classifiable"
            reasons.append("status signals do not support a safe route class")

    disclosure = envelope.get("disclosure")
    if not isinstance(disclosure, dict):
        reasons.append("disclosure must be an object")
    else:
        count = disclosure.get("cellCount")
        suppressed = disclosure.get("suppressed")
        if not isinstance(count, int) or count < 0:
            reasons.append("disclosure.cellCount must be a non-negative integer")
        if envelope.get("publicExportRequested") is True:
            if not isinstance(count, int):
                pass
            elif count < 5 and suppressed is not True:
                route_class = "suppressed_small_cell"
                reasons.append("public export requested for unsuppressed n < 5 route cell")
            elif count < 5 and suppressed is True:
                route_class = "suppressed_small_cell"

    expected_route = envelope.get("expectedRouteClass")
    if isinstance(expected_route, str) and route_class != expected_route:
        reasons.append(f"expectedRouteClass={expected_route!r} but observed={route_class!r}")

    decision = "allow-route-classification" if not reasons else "block-route-classification"
    if route_class == "missing_or_nonresponse":
        decision = "block-route-classification"
    if route_class == "not_classifiable":
        decision = "block-route-classification"
    if route_class == "excluded_sensitive_or_restricted_required":
        decision = "block-route-classification"
    return decision, route_class, reasons


def build_report(
    protocol_path: Path,
    test_cases_path: Path,
    protocol: dict[str, Any],
    test_cases: dict[str, Any],
) -> dict[str, Any]:
    protocol_reasons = validate_protocol(protocol)
    boundary = test_cases.get("currentBoundary")
    boundary_reasons: list[str] = []
    if test_cases.get("schemaVersion") != "human-infra.life-path-nhats-missingness-route-test-cases.v1":
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
        if boundary.get("routeMapProofOnly") is not True:
            boundary_reasons.append("test cases must be route-map proof only")
        if boundary.get("calibrationAllowed") is not False:
            boundary_reasons.append("test cases must keep calibration disallowed")
        if boundary.get("individualPredictionAllowed") is not False:
            boundary_reasons.append("test cases must keep individual prediction disallowed")

    case_rows: list[dict[str, Any]] = []
    cases = test_cases.get("cases")
    case_failures = 0
    allowed_count = 0
    blocked_count = 0
    observed_route_classes: set[str] = set()
    if isinstance(cases, list):
        for case in cases:
            if not isinstance(case, dict):
                case_failures += 1
                case_rows.append(
                    {
                        "id": "invalid-case",
                        "expectedDecision": "block-route-classification",
                        "observedDecision": "block-route-classification",
                        "observedRouteClass": None,
                        "status": "FAIL",
                        "reasons": ["case must be an object"],
                    }
                )
                continue
            envelope = case.get("routeEnvelope")
            expected = case.get("expectedDecision")
            if not isinstance(envelope, dict):
                observed, route_class, reasons = (
                    "block-route-classification",
                    None,
                    ["case routeEnvelope must be an object"],
                )
            else:
                observed, route_class, reasons = validate_route_envelope(envelope, protocol)
            if route_class:
                observed_route_classes.add(route_class)
            if protocol_reasons:
                observed = "block-route-classification"
                reasons = [*reasons, *protocol_reasons]
            if boundary_reasons:
                observed = "block-route-classification"
                reasons = [*reasons, *boundary_reasons]
            status = "PASS" if observed == expected else "FAIL"
            if status == "FAIL":
                case_failures += 1
            if observed == "allow-route-classification":
                allowed_count += 1
            if observed == "block-route-classification":
                blocked_count += 1
            case_rows.append(
                {
                    "id": case.get("id"),
                    "expectedDecision": expected,
                    "observedDecision": observed,
                    "observedRouteClass": route_class,
                    "status": status,
                    "reasons": reasons,
                }
            )
    else:
        case_failures += 1

    case_count = len(cases) if isinstance(cases, list) else 0
    required_demonstrated_classes = {
        "alive_self_interview",
        "alive_proxy_interview",
        "alive_facility_or_residential_route",
        "decedent_or_death_boundary",
        "missing_or_nonresponse",
        "not_classifiable",
        "suppressed_small_cell",
    }
    route_coverage_ok = required_demonstrated_classes.issubset(observed_route_classes)
    overall = (
        "PASS"
        if not protocol_reasons
        and not boundary_reasons
        and case_count > 0
        and case_failures == 0
        and allowed_count > 0
        and blocked_count > 0
        and route_coverage_ok
        else "FAIL"
    )
    return {
        "schemaVersion": "human-infra.life-path-nhats-missingness-route-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "testCasesPath": repo_rel(test_cases_path),
        "testCasesSha256": sha256_file(test_cases_path),
        "overallStatus": overall,
        "boundary": {
            "containsRealNhatsData": False,
            "containsSyntheticOnly": True,
            "routeMapProofOnly": True,
            "publicInferenceProofOnly": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "note": "This report validates synthetic missingness and endpoint-route envelopes only; it does not validate real NHATS extraction, route fields, weighted route counts, public export, calibration, clinical use or individual prediction."
        },
        "summary": {
            "caseCount": case_count,
            "pass": sum(1 for row in case_rows if row["status"] == "PASS"),
            "fail": case_failures,
            "allowedCount": allowed_count,
            "blockedCount": blocked_count,
            "protocolIssueCount": len(protocol_reasons),
            "boundaryIssueCount": len(boundary_reasons),
            "routeCoverageOk": route_coverage_ok,
            "observedRouteClasses": sorted(observed_route_classes)
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
