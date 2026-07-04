#!/usr/bin/env python3
"""Validate future L4 evidence packet shapes against the intake contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-l4-evidence-intake-register.json"
CASES_PATH = ROOT / "docs/reference/human-infra-l4-evidence-packet-validator-test-cases.json"
DEFAULT_JSON_OUT = ROOT / "web/src/data/life-path-l4-evidence-packet-validator-validation.json"

CASES_SCHEMA = "human-infra.l4-evidence-packet-validator-test-cases.v1"
VALIDATION_SCHEMA = "human-infra.l4-evidence-packet-validator-validation.v1"
PACKET_SCHEMA = "human-infra.l4-evidence-packet.v1"
HASH_RE = re.compile(r"^[a-fA-F0-9]{64}$")

VERDICT_REJECTED = "rejected"
VERDICT_CANNOT_EVALUATE = "cannot-evaluate"
VERDICT_REVIEWABLE = "reviewable-but-still-blocked"

BLOCKED_DECISION = {
    "slotClosureAllowed": False,
    "l4AggregateCalibratedAdmissionAllowed": False,
    "publicWeightedDomainOutputAllowed": False,
    "calibratedPredictionAvailable": False,
    "individualUseAllowed": False,
}


def load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.exists():
        raise ValueError(f"missing {label}: {path.relative_to(ROOT)}")
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


def slot_index(register: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    index: dict[tuple[str, str], dict[str, Any]] = {}
    for group in register.get("evidenceSlotGroups", []):
        if not isinstance(group, dict):
            continue
        work_order_id = str(group.get("workOrderId", ""))
        candidate = str(group.get("candidatePath", ""))
        for slot in group.get("slots", []):
            if not isinstance(slot, dict):
                continue
            key = (work_order_id, str(slot.get("slotId", "")))
            index[key] = {
                "workOrderId": work_order_id,
                "candidatePath": candidate,
                "slotId": str(slot.get("slotId", "")),
                "evidenceClass": str(slot.get("evidenceClass", "")),
                "repositoryPolicy": str(slot.get("repositoryPolicy", "")),
                "status": slot.get("status"),
                "blocksL4": slot.get("blocksL4"),
            }
    return index


def string_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {item for item in value if isinstance(item, str)}


def contains_forbidden_case_insensitive(value: str, phrases: set[str]) -> bool:
    lowered = value.lower()
    return any(phrase.lower() in lowered for phrase in phrases)


def packet_role_is_ai_only(role: Any) -> bool:
    return not isinstance(role, str) or role.strip().lower() in {"", "ai-only", "ai only", "automated-only"}


def evaluate_packet(packet: Any, register: dict[str, Any]) -> dict[str, Any]:
    contract = register.get("evidencePacketContract", {})
    if not isinstance(contract, dict):
        raise ValueError("register.evidencePacketContract must be an object")

    required_fields = string_set(contract.get("requiredPacketFields"))
    forbidden_fields = string_set(contract.get("forbiddenPacketFields"))
    allowed_statuses = string_set(contract.get("allowedPacketStatuses"))
    accepted_classes = string_set(register.get("acceptedEvidenceClasses"))
    rejected_classes = string_set(register.get("rejectedEvidenceClasses"))
    required_false_booleans = {
        key for key, value in (contract.get("requiredBooleanDefaults") or {}).items() if value is False
    }
    prohibited_uses = string_set(contract.get("prohibitedPacketUses"))

    reject_reasons: list[str] = []
    cannot_evaluate_reasons: list[str] = []
    matched_slot: dict[str, Any] | None = None

    if not isinstance(packet, dict):
        return {
            "verdict": VERDICT_REJECTED,
            "slotClosureAllowed": False,
            "l4AggregateCalibratedAdmissionAllowed": False,
            "rejectReasons": ["packet must be a JSON object"],
            "cannotEvaluateReasons": [],
            "matchedSlot": None,
        }

    packet_keys = set(packet)
    missing = sorted(required_fields - packet_keys)
    if missing:
        cannot_evaluate_reasons.append(f"missing required fields: {', '.join(missing)}")

    present_forbidden = sorted(forbidden_fields & packet_keys)
    if present_forbidden:
        reject_reasons.append(f"forbidden fields present: {', '.join(present_forbidden)}")

    for key in required_false_booleans:
        if packet.get(key) is not False:
            reject_reasons.append(f"{key} must be false")

    if packet.get("packetSchema") not in {None, PACKET_SCHEMA}:
        reject_reasons.append("packetSchema mismatch")

    if packet.get("evidenceClass") in rejected_classes:
        reject_reasons.append("evidenceClass is explicitly rejected")
    elif packet.get("evidenceClass") not in accepted_classes:
        reject_reasons.append("evidenceClass is not accepted by the intake register")

    evidence_status = packet.get("evidenceStatus")
    if evidence_status not in allowed_statuses:
        reject_reasons.append("evidenceStatus is not allowed by the packet contract")
    elif evidence_status == "rejected":
        reject_reasons.append("packet evidenceStatus is rejected")

    if packet.get("artifactHashAlgorithm") != "sha256":
        reject_reasons.append("artifactHashAlgorithm must be sha256")
    artifact_hash = packet.get("artifactHash")
    if not isinstance(artifact_hash, str) or not HASH_RE.fullmatch(artifact_hash):
        reject_reasons.append("artifactHash must be a 64-character sha256 hex digest")

    if packet.get("allowedUse") != "bounded L4 evidence review only":
        reject_reasons.append("allowedUse must remain bounded L4 evidence review only")
    if packet.get("downstreamDecision") != "l4-still-blocked":
        reject_reasons.append("downstreamDecision must remain l4-still-blocked")

    packet_prohibited = string_set(packet.get("prohibitedUse"))
    if packet_prohibited != prohibited_uses:
        reject_reasons.append("prohibitedUse must exactly match the intake register prohibited uses")

    if packet_role_is_ai_only(packet.get("firstReviewerRole")):
        if evidence_status in {"human-reviewed-redacted", "second-reviewed-redacted"}:
            reject_reasons.append("firstReviewerRole must be a non-AI human reviewer")
        else:
            cannot_evaluate_reasons.append("first human reviewer is not attached")
    if packet.get("aiOnlySignoff") is True:
        reject_reasons.append("AI-only signoff is forbidden")
    if packet.get("firstReviewerRole") == packet.get("producerRole") and packet.get("firstReviewerRole"):
        reject_reasons.append("producer cannot approve its own packet")

    if evidence_status == "second-reviewed-redacted":
        if packet_role_is_ai_only(packet.get("secondReviewerRole")):
            reject_reasons.append("secondReviewerRole must be a non-AI reviewer")
        if packet.get("secondReviewerRole") == packet.get("firstReviewerRole"):
            reject_reasons.append("second reviewer must be independent from first reviewer")
    elif evidence_status == "draft-redacted":
        cannot_evaluate_reasons.append("draft-redacted packet has no completed review")
    elif evidence_status == "human-reviewed-redacted":
        if packet_role_is_ai_only(packet.get("secondReviewerRole")):
            cannot_evaluate_reasons.append("second reviewer is not attached")

    review_date = packet.get("reviewDate")
    if evidence_status in {"human-reviewed-redacted", "second-reviewed-redacted"} and (
        not isinstance(review_date, str) or review_date == "not-reviewed"
    ):
        cannot_evaluate_reasons.append("reviewDate must be present for reviewed packet status")

    description = packet.get("artifactDescriptionRedacted")
    if not isinstance(description, str) or not description.strip():
        cannot_evaluate_reasons.append("artifactDescriptionRedacted must be non-empty")
    elif contains_forbidden_case_insensitive(
        description,
        {"real weighted rate", "real standard error", "real confidence interval", "individual death date"},
    ):
        reject_reasons.append("artifactDescriptionRedacted appears to disclose forbidden real output semantics")

    index = slot_index(register)
    key = (str(packet.get("workOrderId", "")), str(packet.get("slotId", "")))
    matched_slot = index.get(key)
    if matched_slot is None:
        reject_reasons.append("packet does not match exactly one known pending slot")
    else:
        for field in ("candidatePath", "evidenceClass", "repositoryPolicy"):
            if packet.get(field) != matched_slot[field]:
                reject_reasons.append(f"{field} does not match the registered slot")
        if matched_slot["status"] != "pending":
            reject_reasons.append("registered slot is not pending")
        if matched_slot["blocksL4"] is not True:
            reject_reasons.append("registered slot must keep blocksL4=true")

    if reject_reasons:
        verdict = VERDICT_REJECTED
    elif cannot_evaluate_reasons:
        verdict = VERDICT_CANNOT_EVALUATE
    else:
        verdict = VERDICT_REVIEWABLE

    return {
        "packetId": packet.get("packetId"),
        "workOrderId": packet.get("workOrderId"),
        "slotId": packet.get("slotId"),
        "verdict": verdict,
        "slotClosureAllowed": False,
        "l4AggregateCalibratedAdmissionAllowed": False,
        "publicWeightedDomainOutputAllowed": False,
        "calibratedPredictionAvailable": False,
        "individualUseAllowed": False,
        "rejectReasons": reject_reasons,
        "cannotEvaluateReasons": cannot_evaluate_reasons,
        "matchedSlot": matched_slot,
    }


def validate_cases(cases: dict[str, Any], register: dict[str, Any]) -> dict[str, Any]:
    if cases.get("schemaVersion") != CASES_SCHEMA:
        raise ValueError("test case schemaVersion mismatch")
    raw_cases = cases.get("testCases")
    if not isinstance(raw_cases, list) or not raw_cases:
        raise ValueError("testCases must be a non-empty array")

    case_results: list[dict[str, Any]] = []
    failures: list[str] = []
    counts = {VERDICT_REVIEWABLE: 0, VERDICT_CANNOT_EVALUATE: 0, VERDICT_REJECTED: 0}

    for index, case in enumerate(raw_cases):
        if not isinstance(case, dict):
            failures.append(f"testCases[{index}] must be an object")
            continue
        case_id = case.get("caseId", f"case-{index}")
        expected = case.get("expectedVerdict")
        result = evaluate_packet(case.get("packet"), register)
        verdict = result["verdict"]
        counts[verdict] = counts.get(verdict, 0) + 1
        passed = verdict == expected and result["slotClosureAllowed"] is False and result["l4AggregateCalibratedAdmissionAllowed"] is False
        if not passed:
            failures.append(f"{case_id} expected {expected}, got {verdict}")
        case_results.append(
            {
                "caseId": case_id,
                "expectedVerdict": expected,
                "actualVerdict": verdict,
                "passed": passed,
                "slotClosureAllowed": result["slotClosureAllowed"],
                "l4AggregateCalibratedAdmissionAllowed": result["l4AggregateCalibratedAdmissionAllowed"],
                "rejectReasons": result["rejectReasons"],
                "cannotEvaluateReasons": result["cannotEvaluateReasons"],
            }
        )

    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "validationId": "life-path-l4-evidence-packet-validator-validation-2026-07-04",
        "status": "pass" if not failures else "fail",
        "sourceRefs": {
            "l4EvidenceIntakeRegister": str(REGISTER_PATH.relative_to(ROOT)),
            "l4EvidencePacketValidatorTestCases": str(CASES_PATH.relative_to(ROOT)),
            "validator": "tools/audit_human_infra_l4_evidence_packet_validator.py",
        },
        "currentDecision": {
            "validatorReady": not failures,
            "testCaseCount": len(raw_cases),
            "reviewableButStillBlockedCount": counts.get(VERDICT_REVIEWABLE, 0),
            "cannotEvaluateCount": counts.get(VERDICT_CANNOT_EVALUATE, 0),
            "rejectedCount": counts.get(VERDICT_REJECTED, 0),
            "realEvidencePacketAttached": False,
            "slotClosureAllowed": False,
            "l4AggregateCalibratedAdmissionAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibratedPredictionAvailable": False,
            "individualUseAllowed": False,
            "reason": "Validator test cases exercise synthetic packet verdict semantics only. They do not attach real evidence, close slots, open L4 admission, publish weighted output, calibrate a model or support individual use.",
        },
        "caseResults": case_results,
        "hardBoundaries": [
            "Validator pass does not mean evidence pass.",
            "A reviewable packet verdict does not close a slot.",
            "No output from this validator may open L4 aggregate calibrated admission.",
            "No output from this validator may be used for public weighted output, calibrated prediction, medical advice, intervention ranking, individual prediction or individual death-date output.",
        ],
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=REGISTER_PATH)
    parser.add_argument("--cases", type=Path, default=CASES_PATH)
    parser.add_argument("--packet", type=Path, help="Optional single packet JSON to evaluate instead of test cases.")
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        register = load_json(args.register, "L4 evidence intake register")
        if args.packet:
            packet = load_json(args.packet, "L4 evidence packet")
            validation = {
                "schemaVersion": VALIDATION_SCHEMA,
                "status": "single-packet-evaluated-l4-still-blocked",
                "currentDecision": BLOCKED_DECISION | {"validatorReady": True, "realEvidencePacketAttached": False},
                "packetResult": evaluate_packet(packet, register),
            }
        else:
            cases = load_json(args.cases, "L4 evidence packet validator test cases")
            validation = validate_cases(cases, register)
        write_json(args.json_out, validation)
        if validation["status"] == "fail":
            for failure in validation.get("failures", []):
                print(f"ERROR: {failure}", file=sys.stderr)
            return 1
        decision = validation["currentDecision"]
        print(
            "L4 evidence packet validator audit ok: "
            f"cases={decision.get('testCaseCount', 1)} "
            f"reviewable={decision.get('reviewableButStillBlockedCount', 0)} "
            f"cannot_evaluate={decision.get('cannotEvaluateCount', 0)} "
            f"rejected={decision.get('rejectedCount', 0)} l4=blocked"
        )
        return 0
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
