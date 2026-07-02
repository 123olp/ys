#!/usr/bin/env python3
"""Validate the NHATS R13/R14 route-field discovery register."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_REGISTER = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_route_field_discovery_register.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-field-discovery-validation.json"
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
REQUIRED_EVIDENCE_IDS = {
    "nhats-cross-year-search-colectica",
    "nhats-conditions-of-use-ai-and-small-cell",
    "nhats-user-guide-proxy-prefixes",
    "nhats-user-guide-weight-design",
    "nhats-user-guide-missing-negative-codes",
    "nhats-user-guide-lml-death-boundary",
    "nhats-r14-crosswalk-route-fields",
    "nhats-r13-crosswalk-route-fields",
    "nhats-r14-crosswalk-design-fields",
    "nhats-r13-crosswalk-design-fields",
}
REQUIRED_BLOCKING_GATES = {
    "colectica-value-labels-confirmed",
    "public-use-file-access-confirmed",
    "canonical-file-format-selected",
    "sensitive-death-date-exclusion-reviewed",
    "route-value-crosswalk-reviewed",
    "negative-missing-code-map-reviewed",
    "survey-design-linkage-reviewed",
    "route-classifier-code-reviewed",
    "disclosure-output-review-ready",
}
REQUIRED_FALSE_DECISIONS = {
    "colecticaValueLabelsConfirmed",
    "publicUseDataDownloaded",
    "routeClassifierAllowed",
    "endpointClassificationAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {"routeFieldsDiscoveredFromOfficialCrosswalk"}
REQUIRED_SOURCE_TOKENS = {
    "cross-year-search",
    "conditions-of-use",
    "nhats/13",
    "nhats/14",
    "NHATSUserGuideR14",
    "NHATSR13Instrument-VariableCrosswalk",
    "NHATSR14Instrument-VariableCrosswalk",
}
SENSITIVE_DEATH_FIELDS = {
    "dm13mthdied",
    "dm13yrdied",
    "dm14mthdied",
    "dm14yrdied",
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


def validate_register(register: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-route-field-discovery-register.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )
    add_check(
        checks,
        "register-identity",
        register.get("sourceId") == "nhats"
        and register.get("registerId") == "nhats-r13-r14-route-field-discovery-register-draft"
        and register.get("routeProtocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and register.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and register.get("status") == "crosswalk-confirmed-colectica-pending-cannot-route",
        "register must bind NHATS, route protocol, variable matrix and cannot-route status",
    )

    decision = register.get("fieldDiscoveryDecision")
    decision_ok = isinstance(decision, dict)
    if decision_ok:
        for field in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is True
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "field-discovery-decision-boundary",
        decision_ok,
        "official crosswalk discovery may be true, but Colectica, data download, classifier, endpoint, weighted counts, public export, calibration and individual prediction must remain false",
    )

    evidence = register.get("sourceEvidence")
    observed_evidence_ids = row_ids(evidence)
    add_check(
        checks,
        "required-source-evidence",
        REQUIRED_EVIDENCE_IDS.issubset(observed_evidence_ids),
        f"missing={sorted(REQUIRED_EVIDENCE_IDS - observed_evidence_ids)}",
    )
    evidence_boundary_ok = isinstance(evidence, list) and all(
        isinstance(item, dict)
        and isinstance(item.get("url"), str)
        and item["url"].startswith("https://")
        and isinstance(item.get("supports"), list)
        and isinstance(item.get("doesNotSupport"), list)
        for item in evidence
    )
    add_check(
        checks,
        "source-evidence-boundaries",
        evidence_boundary_ok,
        "every source evidence row must include https URL, supports and doesNotSupport boundaries",
    )

    families = register.get("routeFieldFamilies")
    observed_field_ids = set()
    if isinstance(families, list):
        observed_field_ids = {
            str(item["requiredRouteFieldId"])
            for item in families
            if isinstance(item, dict) and isinstance(item.get("requiredRouteFieldId"), str)
        }
    add_check(
        checks,
        "required-route-field-families",
        REQUIRED_ROUTE_FIELDS.issubset(observed_field_ids),
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - observed_field_ids)}",
    )

    families_ok = isinstance(families, list)
    if isinstance(families, list):
        for family in families:
            if not isinstance(family, dict):
                families_ok = False
                continue
            if family.get("classificationReadiness") is not False:
                families_ok = False
            if not str(family.get("status", "")).strip():
                families_ok = False
            if not isinstance(family.get("candidateVariables"), dict):
                families_ok = False
            evidence_ids = family.get("evidenceIds")
            if not isinstance(evidence_ids, list) or not evidence_ids:
                families_ok = False
            if not isinstance(family.get("remainingChecks"), list) or not family["remainingChecks"]:
                families_ok = False
    add_check(
        checks,
        "field-families-not-classification-ready",
        families_ok,
        "every discovered field family must remain not classification-ready and retain evidence plus remaining checks",
    )

    death_family = next(
        (
            family
            for family in families
            if isinstance(family, dict)
            and family.get("requiredRouteFieldId") == "death_decedent_indicator"
        ),
        {},
    ) if isinstance(families, list) else {}
    sensitive_excluded = set()
    if isinstance(death_family, dict):
        excluded = death_family.get("sensitiveExcludedVariables")
        if isinstance(excluded, dict):
            for values in excluded.values():
                if isinstance(values, list):
                    sensitive_excluded.update(str(value) for value in values)
    add_check(
        checks,
        "sensitive-death-date-fields-excluded",
        SENSITIVE_DEATH_FIELDS.issubset(sensitive_excluded)
        and has_text(register.get("prohibitedActions", []), "individual death dates"),
        f"excluded={sorted(sensitive_excluded)}",
    )

    gates = register.get("blockingGates")
    observed_gate_ids = row_ids(gates)
    gate_status_ok = isinstance(gates, list) and all(
        isinstance(gate, dict)
        and gate.get("status") == "missing"
        and gate.get("blocksRouteClassification") is True
        for gate in gates
    )
    add_check(
        checks,
        "required-blocking-gates",
        REQUIRED_BLOCKING_GATES.issubset(observed_gate_ids) and gate_status_ok,
        f"missing={sorted(REQUIRED_BLOCKING_GATES - observed_gate_ids)}",
    )

    prohibited = register.get("prohibitedActions")
    prohibited_ok = (
        has_text(prohibited, "classify real NHATS records")
        and has_text(prohibited, "weighted route counts")
        and has_text(prohibited, "public AI")
        and has_text(prohibited, "individual death dates")
        and has_text(prohibited, "Colectica value-label confirmation")
    )
    add_check(
        checks,
        "prohibited-actions-boundary",
        prohibited_ok,
        "register must prohibit premature routing, weighted counts, public AI, individual death dates and crosswalk-as-Colectica substitution",
    )

    source_trace = register.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and all(has_text(source_trace, token) for token in REQUIRED_SOURCE_TOKENS)
    )
    add_check(
        checks,
        "official-source-trace",
        source_trace_ok,
        f"required_tokens={sorted(REQUIRED_SOURCE_TOKENS)}",
    )
    return checks


def build_report(register_path: Path) -> dict[str, Any]:
    register = load_json(register_path)
    checks = validate_register(register)
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-route-field-discovery-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": register.get("sourceId"),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "boundary": "Official crosswalk field discovery is registered, but Colectica value labels, governed public-use access, route classifier review, weighted route counts, public export, calibration and individual prediction remain blocked.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.register.resolve())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(args.out.resolve())}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
