#!/usr/bin/env python3
"""Validate the NHATS Colectica value-label review protocol."""

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
    / "life_path_nhats_colectica_value_label_review_protocol.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-value-label-validation.json"
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
    "nhats-cross-year-search-colectica-values",
    "nhats-cross-year-search-colectica-login",
    "nhats-conditions-of-use-public-ai-and-aggregation",
}
REQUIRED_ARTIFACT_IDS = {
    "colectica-access-log",
    "field-level-source-trace",
    "route-value-crosswalk",
    "reviewer-signoff",
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
REQUIRED_FALSE_DECISIONS = {
    "colecticaLoginCompleted",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkReady",
    "negativeMissingCodeMapReady",
    "routeClassifierAllowed",
    "endpointClassificationAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {"colecticaReviewProtocolReady"}
SENSITIVE_DEATH_FIELDS = {
    "dm13mthdied",
    "dm13yrdied",
    "dm14mthdied",
    "dm14yrdied",
}
PROHIBITED_VALUE_LABEL_KEYS = {
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


def validate_protocol(protocol: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-review-protocol.v1",
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )
    identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId")
        == "nhats-r13-r14-colectica-value-label-review-protocol-draft"
        and protocol.get("routeFieldDiscoveryRegisterId")
        == "nhats-r13-r14-route-field-discovery-register-draft"
        and protocol.get("missingnessRouteProtocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and protocol.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and protocol.get("status") == "protocol-only-value-labels-not-reviewed"
    )
    add_check(
        checks,
        "protocol-identity",
        identity_ok,
        "protocol must bind NHATS, route-field discovery, missingness route, variable matrix and value-labels-not-reviewed status",
    )

    decision = protocol.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if decision_ok:
        for field in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is True
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "decision-boundary",
        decision_ok,
        "only the review protocol may be ready; login, labels, route crosswalk, classifier, endpoint, weighted counts, export, calibration and individual prediction must remain false",
    )

    evidence = protocol.get("sourceEvidence")
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
        "required-source-evidence",
        REQUIRED_EVIDENCE_IDS.issubset(evidence_ids) and evidence_ok,
        f"missing={sorted(REQUIRED_EVIDENCE_IDS - evidence_ids)}",
    )

    artifacts = protocol.get("reviewArtifactRequirements")
    artifact_ids = row_ids(artifacts)
    artifacts_ok = isinstance(artifacts, list) and all(
        isinstance(row, dict)
        and row.get("status") == "missing"
        and row.get("blocksPromotion") is True
        and isinstance(row.get("requiredFields"), list)
        and len(row["requiredFields"]) >= 4
        for row in artifacts
    )
    add_check(
        checks,
        "review-artifact-requirements",
        REQUIRED_ARTIFACT_IDS.issubset(artifact_ids) and artifacts_ok,
        f"missing={sorted(REQUIRED_ARTIFACT_IDS - artifact_ids)}",
    )

    units = protocol.get("routeFieldReviewUnits")
    unit_ids = set()
    if isinstance(units, list):
        unit_ids = {
            str(unit["requiredRouteFieldId"])
            for unit in units
            if isinstance(unit, dict) and isinstance(unit.get("requiredRouteFieldId"), str)
        }
    units_ok = isinstance(units, list)
    if isinstance(units, list):
        for unit in units:
            if not isinstance(unit, dict):
                units_ok = False
                continue
            if unit.get("promotionAllowed") is not False:
                units_ok = False
            if unit.get("status") not in {
                "pending-colectica-review",
                "computed-output-gate-pending-review",
            }:
                units_ok = False
            if not isinstance(unit.get("candidateVariables"), list) or not unit["candidateVariables"]:
                units_ok = False
            if not isinstance(unit.get("mustConfirm"), list) or len(unit["mustConfirm"]) < 3:
                units_ok = False
    add_check(
        checks,
        "route-field-review-units",
        REQUIRED_ROUTE_FIELDS.issubset(unit_ids) and units_ok,
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - unit_ids)}",
    )

    death_unit = {}
    if isinstance(units, list):
        death_unit = next(
            (
                unit
                for unit in units
                if isinstance(unit, dict)
                and unit.get("requiredRouteFieldId") == "death_decedent_indicator"
            ),
            {},
        )
    sensitive_excluded = set()
    if isinstance(death_unit, dict):
        excluded = death_unit.get("sensitiveExcludedVariables")
        if isinstance(excluded, list):
            sensitive_excluded = {str(item) for item in excluded}
    add_check(
        checks,
        "sensitive-death-date-exclusion",
        SENSITIVE_DEATH_FIELDS.issubset(sensitive_excluded)
        and has_text(protocol.get("prohibitedActions", []), "individual death dates"),
        f"excluded={sorted(sensitive_excluded)}",
    )

    gates = protocol.get("blockingGates")
    gate_ids = row_ids(gates)
    gates_ok = isinstance(gates, list) and all(
        isinstance(gate, dict)
        and gate.get("status") == "missing"
        and gate.get("blocksValueLabelPromotion") is True
        for gate in gates
    )
    add_check(
        checks,
        "blocking-gates",
        REQUIRED_GATE_IDS.issubset(gate_ids) and gates_ok,
        f"missing={sorted(REQUIRED_GATE_IDS - gate_ids)}",
    )

    prohibited = protocol.get("prohibitedActions")
    prohibited_ok = (
        has_text(prohibited, "unreviewed Colectica value-label tables")
        and has_text(prohibited, "crosswalk variable names")
        and has_text(prohibited, "real NHATS route classifier")
        and has_text(prohibited, "weighted route counts")
        and has_text(prohibited, "public AI")
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "protocol must prohibit unreviewed value-label tables, crosswalk-as-values, route classifier, weighted counts and public AI upload",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSR13Instrument-VariableCrosswalk")
        and has_text(source_trace, "NHATSR14Instrument-VariableCrosswalk")
    )
    add_check(
        checks,
        "official-source-trace",
        source_trace_ok,
        "sourceTrace must include official Colectica, conditions, User Guide and R13/R14 crosswalk URLs",
    )

    prohibited_key_hits = sorted(collect_keys(protocol) & PROHIBITED_VALUE_LABEL_KEYS)
    add_check(
        checks,
        "no-confirmed-value-label-map",
        not prohibited_key_hits,
        f"prohibited_keys={prohibited_key_hits}",
    )
    return checks


def build_report(protocol_path: Path) -> dict[str, Any]:
    protocol = load_json(protocol_path)
    checks = validate_protocol(protocol)
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-colectica-value-label-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "sourceId": protocol.get("sourceId"),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "boundary": "The Colectica value-label review protocol is present, but value labels, question text, universe/skip logic, route-value crosswalk, missing-code map, classifier promotion, weighted route counts, public export, calibration and individual prediction remain blocked.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(args.protocol.resolve())
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(args.out.resolve())}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
