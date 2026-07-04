#!/usr/bin/env python3
"""审计 Human Infra L4 证据 intake register。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-l4-evidence-intake-register.json"
PLAYBOOK_PATH = ROOT / "docs/reference/human-infra-l4-evidence-packet-review-playbook.md"

SCHEMA = "human-infra.l4-evidence-intake-register.v1"
STATUS = "active-intake-register-no-direct-evidence-l4-blocked"
REGISTER_LINK = "human-infra-l4-evidence-intake-register.json"
SCRIPT_LINK = "audit_human_infra_l4_evidence_intake_register.py"

REQUIRED_SOURCE_KEYS = {
    "l4UnblockExecutionPlan",
    "l4ReadinessBlockerMatrix",
    "l4EvidencePacketReviewPlaybook",
    "modelAdmissionCandidateRegistry",
    "nhanesDisclosureReviewExecutionRegister",
    "nhanesLocalRunEvidenceManifest",
    "nhatsL4ReadinessRunway",
    "calibrationReadiness",
}
REQUIRED_WORK_ORDER_SLOT_COUNTS = {
    "L4WO-01-nhats-governed-access-and-workspace": 4,
    "L4WO-02-nhats-exact-field-value-confirmation": 5,
    "L4WO-03-nhats-real-extraction-cohort-flow": 4,
    "L4WO-04-nhanes-human-disclosure-review": 6,
    "L4WO-05-validation-calibration-diagnostics": 5,
}
REQUIRED_CANDIDATES = {
    "L4C-NHANES-PUBLIC-LMF-WEIGHTED-DOMAIN",
    "L4C-NHATS-R13-R14-FUNCTIONAL-SURVIVAL",
}
REQUIRED_ACCEPTED_CLASSES = {
    "redacted-artifact-hash",
    "human-review-signoff",
    "second-reviewer-signoff",
    "governed-access-log",
    "controlled-workspace-inventory",
    "storage-destruction-evidence",
    "authenticated-variable-page-capture-hash",
    "aggregate-only-run-manifest",
    "suppression-review-record",
    "calibration-diagnostic-report",
    "bias-applicability-review",
}
REQUIRED_REJECTED_CLASSES = {
    "raw-row-file",
    "identifier-bearing-file",
    "restricted-data-copy",
    "public-ai-upload",
    "ai-only-signoff",
    "natural-language-claim-without-artifact-hash",
    "unreviewed-notebook",
    "screenshot-with-sensitive-values",
    "public-web-json-with-real-weighted-values",
}
REQUIRED_PACKET_FIELDS = {
    "packetId",
    "workOrderId",
    "slotId",
    "candidatePath",
    "evidenceClass",
    "evidenceStatus",
    "repositoryPolicy",
    "artifactHash",
    "artifactHashAlgorithm",
    "artifactDescriptionRedacted",
    "producerRole",
    "firstReviewerRole",
    "secondReviewerRole",
    "reviewDate",
    "sensitivityClass",
    "rawDataTracked",
    "restrictedDataTracked",
    "identifierTracked",
    "publicAiUpload",
    "aiOnlySignoff",
    "allowedUse",
    "prohibitedUse",
    "downstreamDecision",
}
REQUIRED_FORBIDDEN_PACKET_FIELDS = {
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
REQUIRED_PACKET_STATUSES = {
    "draft-redacted",
    "human-reviewed-redacted",
    "second-reviewed-redacted",
    "rejected",
}
REQUIRED_PACKET_BOOLEAN_DEFAULTS = {
    "rawDataTracked",
    "restrictedDataTracked",
    "identifierTracked",
    "publicAiUpload",
    "aiOnlySignoff",
}
REQUIRED_PACKET_RULE_PHRASES = {
    "workOrderId must match",
    "slotId must match",
    "candidatePath must match",
    "evidenceClass must match",
    "repositoryPolicy must match",
    "sha256 hash",
    "human-reviewed-redacted or second-reviewed-redacted",
    "firstReviewerRole must not be ai-only",
    "must all be false",
    "bounded L4 evidence review only",
    "l4-still-blocked",
}
REQUIRED_PROHIBITED_PACKET_USES = {
    "public-weighted-domain-output",
    "calibrated-prediction",
    "individual-prediction",
    "individual-death-date-output",
    "medical-advice",
    "intervention-ranking",
    "raw-row-reconstruction",
}
REQUIRED_FALSE_DECISION_KEYS = {
    "directEvidenceAttached",
    "humanReviewEvidenceAttached",
    "externalGovernedAccessEvidenceAttached",
    "l4AggregateCalibratedAdmissionAllowed",
    "publicWeightedDomainOutputAllowed",
    "calibratedPredictionAvailable",
    "individualUseAllowed",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "docs/reference/human-infra-model-admission-candidate-registry.json": REGISTER_LINK,
    "docs/reference/human-infra-l4-unblock-execution-plan.json": REGISTER_LINK,
    "Makefile": "l4-evidence-intake-register-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
}
REQUIRED_PLAYBOOK_INDEX_LINKS = {
    "README.md": "human-infra-l4-evidence-packet-review-playbook.md",
    "docs/AGENTS.md": "human-infra-l4-evidence-packet-review-playbook.md",
    "docs/reference/README.md": "human-infra-l4-evidence-packet-review-playbook.md",
    "docs/reference/human-infra-maturity-roadmap.md": "human-infra-l4-evidence-packet-review-playbook.md",
    "docs/reference/human-infra-maturity-gap-register.json": "human-infra-l4-evidence-packet-review-playbook.md",
}
REQUIRED_PLAYBOOK_PHRASES = {
    "human-infra.l4-evidence-packet.v1",
    "packetCount = 0",
    "closedSlotCount = 0",
    "redacted SHA-256",
    "first human reviewer",
    "second reviewer",
    "bounded L4 evidence review",
    "l4-still-blocked",
    "No raw rows",
    "AI-only signoff",
    "must not use the packet",
    "The audit must check that this playbook exists",
}
REQUIRED_PLAYBOOK_BOUNDARY_PHRASES = {
    "public weighted domain output = blocked",
    "calibrated prediction = blocked",
    "individual use = blocked",
    "individual death-date output",
    "medical advice",
    "intervention ranking",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], context: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {context}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid {context} JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{context} must be a JSON object")
        return {}
    return data


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_bool(value: Any, context: str, errors: list[str]) -> bool | None:
    if not isinstance(value, bool):
        fail(errors, f"{context} must be boolean")
        return None
    return value


def require_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
        return []
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    result: list[str] = []
    for index, item in enumerate(require_list(value, context, errors, min_len)):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")
        return None
    return target


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(register: dict[str, Any], errors: list[str]) -> None:
    decision = register.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if decision.get("evidenceIntakeRegisterReady") is not True:
        fail(errors, "currentDecision.evidenceIntakeRegisterReady must be true")
    if "L3" not in require_string(decision.get("highestCurrentModelLevel"), "currentDecision.highestCurrentModelLevel", errors):
        fail(errors, "currentDecision.highestCurrentModelLevel must remain L3")
    for key in REQUIRED_FALSE_DECISION_KEYS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in ["no direct evidence", "pending", "blocked"]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase!r}")


def validate_evidence_classes(register: dict[str, Any], errors: list[str]) -> None:
    accepted = set(require_string_list(register.get("acceptedEvidenceClasses"), "acceptedEvidenceClasses", errors))
    rejected = set(require_string_list(register.get("rejectedEvidenceClasses"), "rejectedEvidenceClasses", errors))
    if accepted != REQUIRED_ACCEPTED_CLASSES:
        fail(errors, "acceptedEvidenceClasses mismatch")
    if rejected != REQUIRED_REJECTED_CLASSES:
        fail(errors, "rejectedEvidenceClasses mismatch")
    overlap = accepted & rejected
    if overlap:
        fail(errors, f"evidence class overlap: {sorted(overlap)}")


def validate_evidence_packet_contract(register: dict[str, Any], errors: list[str]) -> None:
    contract = register.get("evidencePacketContract")
    if not isinstance(contract, dict):
        fail(errors, "evidencePacketContract must be an object")
        return
    if contract.get("schemaName") != "human-infra.l4-evidence-packet.v1":
        fail(errors, "evidencePacketContract.schemaName mismatch")
    if contract.get("contractStatus") != "template-only-no-packets-accepted":
        fail(errors, "evidencePacketContract.contractStatus must keep packets unaccepted")
    if "one-reviewed-packet" not in require_string(contract.get("packetCardinality"), "evidencePacketContract.packetCardinality", errors):
        fail(errors, "evidencePacketContract.packetCardinality must require one reviewed packet per slot")

    required_fields = set(
        require_string_list(
            contract.get("requiredPacketFields"),
            "evidencePacketContract.requiredPacketFields",
            errors,
        )
    )
    if required_fields != REQUIRED_PACKET_FIELDS:
        fail(errors, "evidencePacketContract.requiredPacketFields mismatch")

    forbidden_fields = set(
        require_string_list(
            contract.get("forbiddenPacketFields"),
            "evidencePacketContract.forbiddenPacketFields",
            errors,
        )
    )
    if forbidden_fields != REQUIRED_FORBIDDEN_PACKET_FIELDS:
        fail(errors, "evidencePacketContract.forbiddenPacketFields mismatch")
    overlap = required_fields & forbidden_fields
    if overlap:
        fail(errors, f"evidencePacketContract field overlap: {sorted(overlap)}")

    statuses = set(
        require_string_list(
            contract.get("allowedPacketStatuses"),
            "evidencePacketContract.allowedPacketStatuses",
            errors,
        )
    )
    if statuses != REQUIRED_PACKET_STATUSES:
        fail(errors, "evidencePacketContract.allowedPacketStatuses mismatch")

    defaults = contract.get("requiredBooleanDefaults")
    if not isinstance(defaults, dict):
        fail(errors, "evidencePacketContract.requiredBooleanDefaults must be an object")
    else:
        if set(defaults) != REQUIRED_PACKET_BOOLEAN_DEFAULTS:
            fail(errors, "evidencePacketContract.requiredBooleanDefaults keys mismatch")
        for key, value in defaults.items():
            if value is not False:
                fail(errors, f"evidencePacketContract.requiredBooleanDefaults.{key} must be false")

    hash_algorithms = set(
        require_string_list(
            contract.get("hashAlgorithms"),
            "evidencePacketContract.hashAlgorithms",
            errors,
        )
    )
    if hash_algorithms != {"sha256"}:
        fail(errors, "evidencePacketContract.hashAlgorithms must be exactly sha256")

    rules = " ".join(
        require_string_list(
            contract.get("acceptanceRules"),
            "evidencePacketContract.acceptanceRules",
            errors,
            min_len=len(REQUIRED_PACKET_RULE_PHRASES),
        )
    )
    for phrase in REQUIRED_PACKET_RULE_PHRASES:
        if phrase not in rules:
            fail(errors, f"evidencePacketContract.acceptanceRules missing {phrase!r}")

    prohibited = set(
        require_string_list(
            contract.get("prohibitedPacketUses"),
            "evidencePacketContract.prohibitedPacketUses",
            errors,
        )
    )
    if prohibited != REQUIRED_PROHIBITED_PACKET_USES:
        fail(errors, "evidencePacketContract.prohibitedPacketUses mismatch")

    if contract.get("packetCount") != 0:
        fail(errors, "evidencePacketContract.packetCount must remain 0")
    if contract.get("closedSlotCount") != 0:
        fail(errors, "evidencePacketContract.closedSlotCount must remain 0")


def validate_slot_groups(register: dict[str, Any], errors: list[str]) -> dict[str, int]:
    groups = register.get("evidenceSlotGroups")
    summary = {
        "workOrderCount": 0,
        "totalSlotCount": 0,
        "pendingSlotCount": 0,
        "evidenceAttachedCount": 0,
        "humanSignoffCount": 0,
        "externalEvidenceSlotCount": 0,
    }
    if not isinstance(groups, list):
        fail(errors, "evidenceSlotGroups must be a list")
        return summary
    observed: dict[str, int] = {}
    for group_index, group in enumerate(groups):
        if not isinstance(group, dict):
            fail(errors, f"evidenceSlotGroups[{group_index}] must be an object")
            continue
        work_order_id = require_string(group.get("workOrderId"), f"evidenceSlotGroups[{group_index}].workOrderId", errors)
        candidate = require_string(group.get("candidatePath"), f"{work_order_id}.candidatePath", errors)
        if candidate not in REQUIRED_CANDIDATES:
            fail(errors, f"{work_order_id}.candidatePath must be a known L4 candidate")
        if group.get("status") != "pending-no-direct-evidence":
            fail(errors, f"{work_order_id}.status must be pending-no-direct-evidence")
        slots = group.get("slots")
        if not isinstance(slots, list):
            fail(errors, f"{work_order_id}.slots must be a list")
            continue
        observed[work_order_id] = len(slots)
        summary["workOrderCount"] += 1
        slot_ids: set[str] = set()
        for slot_index, slot in enumerate(slots):
            if not isinstance(slot, dict):
                fail(errors, f"{work_order_id}.slots[{slot_index}] must be an object")
                continue
            slot_id = require_string(slot.get("slotId"), f"{work_order_id}.slots[{slot_index}].slotId", errors)
            if slot_id in slot_ids:
                fail(errors, f"{work_order_id} duplicate slotId {slot_id}")
            slot_ids.add(slot_id)
            evidence_class = require_string(slot.get("evidenceClass"), f"{work_order_id}.{slot_id}.evidenceClass", errors)
            if evidence_class not in REQUIRED_ACCEPTED_CLASSES:
                fail(errors, f"{work_order_id}.{slot_id}.evidenceClass is not accepted")
            if require_bool(slot.get("requiredHumanSignoff"), f"{work_order_id}.{slot_id}.requiredHumanSignoff", errors) is not True:
                fail(errors, f"{work_order_id}.{slot_id}.requiredHumanSignoff must be true")
            external = require_bool(slot.get("externalOnly"), f"{work_order_id}.{slot_id}.externalOnly", errors)
            if external is True:
                summary["externalEvidenceSlotCount"] += 1
            require_string(slot.get("repositoryPolicy"), f"{work_order_id}.{slot_id}.repositoryPolicy", errors)
            if slot.get("status") != "pending":
                fail(errors, f"{work_order_id}.{slot_id}.status must be pending")
            if slot.get("evidenceRef") is not None:
                fail(errors, f"{work_order_id}.{slot_id}.evidenceRef must be null until direct evidence is reviewed")
                summary["evidenceAttachedCount"] += 1
            if slot.get("reviewerSignoff") is not None:
                fail(errors, f"{work_order_id}.{slot_id}.reviewerSignoff must be null until reviewed")
                summary["humanSignoffCount"] += 1
            if require_bool(slot.get("blocksL4"), f"{work_order_id}.{slot_id}.blocksL4", errors) is not True:
                fail(errors, f"{work_order_id}.{slot_id}.blocksL4 must be true")
            summary["totalSlotCount"] += 1
            summary["pendingSlotCount"] += 1
    if observed != REQUIRED_WORK_ORDER_SLOT_COUNTS:
        fail(errors, f"work-order slot counts mismatch: {observed}")
    return summary


def validate_summary(register: dict[str, Any], calculated: dict[str, int], errors: list[str]) -> None:
    summary = register.get("slotStatusSummary")
    if not isinstance(summary, dict):
        fail(errors, "slotStatusSummary must be an object")
        return
    for key, value in calculated.items():
        if summary.get(key) != value:
            fail(errors, f"slotStatusSummary.{key} must be {value}")
    if summary.get("l4ReviewOpen") is not False:
        fail(errors, "slotStatusSummary.l4ReviewOpen must be false")


def validate_boundaries(register: dict[str, Any], errors: list[str]) -> None:
    boundaries = " ".join(require_string_list(register.get("hardBoundaries"), "hardBoundaries", errors, min_len=7))
    for phrase in [
        "No raw rows",
        "No AI-only signoff",
        "No individual death-date output.",
        "No individual medical advice.",
        "No calibration claim before validation and calibration diagnostics.",
        "No L4 candidate review can open while any slot remains pending.",
    ]:
        if phrase not in boundaries:
            fail(errors, f"hardBoundaries missing {phrase!r}")


def validate_index_links(errors: list[str]) -> None:
    index_links: dict[str, list[str]] = {}
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        index_links.setdefault(relative_path, []).append(needle)
    for relative_path, needle in REQUIRED_PLAYBOOK_INDEX_LINKS.items():
        index_links.setdefault(relative_path, []).append(needle)
    for relative_path, needles in index_links.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                fail(errors, f"{relative_path} missing reference to {needle}")


def validate_playbook(errors: list[str]) -> None:
    if not PLAYBOOK_PATH.exists():
        fail(errors, f"missing L4 evidence packet review playbook: {PLAYBOOK_PATH.relative_to(ROOT)}")
        return
    text = PLAYBOOK_PATH.read_text(encoding="utf-8")
    for phrase in REQUIRED_PLAYBOOK_PHRASES:
        if phrase not in text:
            fail(errors, f"L4 evidence packet review playbook missing {phrase!r}")
    lower_text = text.lower()
    for phrase in REQUIRED_PLAYBOOK_BOUNDARY_PHRASES:
        if phrase.lower() not in lower_text:
            fail(errors, f"L4 evidence packet review playbook missing boundary {phrase!r}")
    for forbidden in ["packetCount = 1", "closedSlotCount = 1", "L4 aggregate calibrated admission = allowed"]:
        if forbidden in text:
            fail(errors, f"L4 evidence packet review playbook must not contain {forbidden!r}")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "L4 evidence intake register")
    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, "schemaVersion mismatch")
        if register.get("status") != STATUS:
            fail(errors, "status mismatch")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("owner"), "owner", errors)
        validate_source_of_truth(register, errors)
        validate_current_decision(register, errors)
        validate_evidence_classes(register, errors)
        validate_evidence_packet_contract(register, errors)
        summary = validate_slot_groups(register, errors)
        validate_summary(register, summary, errors)
        validate_boundaries(register, errors)
    validate_index_links(errors)
    validate_playbook(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "L4 evidence intake register audit ok: "
        f"work_orders={register['slotStatusSummary']['workOrderCount']} "
        f"slots={register['slotStatusSummary']['totalSlotCount']} l4=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
