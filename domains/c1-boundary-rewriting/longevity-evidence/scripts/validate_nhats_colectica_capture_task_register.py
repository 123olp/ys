#!/usr/bin/env python3
"""Validate the NHATS Colectica capture task register."""

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
DEFAULT_REGISTER = MANUAL_DIR / "life_path_nhats_colectica_capture_task_register.json"
DEFAULT_ROUTE_FIELD_REGISTER = MANUAL_DIR / "life_path_nhats_route_field_discovery_register.json"
DEFAULT_CAPTURE_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_ROUTE_CLASSIFIER_READINESS = MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-capture-task-register-validation.json"
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
REQUIRED_TRUE_DECISIONS = {"captureTaskRegisterReady"}
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
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
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
    "accessToken",
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


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


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


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def route_field_ids(rows: Any, key: str = "requiredRouteFieldId") -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def task_variables_by_group(register: dict[str, Any]) -> dict[str, set[str]]:
    observed: dict[str, set[str]] = {}
    groups = register.get("captureTaskGroups")
    if not isinstance(groups, list):
        return observed
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("requiredRouteFieldId"), str):
            continue
        variables: set[str] = set()
        tasks = group.get("tasks")
        if isinstance(tasks, list):
            for task in tasks:
                if isinstance(task, dict) and isinstance(task.get("variableName"), str):
                    variables.add(task["variableName"])
        observed[group["requiredRouteFieldId"]] = variables
    return observed


def expected_variables_by_group(template: dict[str, Any]) -> dict[str, set[str]]:
    expected: dict[str, set[str]] = {}
    units = template.get("requiredCaptureUnits")
    if not isinstance(units, list):
        return expected
    for unit in units:
        if not isinstance(unit, dict) or not isinstance(unit.get("requiredRouteFieldId"), str):
            continue
        variables = unit.get("candidateVariables")
        expected[unit["requiredRouteFieldId"]] = {
            str(variable) for variable in variables if isinstance(variable, str)
        } if isinstance(variables, list) else set()
    return expected


def validate_register(
    register: dict[str, Any],
    route_field_register: dict[str, Any],
    capture_template: dict[str, Any],
    route_classifier_readiness: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-capture-task-register.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("taskRegisterId")
        == "nhats-r13-r14-colectica-capture-task-register-2026-07-03"
        and register.get("status") == "task-register-only-controlled-capture-not-started"
        and register.get("routeFieldDiscoveryRegisterId") == route_field_register.get("registerId")
        and register.get("authenticatedCaptureTemplateId") == capture_template.get("templateId")
        and register.get("routeClassifierReadinessId")
        == route_classifier_readiness.get("readinessId")
    )
    add_check(
        checks,
        "identity-and-upstream-bindings",
        identity_ok,
        "task register must bind NHATS route-field discovery, authenticated capture template and route-classifier readiness",
    )

    bindings = register.get("sourceBindings")
    expected_bindings = {
        "routeFieldDiscoveryRegisterPath": repo_rel(DEFAULT_ROUTE_FIELD_REGISTER),
        "authenticatedCaptureTemplatePath": repo_rel(DEFAULT_CAPTURE_TEMPLATE),
        "routeClassifierReadinessPath": repo_rel(DEFAULT_ROUTE_CLASSIFIER_READINESS),
    }
    bindings_ok = isinstance(bindings, dict) and all(
        bindings.get(key) == expected for key, expected in expected_bindings.items()
    )
    add_check(
        checks,
        "source-bindings",
        bindings_ok,
        "source bindings must point to current route-field, capture-template and readiness records",
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
        "only captureTaskRegisterReady may be true; capture, labels, classifier, extraction, export, calibration and individual prediction must remain false",
    )

    slots = set(register.get("requiredEvidenceSlots") or [])
    add_check(
        checks,
        "required-evidence-slots",
        REQUIRED_EVIDENCE_SLOTS.issubset(slots),
        f"missing={sorted(REQUIRED_EVIDENCE_SLOTS - slots)}",
    )

    groups = register.get("captureTaskGroups")
    group_ids = route_field_ids(groups)
    groups_shape_ok = isinstance(groups, list) and all(
        isinstance(group, dict)
        and group.get("requiredRouteFieldId") in REQUIRED_ROUTE_FIELDS
        and group.get("promotionAllowed") is False
        and isinstance(group.get("completionCriteria"), list)
        and len(group["completionCriteria"]) >= 2
        and isinstance(group.get("tasks"), list)
        and bool(group["tasks"])
        for group in groups or []
    )
    add_check(
        checks,
        "capture-task-groups",
        groups_shape_ok and REQUIRED_ROUTE_FIELDS.issubset(group_ids),
        f"missing={sorted(REQUIRED_ROUTE_FIELDS - group_ids)}",
    )

    expected_vars = expected_variables_by_group(capture_template)
    observed_vars = task_variables_by_group(register)
    variable_coverage_ok = REQUIRED_ROUTE_FIELDS.issubset(expected_vars) and all(
        expected_vars.get(group_id, set()).issubset(observed_vars.get(group_id, set()))
        for group_id in REQUIRED_ROUTE_FIELDS
    )
    missing_by_group = {
        group_id: sorted(expected_vars.get(group_id, set()) - observed_vars.get(group_id, set()))
        for group_id in sorted(REQUIRED_ROUTE_FIELDS)
        if expected_vars.get(group_id, set()) - observed_vars.get(group_id, set())
    }
    add_check(
        checks,
        "template-variable-coverage",
        variable_coverage_ok,
        f"missing_by_group={missing_by_group}",
    )

    tasks_ok = True
    task_count = 0
    if isinstance(groups, list):
        for group in groups:
            if not isinstance(group, dict) or not isinstance(group.get("tasks"), list):
                tasks_ok = False
                continue
            for task in group["tasks"]:
                task_count += 1
                if not (
                    isinstance(task, dict)
                    and isinstance(task.get("taskId"), str)
                    and isinstance(task.get("variableName"), str)
                    and isinstance(task.get("round"), str)
                    and isinstance(task.get("captureMode"), str)
                    and task.get("status") in {"pending", "pending-real-extraction"}
                ):
                    tasks_ok = False
    add_check(
        checks,
        "task-shape-and-status",
        tasks_ok and task_count >= 30,
        f"task_count={task_count}",
    )

    observed_task_variables = set().union(*observed_vars.values()) if observed_vars else set()
    sensitive_excluded = set()
    if isinstance(groups, list):
        for group in groups:
            if (
                isinstance(group, dict)
                and group.get("requiredRouteFieldId") == "death_decedent_indicator"
            ):
                sensitive_excluded = set(group.get("sensitiveExcludedVariables") or [])
    sensitive_ok = (
        SENSITIVE_DEATH_FIELDS.isdisjoint(observed_task_variables)
        and SENSITIVE_DEATH_FIELDS.issubset(sensitive_excluded)
    )
    add_check(
        checks,
        "sensitive-death-field-exclusion",
        sensitive_ok,
        f"sensitive_excluded={sorted(sensitive_excluded)}",
    )

    blockers = register.get("blockingGates")
    blockers_ok = isinstance(blockers, list) and all(
        has_text(blockers, phrase)
        for phrase in [
            "controlled Colectica account",
            "Colectica login",
            "capture hashes",
            "route-value crosswalk",
            "second reviewer",
            "route classifier code",
        ]
    )
    add_check(
        checks,
        "blocking-gates",
        blockers_ok,
        "task register must keep account, login, capture hash, route crosswalk, second review and route classifier code blocked",
    )

    prohibited = register.get("prohibitedActions")
    prohibited_ok = isinstance(prohibited, list) and all(
        has_text(prohibited, phrase)
        for phrase in [
            "credentials",
            "task presence",
            "crosswalk field names",
            "sensitive month/year death fields",
            "individual prediction",
        ]
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "task register must prohibit credentials, inferred labels, sensitive death fields, classifier/extractor/export/calibration and individual prediction",
    )

    next_evidence = register.get("nextEvidenceRequired")
    next_evidence_ok = isinstance(next_evidence, list) and all(
        has_text(next_evidence, phrase)
        for phrase in [
            "Controlled Colectica login",
            "Details page URL",
            "Source capture SHA-256",
            "Value labels",
            "missing-code map",
            "Second reviewer",
        ]
    )
    add_check(
        checks,
        "next-evidence-required",
        next_evidence_ok,
        "next evidence must require controlled login, variable pages, hashes, labels, missing-code map and second review",
    )

    prohibited_keys = sorted(collect_keys(register) & PROHIBITED_KEYS)
    add_check(
        checks,
        "no-secret-or-individual-output-keys",
        not prohibited_keys,
        f"prohibited_keys={prohibited_keys}",
    )

    return checks


def build_validation(
    register_path: Path,
    route_field_register_path: Path,
    capture_template_path: Path,
    route_classifier_readiness_path: Path,
) -> dict[str, Any]:
    register = load_json(register_path)
    route_field_register = load_json(route_field_register_path)
    capture_template = load_json(capture_template_path)
    route_classifier_readiness = load_json(route_classifier_readiness_path)
    checks = validate_register(
        register,
        route_field_register,
        capture_template,
        route_classifier_readiness,
    )
    groups = register.get("captureTaskGroups")
    task_count = 0
    if isinstance(groups, list):
        for group in groups:
            if isinstance(group, dict) and isinstance(group.get("tasks"), list):
                task_count += len(group["tasks"])
    return {
        "schemaVersion": "human-infra.life-path-nhats-colectica-capture-task-register-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "routeFieldDiscoveryRegisterPath": repo_rel(route_field_register_path),
        "routeFieldDiscoveryRegisterSha256": sha256_file(route_field_register_path),
        "authenticatedCaptureTemplatePath": repo_rel(capture_template_path),
        "authenticatedCaptureTemplateSha256": sha256_file(capture_template_path),
        "routeClassifierReadinessPath": repo_rel(route_classifier_readiness_path),
        "routeClassifierReadinessSha256": sha256_file(route_classifier_readiness_path),
        "overallStatus": "PASS" if summarize(checks)["fail"] == 0 else "FAIL",
        "summary": summarize(checks),
        "captureTaskGroupCount": len(groups) if isinstance(groups, list) else 0,
        "captureTaskCount": task_count,
        "boundary": register.get("currentDecision"),
        "checks": checks,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS Colectica capture task register."
    )
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument(
        "--route-field-register",
        type=Path,
        default=DEFAULT_ROUTE_FIELD_REGISTER,
    )
    parser.add_argument(
        "--capture-template",
        type=Path,
        default=DEFAULT_CAPTURE_TEMPLATE,
    )
    parser.add_argument(
        "--route-classifier-readiness",
        type=Path,
        default=DEFAULT_ROUTE_CLASSIFIER_READINESS,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validation = build_validation(
        args.register.resolve(),
        args.route_field_register.resolve(),
        args.capture_template.resolve(),
        args.route_classifier_readiness.resolve(),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        json.dump(validation, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {args.out.resolve().relative_to(REPO_ROOT)}")
    return 0 if validation["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
