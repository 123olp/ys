#!/usr/bin/env python3
"""审计脑-身接口协议变量寄存器。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "domains/c1-boundary-rewriting/disembodied-cns/docs/brain-body-interface-protocol-register.json"
)
SOURCE_CARDS_PATH = ROOT / "domains/c1-boundary-rewriting/disembodied-cns/literature/source-cards.md"
SCHEMA = "human-infra.brain-body-interface-protocol-register.v1"
STATUS = "active-c1-protocol-candidate-equivalence-no-operational-use"
FORBIDDEN_STATUS_TOKENS = {"achieved", "proven", "safe", "operational"}
REQUIRED_SOURCE_KEYS = {
    "domainReadme",
    "domainAgentContract",
    "theoryModule",
    "protocolContract",
    "sourceSignals",
    "sourceCards",
    "domainToModelBridge",
}
REQUIRED_CURRENT_FALSE_FLAGS = {
    "operationalUseAllowed",
    "clinicalUseAllowed",
    "individualPredictionAllowed",
    "subjectSurvivalClaimAllowed",
    "engineeringFeasibilityClaimAllowed",
}
REQUIRED_BLOCKED_USES = {
    "life-support-instructions",
    "perfusion-protocol",
    "bci-implantation-or-stimulation-protocol",
    "clinical-claim",
    "engineering-feasibility-claim",
    "personal-survival-claim",
    "individual-prediction",
    "whole-body-replacement-claim",
    "mind-upload-or-revival-claim",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing register: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "register must be a JSON object")
        return {}
    return data


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    if isinstance(value, str) and value.strip():
        return [value]
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a string or list with at least {min_len} item(s)")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a repository path, not URL")
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
        fail(errors, f"sourceOfTruth must contain exactly {sorted(REQUIRED_SOURCE_KEYS)}")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(register: dict[str, Any], row_count: int, errors: list[str]) -> None:
    decision = register.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if decision.get("rowCount") != row_count:
        fail(errors, "currentDecision.rowCount must match protocolRows length")
    if decision.get("modelAdmissionLevel") != "L2":
        fail(errors, "currentDecision.modelAdmissionLevel must remain L2")
    if decision.get("quantitativeCapability") != "Q2":
        fail(errors, "currentDecision.quantitativeCapability must remain Q2")
    for flag in REQUIRED_CURRENT_FALSE_FLAGS:
        if decision.get(flag) is not False:
            fail(errors, f"currentDecision.{flag} must be false")


def validate_protocol_rows(register: dict[str, Any], errors: list[str]) -> int:
    required_fields = register.get("requiredProtocolFields")
    if not isinstance(required_fields, list) or not required_fields:
        fail(errors, "requiredProtocolFields must be a non-empty list")
        required_fields = []
    required_field_set = {item for item in required_fields if isinstance(item, str)}
    if "equivalence_status" not in required_field_set:
        fail(errors, "requiredProtocolFields must include equivalence_status")

    allowed_statuses = register.get("allowedEquivalenceStatus")
    if not isinstance(allowed_statuses, list) or not allowed_statuses:
        fail(errors, "allowedEquivalenceStatus must be a non-empty list")
        allowed_statuses = []
    allowed_status_set = {item for item in allowed_statuses if isinstance(item, str)}
    if allowed_status_set & FORBIDDEN_STATUS_TOKENS:
        fail(errors, "allowedEquivalenceStatus contains forbidden operational/safety language")

    source_card_text = SOURCE_CARDS_PATH.read_text(encoding="utf-8") if SOURCE_CARDS_PATH.exists() else ""
    rows = register.get("protocolRows")
    if not isinstance(rows, list) or not rows:
        fail(errors, "protocolRows must be a non-empty list")
        return 0

    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"protocolRows[{index}] must be an object")
            continue
        row_id = require_string(row.get("protocol_id"), f"protocolRows[{index}].protocol_id", errors)
        if row_id in seen:
            fail(errors, f"duplicate protocol_id: {row_id}")
        seen.add(row_id)
        missing = sorted(required_field_set - set(row))
        if missing:
            fail(errors, f"{row_id or index} missing required fields: {missing}")
        status = require_string(row.get("equivalence_status"), f"{row_id}.equivalence_status", errors)
        if status not in allowed_status_set:
            fail(errors, f"{row_id}.equivalence_status is not allowed: {status}")
        if any(token in status for token in FORBIDDEN_STATUS_TOKENS):
            fail(errors, f"{row_id}.equivalence_status uses forbidden language: {status}")

        for field in [
            "channel_family",
            "exchange_content",
            "direction",
            "carrier",
            "unit_or_scale",
            "frequency_or_cadence",
            "latency_bound",
            "precision_requirement",
            "error_tolerance",
            "closed_loop_role",
            "abort_gate",
            "scope_boundary",
        ]:
            require_string(row.get(field), f"{row_id}.{field}", errors)
        for field in [
            "subject_state_dependency",
            "observable_proxy",
            "replacement_candidate",
            "failure_modes",
            "evidence_anchor",
        ]:
            values = require_string_list(row.get(field), f"{row_id}.{field}", errors)
            if field == "evidence_anchor":
                for card_id in values:
                    if card_id not in source_card_text:
                        fail(errors, f"{row_id}.evidence_anchor not found in source cards: {card_id}")
        scope = str(row.get("scope_boundary", "")).lower()
        if not any(term in scope for term in ["not", "no ", "does not", "不"]):
            fail(errors, f"{row_id}.scope_boundary must explicitly state a non-claim boundary")
    return len(rows)


def validate_blocked_uses(register: dict[str, Any], errors: list[str]) -> None:
    blocked = register.get("blockedUses")
    if not isinstance(blocked, list):
        fail(errors, "blockedUses must be a list")
        return
    blocked_set = {item for item in blocked if isinstance(item, str)}
    missing = REQUIRED_BLOCKED_USES - blocked_set
    if missing:
        fail(errors, f"blockedUses missing required boundaries: {sorted(missing)}")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors)
    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, "schemaVersion mismatch")
        if register.get("status") != STATUS:
            fail(errors, "status mismatch")
        validate_source_of_truth(register, errors)
        validate_blocked_uses(register, errors)
        row_count = validate_protocol_rows(register, errors)
        validate_current_decision(register, row_count, errors)

    if errors:
        print("brain-body interface protocol register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"brain-body interface protocol register audit ok: rows={len(register.get('protocolRows', []))} level=L2 q=Q2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
