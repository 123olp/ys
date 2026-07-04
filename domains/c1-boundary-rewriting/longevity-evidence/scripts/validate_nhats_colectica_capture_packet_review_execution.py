#!/usr/bin/env python3
"""Validate the NHATS Colectica capture-packet review execution register."""

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
DEFAULT_REGISTER = (
    MANUAL_DIR
    / "life_path_nhats_colectica_capture_packet_review_execution_register.json"
)
DEFAULT_TASK_REGISTER = MANUAL_DIR / "life_path_nhats_colectica_capture_task_register.json"
DEFAULT_PACKET_VALIDATOR_CASES = (
    MANUAL_DIR / "life_path_nhats_colectica_capture_packet_validator_test_cases.json"
)
DEFAULT_ROUTE_CLASSIFIER_READINESS = MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-capture-packet-review-execution-validation.json"
)

REQUIRED_TRUE_DECISIONS = {"reviewExecutionRegisterReady"}
REQUIRED_FALSE_DECISIONS = {
    "realCapturePacketsAttached",
    "humanReviewComplete",
    "secondReviewerSignoff",
    "captureSlotClosureAllowed",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkReady",
    "variableSpecificMissingCodeMapReady",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_FALSE_SLOT_FIELDS = {
    "packetReceived",
    "humanReviewComplete",
    "secondReviewComplete",
    "valueLabelsConfirmed",
    "questionTextConfirmed",
    "universeSkipLogicConfirmed",
    "routeValueCrosswalkReady",
    "variableSpecificMissingCodesConfirmed",
    "slotClosureAllowed",
    "promotionAllowed",
    "routeClassifierAllowed",
}
REQUIRED_SLOT_FIELDS = {
    "slotId",
    "requiredRouteFieldId",
    "taskId",
    "variableName",
    "round",
    "packetRequired",
    "packetReceived",
    "packetVerdict",
    "sourceCaptureSha256",
    "humanReviewerStatus",
    "secondReviewerStatus",
    "slotClosureAllowed",
    "promotionAllowed",
    "routeClassifierAllowed",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "accessToken",
    "accountEmail",
    "accountId",
    "rawMetadataDump",
    "rawValueLabels",
    "colecticaExportRows",
    "rowLevelData",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
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


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def expected_tasks(task_register: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    expected: dict[tuple[str, str], dict[str, Any]] = {}
    groups = task_register.get("captureTaskGroups")
    if not isinstance(groups, list):
        return expected
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("requiredRouteFieldId"), str):
            continue
        route_field_id = group["requiredRouteFieldId"]
        tasks = group.get("tasks")
        if not isinstance(tasks, list):
            continue
        for task in tasks:
            if not isinstance(task, dict) or not isinstance(task.get("taskId"), str):
                continue
            expected[(route_field_id, task["taskId"])] = {
                "requiredRouteFieldId": route_field_id,
                "taskId": task["taskId"],
                "variableName": task.get("variableName"),
                "round": task.get("round"),
            }
    return expected


def slot_index(slots: Any) -> dict[tuple[str, str], dict[str, Any]]:
    if not isinstance(slots, list):
        return {}
    indexed: dict[tuple[str, str], dict[str, Any]] = {}
    for slot in slots:
        if (
            isinstance(slot, dict)
            and isinstance(slot.get("requiredRouteFieldId"), str)
            and isinstance(slot.get("taskId"), str)
        ):
            indexed[(slot["requiredRouteFieldId"], slot["taskId"])] = slot
    return indexed


def validate_register(
    register: dict[str, Any],
    task_register: dict[str, Any],
    packet_validator_cases: dict[str, Any],
    route_classifier_readiness: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-capture-packet-review-execution-register.v1",
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("executionRegisterId")
        == "nhats-r13-r14-colectica-capture-packet-review-execution-2026-07-04"
        and register.get("status") == "execution-register-empty-controlled-capture-not-started"
        and register.get("captureTaskRegisterId") == task_register.get("taskRegisterId")
        and register.get("packetValidatorTestSetId") == packet_validator_cases.get("testSetId")
        and register.get("routeClassifierReadinessId")
        == route_classifier_readiness.get("readinessId")
    )
    add_check(
        checks,
        "identity-and-upstream-bindings",
        identity_ok,
        "execution register must bind task register, packet validator cases and route-classifier readiness",
    )

    bindings = register.get("sourceBindings")
    expected_bindings = {
        "captureTaskRegisterPath": repo_rel(DEFAULT_TASK_REGISTER),
        "packetValidatorTestCasesPath": repo_rel(DEFAULT_PACKET_VALIDATOR_CASES),
        "routeClassifierReadinessPath": repo_rel(DEFAULT_ROUTE_CLASSIFIER_READINESS),
    }
    bindings_ok = isinstance(bindings, dict) and all(
        bindings.get(key) == value for key, value in expected_bindings.items()
    )
    add_check(checks, "source-bindings", bindings_ok, "source bindings must point to current upstream records")

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
        "only reviewExecutionRegisterReady may be true; capture, slot closure, classifier, extraction, export, calibration and individual prediction must remain false",
    )

    expected = expected_tasks(task_register)
    observed = slot_index(register.get("reviewSlots"))
    missing_slots = sorted(f"{route}:{task}" for route, task in set(expected) - set(observed))
    extra_slots = sorted(f"{route}:{task}" for route, task in set(observed) - set(expected))
    add_check(
        checks,
        "review-slot-task-coverage",
        not missing_slots and not extra_slots and len(observed) >= 30,
        f"expected={len(expected)} observed={len(observed)} missing={missing_slots} extra={extra_slots}",
    )

    slot_shape_ok = isinstance(register.get("reviewSlots"), list)
    for key, expected_task in expected.items():
        slot = observed.get(key)
        if not isinstance(slot, dict):
            slot_shape_ok = False
            continue
        if not REQUIRED_SLOT_FIELDS.issubset(slot):
            slot_shape_ok = False
        if slot.get("slotId") != f"capture-packet-review-{slot.get('taskId')}":
            slot_shape_ok = False
        if slot.get("variableName") != expected_task.get("variableName"):
            slot_shape_ok = False
        if slot.get("round") != expected_task.get("round"):
            slot_shape_ok = False
        if slot.get("packetRequired") is not True:
            slot_shape_ok = False
        if slot.get("packetVerdict") is not None or slot.get("sourceCaptureSha256") is not None:
            slot_shape_ok = False
        for false_field in REQUIRED_FALSE_SLOT_FIELDS:
            if slot.get(false_field) is not False:
                slot_shape_ok = False
    add_check(
        checks,
        "review-slot-shape-and-blocked-state",
        slot_shape_ok,
        "every task slot must be pending, have no packet/hash/verdict, and keep slot closure plus route classifier blocked",
    )

    summary = register.get("summary")
    summary_ok = isinstance(summary, dict) and summary == {
        "reviewSlotCount": len(expected),
        "packetsReceived": 0,
        "humanReviewsComplete": 0,
        "secondReviewsComplete": 0,
        "slotsClosed": 0,
        "routeClassifierAdmissions": 0,
        "realExtractionAdmissions": 0,
        "calibrationAdmissions": 0,
        "individualPredictionAdmissions": 0,
    }
    add_check(
        checks,
        "summary-counts",
        summary_ok,
        f"summary={summary!r}",
    )

    blockers = register.get("blockedUntil")
    blockers_ok = isinstance(blockers, list) and all(
        has_text(blockers, phrase)
        for phrase in [
            "controlled Colectica login",
            "source capture SHA-256",
            "human reviewer",
            "second reviewer",
            "value labels",
            "route-value crosswalk",
            "variable-specific missing-code",
        ]
    )
    add_check(
        checks,
        "blocked-until",
        blockers_ok,
        "blockedUntil must require login, hashes, human review, second review, labels, route crosswalk and missing-code map",
    )

    prohibited = register.get("prohibitedActions")
    prohibited_ok = isinstance(prohibited, list) and all(
        has_text(prohibited, phrase)
        for phrase in [
            "credentials",
            "AI-only",
            "slot closure",
            "route classifier",
            "individual prediction",
        ]
    )
    add_check(
        checks,
        "prohibited-actions",
        prohibited_ok,
        "prohibited actions must block credentials, AI-only signoff, slot closure, route classifier and individual prediction",
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
    task_register_path: Path,
    packet_validator_cases_path: Path,
    route_classifier_readiness_path: Path,
) -> dict[str, Any]:
    register = load_json(register_path)
    task_register = load_json(task_register_path)
    packet_validator_cases = load_json(packet_validator_cases_path)
    route_classifier_readiness = load_json(route_classifier_readiness_path)
    checks = validate_register(
        register,
        task_register,
        packet_validator_cases,
        route_classifier_readiness,
    )
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-colectica-capture-packet-review-execution-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "registerPath": repo_rel(register_path),
        "registerSha256": sha256_file(register_path),
        "captureTaskRegisterPath": repo_rel(task_register_path),
        "captureTaskRegisterSha256": sha256_file(task_register_path),
        "packetValidatorTestCasesPath": repo_rel(packet_validator_cases_path),
        "packetValidatorTestCasesSha256": sha256_file(packet_validator_cases_path),
        "routeClassifierReadinessPath": repo_rel(route_classifier_readiness_path),
        "routeClassifierReadinessSha256": sha256_file(route_classifier_readiness_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "summary": summary,
        "reviewExecutionSummary": register.get("summary"),
        "boundary": register.get("currentDecision"),
        "checks": checks,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS Colectica capture-packet review execution register."
    )
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--task-register", type=Path, default=DEFAULT_TASK_REGISTER)
    parser.add_argument(
        "--packet-validator-cases",
        type=Path,
        default=DEFAULT_PACKET_VALIDATOR_CASES,
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
        args.task_register.resolve(),
        args.packet_validator_cases.resolve(),
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
