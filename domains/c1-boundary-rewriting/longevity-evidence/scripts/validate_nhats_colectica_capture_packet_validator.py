#!/usr/bin/env python3
"""Validate future NHATS Colectica capture packet preflight semantics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
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
DEFAULT_TEST_CASES = (
    MANUAL_DIR / "life_path_nhats_colectica_capture_packet_validator_test_cases.json"
)
DEFAULT_TEMPLATE = (
    MANUAL_DIR / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_TASK_REGISTER = MANUAL_DIR / "life_path_nhats_colectica_capture_task_register.json"
DEFAULT_ROUTE_CLASSIFIER_READINESS = (
    MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-capture-packet-validator-validation.json"
)

TEST_CASES_SCHEMA = (
    "human-infra.life-path-nhats-colectica-capture-packet-validator-test-cases.v1"
)
VALIDATION_SCHEMA = (
    "human-infra.life-path-nhats-colectica-capture-packet-validator-validation.v1"
)
PACKET_SCHEMA = "human-infra.life-path-nhats-colectica-capture-packet.v1"
HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")

VERDICT_REVIEWABLE = "reviewable-but-still-blocked"
VERDICT_CANNOT_EVALUATE = "cannot-evaluate"
VERDICT_REJECTED = "rejected"
ALLOWED_VERDICTS = {VERDICT_REVIEWABLE, VERDICT_CANNOT_EVALUATE, VERDICT_REJECTED}

REQUIRED_PACKET_FIELDS = {
    "packetSchema",
    "packetId",
    "sourceId",
    "taskRegisterId",
    "templateId",
    "routeClassifierReadinessId",
    "requiredRouteFieldId",
    "taskId",
    "variableName",
    "round",
    "detailsPageUrlRedacted",
    "sourceCaptureSha256",
    "artifactHashAlgorithm",
    "captureMethod",
    "captureDate",
    "artifactDescriptionRedacted",
    "reviewerRole",
    "secondReviewerRole",
    "aiOnlySignoff",
    "publicAiUpload",
    "promotionAllowed",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_FALSE_FIELDS = {
    "aiOnlySignoff",
    "publicAiUpload",
    "promotionAllowed",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
OPTIONAL_FALSE_FIELDS = {"rawMetadataAttached", "rawValueLabelsAttached"}
REVIEW_FLAGS = {
    "valueLabelsReviewed",
    "questionTextReviewed",
    "universeSkipLogicReviewed",
    "concordanceReviewed",
    "publicUseTierReviewed",
    "sensitiveRestrictedExclusionReviewed",
    "variableSpecificMissingCodesReviewed",
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
SENSITIVE_DEATH_FIELDS = {
    "dm13mthdied",
    "dm13yrdied",
    "dm14mthdied",
    "dm14yrdied",
}
REQUIRED_BLOCKED_DECISION = {
    "realCaptureAttached": False,
    "captureSlotClosureAllowed": False,
    "routeClassifierAllowed": False,
    "realExtractionAllowed": False,
    "aggregateCohortFlowAllowed": False,
    "weightedRouteCountsAllowed": False,
    "publicExportAllowed": False,
    "calibrationAllowed": False,
    "individualPredictionAllowed": False,
}


def load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.exists():
        raise ValueError(f"missing {label}: {repo_rel(path)}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid {label} JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{label} must be a JSON object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


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


def task_index(register: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}
    groups = register.get("captureTaskGroups")
    if not isinstance(groups, list):
        return index
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("requiredRouteFieldId"), str):
            continue
        route_field_id = group["requiredRouteFieldId"]
        for task in group.get("tasks", []):
            if not isinstance(task, dict) or not isinstance(task.get("taskId"), str):
                continue
            index[(route_field_id, task["taskId"])] = {
                "requiredRouteFieldId": route_field_id,
                "taskId": task["taskId"],
                "variableName": task.get("variableName"),
                "round": task.get("round"),
                "taskStatus": task.get("status"),
                "groupPromotionAllowed": group.get("promotionAllowed"),
            }
    return index


def reviewer_is_human(role: Any) -> bool:
    if not isinstance(role, str):
        return False
    normalized = role.strip().lower()
    return bool(normalized) and "human" in normalized and "ai-only" not in normalized


def evaluate_packet(
    packet: Any,
    template: dict[str, Any],
    task_register: dict[str, Any],
    route_classifier_readiness: dict[str, Any],
) -> dict[str, Any]:
    reject_reasons: list[str] = []
    cannot_evaluate_reasons: list[str] = []
    matched_task: dict[str, Any] | None = None

    if not isinstance(packet, dict):
        return {
            **REQUIRED_BLOCKED_DECISION,
            "packetId": None,
            "verdict": VERDICT_REJECTED,
            "rejectReasons": ["packet must be a JSON object"],
            "cannotEvaluateReasons": [],
            "matchedTask": None,
        }

    missing_fields = sorted(REQUIRED_PACKET_FIELDS - set(packet))
    if missing_fields:
        cannot_evaluate_reasons.append(f"missing required fields: {', '.join(missing_fields)}")

    forbidden_keys = sorted(collect_keys(packet) & PROHIBITED_KEYS)
    if forbidden_keys:
        reject_reasons.append(f"forbidden keys present: {', '.join(forbidden_keys)}")

    if packet.get("packetSchema") != PACKET_SCHEMA:
        reject_reasons.append("packetSchema mismatch")
    if packet.get("sourceId") != "nhats":
        reject_reasons.append("sourceId must be nhats")
    if packet.get("taskRegisterId") != task_register.get("taskRegisterId"):
        reject_reasons.append("taskRegisterId does not match capture task register")
    if packet.get("templateId") != template.get("templateId"):
        reject_reasons.append("templateId does not match authenticated capture template")
    if packet.get("routeClassifierReadinessId") != route_classifier_readiness.get("readinessId"):
        reject_reasons.append("routeClassifierReadinessId does not match readiness gate")

    if packet.get("artifactHashAlgorithm") != "sha256":
        reject_reasons.append("artifactHashAlgorithm must be sha256")
    source_hash = packet.get("sourceCaptureSha256")
    if "sourceCaptureSha256" in packet and (
        not isinstance(source_hash, str) or not HASH_RE.fullmatch(source_hash)
    ):
        reject_reasons.append("sourceCaptureSha256 must be a 64-character sha256 hex digest")

    if packet.get("captureMethod") != "controlled-colectica-authenticated-page-redacted":
        reject_reasons.append("captureMethod must be controlled-colectica-authenticated-page-redacted")

    if packet.get("variableName") in SENSITIVE_DEATH_FIELDS:
        reject_reasons.append("sensitive month/year death fields are prohibited")

    for field in REQUIRED_FALSE_FIELDS:
        if packet.get(field) is not False:
            reject_reasons.append(f"{field} must be false")
    for field in OPTIONAL_FALSE_FIELDS:
        if field in packet and packet.get(field) is not False:
            reject_reasons.append(f"{field} must be false when present")

    if not reviewer_is_human(packet.get("reviewerRole")):
        reject_reasons.append("reviewerRole must identify a human reviewer")
    if not reviewer_is_human(packet.get("secondReviewerRole")):
        reject_reasons.append("secondReviewerRole must identify an independent human reviewer")
    if packet.get("reviewerRole") == packet.get("secondReviewerRole"):
        reject_reasons.append("secondReviewerRole must differ from reviewerRole")

    description = packet.get("artifactDescriptionRedacted")
    if not isinstance(description, str) or not description.strip():
        cannot_evaluate_reasons.append("artifactDescriptionRedacted must be non-empty")
    elif any(
        phrase in description.lower()
        for phrase in [
            "raw value label",
            "raw metadata",
            "session",
            "password",
            "individual death",
            "real row",
        ]
    ):
        reject_reasons.append("artifactDescriptionRedacted appears to describe forbidden raw or individual material")

    if "detailsPageUrlRedacted" in packet and not isinstance(packet.get("detailsPageUrlRedacted"), str):
        reject_reasons.append("detailsPageUrlRedacted must be a redacted string")

    missing_review_flags = sorted(flag for flag in REVIEW_FLAGS if packet.get(flag) is not True)
    if missing_review_flags:
        cannot_evaluate_reasons.append(
            f"review flags must all be true for a reviewable packet: {', '.join(missing_review_flags)}"
        )

    index = task_index(task_register)
    task_key = (str(packet.get("requiredRouteFieldId", "")), str(packet.get("taskId", "")))
    matched_task = index.get(task_key)
    if matched_task is None:
        reject_reasons.append("packet does not match a registered capture task")
    else:
        if packet.get("variableName") != matched_task.get("variableName"):
            reject_reasons.append("variableName does not match registered task")
        if packet.get("round") != matched_task.get("round"):
            reject_reasons.append("round does not match registered task")
        if matched_task.get("taskStatus") not in {"pending", "pending-real-extraction"}:
            reject_reasons.append("registered task is not pending")
        if matched_task.get("groupPromotionAllowed") is not False:
            reject_reasons.append("registered task group must keep promotionAllowed=false")

    if reject_reasons:
        verdict = VERDICT_REJECTED
    elif cannot_evaluate_reasons:
        verdict = VERDICT_CANNOT_EVALUATE
    else:
        verdict = VERDICT_REVIEWABLE

    return {
        **REQUIRED_BLOCKED_DECISION,
        "packetId": packet.get("packetId"),
        "requiredRouteFieldId": packet.get("requiredRouteFieldId"),
        "taskId": packet.get("taskId"),
        "variableName": packet.get("variableName"),
        "verdict": verdict,
        "rejectReasons": reject_reasons,
        "cannotEvaluateReasons": cannot_evaluate_reasons,
        "matchedTask": matched_task,
    }


def validate_test_cases(
    test_cases: dict[str, Any],
    template: dict[str, Any],
    task_register: dict[str, Any],
    route_classifier_readiness: dict[str, Any],
) -> dict[str, Any]:
    if test_cases.get("schemaVersion") != TEST_CASES_SCHEMA:
        raise ValueError("test case schemaVersion mismatch")
    if test_cases.get("status") != "synthetic-validator-test-cases-only-model-g4-blocked":
        raise ValueError("test cases must remain synthetic-only and model-g4 blocked")

    expected_bindings = {
        "authenticatedCaptureTemplatePath": repo_rel(DEFAULT_TEMPLATE),
        "captureTaskRegisterPath": repo_rel(DEFAULT_TASK_REGISTER),
        "routeClassifierReadinessPath": repo_rel(DEFAULT_ROUTE_CLASSIFIER_READINESS),
    }
    bindings = test_cases.get("sourceBindings")
    if not isinstance(bindings, dict) or any(
        bindings.get(key) != expected for key, expected in expected_bindings.items()
    ):
        raise ValueError("test case sourceBindings do not match validator defaults")

    raw_cases = test_cases.get("testCases")
    if not isinstance(raw_cases, list) or len(raw_cases) < 5:
        raise ValueError("testCases must contain at least five cases")

    case_results: list[dict[str, Any]] = []
    failures: list[str] = []
    counts = {VERDICT_REVIEWABLE: 0, VERDICT_CANNOT_EVALUATE: 0, VERDICT_REJECTED: 0}
    for index, case in enumerate(raw_cases):
        if not isinstance(case, dict):
            failures.append(f"testCases[{index}] must be an object")
            continue
        case_id = str(case.get("caseId", f"case-{index}"))
        expected = case.get("expectedVerdict")
        if expected not in ALLOWED_VERDICTS:
            failures.append(f"{case_id} has invalid expectedVerdict")
            continue
        result = evaluate_packet(
            case.get("packet"),
            template,
            task_register,
            route_classifier_readiness,
        )
        verdict = result["verdict"]
        counts[verdict] = counts.get(verdict, 0) + 1
        blocked_ok = all(result.get(key) is value for key, value in REQUIRED_BLOCKED_DECISION.items())
        passed = verdict == expected and blocked_ok
        if not passed:
            failures.append(f"{case_id} expected {expected}, got {verdict}")
        case_results.append(
            {
                "caseId": case_id,
                "expectedVerdict": expected,
                "actualVerdict": verdict,
                "passed": passed,
                "rejectReasons": result["rejectReasons"],
                "cannotEvaluateReasons": result["cannotEvaluateReasons"],
                "matchedTask": result["matchedTask"],
            }
        )

    if counts[VERDICT_REVIEWABLE] < 1:
        failures.append("at least one reviewable-but-still-blocked case is required")
    if counts[VERDICT_CANNOT_EVALUATE] < 1:
        failures.append("at least one cannot-evaluate case is required")
    if counts[VERDICT_REJECTED] < 3:
        failures.append("at least three rejected cases are required")

    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "validationId": "nhats-r13-r14-colectica-capture-packet-validator-validation-2026-07-04",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "testCasesPath": repo_rel(DEFAULT_TEST_CASES),
            "testCasesSha256": sha256_file(DEFAULT_TEST_CASES),
            "authenticatedCaptureTemplatePath": repo_rel(DEFAULT_TEMPLATE),
            "authenticatedCaptureTemplateSha256": sha256_file(DEFAULT_TEMPLATE),
            "captureTaskRegisterPath": repo_rel(DEFAULT_TASK_REGISTER),
            "captureTaskRegisterSha256": sha256_file(DEFAULT_TASK_REGISTER),
            "routeClassifierReadinessPath": repo_rel(DEFAULT_ROUTE_CLASSIFIER_READINESS),
            "routeClassifierReadinessSha256": sha256_file(DEFAULT_ROUTE_CLASSIFIER_READINESS),
            "validator": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_capture_packet_validator.py",
        },
        "currentDecision": {
            "validatorReady": not failures,
            "testCaseCount": len(raw_cases),
            "reviewableButStillBlockedCount": counts[VERDICT_REVIEWABLE],
            "cannotEvaluateCount": counts[VERDICT_CANNOT_EVALUATE],
            "rejectedCount": counts[VERDICT_REJECTED],
            **REQUIRED_BLOCKED_DECISION,
            "reason": "This validator only checks synthetic future Colectica capture packet shapes. It does not attach real captures, close slots, promote route classifier, extract NHATS rows, publish weighted output, calibrate a model or support individual use.",
        },
        "caseResults": case_results,
        "hardBoundaries": [
            "Validator pass does not mean a real Colectica capture exists.",
            "A reviewable packet remains blocked until governed access, redacted source hashes, human review and second-reviewer signoff are externally evidenced.",
            "No output from this validator can close a capture slot or open route classifier, extraction, aggregate cohort flow, public export, calibration or individual prediction.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--task-register", type=Path, default=DEFAULT_TASK_REGISTER)
    parser.add_argument(
        "--route-classifier-readiness",
        type=Path,
        default=DEFAULT_ROUTE_CLASSIFIER_READINESS,
    )
    parser.add_argument("--packet", type=Path, help="Optional single packet JSON to evaluate.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        template = load_json(args.template.resolve(), "authenticated capture template")
        task_register = load_json(args.task_register.resolve(), "capture task register")
        route_classifier_readiness = load_json(
            args.route_classifier_readiness.resolve(),
            "route classifier readiness",
        )
        if args.packet:
            packet = load_json(args.packet.resolve(), "capture packet")
            validation = {
                "schemaVersion": VALIDATION_SCHEMA,
                "generatedAt": datetime.now(timezone.utc).isoformat(),
                "status": "single-packet-evaluated-model-g4-still-blocked",
                "currentDecision": {"validatorReady": True, **REQUIRED_BLOCKED_DECISION},
                "packetResult": evaluate_packet(
                    packet,
                    template,
                    task_register,
                    route_classifier_readiness,
                ),
            }
        else:
            test_cases = load_json(args.test_cases.resolve(), "capture packet validator test cases")
            validation = validate_test_cases(
                test_cases,
                template,
                task_register,
                route_classifier_readiness,
            )
        write_json(args.out.resolve(), validation)
        if validation["status"] == "fail":
            for failure in validation.get("failures", []):
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        decision = validation["currentDecision"]
        print(
            "NHATS Colectica capture packet validator ok: "
            f"cases={decision.get('testCaseCount', 1)} "
            f"reviewable={decision.get('reviewableButStillBlockedCount', 0)} "
            f"cannot_evaluate={decision.get('cannotEvaluateCount', 0)} "
            f"rejected={decision.get('rejectedCount', 0)} model_g4=blocked"
        )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
