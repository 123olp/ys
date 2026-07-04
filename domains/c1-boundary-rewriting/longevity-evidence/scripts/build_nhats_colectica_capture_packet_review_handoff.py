#!/usr/bin/env python3
"""Build a fail-closed NHATS Colectica capture packet review handoff.

This handoff is an ignored local report for maintainers. It turns a packet
validator result into a review-routing state, but never closes a capture slot,
updates tracked review registers, opens route classification, extracts data,
publishes output, calibrates a model or supports individual prediction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_nhats_colectica_capture_packet_validator import (
    DEFAULT_ROUTE_CLASSIFIER_READINESS,
    DEFAULT_TASK_REGISTER,
    DEFAULT_TEMPLATE,
    REQUIRED_BLOCKED_DECISION,
    VERDICT_CANNOT_EVALUATE,
    VERDICT_REJECTED,
    VERDICT_REVIEWABLE,
    evaluate_packet,
    load_json,
    repo_rel,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_PACKET = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhats-colectica-capture-packet-draft"
    / "identity_join_key-spid-draft.json"
)
DEFAULT_OUT_DIR = (
    REPO_ROOT / "build" / "reports" / "nhats-colectica-capture-packet-handoff"
)
HANDOFF_SCHEMA = "human-infra.life-path-nhats-colectica-capture-packet-review-handoff.v1"
BATCH_HANDOFF_SCHEMA = "human-infra.life-path-nhats-colectica-capture-packet-review-handoff-batch.v1"
ALLOWED_HANDOFF_STATES = {
    "blocked-not-reviewable",
    "review-handoff-ready-but-slot-still-open",
}


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_id(value: Any) -> str:
    text = str(value or "unknown-packet").strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = text.strip(".-_")
    return text or "unknown-packet"


def default_out(packet: dict[str, Any]) -> Path:
    packet_id = safe_id(packet.get("packetId"))
    return DEFAULT_OUT_DIR / f"{packet_id}-handoff.json"


def review_slots_for_state(handoff_state: str) -> list[dict[str, Any]]:
    if handoff_state == "review-handoff-ready-but-slot-still-open":
        status = "pending-human-review"
        reason = (
            "Packet is validator-reviewable, but capture slot closure requires "
            "human review, independent second review and a later governed register update."
        )
    else:
        status = "blocked-not-reviewable"
        reason = "Packet is rejected or cannot-evaluate, so no human review handoff may proceed."

    return [
        {
            "slotId": "packet-shape-review",
            "requiredRole": "human-domain-reviewer",
            "status": status,
            "slotClosureAllowed": False,
            "reason": reason,
        },
        {
            "slotId": "independent-second-review",
            "requiredRole": "independent-human-reviewer",
            "status": status,
            "slotClosureAllowed": False,
            "reason": reason,
        },
        {
            "slotId": "governed-register-update",
            "requiredRole": "maintainer-governance-review",
            "status": "blocked",
            "slotClosureAllowed": False,
            "reason": (
                "This builder is intentionally read-only with respect to tracked review "
                "execution registers."
            ),
        },
    ]


def build_handoff(
    *,
    packet: dict[str, Any],
    packet_path: Path,
    template: dict[str, Any],
    task_register: dict[str, Any],
    readiness: dict[str, Any],
    template_path: Path,
    task_register_path: Path,
    readiness_path: Path,
) -> dict[str, Any]:
    packet_result = evaluate_packet(packet, template, task_register, readiness)
    verdict = packet_result.get("verdict")
    if verdict == VERDICT_REVIEWABLE:
        handoff_state = "review-handoff-ready-but-slot-still-open"
        next_actions = [
            "Route the redacted packet to the human-domain-reviewer outside the repository.",
            "Route the same packet to an independent-human-reviewer outside the repository.",
            "Only after both reviews complete, prepare a separate governed register update.",
        ]
    elif verdict in {VERDICT_REJECTED, VERDICT_CANNOT_EVALUATE}:
        handoff_state = "blocked-not-reviewable"
        next_actions = [
            "Repair the external redacted packet according to rejectReasons and cannotEvaluateReasons.",
            "Re-run the single-packet validator before any review handoff.",
            "Do not modify tracked review execution registers from this output.",
        ]
    else:
        handoff_state = "blocked-not-reviewable"
        next_actions = ["Unexpected validator verdict; repair validator or packet before handoff."]

    failures: list[str] = []
    if handoff_state not in ALLOWED_HANDOFF_STATES:
        failures.append("invalid handoff state")
    blocked_ok = all(
        packet_result.get(field) is expected for field, expected in REQUIRED_BLOCKED_DECISION.items()
    )
    if not blocked_ok:
        failures.append("packet result must keep all blocked decision flags false")

    return {
        "schemaVersion": HANDOFF_SCHEMA,
        "handoffId": f"nhats-colectica-capture-packet-handoff-{safe_id(packet.get('packetId'))}",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "packetPath": repo_rel(packet_path),
            "packetSha256": sha256_file(packet_path),
            "authenticatedCaptureTemplatePath": repo_rel(template_path),
            "authenticatedCaptureTemplateSha256": sha256_file(template_path),
            "captureTaskRegisterPath": repo_rel(task_register_path),
            "captureTaskRegisterSha256": sha256_file(task_register_path),
            "routeClassifierReadinessPath": repo_rel(readiness_path),
            "routeClassifierReadinessSha256": sha256_file(readiness_path),
            "validatorPath": "domains/c1-boundary-rewriting/longevity-evidence/scripts/validate_nhats_colectica_capture_packet_validator.py",
        },
        "currentDecision": {
            "handoffGenerated": True,
            "validatorVerdict": verdict,
            "handoffState": handoff_state,
            "reviewHandoffAllowed": verdict == VERDICT_REVIEWABLE,
            "modelG4": "blocked",
            **REQUIRED_BLOCKED_DECISION,
            "reason": (
                "This handoff only routes packet review state. It cannot attach controlled "
                "Colectica evidence, close a capture slot, promote a route classifier, "
                "extract NHATS rows, publish output, calibrate a model or support individual "
                "prediction."
            ),
        },
        "packetResult": packet_result,
        "reviewSlots": review_slots_for_state(handoff_state),
        "blockers": {
            "rejectReasons": packet_result.get("rejectReasons", []),
            "cannotEvaluateReasons": packet_result.get("cannotEvaluateReasons", []),
        },
        "nextActions": next_actions,
        "hardBoundaries": [
            "Generated handoffs are ignored local artifacts under build/reports/.",
            "A handoff-ready packet remains model_g4=blocked until tracked governance registers are separately reviewed and updated.",
            "This builder is not allowed to write tracked review execution registers or public Web model data.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packet", type=Path, default=DEFAULT_PACKET)
    parser.add_argument(
        "--packet-dir",
        type=Path,
        default=DEFAULT_PACKET.parent,
        help="Directory containing *-draft.json packets when --all-packets is used.",
    )
    parser.add_argument(
        "--all-packets",
        action="store_true",
        help="Generate handoffs for every draft packet in --packet-dir.",
    )
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--task-register", type=Path, default=DEFAULT_TASK_REGISTER)
    parser.add_argument("--route-classifier-readiness", type=Path, default=DEFAULT_ROUTE_CLASSIFIER_READINESS)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    parser.add_argument(
        "--batch-out",
        type=Path,
        default=DEFAULT_OUT_DIR / "all-handoffs-validation.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        packet_path = args.packet.resolve()
        template_path = args.template.resolve()
        task_register_path = args.task_register.resolve()
        readiness_path = args.route_classifier_readiness.resolve()

        template = load_json(template_path, "authenticated capture template")
        task_register = load_json(task_register_path, "capture task register")
        readiness = load_json(readiness_path, "route classifier readiness")

        if args.all_packets:
            packet_dir = args.packet_dir.resolve()
            out_dir = args.out_dir.resolve()
            batch_out = args.batch_out.resolve()
            packet_paths = sorted(packet_dir.glob("*-draft.json"))
            if not packet_paths:
                raise ValueError(f"no draft packets found in {packet_dir}")
            failures: list[str] = []
            results: list[dict[str, Any]] = []
            for draft_path in packet_paths:
                packet = load_json(draft_path, "capture packet")
                handoff = build_handoff(
                    packet=packet,
                    packet_path=draft_path,
                    template=template,
                    task_register=task_register,
                    readiness=readiness,
                    template_path=template_path,
                    task_register_path=task_register_path,
                    readiness_path=readiness_path,
                )
                handoff_out = (out_dir / default_out(packet).name).resolve()
                write_json(handoff_out, handoff)
                if handoff["status"] != "pass":
                    failures.extend(f"{draft_path.name}: {failure}" for failure in handoff["failures"])
                decision = handoff["currentDecision"]
                results.append(
                    {
                        "taskId": packet.get("taskId"),
                        "packetPath": repo_rel(draft_path),
                        "handoffPath": repo_rel(handoff_out),
                        "validatorVerdict": decision["validatorVerdict"],
                        "handoffState": decision["handoffState"],
                        "reviewHandoffAllowed": decision["reviewHandoffAllowed"],
                        "modelG4": decision["modelG4"],
                        "status": handoff["status"],
                    }
                )
            batch = {
                "schemaVersion": BATCH_HANDOFF_SCHEMA,
                "handoffBatchId": "nhats-colectica-capture-packet-handoff-all-drafts",
                "generatedAt": datetime.now(timezone.utc).isoformat(),
                "status": "pass" if not failures else "fail",
                "sourceRefs": {
                    "packetDir": repo_rel(packet_dir),
                    "authenticatedCaptureTemplatePath": repo_rel(template_path),
                    "authenticatedCaptureTemplateSha256": sha256_file(template_path),
                    "captureTaskRegisterPath": repo_rel(task_register_path),
                    "captureTaskRegisterSha256": sha256_file(task_register_path),
                    "routeClassifierReadinessPath": repo_rel(readiness_path),
                    "routeClassifierReadinessSha256": sha256_file(readiness_path),
                },
                "summary": {
                    "draftPacketCount": len(packet_paths),
                    "handoffCount": len(results),
                    "passCount": sum(1 for item in results if item["status"] == "pass"),
                    "handoffReadyCount": sum(1 for item in results if item["reviewHandoffAllowed"]),
                    "trackedReviewSlotClosures": 0,
                    "modelG4Decision": "blocked",
                },
                "results": results,
                "hardBoundaries": [
                    "Generated handoff batch files are ignored local artifacts under build/reports/.",
                    "Batch handoffs do not write tracked review execution registers or close capture slots.",
                    "Handoff-ready packets still require external human review, second review and governed register updates.",
                ],
                "failures": failures,
            }
            write_json(batch_out, batch)
            if failures:
                for failure in failures:
                    print(f"ERROR: {failure}", file=sys.stderr)
                return 1
            print(
                "NHATS Colectica capture packet review handoff batch ok: "
                f"packets={len(packet_paths)} handoff_ready={batch['summary']['handoffReadyCount']} "
                "model_g4=blocked"
            )
        else:
            packet = load_json(packet_path, "capture packet")
            handoff = build_handoff(
                packet=packet,
                packet_path=packet_path,
                template=template,
                task_register=task_register,
                readiness=readiness,
                template_path=template_path,
                task_register_path=task_register_path,
                readiness_path=readiness_path,
            )
            out = args.out.resolve() if args.out else default_out(packet).resolve()
            write_json(out, handoff)
            if handoff["status"] != "pass":
                for failure in handoff["failures"]:
                    print(f"ERROR: {failure}", file=sys.stderr)
                return 1
            decision = handoff["currentDecision"]
            print(
                "NHATS Colectica capture packet review handoff ok: "
                f"packet={packet.get('taskId')} "
                f"verdict={decision['validatorVerdict']} "
                f"handoff={decision['handoffState']} model_g4=blocked"
            )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
