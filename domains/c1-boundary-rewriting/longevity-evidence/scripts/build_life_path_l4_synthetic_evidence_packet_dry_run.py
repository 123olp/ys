#!/usr/bin/env python3
"""Build and audit a synthetic L4 evidence packet dry-run.

The output rehearses the L4 evidence-packet intake workflow with redacted,
hash-only synthetic packet shapes. It must never be interpreted as real
evidence, human review, slot closure, L4 admission, public weighted output,
calibration, medical advice or an individual prediction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_REGISTER = (
    REPO_ROOT / "docs" / "reference" / "human-infra-l4-evidence-intake-register.json"
)
DEFAULT_PLAYBOOK = (
    REPO_ROOT / "docs" / "reference" / "human-infra-l4-evidence-packet-review-playbook.md"
)
DEFAULT_REPORT = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-synthetic-validation-calibration-report.json"
)
DEFAULT_JSON_OUT = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-l4-synthetic-evidence-packet-dry-run.json"
)
DEFAULT_MD_OUT = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-l4-synthetic-evidence-packet-dry-run.md"
)

DRY_RUN_ID = "life-path-l4-synthetic-evidence-packet-dry-run-2026-07-04"
GENERATED_AT = "2026-07-04T00:00:00+00:00"
SCHEMA = "human-infra.life-path-l4-synthetic-evidence-packet-dry-run.v1"
PACKET_SCHEMA = "human-infra.l4-evidence-packet.v1"
STATUS = "synthetic-evidence-packet-dry-run-l4-blocked"
HASH_ALGORITHM = "sha256"

PROHIBITED_PACKET_FIELDS = {
    "rawRows",
    "identifiers",
    "restrictedFilePath",
    "realWeightedRate",
    "realStandardError",
    "realConfidenceInterval",
    "individualPrediction",
    "individualDeathDate",
    "secretToken",
    "screenshotWithSensitiveValues",
}
REQUIRED_FALSE_PACKET_BOOLEANS = {
    "rawDataTracked",
    "restrictedDataTracked",
    "identifierTracked",
    "publicAiUpload",
    "aiOnlySignoff",
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


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def source_ref(path: Path) -> dict[str, str]:
    return {"path": rel(path), "sha256": sha256_file(path)}


def require_dict(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    return value


def require_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be an array")
    return value


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, nested in value.items():
            keys.add(str(key))
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def synthetic_packet_hash(work_order: dict[str, Any], slot: dict[str, Any]) -> str:
    descriptor = {
        "dryRunId": DRY_RUN_ID,
        "workOrderId": work_order["workOrderId"],
        "slotId": slot["slotId"],
        "candidatePath": work_order["candidatePath"],
        "evidenceClass": slot["evidenceClass"],
        "repositoryPolicy": slot["repositoryPolicy"],
        "syntheticOnly": True,
        "realEvidenceAttached": False,
        "downstreamDecision": "l4-still-blocked",
    }
    return sha256_text(canonical_json(descriptor))


def build_packet(work_order: dict[str, Any], slot: dict[str, Any], prohibited_use: list[str]) -> dict[str, Any]:
    work_order_id = str(work_order["workOrderId"])
    slot_id = str(slot["slotId"])
    return {
        "packetSchema": PACKET_SCHEMA,
        "packetId": f"SYN-L4PKT-{work_order_id}-{slot_id}",
        "workOrderId": work_order_id,
        "slotId": slot_id,
        "candidatePath": work_order["candidatePath"],
        "evidenceClass": slot["evidenceClass"],
        "evidenceStatus": "draft-redacted",
        "repositoryPolicy": slot["repositoryPolicy"],
        "artifactHash": synthetic_packet_hash(work_order, slot),
        "artifactHashAlgorithm": HASH_ALGORITHM,
        "artifactDescriptionRedacted": (
            "Synthetic hash-only packet shape. No raw rows, no restricted data, "
            "no identifiers, no real aggregate values and no human review are attached."
        ),
        "producerRole": "synthetic-script",
        "firstReviewerRole": "human-review-required-not-attached",
        "secondReviewerRole": "second-review-required-not-attached",
        "reviewDate": "not-reviewed",
        "sensitivityClass": "synthetic-redacted-hash-only-no-real-data",
        "rawDataTracked": False,
        "restrictedDataTracked": False,
        "identifierTracked": False,
        "publicAiUpload": False,
        "aiOnlySignoff": False,
        "allowedUse": "bounded L4 evidence review only",
        "prohibitedUse": prohibited_use,
        "downstreamDecision": "l4-still-blocked",
        "syntheticOnly": True,
        "realEvidenceAttached": False,
        "slotCloseAllowed": False,
        "packetVerdict": "cannot-evaluate-synthetic-only",
    }


def build_packets(register: dict[str, Any]) -> list[dict[str, Any]]:
    packet_contract = require_dict(register.get("evidencePacketContract"), "evidencePacketContract")
    prohibited_use = [str(item) for item in require_list(packet_contract.get("prohibitedPacketUses"), "prohibitedPacketUses")]
    packets: list[dict[str, Any]] = []
    for raw_group in require_list(register.get("evidenceSlotGroups"), "evidenceSlotGroups"):
        group = require_dict(raw_group, "evidenceSlotGroups row")
        for raw_slot in require_list(group.get("slots"), f"{group.get('workOrderId')}.slots"):
            slot = require_dict(raw_slot, "slot row")
            packets.append(build_packet(group, slot, prohibited_use))
    return packets


def build_slot_outcomes(register: dict[str, Any], packets: list[dict[str, Any]]) -> list[dict[str, Any]]:
    packet_by_slot = {(packet["workOrderId"], packet["slotId"]): packet for packet in packets}
    outcomes: list[dict[str, Any]] = []
    for raw_group in require_list(register.get("evidenceSlotGroups"), "evidenceSlotGroups"):
        group = require_dict(raw_group, "evidenceSlotGroups row")
        work_order_id = str(group["workOrderId"])
        for raw_slot in require_list(group.get("slots"), f"{work_order_id}.slots"):
            slot = require_dict(raw_slot, "slot row")
            slot_id = str(slot["slotId"])
            packet = packet_by_slot[(work_order_id, slot_id)]
            outcomes.append(
                {
                    "workOrderId": work_order_id,
                    "slotId": slot_id,
                    "slotStatusInRegister": slot.get("status"),
                    "syntheticPacketId": packet["packetId"],
                    "syntheticPacketStatus": packet["evidenceStatus"],
                    "realEvidenceRefInRegister": slot.get("evidenceRef"),
                    "reviewerSignoffInRegister": slot.get("reviewerSignoff"),
                    "requiredHumanSignoff": slot.get("requiredHumanSignoff"),
                    "syntheticPacketGenerated": True,
                    "realEvidenceAttached": False,
                    "reviewerSignoffAttached": False,
                    "slotCloseAllowed": False,
                    "reason": "Synthetic draft packet exercises schema only; register slot remains pending and cannot close.",
                }
            )
    return outcomes


def build_dry_run(
    register: dict[str, Any],
    report: dict[str, Any],
    register_path: Path,
    playbook_path: Path,
    report_path: Path,
) -> dict[str, Any]:
    packets = build_packets(register)
    slot_outcomes = build_slot_outcomes(register, packets)
    register_summary = require_dict(register.get("slotStatusSummary"), "slotStatusSummary")
    return {
        "schemaVersion": SCHEMA,
        "dryRunId": DRY_RUN_ID,
        "status": STATUS,
        "generatedAt": GENERATED_AT,
        "owner": "tradecatlabs",
        "sourceRefs": {
            "l4EvidenceIntakeRegister": source_ref(register_path),
            "l4EvidencePacketReviewPlaybook": source_ref(playbook_path),
            "syntheticValidationCalibrationReport": source_ref(report_path),
        },
        "currentDecision": {
            "syntheticEvidencePacketDryRunGenerated": True,
            "syntheticPacketSchemaExercised": True,
            "syntheticPacketCount": len(packets),
            "realEvidencePacketCount": 0,
            "registerPacketCountRemainsZero": True,
            "closedSlotCountRemainsZero": True,
            "humanReviewEvidenceAttached": False,
            "secondReviewerEvidenceAttached": False,
            "slotClosureAllowed": False,
            "l4AggregateCalibratedAdmissionAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibratedPredictionAvailable": False,
            "individualUseAllowed": False,
            "reason": "This dry-run generates synthetic draft packets for every pending slot, using hash-only placeholders. It does not attach direct evidence, human review, second review, real validation, calibration diagnostics or any slot-closing decision.",
        },
        "dryRunBoundary": {
            "modelClass": "synthetic L4 evidence-packet intake rehearsal",
            "allowedUse": "machine-readable packet-shape rehearsal and boundary audit",
            "evidenceBoundary": "No real evidence packet, no raw data, no restricted data, no identifiers, no real aggregate values, no human signoff and no second-reviewer signoff are present.",
            "nonUses": [
                "direct L4 evidence",
                "slot closure",
                "model calibration",
                "public weighted output",
                "clinical prediction",
                "medical advice",
                "intervention ranking",
                "individual lifetime prediction",
                "individual death-date output",
            ],
        },
        "registerInvariantCheck": {
            "registerWorkOrderCount": register_summary.get("workOrderCount"),
            "registerTotalSlotCount": register_summary.get("totalSlotCount"),
            "registerPendingSlotCount": register_summary.get("pendingSlotCount"),
            "registerEvidenceAttachedCount": register_summary.get("evidenceAttachedCount"),
            "registerHumanSignoffCount": register_summary.get("humanSignoffCount"),
            "registerL4ReviewOpen": register_summary.get("l4ReviewOpen"),
            "registerPacketCount": require_dict(register.get("evidencePacketContract"), "evidencePacketContract").get("packetCount"),
            "registerClosedSlotCount": require_dict(register.get("evidencePacketContract"), "evidencePacketContract").get("closedSlotCount"),
        },
        "upstreamSyntheticReportCheck": {
            "reportId": report.get("reportId"),
            "reportStatus": report.get("status"),
            "realReportPacketCount": require_dict(report.get("contractCoverage"), "report.contractCoverage").get("realReportPacketCount"),
            "l4AdmissionAllowed": require_dict(report.get("currentDecision"), "report.currentDecision").get("l4AggregateCalibratedAdmissionAllowed"),
        },
        "packets": packets,
        "slotOutcomes": slot_outcomes,
        "auditSummary": {
            "allSlotsExercised": len(slot_outcomes) == register_summary.get("totalSlotCount"),
            "allPacketsSyntheticOnly": all(packet.get("syntheticOnly") is True for packet in packets),
            "allPacketHashesSha256": all(len(str(packet.get("artifactHash"))) == 64 for packet in packets),
            "allFalseSafetyBooleans": all(
                packet.get(key) is False for packet in packets for key in REQUIRED_FALSE_PACKET_BOOLEANS
            ),
            "allSlotsRemainPending": all(outcome.get("slotStatusInRegister") == "pending" for outcome in slot_outcomes),
            "allSlotClosureBlocked": all(outcome.get("slotCloseAllowed") is False for outcome in slot_outcomes),
            "l4StillBlocked": True,
        },
    }


def validate_packet(packet: dict[str, Any], required_fields: set[str], forbidden_fields: set[str]) -> None:
    if packet.get("packetSchema") != PACKET_SCHEMA:
        raise ValueError(f"{packet.get('packetId')} packetSchema mismatch")
    missing = sorted(required_fields - set(packet))
    if missing:
        raise ValueError(f"{packet.get('packetId')} missing required fields: {missing}")
    present_forbidden = sorted(forbidden_fields & set(packet))
    if present_forbidden:
        raise ValueError(f"{packet.get('packetId')} contains forbidden fields: {present_forbidden}")
    if packet.get("artifactHashAlgorithm") != HASH_ALGORITHM:
        raise ValueError(f"{packet.get('packetId')} must use sha256")
    artifact_hash = packet.get("artifactHash")
    if not isinstance(artifact_hash, str) or len(artifact_hash) != 64:
        raise ValueError(f"{packet.get('packetId')} must contain a sha256 artifactHash")
    for key in REQUIRED_FALSE_PACKET_BOOLEANS:
        if packet.get(key) is not False:
            raise ValueError(f"{packet.get('packetId')}.{key} must be false")
    if packet.get("allowedUse") != "bounded L4 evidence review only":
        raise ValueError(f"{packet.get('packetId')} allowedUse must stay bounded")
    if packet.get("downstreamDecision") != "l4-still-blocked":
        raise ValueError(f"{packet.get('packetId')} downstreamDecision must keep L4 blocked")
    if packet.get("slotCloseAllowed") is not False:
        raise ValueError(f"{packet.get('packetId')} must not close a slot")
    if packet.get("realEvidenceAttached") is not False:
        raise ValueError(f"{packet.get('packetId')} must not attach real evidence")


def validate_dry_run(dry_run: dict[str, Any], register: dict[str, Any], report: dict[str, Any]) -> None:
    if dry_run.get("schemaVersion") != SCHEMA:
        raise ValueError("unexpected dry-run schemaVersion")
    if dry_run.get("status") != STATUS:
        raise ValueError("dry-run status must keep L4 blocked")

    packet_contract = require_dict(register.get("evidencePacketContract"), "evidencePacketContract")
    required_fields = set(str(item) for item in require_list(packet_contract.get("requiredPacketFields"), "requiredPacketFields"))
    forbidden_fields = set(str(item) for item in require_list(packet_contract.get("forbiddenPacketFields"), "forbiddenPacketFields"))
    if not PROHIBITED_PACKET_FIELDS <= forbidden_fields:
        raise ValueError("register forbidden packet fields must include the hard dry-run boundary")

    packets = require_list(dry_run.get("packets"), "packets")
    expected_count = require_dict(register.get("slotStatusSummary"), "slotStatusSummary").get("totalSlotCount")
    if len(packets) != expected_count:
        raise ValueError("synthetic packet count must equal register total slot count")
    for raw_packet in packets:
        validate_packet(require_dict(raw_packet, "packet"), required_fields, forbidden_fields)

    decision = require_dict(dry_run.get("currentDecision"), "currentDecision")
    for key in (
        "humanReviewEvidenceAttached",
        "secondReviewerEvidenceAttached",
        "slotClosureAllowed",
        "l4AggregateCalibratedAdmissionAllowed",
        "publicWeightedDomainOutputAllowed",
        "calibratedPredictionAvailable",
        "individualUseAllowed",
    ):
        if decision.get(key) is not False:
            raise ValueError(f"currentDecision.{key} must be false")
    if decision.get("realEvidencePacketCount") != 0:
        raise ValueError("realEvidencePacketCount must remain 0")

    invariants = require_dict(dry_run.get("registerInvariantCheck"), "registerInvariantCheck")
    if invariants.get("registerPacketCount") != 0 or invariants.get("registerClosedSlotCount") != 0:
        raise ValueError("register packet and closed-slot counts must remain zero")
    if invariants.get("registerL4ReviewOpen") is not False:
        raise ValueError("register L4 review must remain closed")

    upstream = require_dict(dry_run.get("upstreamSyntheticReportCheck"), "upstreamSyntheticReportCheck")
    if upstream.get("reportStatus") != report.get("status"):
        raise ValueError("upstream report status mismatch")
    if upstream.get("realReportPacketCount") != 0:
        raise ValueError("upstream real report packet count must remain 0")
    if upstream.get("l4AdmissionAllowed") is not False:
        raise ValueError("upstream L4 admission must remain blocked")

    prohibited_keys = PROHIBITED_PACKET_FIELDS & collect_keys(dry_run)
    if prohibited_keys:
        raise ValueError(f"prohibited packet field keys present in dry-run: {sorted(prohibited_keys)}")

    audit = require_dict(dry_run.get("auditSummary"), "auditSummary")
    for key, expected in {
        "allSlotsExercised": True,
        "allPacketsSyntheticOnly": True,
        "allPacketHashesSha256": True,
        "allFalseSafetyBooleans": True,
        "allSlotsRemainPending": True,
        "allSlotClosureBlocked": True,
        "l4StillBlocked": True,
    }.items():
        if audit.get(key) is not expected:
            raise ValueError(f"auditSummary.{key} must be {expected}")


def write_markdown(dry_run: dict[str, Any], out_path: Path) -> None:
    decision = require_dict(dry_run.get("currentDecision"), "currentDecision")
    invariants = require_dict(dry_run.get("registerInvariantCheck"), "registerInvariantCheck")
    lines = [
        "# Life-Path L4 Synthetic Evidence Packet Dry-Run",
        "",
        f"- Status: `{dry_run['status']}`",
        f"- Synthetic packets: {decision['syntheticPacketCount']}",
        f"- Real evidence packets: {decision['realEvidencePacketCount']}",
        f"- Register packet count: {invariants['registerPacketCount']}",
        f"- Register closed slot count: {invariants['registerClosedSlotCount']}",
        f"- L4 admission allowed: `{decision['l4AggregateCalibratedAdmissionAllowed']}`",
        f"- Individual use allowed: `{decision['individualUseAllowed']}`",
        "",
        "This artifact only rehearses L4 evidence-packet shape and abort boundaries. It contains no real evidence, no human review and no slot closure.",
        "",
        "## Work Order Coverage",
        "",
        "| Work order | Synthetic slots | Slot close allowed |",
        "| --- | ---: | --- |",
    ]
    counts: dict[str, int] = {}
    for outcome in require_list(dry_run.get("slotOutcomes"), "slotOutcomes"):
        row = require_dict(outcome, "slot outcome")
        counts[str(row["workOrderId"])] = counts.get(str(row["workOrderId"]), 0) + 1
    for work_order_id in sorted(counts):
        lines.append(f"| `{work_order_id}` | {counts[work_order_id]} | `False` |")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            str(require_dict(dry_run.get("dryRunBoundary"), "dryRunBoundary")["evidenceBoundary"]),
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--playbook", type=Path, default=DEFAULT_PLAYBOOK)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register_path = args.register.resolve()
    playbook_path = args.playbook.resolve()
    report_path = args.report.resolve()
    json_out = args.json_out.resolve()
    md_out = args.md_out.resolve()

    register = load_json(register_path)
    report = load_json(report_path)
    if not playbook_path.exists():
        raise FileNotFoundError(playbook_path)

    dry_run = build_dry_run(register, report, register_path, playbook_path, report_path)
    validate_dry_run(dry_run, register, report)

    json_out.parent.mkdir(parents=True, exist_ok=True)
    with json_out.open("w", encoding="utf-8") as handle:
        json.dump(dry_run, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    write_markdown(dry_run, md_out)
    print(
        "life-path L4 synthetic evidence packet dry-run ok: "
        f"synthetic_packets={dry_run['currentDecision']['syntheticPacketCount']} "
        "real_packets=0 l4=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
