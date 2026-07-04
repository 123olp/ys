#!/usr/bin/env python3
"""Validate synthetic NHATS route-value crosswalk entry preflight semantics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
    MANUAL_DIR / "life_path_nhats_route_value_crosswalk_entry_validator_test_cases.json"
)
DEFAULT_PROTOCOL = MANUAL_DIR / "life_path_nhats_route_value_crosswalk_assembly_protocol.json"
DEFAULT_CAPTURE_REVIEW = (
    MANUAL_DIR / "life_path_nhats_colectica_capture_packet_review_execution_register.json"
)
DEFAULT_CAPTURE_TASKS = MANUAL_DIR / "life_path_nhats_colectica_capture_task_register.json"
DEFAULT_ROUTE_READINESS = MANUAL_DIR / "life_path_nhats_route_classifier_readiness.json"
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-value-crosswalk-entry-validator-validation.json"
)

TEST_CASES_SCHEMA = (
    "human-infra.life-path-nhats-route-value-crosswalk-entry-validator-test-cases.v1"
)
VALIDATION_SCHEMA = (
    "human-infra.life-path-nhats-route-value-crosswalk-entry-validator-validation.v1"
)
ENTRY_SCHEMA = "human-infra.life-path-nhats-route-value-crosswalk-entry.v1"
HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")

VERDICT_REVIEWABLE = "reviewable-but-still-blocked"
VERDICT_CANNOT_EVALUATE = "cannot-evaluate"
VERDICT_REJECTED = "rejected"
ALLOWED_VERDICTS = {VERDICT_REVIEWABLE, VERDICT_CANNOT_EVALUATE, VERDICT_REJECTED}

REQUIRED_ENTRY_FIELDS = {
    "entrySchema",
    "entryId",
    "sourceId",
    "assemblyProtocolId",
    "capturePacketReviewExecutionRegisterId",
    "captureTaskRegisterId",
    "routeClassifierReadinessId",
    "requiredRouteFieldId",
    "sourceTaskIds",
    "reviewedCapturePacketIds",
    "sourceCaptureSha256",
    "routeValueRowsRedacted",
    "variableSpecificMissingCodeRowsRedacted",
    "valueLabelsReviewed",
    "questionTextReviewed",
    "universeSkipLogicReviewed",
    "routeValueRowsReviewed",
    "variableSpecificMissingCodesReviewed",
    "sensitiveRestrictedExclusionReviewed",
    "sensitiveDeathDateFieldsExcluded",
    "reviewerRole",
    "secondReviewerRole",
    "aiOnlySignoff",
    "publicAiUpload",
    "assemblyUnitClosureAllowed",
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
    "assemblyUnitClosureAllowed",
    "routeClassifierAllowed",
    "realExtractionAllowed",
    "aggregateCohortFlowAllowed",
    "weightedRouteCountsAllowed",
    "publicExportAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REVIEW_FLAGS = {
    "valueLabelsReviewed",
    "questionTextReviewed",
    "universeSkipLogicReviewed",
    "routeValueRowsReviewed",
    "variableSpecificMissingCodesReviewed",
    "sensitiveRestrictedExclusionReviewed",
    "sensitiveDeathDateFieldsExcluded",
}
PROHIBITED_KEYS = {
    "password",
    "sessionCookie",
    "sessionCookies",
    "authToken",
    "accessToken",
    "accountEmail",
    "accountId",
    "rawValueLabels",
    "rawColecticaExport",
    "rawMetadataDump",
    "rowLevelData",
    "deathDate",
    "deathMonth",
    "deathYear",
    "individualDeathDate",
    "predictedDeathDate",
    "individualPrediction",
    "realWeightedCount",
}
SENSITIVE_DEATH_VARIABLES = {
    "dm13mthdied",
    "dm13yrdied",
    "dm14mthdied",
    "dm14yrdied",
}
REQUIRED_BLOCKED_DECISION = {
    "realEntryAttached": False,
    "assemblyUnitClosureAllowed": False,
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


def reviewer_is_human(role: Any) -> bool:
    if not isinstance(role, str):
        return False
    normalized = role.strip().lower()
    return bool(normalized) and "human" in normalized and "ai-only" not in normalized


def task_index(capture_tasks: dict[str, Any]) -> dict[str, set[str]]:
    index: dict[str, set[str]] = {}
    groups = capture_tasks.get("captureTaskGroups")
    if not isinstance(groups, list):
        return index
    for group in groups:
        if not isinstance(group, dict) or not isinstance(group.get("requiredRouteFieldId"), str):
            continue
        tasks = group.get("tasks")
        if not isinstance(tasks, list):
            continue
        index[group["requiredRouteFieldId"]] = {
            str(task["taskId"])
            for task in tasks
            if isinstance(task, dict) and isinstance(task.get("taskId"), str)
        }
    return index


def protocol_field_ids(protocol: dict[str, Any]) -> set[str]:
    units = protocol.get("assemblyUnits")
    if not isinstance(units, list):
        return set()
    return {
        str(unit["requiredRouteFieldId"])
        for unit in units
        if isinstance(unit, dict) and isinstance(unit.get("requiredRouteFieldId"), str)
    }


def rows_have_hashes(rows: Any, row_label: str) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if not isinstance(rows, list) or not rows:
        return False, [f"{row_label} must be a non-empty list"]
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            reasons.append(f"{row_label}[{index}] must be an object")
            continue
        if not isinstance(row.get("variableName"), str) or not row["variableName"].strip():
            reasons.append(f"{row_label}[{index}].variableName is required")
        if not isinstance(row.get("sourceValueHash"), str) or not HASH_RE.fullmatch(
            row["sourceValueHash"]
        ):
            reasons.append(f"{row_label}[{index}].sourceValueHash must be a sha256 hash")
    return not reasons, reasons


def contains_sensitive_death_variable(entry: dict[str, Any]) -> bool:
    text = json.dumps(entry, ensure_ascii=False).lower()
    return any(variable in text for variable in SENSITIVE_DEATH_VARIABLES)


def evaluate_entry(
    entry: Any,
    protocol: dict[str, Any],
    capture_review: dict[str, Any],
    capture_tasks: dict[str, Any],
    route_readiness: dict[str, Any],
) -> dict[str, Any]:
    reject_reasons: list[str] = []
    cannot_evaluate_reasons: list[str] = []
    matched_field: str | None = None

    if not isinstance(entry, dict):
        return {
            **REQUIRED_BLOCKED_DECISION,
            "entryId": None,
            "verdict": VERDICT_REJECTED,
            "rejectReasons": ["entry must be a JSON object"],
            "cannotEvaluateReasons": [],
            "matchedField": None,
        }

    missing_fields = sorted(REQUIRED_ENTRY_FIELDS - set(entry))
    if missing_fields:
        cannot_evaluate_reasons.append(f"missing required fields: {', '.join(missing_fields)}")

    if entry.get("entrySchema") != ENTRY_SCHEMA:
        reject_reasons.append("entrySchema is invalid")
    if entry.get("sourceId") != "nhats":
        reject_reasons.append("sourceId must be nhats")
    if entry.get("assemblyProtocolId") != protocol.get("protocolId"):
        reject_reasons.append("assemblyProtocolId does not match protocol")
    if entry.get("capturePacketReviewExecutionRegisterId") != capture_review.get(
        "executionRegisterId"
    ):
        reject_reasons.append("capturePacketReviewExecutionRegisterId does not match")
    if entry.get("captureTaskRegisterId") != capture_tasks.get("taskRegisterId"):
        reject_reasons.append("captureTaskRegisterId does not match")
    if entry.get("routeClassifierReadinessId") != route_readiness.get("readinessId"):
        reject_reasons.append("routeClassifierReadinessId does not match")

    field_id = entry.get("requiredRouteFieldId")
    field_ids = protocol_field_ids(protocol)
    tasks_by_field = task_index(capture_tasks)
    if isinstance(field_id, str) and field_id in field_ids:
        matched_field = field_id
        source_tasks = entry.get("sourceTaskIds")
        if not isinstance(source_tasks, list) or not source_tasks:
            cannot_evaluate_reasons.append("sourceTaskIds must be a non-empty list")
        elif set(map(str, source_tasks)) != tasks_by_field.get(field_id, set()):
            reject_reasons.append("sourceTaskIds must exactly match registered tasks")
    else:
        reject_reasons.append("requiredRouteFieldId is not registered in assembly protocol")

    if not isinstance(entry.get("reviewedCapturePacketIds"), list) or not entry.get(
        "reviewedCapturePacketIds"
    ):
        cannot_evaluate_reasons.append("reviewedCapturePacketIds must be a non-empty list")
    if not isinstance(entry.get("sourceCaptureSha256"), str) or not HASH_RE.fullmatch(
        str(entry.get("sourceCaptureSha256"))
    ):
        cannot_evaluate_reasons.append("sourceCaptureSha256 must be a sha256 hash")

    route_rows_ok, route_row_reasons = rows_have_hashes(
        entry.get("routeValueRowsRedacted"), "routeValueRowsRedacted"
    )
    missing_rows_ok, missing_row_reasons = rows_have_hashes(
        entry.get("variableSpecificMissingCodeRowsRedacted"),
        "variableSpecificMissingCodeRowsRedacted",
    )
    if not route_rows_ok:
        cannot_evaluate_reasons.extend(route_row_reasons)
    if not missing_rows_ok:
        cannot_evaluate_reasons.extend(missing_row_reasons)

    for key in REVIEW_FLAGS:
        if entry.get(key) is not True:
            cannot_evaluate_reasons.append(f"{key} must be true before entry review")
    for key in REQUIRED_FALSE_FIELDS:
        if entry.get(key) is not False:
            reject_reasons.append(f"{key} must remain false")

    if entry.get("aiOnlySignoff") is True or entry.get("publicAiUpload") is True:
        reject_reasons.append("AI-only signoff and public AI upload are prohibited")
    if not reviewer_is_human(entry.get("reviewerRole")):
        reject_reasons.append("reviewerRole must identify a human reviewer")
    if not reviewer_is_human(entry.get("secondReviewerRole")):
        reject_reasons.append("secondReviewerRole must identify an independent human reviewer")
    if entry.get("reviewerRole") == entry.get("secondReviewerRole"):
        reject_reasons.append("secondReviewerRole must differ from reviewerRole")

    prohibited_keys_found = collect_keys(entry) & PROHIBITED_KEYS
    if prohibited_keys_found:
        reject_reasons.append(
            "entry contains prohibited keys: " + ", ".join(sorted(prohibited_keys_found))
        )
    if contains_sensitive_death_variable(entry) or entry.get("sensitiveDeathDateFieldsExcluded") is not True:
        reject_reasons.append("sensitive death timing fields must be excluded")

    downstream = route_readiness.get("currentDecision", {})
    if (
        downstream.get("routeClassifierReady") is not False
        or downstream.get("routeValueCrosswalkConfirmed") is not False
        or downstream.get("variableSpecificMissingCodeMapConfirmed") is not False
    ):
        reject_reasons.append("downstream route classifier readiness must remain blocked")

    if reject_reasons:
        verdict = VERDICT_REJECTED
    elif cannot_evaluate_reasons:
        verdict = VERDICT_CANNOT_EVALUATE
    else:
        verdict = VERDICT_REVIEWABLE

    return {
        **REQUIRED_BLOCKED_DECISION,
        "entryId": entry.get("entryId"),
        "verdict": verdict,
        "rejectReasons": reject_reasons,
        "cannotEvaluateReasons": cannot_evaluate_reasons,
        "matchedField": matched_field,
    }


def evaluate_test_cases(
    test_cases: dict[str, Any],
    protocol: dict[str, Any],
    capture_review: dict[str, Any],
    capture_tasks: dict[str, Any],
    route_readiness: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[str]]:
    failures: list[str] = []
    results: list[dict[str, Any]] = []
    if test_cases.get("schemaVersion") != TEST_CASES_SCHEMA:
        failures.append("invalid test case schemaVersion")
    if test_cases.get("status") != "synthetic-entry-validator-test-cases-only-model-g4-blocked":
        failures.append("test case status must keep model G4 blocked")
    cases = test_cases.get("testCases")
    if not isinstance(cases, list) or len(cases) < 6:
        failures.append("at least six test cases are required")
        cases = []
    counts = {verdict: 0 for verdict in ALLOWED_VERDICTS}
    for case in cases:
        if not isinstance(case, dict):
            failures.append("each test case must be an object")
            continue
        case_id = case.get("caseId")
        expected = case.get("expectedVerdict")
        if expected not in ALLOWED_VERDICTS:
            failures.append(f"{case_id}: invalid expectedVerdict={expected!r}")
            continue
        result = evaluate_entry(
            case.get("entry"), protocol, capture_review, capture_tasks, route_readiness
        )
        counts[result["verdict"]] += 1
        result = {
            "caseId": case_id,
            "expectedVerdict": expected,
            **result,
        }
        results.append(result)
        if result["verdict"] != expected:
            failures.append(
                f"{case_id}: expected {expected}, got {result['verdict']}"
            )
        for key, expected_value in REQUIRED_BLOCKED_DECISION.items():
            if result.get(key) is not expected_value:
                failures.append(f"{case_id}: {key} must remain {expected_value}")
    if counts[VERDICT_REVIEWABLE] < 1:
        failures.append("at least one reviewable-but-still-blocked case is required")
    if counts[VERDICT_CANNOT_EVALUATE] < 1:
        failures.append("at least one cannot-evaluate case is required")
    if counts[VERDICT_REJECTED] < 3:
        failures.append("at least three rejected cases are required")
    return results, failures


def build_report(
    test_cases_path: Path,
    protocol_path: Path,
    capture_review_path: Path,
    capture_tasks_path: Path,
    route_readiness_path: Path,
) -> dict[str, Any]:
    test_cases = load_json(test_cases_path, "test cases")
    protocol = load_json(protocol_path, "assembly protocol")
    capture_review = load_json(capture_review_path, "capture review execution")
    capture_tasks = load_json(capture_tasks_path, "capture task register")
    route_readiness = load_json(route_readiness_path, "route classifier readiness")
    results, failures = evaluate_test_cases(
        test_cases, protocol, capture_review, capture_tasks, route_readiness
    )
    verdict_counts = {
        verdict: sum(1 for result in results if result["verdict"] == verdict)
        for verdict in sorted(ALLOWED_VERDICTS)
    }
    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "validationId": "life-path-nhats-route-value-crosswalk-entry-validator-validation",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "overallStatus": "PASS" if not failures else "FAIL",
        "summary": {
            "caseCount": len(results),
            "reviewableButStillBlockedCount": verdict_counts[VERDICT_REVIEWABLE],
            "cannotEvaluateCount": verdict_counts[VERDICT_CANNOT_EVALUATE],
            "rejectedCount": verdict_counts[VERDICT_REJECTED],
            "failureCount": len(failures),
        },
        "testCases": {
            "path": repo_rel(test_cases_path),
            "sha256": sha256_file(test_cases_path),
            "testSetId": test_cases.get("testSetId"),
            "status": test_cases.get("status"),
        },
        "upstreams": [
            {
                "path": repo_rel(protocol_path),
                "sha256": sha256_file(protocol_path),
                "id": protocol.get("protocolId"),
            },
            {
                "path": repo_rel(capture_review_path),
                "sha256": sha256_file(capture_review_path),
                "id": capture_review.get("executionRegisterId"),
            },
            {
                "path": repo_rel(capture_tasks_path),
                "sha256": sha256_file(capture_tasks_path),
                "id": capture_tasks.get("taskRegisterId"),
            },
            {
                "path": repo_rel(route_readiness_path),
                "sha256": sha256_file(route_readiness_path),
                "id": route_readiness.get("readinessId"),
            },
        ],
        "results": results,
        "failures": failures,
        "decision": {
            "modelG4Status": "blocked",
            **REQUIRED_BLOCKED_DECISION,
        },
        "boundary": "This validation proves only that synthetic future route-value crosswalk entry shapes are classified as rejected, cannot-evaluate or reviewable-but-still-blocked. It closes no assembly unit, confirms no real route-value row, confirms no real variable-specific missing-code map, and does not allow route classifier, extraction, public output, calibration or individual prediction.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS route-value crosswalk entry preflight semantics."
    )
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--capture-review", type=Path, default=DEFAULT_CAPTURE_REVIEW)
    parser.add_argument("--capture-tasks", type=Path, default=DEFAULT_CAPTURE_TASKS)
    parser.add_argument("--route-readiness", type=Path, default=DEFAULT_ROUTE_READINESS)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        args.test_cases,
        args.protocol,
        args.capture_review,
        args.capture_tasks,
        args.route_readiness,
    )
    write_json(args.out, report)
    print(
        "NHATS route-value crosswalk entry validator audit ok: "
        f"cases={report['summary']['caseCount']} "
        f"reviewable={report['summary']['reviewableButStillBlockedCount']} "
        f"cannot_evaluate={report['summary']['cannotEvaluateCount']} "
        f"rejected={report['summary']['rejectedCount']} model_g4=blocked"
    )
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
