#!/usr/bin/env python3
"""Build a fail-closed NHATS route-value crosswalk entry draft.

The draft is a local maintainer artifact for preparing future redacted
route-value / missing-code entries. It intentionally contains placeholder
hashes and must not become reviewable until controlled human review fills the
redacted evidence outside the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_nhats_route_value_crosswalk_entry_validator import (
    DEFAULT_CAPTURE_REVIEW,
    DEFAULT_CAPTURE_TASKS,
    DEFAULT_PROTOCOL,
    DEFAULT_ROUTE_READINESS,
    ENTRY_SCHEMA,
    REQUIRED_BLOCKED_DECISION,
    VERDICT_REVIEWABLE,
    evaluate_entry,
    load_json,
    repo_rel,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_ROUTE_FIELD_ID = "identity_join_key"
DEFAULT_OUT_DIR = (
    REPO_ROOT / "build" / "reports" / "nhats-route-value-crosswalk-entry-draft"
)
DEFAULT_ENTRY_OUT = DEFAULT_OUT_DIR / f"{DEFAULT_ROUTE_FIELD_ID}-draft.json"
DEFAULT_VALIDATION_OUT = DEFAULT_OUT_DIR / f"{DEFAULT_ROUTE_FIELD_ID}-draft-validation.json"
DRAFT_VALIDATION_SCHEMA = "human-infra.life-path-nhats-route-value-crosswalk-entry-draft.v1"


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_tasks(capture_tasks: dict[str, Any], route_field_id: str) -> list[dict[str, Any]]:
    groups = capture_tasks.get("captureTaskGroups")
    if not isinstance(groups, list):
        return []
    for group in groups:
        if not isinstance(group, dict) or group.get("requiredRouteFieldId") != route_field_id:
            continue
        tasks = group.get("tasks")
        if not isinstance(tasks, list):
            return []
        return [task for task in tasks if isinstance(task, dict)]
    return []


def build_entry(
    *,
    route_field_id: str,
    protocol: dict[str, Any],
    capture_review: dict[str, Any],
    capture_tasks: dict[str, Any],
    route_readiness: dict[str, Any],
    tasks: list[dict[str, Any]],
) -> dict[str, Any]:
    today = datetime.now(timezone.utc).date().isoformat()
    variable_name = str(tasks[0].get("variableName", route_field_id)) if tasks else route_field_id
    task_ids = [str(task["taskId"]) for task in tasks if isinstance(task.get("taskId"), str)]
    return {
        "entrySchema": ENTRY_SCHEMA,
        "entryId": f"DRAFT-NHATS-ROUTE-VALUE-CROSSWALK-{route_field_id}",
        "sourceId": "nhats",
        "assemblyProtocolId": protocol.get("protocolId"),
        "capturePacketReviewExecutionRegisterId": capture_review.get("executionRegisterId"),
        "captureTaskRegisterId": capture_tasks.get("taskRegisterId"),
        "routeClassifierReadinessId": route_readiness.get("readinessId"),
        "requiredRouteFieldId": route_field_id,
        "sourceTaskIds": task_ids,
        "reviewedCapturePacketIds": ["REPLACE_WITH_REVIEWED_CAPTURE_PACKET_ID"],
        "sourceCaptureSha256": "REPLACE_WITH_REAL_64_HEX_SHA256",
        "artifactHashAlgorithm": "sha256",
        "captureDate": today,
        "entryDescriptionRedacted": (
            "Draft crosswalk entry shape only; real Colectica value labels, row-level "
            "data, restricted exports, credentials and individual dates are not attached."
        ),
        "routeValueRowsRedacted": [
            {
                "variableName": variable_name,
                "sourceValueHash": "REPLACE_WITH_REAL_64_HEX_SHA256",
                "routeValueClassRedacted": "REPLACE_WITH_REDACTED_ROUTE_VALUE_CLASS",
                "routeInterpretationRedacted": "REPLACE_WITH_REDACTED_ROUTE_INTERPRETATION",
            }
        ],
        "variableSpecificMissingCodeRowsRedacted": [
            {
                "variableName": variable_name,
                "sourceValueHash": "REPLACE_WITH_REAL_64_HEX_SHA256",
                "missingnessClassRedacted": "REPLACE_WITH_REDACTED_MISSINGNESS_CLASS",
                "missingnessInterpretationRedacted": (
                    "REPLACE_WITH_REDACTED_MISSINGNESS_INTERPRETATION"
                ),
            }
        ],
        "valueLabelsReviewed": False,
        "questionTextReviewed": False,
        "universeSkipLogicReviewed": False,
        "routeValueRowsReviewed": False,
        "variableSpecificMissingCodesReviewed": False,
        "sensitiveRestrictedExclusionReviewed": False,
        "sensitiveDeathDateFieldsExcluded": True,
        "reviewerRole": "human-domain-reviewer",
        "secondReviewerRole": "independent-human-reviewer",
        "aiOnlySignoff": False,
        "publicAiUpload": False,
        "assemblyUnitClosureAllowed": False,
        "routeClassifierAllowed": False,
        "realExtractionAllowed": False,
        "aggregateCohortFlowAllowed": False,
        "weightedRouteCountsAllowed": False,
        "publicExportAllowed": False,
        "calibrationAllowed": False,
        "individualPredictionAllowed": False,
        "draftHumanActions": [
            "Replace reviewedCapturePacketIds with governed reviewed capture packet ids.",
            "Replace placeholder SHA-256 fields with hashes of external redacted evidence artifacts.",
            "Fill redacted route-value and missing-code interpretations outside the repository.",
            "Set review flags to true only after controlled human review and independent second review.",
            "Keep every downstream permission flag false until a later governed register update.",
        ],
    }


def build_validation(
    *,
    entry: dict[str, Any],
    entry_out: Path,
    protocol: dict[str, Any],
    capture_review: dict[str, Any],
    capture_tasks: dict[str, Any],
    route_readiness: dict[str, Any],
    protocol_path: Path,
    capture_review_path: Path,
    capture_tasks_path: Path,
    route_readiness_path: Path,
) -> dict[str, Any]:
    entry_result = evaluate_entry(entry, protocol, capture_review, capture_tasks, route_readiness)
    failures: list[str] = []
    if entry_result.get("verdict") == VERDICT_REVIEWABLE:
        failures.append("draft entry must not become reviewable without controlled human review")
    blocked_ok = all(
        entry_result.get(field) is expected
        for field, expected in REQUIRED_BLOCKED_DECISION.items()
    )
    if not blocked_ok:
        failures.append("draft entry validator result must keep all blocked decision flags false")

    return {
        "schemaVersion": DRAFT_VALIDATION_SCHEMA,
        "validationId": f"nhats-route-value-crosswalk-entry-draft-{entry['requiredRouteFieldId']}",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "draftEntryPath": repo_rel(entry_out),
            "assemblyProtocolPath": repo_rel(protocol_path),
            "assemblyProtocolSha256": sha256_file(protocol_path),
            "capturePacketReviewExecutionPath": repo_rel(capture_review_path),
            "capturePacketReviewExecutionSha256": sha256_file(capture_review_path),
            "captureTaskRegisterPath": repo_rel(capture_tasks_path),
            "captureTaskRegisterSha256": sha256_file(capture_tasks_path),
            "routeClassifierReadinessPath": repo_rel(route_readiness_path),
            "routeClassifierReadinessSha256": sha256_file(route_readiness_path),
            "validatorPath": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_route_value_crosswalk_entry_validator.py",
        },
        "currentDecision": {
            "draftGenerated": True,
            "validatorVerdict": entry_result.get("verdict"),
            "modelG4": "blocked",
            **REQUIRED_BLOCKED_DECISION,
            "reason": (
                "This output is a fail-closed draft for route-value crosswalk entry "
                "preparation only. It does not attach reviewed capture packets, confirm "
                "value labels, close an assembly unit, open a route classifier, extract "
                "NHATS rows, publish output, calibrate a model or support individual "
                "prediction."
            ),
        },
        "entryResult": entry_result,
        "hardBoundaries": [
            "Generated drafts are ignored local artifacts under build/reports/.",
            "A generated draft is intentionally cannot-evaluate until external redacted hashes and human review flags are filled.",
            "A reviewable validator result would still remain model_g4=blocked and cannot close assembly units by itself.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--capture-review", type=Path, default=DEFAULT_CAPTURE_REVIEW)
    parser.add_argument("--capture-tasks", type=Path, default=DEFAULT_CAPTURE_TASKS)
    parser.add_argument("--route-readiness", type=Path, default=DEFAULT_ROUTE_READINESS)
    parser.add_argument("--required-route-field-id", default=DEFAULT_ROUTE_FIELD_ID)
    parser.add_argument("--entry-out", type=Path, default=DEFAULT_ENTRY_OUT)
    parser.add_argument("--validation-out", type=Path, default=DEFAULT_VALIDATION_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        protocol_path = args.protocol.resolve()
        capture_review_path = args.capture_review.resolve()
        capture_tasks_path = args.capture_tasks.resolve()
        route_readiness_path = args.route_readiness.resolve()
        entry_out = args.entry_out.resolve()
        validation_out = args.validation_out.resolve()

        protocol = load_json(protocol_path, "route-value crosswalk assembly protocol")
        capture_review = load_json(capture_review_path, "capture packet review execution")
        capture_tasks = load_json(capture_tasks_path, "capture task register")
        route_readiness = load_json(route_readiness_path, "route classifier readiness")
        tasks = collect_tasks(capture_tasks, args.required_route_field_id)
        if not tasks:
            raise ValueError(f"missing registered source tasks: {args.required_route_field_id}")

        entry = build_entry(
            route_field_id=args.required_route_field_id,
            protocol=protocol,
            capture_review=capture_review,
            capture_tasks=capture_tasks,
            route_readiness=route_readiness,
            tasks=tasks,
        )
        validation = build_validation(
            entry=entry,
            entry_out=entry_out,
            protocol=protocol,
            capture_review=capture_review,
            capture_tasks=capture_tasks,
            route_readiness=route_readiness,
            protocol_path=protocol_path,
            capture_review_path=capture_review_path,
            capture_tasks_path=capture_tasks_path,
            route_readiness_path=route_readiness_path,
        )

        write_json(entry_out, entry)
        write_json(validation_out, validation)
        if validation["status"] != "pass":
            for failure in validation["failures"]:
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        print(
            "NHATS route-value crosswalk entry draft ok: "
            f"field={entry['requiredRouteFieldId']} "
            f"verdict={validation['currentDecision']['validatorVerdict']} model_g4=blocked"
        )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
