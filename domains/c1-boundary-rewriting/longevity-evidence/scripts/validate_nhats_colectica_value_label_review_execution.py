#!/usr/bin/env python3
"""Validate the NHATS Colectica value-label review execution register."""

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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_colectica_value_label_review_execution_register.json"
DEFAULT_PROTOCOL = MANUAL_DIR / "life_path_nhats_colectica_value_label_review_protocol.json"
DEFAULT_ROUTE_FIELD_REGISTER = MANUAL_DIR / "life_path_nhats_route_field_discovery_register.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-value-label-review-execution-validation.json"
)

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
REQUIRED_DOMINANCE_RULES = {
    "death-boundary-dominates-functional-state",
    "missingness-is-not-outcome",
    "proxy-and-facility-stay-separate",
    "not-classifiable-keeps-denominator",
    "small-cell-suppression-before-public-export",
}
REQUIRED_SOURCE_EVIDENCE_IDS = {
    "nhats-cross-year-search-entry",
    "nhats-conditions-of-use-boundary",
    "nhats-user-guide-r14-negative-codes",
    "nhats-r13-crosswalk-candidate-fields",
    "nhats-r14-crosswalk-candidate-fields",
}
REQUIRED_GATE_IDS = {
    "colectica-login-recorded",
    "colectica-variable-pages-reviewed",
    "value-label-source-capture-hashed",
    "question-text-and-universe-reviewed",
    "route-value-crosswalk-drafted",
    "negative-missing-code-map-drafted",
    "sensitive-death-date-exclusion-confirmed",
    "second-reviewer-signoff",
    "route-classifier-promotion-review",
    "public-output-disclosure-boundary-reviewed",
}
REQUIRED_TRUE_DECISIONS = {
    "officialSourceTracePrepared",
    "colecticaPortalPublicPageReviewed",
    "fieldLevelSourceTracePrepared",
    "negativeMissingCodeFamilyMapped",
}
REQUIRED_FALSE_DECISIONS = {
    "colecticaLoginCompleted",
    "colecticaVariablePagesCaptured",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkReady",
    "variableSpecificMissingCodeMapReady",
    "secondReviewerSignoff",
    "routeClassifierAllowed",
    "endpointClassificationAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_NEGATIVE_CODES = {-1, -7, -8, -9}
SENSITIVE_DEATH_FIELDS = {
    "dm13mthdied",
    "dm13yrdied",
    "dm14mthdied",
    "dm14yrdied",
}
PROHIBITED_CONFIRMED_MAP_KEYS = {
    "confirmedValueLabels",
    "valueLabelMap",
    "routeValueMap",
    "colecticaValueLabelTable",
    "rawValueLabels",
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


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(collect_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(collect_keys(child))
    return keys


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
    protocol: dict[str, Any],
    route_register: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-review-execution-register.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )
    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("protocolId") == protocol.get("protocolId")
        and register.get("routeFieldDiscoveryRegisterId") == route_register.get("registerId")
        and register.get("status")
        == "partial-executed-official-source-trace-ready-colectica-login-required"
    )
    add_check(
        checks,
        "execution-register-identity",
        identity_ok,
        "register must bind NHATS, current protocol, current route-field register and partial-login-required status",
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
        "only source trace and standard negative-code family may be prepared; login, labels, crosswalk, classifier, export, calibration and individual prediction must remain false",
    )

    access = register.get("accessReview")
    access_ok = (
        isinstance(access, dict)
        and access.get("colecticaAccountStatus") == "not-completed-in-public-repository"
        and has_text(access, "separate login")
        and has_text(access, "must not be committed")
    )
    add_check(
        checks,
        "access-review-boundary",
        access_ok,
        "access review must record login-required status without credentials, raw metadata or restricted materials",
    )

    evidence = register.get("sourceEvidence")
    evidence_ids = row_ids(evidence)
    evidence_ok = isinstance(evidence, list) and all(
        isinstance(row, dict)
        and isinstance(row.get("url"), str)
        and row["url"].startswith("https://")
        and isinstance(row.get("supports"), list)
        and isinstance(row.get("doesNotSupport"), list)
        for row in evidence
    )
    add_check(
        checks,
        "source-evidence",
        REQUIRED_SOURCE_EVIDENCE_IDS.issubset(evidence_ids) and evidence_ok,
        f"missing={sorted(REQUIRED_SOURCE_EVIDENCE_IDS - evidence_ids)}",
    )

    traces = register.get("fieldLevelSourceTrace")
    trace_ids = set()
    trace_ok = isinstance(traces, list)
    sensitive_excluded: set[str] = set()
    if isinstance(traces, list):
        for row in traces:
            if not isinstance(row, dict):
                trace_ok = False
                continue
            route_id = row.get("requiredRouteFieldId")
            if isinstance(route_id, str):
                trace_ids.add(route_id)
            if row.get("promotionAllowed") is not False:
                trace_ok = False
            if not isinstance(row.get("candidateVariables"), list) or not row["candidateVariables"]:
                trace_ok = False
            if not isinstance(row.get("sourceEvidenceIds"), list) or not row["sourceEvidenceIds"]:
                trace_ok = False
            if row.get("sourceCaptureHash") is not None:
                trace_ok = False
            if route_id != "disclosure_cell_count":
                if row.get("valueLabelSourceStatus") != "pending-colectica-variable-page-capture":
                    trace_ok = False
                if row.get("questionTextStatus") != "not-reviewed":
                    trace_ok = False
                if row.get("universeOrSkipLogicStatus") != "not-reviewed":
                    trace_ok = False
            excluded = row.get("sensitiveExcludedVariables")
            if isinstance(excluded, list):
                sensitive_excluded.update(str(item) for item in excluded)
    add_check(
        checks,
        "field-level-source-trace",
        REQUIRED_ROUTE_FIELDS.issubset(trace_ids) and trace_ok,
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - trace_ids)}",
    )
    add_check(
        checks,
        "sensitive-death-date-exclusion",
        SENSITIVE_DEATH_FIELDS.issubset(sensitive_excluded)
        and has_text(register.get("prohibitedActions", []), "individual death dates"),
        f"excluded={sorted(sensitive_excluded)}",
    )

    crosswalk = register.get("routeValueCrosswalkDraft")
    crosswalk_ok = (
        isinstance(crosswalk, dict)
        and crosswalk.get("status") == "skeleton-only-blocked-no-raw-codes"
        and crosswalk.get("rawValueRowsConfirmed") == 0
        and crosswalk.get("promotionAllowed") is False
        and REQUIRED_ROUTE_CLASSES.issubset(set(crosswalk.get("routeClasses", [])))
        and REQUIRED_DOMINANCE_RULES.issubset(set(crosswalk.get("dominanceRules", [])))
    )
    add_check(
        checks,
        "route-value-crosswalk-skeleton",
        crosswalk_ok,
        "route-value crosswalk must be skeleton-only with zero confirmed raw value rows",
    )

    missing_map = register.get("negativeMissingCodeMap")
    missing_codes: set[int] = set()
    if isinstance(missing_map, dict) and isinstance(missing_map.get("standardNegativeCodeFamily"), list):
        for row in missing_map["standardNegativeCodeFamily"]:
            if isinstance(row, dict) and isinstance(row.get("code"), int):
                missing_codes.add(row["code"])
    missing_map_ok = (
        isinstance(missing_map, dict)
        and missing_map.get("status") == "standard-family-only-variable-specific-map-blocked"
        and missing_map.get("fieldSpecificRowsConfirmed") == 0
        and missing_map.get("variableSpecificMapReady") is False
        and missing_map.get("promotionAllowed") is False
        and REQUIRED_NEGATIVE_CODES.issubset(missing_codes)
        and has_text(missing_map.get("boundary"), "does not authorize")
    )
    add_check(
        checks,
        "negative-missing-code-family",
        missing_map_ok,
        f"observed_codes={sorted(missing_codes)}",
    )

    gates = register.get("blockingGates")
    gate_ids = row_ids(gates)
    gates_ok = isinstance(gates, list) and all(
        isinstance(gate, dict)
        and gate.get("blocksValueLabelPromotion") is True
        and isinstance(gate.get("status"), str)
        and gate["status"] != "pass"
        for gate in gates
    )
    add_check(
        checks,
        "blocking-gates",
        REQUIRED_GATE_IDS.issubset(gate_ids) and gates_ok,
        f"missing={sorted(REQUIRED_GATE_IDS - gate_ids)}",
    )

    prohibited_ok = (
        has_text(register.get("prohibitedActions"), "candidate variable names")
        and has_text(register.get("prohibitedActions"), "unreviewed Colectica value-label")
        and has_text(register.get("prohibitedActions"), "standard negative-code family")
        and has_text(register.get("prohibitedActions"), "real NHATS route classifier")
        and has_text(register.get("prohibitedActions"), "public AI")
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "register must prohibit route inference, unreviewed value labels, negative-code overuse, classifier execution and public AI exposure",
    )

    prohibited_key_hits = sorted(collect_keys(register) & PROHIBITED_CONFIRMED_MAP_KEYS)
    add_check(
        checks,
        "no-confirmed-value-label-map",
        not prohibited_key_hits,
        f"prohibited_keys={prohibited_key_hits}",
    )
    return checks


def build_report(register_path: Path, protocol_path: Path, route_register_path: Path) -> dict[str, Any]:
    register = load_json(register_path)
    protocol = load_json(protocol_path)
    route_register = load_json(route_register_path)
    checks = validate_register(register, protocol, route_register)
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-colectica-value-label-review-execution-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": register.get("sourceId"),
        "executionRegisterPath": repo_rel(register_path),
        "executionRegisterSha256": sha256_file(register_path),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "routeFieldDiscoveryRegisterPath": repo_rel(route_register_path),
        "routeFieldDiscoveryRegisterSha256": sha256_file(route_register_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "boundary": {
            "containsRealNhatsData": False,
            "containsConfirmedValueLabels": False,
            "containsRouteValueMap": False,
            "fieldLevelSourceTracePrepared": True,
            "standardNegativeCodeFamilyOnly": True,
            "routeClassifierAllowed": False,
            "weightedRouteCountsAllowed": False,
            "publicExportAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        }
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--route-field-register", type=Path, default=DEFAULT_ROUTE_FIELD_REGISTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        args.register.resolve(),
        args.protocol.resolve(),
        args.route_field_register.resolve(),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(args.out.resolve())}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
