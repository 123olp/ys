#!/usr/bin/env python3
"""Build a fail-closed NHATS Colectica capture packet draft.

The draft is a local working artifact for maintainers. It intentionally does
not contain real Colectica evidence and must not become reviewable until a
controlled human capture fills the redacted evidence fields outside the repo.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_nhats_colectica_capture_packet_validator import (
    DEFAULT_ROUTE_CLASSIFIER_READINESS,
    DEFAULT_TASK_REGISTER,
    DEFAULT_TEMPLATE,
    PACKET_SCHEMA,
    REQUIRED_BLOCKED_DECISION,
    VERDICT_REVIEWABLE,
    evaluate_packet,
    load_json,
    repo_rel,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_TASK_ID = "identity_join_key-spid"
DEFAULT_ROUTE_FIELD_ID = "identity_join_key"
DEFAULT_OUT_DIR = REPO_ROOT / "build" / "reports" / "nhats-colectica-capture-packet-draft"
DEFAULT_PACKET_OUT = DEFAULT_OUT_DIR / f"{DEFAULT_TASK_ID}-draft.json"
DEFAULT_VALIDATION_OUT = DEFAULT_OUT_DIR / f"{DEFAULT_TASK_ID}-draft-validation.json"
DEFAULT_BATCH_VALIDATION_OUT = DEFAULT_OUT_DIR / "all-drafts-validation.json"
DRAFT_VALIDATION_SCHEMA = "human-infra.life-path-nhats-colectica-capture-packet-draft.v1"
BATCH_DRAFT_VALIDATION_SCHEMA = "human-infra.life-path-nhats-colectica-capture-packet-draft-batch.v1"


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_tasks(register: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}
    groups = register.get("captureTaskGroups")
    if not isinstance(groups, list):
        return index
    for group in groups:
        if not isinstance(group, dict):
            continue
        route_field_id = group.get("requiredRouteFieldId")
        if not isinstance(route_field_id, str):
            continue
        for task in group.get("tasks", []):
            if not isinstance(task, dict) or not isinstance(task.get("taskId"), str):
                continue
            index[(route_field_id, task["taskId"])] = {
                **task,
                "requiredRouteFieldId": route_field_id,
                "groupTaskStatus": group.get("taskStatus"),
                "groupPromotionAllowed": group.get("promotionAllowed"),
            }
    return index


def build_packet(
    *,
    task: dict[str, Any],
    task_register: dict[str, Any],
    template: dict[str, Any],
    readiness: dict[str, Any],
) -> dict[str, Any]:
    today = datetime.now(timezone.utc).date().isoformat()
    return {
        "packetSchema": PACKET_SCHEMA,
        "packetId": f"DRAFT-NHATS-COLECTICA-{task['taskId']}",
        "sourceId": "nhats",
        "taskRegisterId": task_register.get("taskRegisterId"),
        "templateId": template.get("templateId"),
        "routeClassifierReadinessId": readiness.get("readinessId"),
        "requiredRouteFieldId": task["requiredRouteFieldId"],
        "taskId": task["taskId"],
        "variableName": task.get("variableName"),
        "round": task.get("round"),
        "fileNameRedacted": "REPLACE_WITH_REDACTED_PUBLIC_USE_FILE_NAME_OR_CONTEXT",
        "detailsPageUrlRedacted": "REPLACE_WITH_REDACTED_CONTROLLED_COLECTICA_DETAILS_URL",
        "sourceCaptureSha256": "REPLACE_WITH_REAL_64_HEX_SHA256",
        "artifactHashAlgorithm": "sha256",
        "captureMethod": "controlled-colectica-authenticated-page-redacted",
        "captureDate": today,
        "artifactDescriptionRedacted": (
            "Draft packet shape only; credential material, row-level material, identifiers, "
            "restricted exports and individual dates are not attached."
        ),
        "valueLabelsReviewed": False,
        "questionTextReviewed": False,
        "universeSkipLogicReviewed": False,
        "concordanceReviewed": False,
        "publicUseTierReviewed": False,
        "sensitiveRestrictedExclusionReviewed": False,
        "variableSpecificMissingCodesReviewed": False,
        "reviewerRole": "human-domain-reviewer",
        "secondReviewerRole": "independent-human-reviewer",
        "aiOnlySignoff": False,
        "publicAiUpload": False,
        "rawMetadataAttached": False,
        "rawValueLabelsAttached": False,
        "promotionAllowed": False,
        "routeClassifierAllowed": False,
        "realExtractionAllowed": False,
        "aggregateCohortFlowAllowed": False,
        "weightedRouteCountsAllowed": False,
        "publicExportAllowed": False,
        "calibrationAllowed": False,
        "individualPredictionAllowed": False,
        "draftHumanActions": [
            "Replace detailsPageUrlRedacted with a redacted controlled page reference.",
            "Replace sourceCaptureSha256 with the SHA-256 of the external redacted capture artifact.",
            "Set review flags to true only after controlled human review outside the repository.",
            "Keep every permission and promotion flag false until governed second review closes a later register update.",
        ],
    }


def build_validation(
    *,
    packet: dict[str, Any],
    packet_out: Path,
    template: dict[str, Any],
    task_register: dict[str, Any],
    readiness: dict[str, Any],
    template_path: Path,
    task_register_path: Path,
    readiness_path: Path,
) -> dict[str, Any]:
    packet_result = evaluate_packet(packet, template, task_register, readiness)
    failures: list[str] = []
    if packet_result.get("verdict") == VERDICT_REVIEWABLE:
        failures.append("draft packet must not become reviewable without controlled human capture")

    blocked_ok = all(
        packet_result.get(field) is expected
        for field, expected in REQUIRED_BLOCKED_DECISION.items()
    )
    if not blocked_ok:
        failures.append("draft packet validator result must keep all blocked decision flags false")

    return {
        "schemaVersion": DRAFT_VALIDATION_SCHEMA,
        "validationId": f"nhats-colectica-capture-packet-draft-{packet['taskId']}",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "draftPacketPath": repo_rel(packet_out),
            "authenticatedCaptureTemplatePath": repo_rel(template_path),
            "authenticatedCaptureTemplateSha256": sha256_file(template_path),
            "captureTaskRegisterPath": repo_rel(task_register_path),
            "captureTaskRegisterSha256": sha256_file(task_register_path),
            "routeClassifierReadinessPath": repo_rel(readiness_path),
            "routeClassifierReadinessSha256": sha256_file(readiness_path),
            "validatorPath": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_capture_packet_validator.py",
        },
        "currentDecision": {
            "draftGenerated": True,
            "validatorVerdict": packet_result.get("verdict"),
            "modelG4": "blocked",
            **REQUIRED_BLOCKED_DECISION,
            "reason": (
                "This output is a fail-closed draft for packet shape preparation only. "
                "It does not attach controlled Colectica evidence, close a capture slot, "
                "promote a route classifier, extract NHATS rows, publish output, calibrate "
                "a model or support individual prediction."
            ),
        },
        "packetResult": packet_result,
        "hardBoundaries": [
            "Generated drafts are ignored local artifacts under build/reports/.",
            "A generated draft is intentionally rejected or cannot-evaluate until real redacted human capture evidence is filled outside the repository.",
            "A reviewable validator result still remains model_g4=blocked and cannot close review registers by itself.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--task-register", type=Path, default=DEFAULT_TASK_REGISTER)
    parser.add_argument("--route-classifier-readiness", type=Path, default=DEFAULT_ROUTE_CLASSIFIER_READINESS)
    parser.add_argument("--required-route-field-id", default=DEFAULT_ROUTE_FIELD_ID)
    parser.add_argument("--task-id", default=DEFAULT_TASK_ID)
    parser.add_argument(
        "--all-tasks",
        action="store_true",
        help="Generate fail-closed draft packets for every registered capture task.",
    )
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument("--packet-out", type=Path, default=DEFAULT_PACKET_OUT)
    parser.add_argument("--validation-out", type=Path, default=DEFAULT_VALIDATION_OUT)
    parser.add_argument("--batch-validation-out", type=Path, default=DEFAULT_BATCH_VALIDATION_OUT)
    return parser.parse_args()


def default_packet_out(out_dir: Path, task: dict[str, Any]) -> Path:
    return out_dir / f"{task['taskId']}-draft.json"


def default_validation_out(out_dir: Path, task: dict[str, Any]) -> Path:
    return out_dir / f"{task['taskId']}-draft-validation.json"


def main() -> int:
    args = parse_args()
    try:
        template_path = args.template.resolve()
        task_register_path = args.task_register.resolve()
        readiness_path = args.route_classifier_readiness.resolve()
        packet_out = args.packet_out.resolve()
        validation_out = args.validation_out.resolve()

        template = load_json(template_path, "authenticated capture template")
        task_register = load_json(task_register_path, "capture task register")
        readiness = load_json(readiness_path, "route classifier readiness")
        tasks = collect_tasks(task_register)
        if args.all_tasks:
            out_dir = args.out_dir.resolve()
            batch_validation_out = args.batch_validation_out.resolve()
            batch_results: list[dict[str, Any]] = []
            failures: list[str] = []
            for task in sorted(tasks.values(), key=lambda item: item["taskId"]):
                task_packet_out = default_packet_out(out_dir, task).resolve()
                task_validation_out = default_validation_out(out_dir, task).resolve()
                packet = build_packet(
                    task=task,
                    task_register=task_register,
                    template=template,
                    readiness=readiness,
                )
                validation = build_validation(
                    packet=packet,
                    packet_out=task_packet_out,
                    template=template,
                    task_register=task_register,
                    readiness=readiness,
                    template_path=template_path,
                    task_register_path=task_register_path,
                    readiness_path=readiness_path,
                )
                write_json(task_packet_out, packet)
                write_json(task_validation_out, validation)
                if validation["status"] != "pass":
                    failures.extend(f"{task['taskId']}: {failure}" for failure in validation["failures"])
                batch_results.append(
                    {
                        "taskId": task["taskId"],
                        "requiredRouteFieldId": task["requiredRouteFieldId"],
                        "draftPacketPath": repo_rel(task_packet_out),
                        "draftValidationPath": repo_rel(task_validation_out),
                        "validatorVerdict": validation["currentDecision"]["validatorVerdict"],
                        "modelG4": validation["currentDecision"]["modelG4"],
                        "status": validation["status"],
                    }
                )
            batch_validation = {
                "schemaVersion": BATCH_DRAFT_VALIDATION_SCHEMA,
                "validationId": "nhats-colectica-capture-packet-draft-all-tasks",
                "generatedAt": datetime.now(timezone.utc).isoformat(),
                "status": "pass" if not failures else "fail",
                "sourceRefs": {
                    "authenticatedCaptureTemplatePath": repo_rel(template_path),
                    "authenticatedCaptureTemplateSha256": sha256_file(template_path),
                    "captureTaskRegisterPath": repo_rel(task_register_path),
                    "captureTaskRegisterSha256": sha256_file(task_register_path),
                    "routeClassifierReadinessPath": repo_rel(readiness_path),
                    "routeClassifierReadinessSha256": sha256_file(readiness_path),
                },
                "summary": {
                    "registeredTaskCount": len(tasks),
                    "draftPacketCount": len(batch_results),
                    "draftValidationCount": len(batch_results),
                    "passCount": sum(1 for item in batch_results if item["status"] == "pass"),
                    "modelG4Decision": "blocked",
                    "trackedReviewSlotClosures": 0,
                },
                "results": batch_results,
                "hardBoundaries": [
                    "Generated batch drafts are ignored local artifacts under build/reports/.",
                    "Batch generation does not prove controlled Colectica login, real variable-page capture or human review.",
                    "Every draft remains model_g4=blocked and cannot close tracked capture slots.",
                ],
                "failures": failures,
            }
            write_json(batch_validation_out, batch_validation)
            if failures:
                for failure in failures:
                    print(f"ERROR: {failure}", file=sys.stderr)
                return 1
            print(
                "NHATS Colectica capture packet draft batch ok: "
                f"tasks={len(batch_results)} model_g4=blocked"
            )
        else:
            task = tasks.get((args.required_route_field_id, args.task_id))
            if task is None:
                raise ValueError(
                    f"missing registered capture task: {args.required_route_field_id}/{args.task_id}"
                )

            packet = build_packet(task=task, task_register=task_register, template=template, readiness=readiness)
            validation = build_validation(
                packet=packet,
                packet_out=packet_out,
                template=template,
                task_register=task_register,
                readiness=readiness,
                template_path=template_path,
                task_register_path=task_register_path,
                readiness_path=readiness_path,
            )

            write_json(packet_out, packet)
            write_json(validation_out, validation)
            if validation["status"] != "pass":
                for failure in validation["failures"]:
                    print(f"ERROR: {failure}", file=sys.stderr)
                return 1
            print(
                "NHATS Colectica capture packet draft ok: "
                f"task={packet['taskId']} "
                f"verdict={validation['currentDecision']['validatorVerdict']} model_g4=blocked"
            )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
