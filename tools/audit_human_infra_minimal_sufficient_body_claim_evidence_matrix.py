#!/usr/bin/env python3
"""审计最小充分身体 Claim-Evidence Matrix。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = (
    ROOT
    / "domains/c1-boundary-rewriting/disembodied-cns/docs/minimal-sufficient-body-claim-evidence-matrix.json"
)
PROTOCOL_REGISTER_PATH = (
    ROOT
    / "domains/c1-boundary-rewriting/disembodied-cns/docs/brain-body-interface-protocol-register.json"
)
SOURCE_CARDS_PATH = ROOT / "domains/c1-boundary-rewriting/disembodied-cns/literature/source-cards.md"
SCHEMA = "human-infra.minimal-sufficient-body-claim-evidence-matrix.v1"
STATUS = "active-c1-claim-evidence-matrix-no-operational-use"
CLAIM_ID_RE = re.compile(r"^MSB-CL\d{3}$")
REQUIRED_SOURCE_KEYS = {
    "domainReadme",
    "domainAgentContract",
    "theoryModule",
    "protocolContract",
    "protocolRegister",
    "sourceCards",
    "maturityGapRegister",
}
REQUIRED_FALSE_FLAGS = {
    "operationalUseAllowed",
    "clinicalUseAllowed",
    "engineeringFeasibilityClaimAllowed",
    "subjectSurvivalClaimAllowed",
    "individualPredictionAllowed",
}
REQUIRED_BLOCKED_USES = {
    "life-support-instructions",
    "perfusion-protocol",
    "bci-implantation-or-stimulation-protocol",
    "clinical-claim",
    "engineering-feasibility-claim",
    "subject-survival-claim",
    "personal-survival-claim",
    "individual-prediction",
    "whole-body-replacement-claim",
    "mind-upload-or-revival-claim",
    "calibrated-prediction",
    "legal-advice",
}
FORBIDDEN_CLAIM_TOKENS = {
    "achieved",
    "proven",
    "safe",
    "operational",
    "validated",
    "confirmed",
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
        fail(errors, f"invalid JSON in {context}: {exc}")
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


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
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


def validate_source_of_truth(matrix: dict[str, Any], errors: list[str]) -> None:
    source = matrix.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, f"sourceOfTruth must contain exactly {sorted(REQUIRED_SOURCE_KEYS)}")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(matrix: dict[str, Any], row_count: int, errors: list[str]) -> None:
    decision = matrix.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if decision.get("rowCount") != row_count:
        fail(errors, "currentDecision.rowCount must match claimRows length")
    if decision.get("modelAdmissionLevel") != "L2":
        fail(errors, "currentDecision.modelAdmissionLevel must remain L2")
    if decision.get("quantitativeCapability") != "Q2":
        fail(errors, "currentDecision.quantitativeCapability must remain Q2")
    if decision.get("claimEvidenceMatrixCompleteForDomain") is not True:
        fail(errors, "currentDecision.claimEvidenceMatrixCompleteForDomain must be true")
    for flag in REQUIRED_FALSE_FLAGS:
        if decision.get(flag) is not False:
            fail(errors, f"currentDecision.{flag} must be false")


def protocol_ids(errors: list[str]) -> set[str]:
    data = load_json(PROTOCOL_REGISTER_PATH, errors, "brain-body interface protocol register")
    rows = data.get("protocolRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "protocol register protocolRows must be a list")
        return set()
    result: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"protocolRows[{index}] must be an object")
            continue
        row_id = require_string(row.get("protocol_id"), f"protocolRows[{index}].protocol_id", errors)
        if row_id:
            result.add(row_id)
    return result


def validate_blocked_uses(matrix: dict[str, Any], errors: list[str]) -> set[str]:
    blocked = matrix.get("blockedUses")
    if not isinstance(blocked, list):
        fail(errors, "blockedUses must be a list")
        return set()
    blocked_set = {item for item in blocked if isinstance(item, str)}
    missing = REQUIRED_BLOCKED_USES - blocked_set
    if missing:
        fail(errors, f"blockedUses missing required boundaries: {sorted(missing)}")
    return blocked_set


def validate_claim_rows(matrix: dict[str, Any], errors: list[str]) -> int:
    required_fields = matrix.get("requiredClaimFields")
    if not isinstance(required_fields, list) or not required_fields:
        fail(errors, "requiredClaimFields must be a non-empty list")
        required_fields = []
    required_field_set = {item for item in required_fields if isinstance(item, str)}
    for required in [
        "claim_id",
        "claim",
        "evidence_role",
        "source_card_ids",
        "protocol_ids",
        "variables",
        "mechanism",
        "falsifier",
        "downgrade_action",
        "scope_boundary",
        "model_position",
        "blocked_inferences",
    ]:
        if required not in required_field_set:
            fail(errors, f"requiredClaimFields missing {required}")

    roles = matrix.get("allowedEvidenceRoles")
    if not isinstance(roles, list) or not roles:
        fail(errors, "allowedEvidenceRoles must be a non-empty list")
        roles = []
    role_set = {item for item in roles if isinstance(item, str)}
    blocked_set = validate_blocked_uses(matrix, errors)
    source_card_text = SOURCE_CARDS_PATH.read_text(encoding="utf-8") if SOURCE_CARDS_PATH.exists() else ""
    available_protocol_ids = protocol_ids(errors)

    rows = matrix.get("claimRows")
    if not isinstance(rows, list) or not rows:
        fail(errors, "claimRows must be a non-empty list")
        return 0

    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"claimRows[{index}] must be an object")
            continue
        claim_id = require_string(row.get("claim_id"), f"claimRows[{index}].claim_id", errors)
        if claim_id and not CLAIM_ID_RE.match(claim_id):
            fail(errors, f"{claim_id}.claim_id must match MSB-CL###")
        if claim_id in seen:
            fail(errors, f"duplicate claim_id: {claim_id}")
        seen.add(claim_id)
        missing = sorted(required_field_set - set(row))
        if missing:
            fail(errors, f"{claim_id or index} missing required fields: {missing}")

        role = require_string(row.get("evidence_role"), f"{claim_id}.evidence_role", errors)
        if role and role not in role_set:
            fail(errors, f"{claim_id}.evidence_role is not allowed: {role}")

        claim_text = require_string(row.get("claim"), f"{claim_id}.claim", errors).lower()
        forbidden_used = sorted(token for token in FORBIDDEN_CLAIM_TOKENS if token in claim_text)
        if forbidden_used:
            fail(errors, f"{claim_id}.claim uses forbidden completion/safety language: {forbidden_used}")

        source_ids = require_string_list(row.get("source_card_ids"), f"{claim_id}.source_card_ids", errors)
        for source_id in source_ids:
            if source_id not in source_card_text:
                fail(errors, f"{claim_id}.source_card_id not found in source cards: {source_id}")

        row_protocol_ids = require_string_list(row.get("protocol_ids"), f"{claim_id}.protocol_ids", errors)
        for protocol_id in row_protocol_ids:
            if protocol_id not in available_protocol_ids:
                fail(errors, f"{claim_id}.protocol_id not found in protocol register: {protocol_id}")

        for field in ["variables", "blocked_inferences"]:
            values = require_string_list(row.get(field), f"{claim_id}.{field}", errors)
            if field == "blocked_inferences":
                for blocked in values:
                    if blocked not in blocked_set:
                        fail(errors, f"{claim_id}.blocked_inferences item not declared in blockedUses: {blocked}")

        for field in ["mechanism", "falsifier", "downgrade_action", "scope_boundary", "model_position"]:
            value = require_string(row.get(field), f"{claim_id}.{field}", errors)
            if field == "scope_boundary":
                lower = value.lower()
                if not any(term in lower for term in ["not", "no ", "does not", "不"]):
                    fail(errors, f"{claim_id}.scope_boundary must state a non-claim boundary")

    return len(rows)


def main() -> int:
    errors: list[str] = []
    matrix = load_json(MATRIX_PATH, errors, "minimal sufficient body claim-evidence matrix")
    if matrix:
        if matrix.get("schemaVersion") != SCHEMA:
            fail(errors, "schemaVersion mismatch")
        if matrix.get("status") != STATUS:
            fail(errors, "status mismatch")
        validate_source_of_truth(matrix, errors)
        row_count = validate_claim_rows(matrix, errors)
        validate_current_decision(matrix, row_count, errors)

    if errors:
        print("minimal sufficient body claim-evidence matrix audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "minimal sufficient body claim-evidence matrix audit ok: "
        f"rows={len(matrix.get('claimRows', []))} level=L2 q=Q2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
