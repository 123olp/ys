#!/usr/bin/env python3
"""Build a fail-closed NHATS route-value crosswalk entry review handoff.

This ignored local report turns a route-value entry validator result into a
review-routing state. It never closes an assembly unit, updates tracked
registers, opens a route classifier, extracts data, publishes output,
calibrates a model or supports individual prediction.
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

from validate_nhats_route_value_crosswalk_entry_validator import (
    DEFAULT_CAPTURE_REVIEW,
    DEFAULT_CAPTURE_TASKS,
    DEFAULT_PROTOCOL,
    DEFAULT_ROUTE_READINESS,
    REQUIRED_BLOCKED_DECISION,
    VERDICT_CANNOT_EVALUATE,
    VERDICT_REJECTED,
    VERDICT_REVIEWABLE,
    evaluate_entry,
    load_json,
    repo_rel,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_ENTRY = (
    REPO_ROOT
    / "build"
    / "reports"
    / "nhats-route-value-crosswalk-entry-draft"
    / "identity_join_key-draft.json"
)
DEFAULT_OUT_DIR = (
    REPO_ROOT / "build" / "reports" / "nhats-route-value-crosswalk-entry-handoff"
)
HANDOFF_SCHEMA = "human-infra.life-path-nhats-route-value-crosswalk-entry-review-handoff.v1"
ALLOWED_HANDOFF_STATES = {
    "blocked-not-reviewable",
    "review-handoff-ready-but-assembly-still-open",
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
    text = str(value or "unknown-entry").strip().lower()
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    text = text.strip(".-_")
    return text or "unknown-entry"


def default_out(entry: dict[str, Any]) -> Path:
    entry_id = safe_id(entry.get("entryId"))
    return DEFAULT_OUT_DIR / f"{entry_id}-handoff.json"


def review_slots_for_state(handoff_state: str) -> list[dict[str, Any]]:
    if handoff_state == "review-handoff-ready-but-assembly-still-open":
        status = "pending-human-review"
        reason = (
            "Entry is validator-reviewable, but assembly closure requires human review, "
            "independent second review and a later governed register update."
        )
    else:
        status = "blocked-not-reviewable"
        reason = "Entry is rejected or cannot-evaluate, so no human review handoff may proceed."

    return [
        {
            "slotId": "route-value-row-review",
            "requiredRole": "human-domain-reviewer",
            "status": status,
            "assemblyUnitClosureAllowed": False,
            "reason": reason,
        },
        {
            "slotId": "missing-code-row-review",
            "requiredRole": "human-domain-reviewer",
            "status": status,
            "assemblyUnitClosureAllowed": False,
            "reason": reason,
        },
        {
            "slotId": "independent-second-review",
            "requiredRole": "independent-human-reviewer",
            "status": status,
            "assemblyUnitClosureAllowed": False,
            "reason": reason,
        },
        {
            "slotId": "governed-assembly-register-update",
            "requiredRole": "maintainer-governance-review",
            "status": "blocked",
            "assemblyUnitClosureAllowed": False,
            "reason": (
                "This builder is read-only with respect to tracked assembly and route "
                "classifier registers."
            ),
        },
    ]


def build_handoff(
    *,
    entry: dict[str, Any],
    entry_path: Path,
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
    verdict = entry_result.get("verdict")
    if verdict == VERDICT_REVIEWABLE:
        handoff_state = "review-handoff-ready-but-assembly-still-open"
        next_actions = [
            "Route the redacted entry to the human-domain-reviewer outside the repository.",
            "Route the same entry to an independent-human-reviewer outside the repository.",
            "Only after both reviews complete, prepare a separate governed assembly update.",
        ]
    elif verdict in {VERDICT_REJECTED, VERDICT_CANNOT_EVALUATE}:
        handoff_state = "blocked-not-reviewable"
        next_actions = [
            "Repair the external redacted entry according to rejectReasons and cannotEvaluateReasons.",
            "Re-run the entry validator before any review handoff.",
            "Do not modify tracked assembly, route classifier or model admission registers from this output.",
        ]
    else:
        handoff_state = "blocked-not-reviewable"
        next_actions = ["Unexpected validator verdict; repair validator or entry before handoff."]

    failures: list[str] = []
    if handoff_state not in ALLOWED_HANDOFF_STATES:
        failures.append("invalid handoff state")
    blocked_ok = all(
        entry_result.get(field) is expected
        for field, expected in REQUIRED_BLOCKED_DECISION.items()
    )
    if not blocked_ok:
        failures.append("entry result must keep all blocked decision flags false")

    return {
        "schemaVersion": HANDOFF_SCHEMA,
        "handoffId": f"nhats-route-value-crosswalk-entry-handoff-{safe_id(entry.get('entryId'))}",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "entryPath": repo_rel(entry_path),
            "entrySha256": sha256_file(entry_path),
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
            "handoffGenerated": True,
            "validatorVerdict": verdict,
            "handoffState": handoff_state,
            "reviewHandoffAllowed": verdict == VERDICT_REVIEWABLE,
            "modelG4": "blocked",
            **REQUIRED_BLOCKED_DECISION,
            "reason": (
                "This handoff only routes entry review state. It cannot close an assembly "
                "unit, update tracked registers, open a route classifier, extract NHATS "
                "rows, publish output, calibrate a model or support individual prediction."
            ),
        },
        "entryResult": entry_result,
        "reviewSlots": review_slots_for_state(handoff_state),
        "blockers": {
            "rejectReasons": entry_result.get("rejectReasons", []),
            "cannotEvaluateReasons": entry_result.get("cannotEvaluateReasons", []),
        },
        "nextActions": next_actions,
        "hardBoundaries": [
            "Generated handoffs are ignored local artifacts under build/reports/.",
            "A handoff-ready entry remains model_g4=blocked until tracked governance registers are separately reviewed and updated.",
            "This builder is not allowed to write tracked assembly registers, route classifier registers or public Web model data.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", type=Path, default=DEFAULT_ENTRY)
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--capture-review", type=Path, default=DEFAULT_CAPTURE_REVIEW)
    parser.add_argument("--capture-tasks", type=Path, default=DEFAULT_CAPTURE_TASKS)
    parser.add_argument("--route-readiness", type=Path, default=DEFAULT_ROUTE_READINESS)
    parser.add_argument("--out", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        entry_path = args.entry.resolve()
        protocol_path = args.protocol.resolve()
        capture_review_path = args.capture_review.resolve()
        capture_tasks_path = args.capture_tasks.resolve()
        route_readiness_path = args.route_readiness.resolve()

        entry = load_json(entry_path, "route-value crosswalk entry")
        protocol = load_json(protocol_path, "route-value crosswalk assembly protocol")
        capture_review = load_json(capture_review_path, "capture packet review execution")
        capture_tasks = load_json(capture_tasks_path, "capture task register")
        route_readiness = load_json(route_readiness_path, "route classifier readiness")

        handoff = build_handoff(
            entry=entry,
            entry_path=entry_path,
            protocol=protocol,
            capture_review=capture_review,
            capture_tasks=capture_tasks,
            route_readiness=route_readiness,
            protocol_path=protocol_path,
            capture_review_path=capture_review_path,
            capture_tasks_path=capture_tasks_path,
            route_readiness_path=route_readiness_path,
        )
        out = args.out.resolve() if args.out else default_out(entry).resolve()
        write_json(out, handoff)
        if handoff["status"] != "pass":
            for failure in handoff["failures"]:
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        decision = handoff["currentDecision"]
        print(
            "NHATS route-value crosswalk entry review handoff ok: "
            f"field={entry.get('requiredRouteFieldId')} "
            f"verdict={decision['validatorVerdict']} "
            f"handoff={decision['handoffState']} model_g4=blocked"
        )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
