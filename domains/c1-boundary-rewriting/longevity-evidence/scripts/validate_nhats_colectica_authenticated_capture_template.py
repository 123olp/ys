#!/usr/bin/env python3
"""Validate the NHATS Colectica authenticated capture template."""

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
DEFAULT_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_ACCESS_ROUTE_PROBE = (
    MANUAL_DIR / "life_path_nhats_colectica_access_route_probe_register.json"
)
DEFAULT_EXECUTION_REGISTER = (
    MANUAL_DIR / "life_path_nhats_colectica_value_label_review_execution_register.json"
)
DEFAULT_PROTOCOL = MANUAL_DIR / "life_path_nhats_colectica_value_label_review_protocol.json"
DEFAULT_ROUTE_FIELD_REGISTER = MANUAL_DIR / "life_path_nhats_route_field_discovery_register.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-authenticated-capture-template-validation.json"
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
REQUIRED_EVIDENCE_SLOTS = {
    "requiredRouteFieldId",
    "candidateVariables",
    "colecticaItemId",
    "variableName",
    "round",
    "fileName",
    "detailsPageUrl",
    "sourceCaptureSha256",
    "captureMethod",
    "captureDate",
    "valueLabelsReviewed",
    "questionTextReviewed",
    "universeSkipLogicReviewed",
    "concordanceReviewed",
    "publicUseTierReviewed",
    "sensitiveRestrictedExclusionReviewed",
    "variableSpecificMissingCodesReviewed",
    "reviewerNotes",
    "secondReviewerSignoff",
    "promotionAllowed",
}
REQUIRED_TRUE_DECISIONS = {"templateReady"}
REQUIRED_FALSE_DECISIONS = {
    "controlledColecticaAccountStatusRecorded",
    "colecticaLoginCompleted",
    "authenticatedVariablePagesCaptured",
    "sourceCaptureHashesRecorded",
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
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "rawMetadataDump",
    "rawValueLabels",
    "colecticaExportRows",
    "rowLevelData",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
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


def row_ids(rows: Any, key: str) -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_template(
    template: dict[str, Any],
    access_route_probe: dict[str, Any],
    execution_register: dict[str, Any],
    protocol: dict[str, Any],
    route_field_register: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        template.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-authenticated-capture-template.v1",
        f"schemaVersion={template.get('schemaVersion')!r}",
    )

    identity_ok = (
        template.get("sourceId") == "nhats"
        and template.get("executionRegisterId") == execution_register.get("executionRegisterId")
        and template.get("accessRouteProbeRegisterId")
        == access_route_probe.get("probeRegisterId")
        and template.get("protocolId") == protocol.get("protocolId")
        and template.get("routeFieldDiscoveryRegisterId")
        == route_field_register.get("registerId")
        and template.get("status") == "template-only-authenticated-capture-not-started"
    )
    add_check(
        checks,
        "template-identity",
        identity_ok,
        "template must bind NHATS, access-route probe, execution register, value-label protocol and route-field register while staying template-only",
    )

    decision = template.get("currentDecision")
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
        "only templateReady may be true; account, login, capture, labels, route map, classifier, export, calibration and individual prediction must remain false",
    )

    source_bindings = template.get("sourceBindings")
    expected_bindings = {
        "accessRouteProbeRegisterPath": repo_rel(DEFAULT_ACCESS_ROUTE_PROBE),
        "executionRegisterPath": repo_rel(DEFAULT_EXECUTION_REGISTER),
        "protocolPath": repo_rel(DEFAULT_PROTOCOL),
        "routeFieldDiscoveryRegisterPath": repo_rel(DEFAULT_ROUTE_FIELD_REGISTER),
    }
    bindings_ok = isinstance(source_bindings, dict) and all(
        source_bindings.get(key) == expected for key, expected in expected_bindings.items()
    )
    add_check(
        checks,
        "source-bindings",
        bindings_ok,
        "template must point to current upstream register paths",
    )

    slots = set(template.get("captureEvidenceSlots") or [])
    add_check(
        checks,
        "capture-evidence-slots",
        REQUIRED_EVIDENCE_SLOTS.issubset(slots),
        f"missing={sorted(REQUIRED_EVIDENCE_SLOTS - slots)}",
    )

    units = template.get("requiredCaptureUnits")
    observed_units = row_ids(units, "requiredRouteFieldId")
    units_ok = isinstance(units, list) and all(
        isinstance(unit, dict)
        and unit.get("captureStatus")
        in {
            "missing-authenticated-source-capture",
            "computed-output-gate-pending-real-extraction",
        }
        and unit.get("promotionAllowed") is False
        and isinstance(unit.get("candidateVariables"), list)
        and unit["candidateVariables"]
        for unit in units
    )
    add_check(
        checks,
        "required-capture-units",
        units_ok and REQUIRED_ROUTE_FIELDS.issubset(observed_units),
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - observed_units)}",
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
    sensitive_excluded = set(death_unit.get("sensitiveExcludedVariables") or [])
    add_check(
        checks,
        "sensitive-death-exclusion",
        SENSITIVE_DEATH_FIELDS.issubset(sensitive_excluded),
        f"sensitive_excluded={sorted(sensitive_excluded)}",
    )

    requirements = template.get("captureCompletionRequirements")
    requirements_ok = isinstance(requirements, list) and all(
        has_text(requirements, phrase)
        for phrase in [
            "controlled Colectica account",
            "source capture SHA-256",
            "value labels",
            "question text",
            "universe and skip logic",
            "second reviewer signoff",
        ]
    )
    add_check(
        checks,
        "capture-completion-requirements",
        requirements_ok,
        "template must require account status, hashes, value labels, question text, universe/skip logic and second review",
    )

    blocked_until = template.get("blockedUntil")
    blocked_ok = isinstance(blocked_until, list) and all(
        has_text(blocked_until, phrase)
        for phrase in [
            "controlled account",
            "authenticated source captures",
            "route-value crosswalk",
            "second reviewer",
            "disclosure and survey-design",
        ]
    )
    add_check(
        checks,
        "blocked-until",
        blocked_ok,
        "template must keep authenticated captures, route crosswalk, second review, disclosure and survey design as blockers",
    )

    prohibited = template.get("prohibitedActions")
    prohibited_ok = isinstance(prohibited, list) and all(
        has_text(prohibited, phrase)
        for phrase in [
            "credentials",
            "raw Colectica metadata dumps",
            "crosswalk variable names",
            "public AI systems",
            "calibration",
            "individual prediction",
        ]
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "template must block credentials, raw dumps, crosswalk-as-labels, public AI upload, calibration and individual prediction",
    )

    key_hits = sorted(collect_keys(template) & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-credential-or-raw-data-keys",
        not key_hits,
        f"prohibited_keys={key_hits}",
    )

    return checks


def write_validation(
    out_path: Path,
    template_path: Path,
    access_route_probe_path: Path,
    execution_register_path: Path,
    protocol_path: Path,
    route_field_register_path: Path,
    template: dict[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    summary = summarize(checks)
    report = {
        "schemaVersion": "human-infra.life-path-nhats-colectica-authenticated-capture-template-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "templatePath": repo_rel(template_path),
        "templateSha256": sha256_file(template_path),
        "accessRouteProbeRegisterPath": repo_rel(access_route_probe_path),
        "accessRouteProbeRegisterSha256": sha256_file(access_route_probe_path),
        "executionRegisterPath": repo_rel(execution_register_path),
        "executionRegisterSha256": sha256_file(execution_register_path),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "routeFieldDiscoveryRegisterPath": repo_rel(route_field_register_path),
        "routeFieldDiscoveryRegisterSha256": sha256_file(route_field_register_path),
        "templateId": template.get("templateId"),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "checks": checks,
        "boundary": {
            "templateReady": template.get("currentDecision", {}).get("templateReady"),
            "controlledColecticaAccountStatusRecorded": template.get("currentDecision", {}).get(
                "controlledColecticaAccountStatusRecorded"
            ),
            "colecticaLoginCompleted": template.get("currentDecision", {}).get(
                "colecticaLoginCompleted"
            ),
            "authenticatedVariablePagesCaptured": template.get("currentDecision", {}).get(
                "authenticatedVariablePagesCaptured"
            ),
            "sourceCaptureHashesRecorded": template.get("currentDecision", {}).get(
                "sourceCaptureHashesRecorded"
            ),
            "valueLabelsConfirmed": template.get("currentDecision", {}).get(
                "valueLabelsConfirmed"
            ),
            "questionTextConfirmed": template.get("currentDecision", {}).get(
                "questionTextConfirmed"
            ),
            "universeSkipLogicConfirmed": template.get("currentDecision", {}).get(
                "universeSkipLogicConfirmed"
            ),
            "routeClassifierAllowed": template.get("currentDecision", {}).get(
                "routeClassifierAllowed"
            ),
            "publicExportAllowed": template.get("currentDecision", {}).get(
                "publicExportAllowed"
            ),
            "calibrationAllowed": template.get("currentDecision", {}).get(
                "calibrationAllowed"
            ),
            "individualPredictionAllowed": template.get("currentDecision", {}).get(
                "individualPredictionAllowed"
            ),
        },
        "note": "This validation proves only that an authenticated Colectica capture template exists. It does not prove account access, variable page capture, value labels, question text, universe/skip logic, route classifiers, public export, calibration or individual prediction.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--access-route-probe", type=Path, default=DEFAULT_ACCESS_ROUTE_PROBE)
    parser.add_argument("--execution-register", type=Path, default=DEFAULT_EXECUTION_REGISTER)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--route-field-register", type=Path, default=DEFAULT_ROUTE_FIELD_REGISTER)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    template_path = args.template.resolve()
    access_route_probe_path = args.access_route_probe.resolve()
    execution_register_path = args.execution_register.resolve()
    protocol_path = args.protocol.resolve()
    route_field_register_path = args.route_field_register.resolve()
    out_path = args.out.resolve()

    template = load_json(template_path)
    access_route_probe = load_json(access_route_probe_path)
    execution_register = load_json(execution_register_path)
    protocol = load_json(protocol_path)
    route_field_register = load_json(route_field_register_path)

    checks = validate_template(
        template,
        access_route_probe,
        execution_register,
        protocol,
        route_field_register,
    )
    write_validation(
        out_path,
        template_path,
        access_route_probe_path,
        execution_register_path,
        protocol_path,
        route_field_register_path,
        template,
        checks,
    )
    summary = summarize(checks)
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={'PASS' if summary['fail'] == 0 else 'FAIL'} checks={summary}")
    return 0 if summary["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
