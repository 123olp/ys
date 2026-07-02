#!/usr/bin/env python3
"""审计 C2-LT-B4 manual/fulltext extraction 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json"
)
SOURCE_RESOLUTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-fourth-batch-source-resolution-register.json"
)

SCHEMA = "human-infra.c2ltb4-manual-fulltext-extraction-register.v1"
STATUS = "active-c2ltb4-manual-fulltext-extracted-fresh-review-required-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_extraction_register.py"
BATCH_ID = "C2-LT-B4"

SOURCE_OF_TRUTH_KEYS = {
    "sourceResolutionRegister",
    "sourceExtractionRegister",
    "localReviewRegister",
    "evidencePolicy",
    "maturityGapRegister",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}

REQUIRED_ROW_FIELDS = {
    "manualExtractionId",
    "batchId",
    "originTaskId",
    "sourceResolutionId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "candidateRole",
    "sourceTitle",
    "sourceUrl",
    "extractionDate",
    "extractionMode",
    "extractionStatus",
    "sourceAccessStatus",
    "sourceIdentityFinding",
    "currentnessBoundary",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSetting",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "downgradeTriggers",
    "modelPosition",
    "artifactPromotionReadiness",
    "modelAdmissionDecision",
    "blockedUses",
    "sourceEvidenceTrace",
    "nextAction",
}

REQUIRED_INDEX_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
    "tools/AGENTS.md",
]

EXPECTED_READY_ROWS = {"C2LTB4-MFEXT-002", "C2LTB4-MFEXT-005", "C2LTB4-MFEXT-007"}
EXPECTED_BLOCKED_ROWS = {
    "C2LTB4-MFEXT-001",
    "C2LTB4-MFEXT-003",
    "C2LTB4-MFEXT-004",
    "C2LTB4-MFEXT-006",
    "C2LTB4-MFEXT-008",
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


def require_int(value: Any, context: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{context} must be an integer")
        return None
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
        fail(errors, f"{context} must be a local path, not URL")
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


def source_resolution_candidates(source_resolution: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    rows = source_resolution.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "source-resolution register missing resolutionRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"source-resolution row[{index}] must be an object")
            continue
        candidates = row.get("sourceResolutionCandidates")
        if not isinstance(candidates, list):
            fail(errors, f"source-resolution row[{index}] missing sourceResolutionCandidates")
            continue
        for candidate in candidates:
            if not isinstance(candidate, dict):
                fail(errors, f"source-resolution row[{index}] candidate must be an object")
                continue
            candidate_id = require_string(candidate.get("candidateId"), "candidate.candidateId", errors)
            if candidate_id in result:
                fail(errors, f"duplicate source-resolution candidateId: {candidate_id}")
            result[candidate_id] = {
                "originTaskId": row.get("taskId"),
                "sourceResolutionId": row.get("resolutionId"),
                "domainId": row.get("domainId"),
                "localDomainPath": row.get("localDomainPath"),
                "candidateRole": candidate.get("candidateRole"),
                "sourceTitle": candidate.get("title"),
                "sourceUrl": candidate.get("url"),
            }
    return result


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        if key in source:
            repo_path(source[key], f"sourceOfTruth.{key}", errors)


def validate_scope(register: dict[str, Any], rows: list[dict[str, Any]], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "sourceResolutionIssueRowCount": 4,
        "sourceResolutionCandidateCount": 8,
        "manualExtractedRowCount": len(rows),
        "boundedFreshReviewCandidateRowCount": len(EXPECTED_READY_ROWS),
        "duplicateOrRouteOnlyBlockedRowCount": len(EXPECTED_BLOCKED_ROWS),
        "directReviewedArtifactRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("manualExtractionLevel") != "c2ltb4-source-resolution-manual-fulltext-extraction-v0.1":
        fail(errors, "scope.manualExtractionLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4)
    for phrase in ["not an independent fresh review", "does not create reviewed artifacts", "does not authorize"]:
        if not any(phrase in item for item in non_claims):
            fail(errors, f"scope.nonClaims must include phrase: {phrase}")


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context} must be an object")
        return
    require_string(value.get("primaryLocation"), f"{context}.primaryLocation", errors)
    require_string_list(value.get("variables"), f"{context}.variables", errors, min_len=2)
    require_string(value.get("admissibleUse"), f"{context}.admissibleUse", errors)


def validate_evidence_trace(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        fail(errors, f"{context} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"{context}[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}[{index}].url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}[{index}].url must be https")
        require_string(item.get("evidenceType"), f"{context}[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"{context}[{index}].finding", errors)


def validate_summary(register: dict[str, Any], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    ready = set(require_string_list(summary.get("boundedFreshReviewCandidateRows"), "summary.ready", errors, 3))
    blocked = set(require_string_list(summary.get("duplicateOrRouteOnlyBlockedRows"), "summary.blocked", errors, 5))
    if ready != EXPECTED_READY_ROWS:
        fail(errors, "summary.boundedFreshReviewCandidateRows must match expected ready rows")
    if blocked != EXPECTED_BLOCKED_ROWS:
        fail(errors, "summary.duplicateOrRouteOnlyBlockedRows must match expected blocked rows")
    require_string_list(summary.get("newFacts"), "summary.newFacts", errors, min_len=4)
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def validate_rows(
    register: dict[str, Any],
    candidates_by_id: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    rows = register.get("manualExtractionRows")
    if not isinstance(rows, list):
        fail(errors, "manualExtractionRows must be a list")
        return []
    seen_ids: set[str] = set()
    seen_candidates: set[str] = set()
    valid_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"manualExtractionRows[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(row)
        if missing:
            fail(errors, f"manualExtractionRows[{index}] missing fields: {sorted(missing)}")
        row_id = require_string(row.get("manualExtractionId"), f"manualExtractionRows[{index}].manualExtractionId", errors)
        if row_id and row_id != f"C2LTB4-MFEXT-{index + 1:03d}":
            fail(errors, f"{row_id} must follow sequential C2LTB4-MFEXT-### order")
        if row_id in seen_ids:
            fail(errors, f"duplicate manualExtractionId: {row_id}")
        seen_ids.add(row_id)
        candidate_id = require_string(row.get("candidateId"), f"{row_id}.candidateId", errors)
        if candidate_id in seen_candidates:
            fail(errors, f"duplicate candidateId row: {candidate_id}")
        seen_candidates.add(candidate_id)
        source_candidate = candidates_by_id.get(candidate_id)
        if not source_candidate:
            fail(errors, f"{row_id} references unknown source-resolution candidate: {candidate_id}")
        else:
            for row_key, candidate_key in {
                "originTaskId": "originTaskId",
                "sourceResolutionId": "sourceResolutionId",
                "domainId": "domainId",
                "localDomainPath": "localDomainPath",
                "candidateRole": "candidateRole",
                "sourceTitle": "sourceTitle",
                "sourceUrl": "sourceUrl",
            }.items():
                if row.get(row_key) != source_candidate.get(candidate_key):
                    fail(errors, f"{row_id}.{row_key} does not match source-resolution candidate")
        for field in REQUIRED_ROW_FIELDS:
            if field in {"blockedUses", "downgradeTriggers", "modelPosition", "sourceEvidenceTrace"}:
                continue
            require_string(row.get(field), f"{row_id}.{field}", errors)
        if row.get("batchId") != BATCH_ID:
            fail(errors, f"{row_id}.batchId must be {BATCH_ID}")
        if row.get("extractionDate") != "2026-07-03":
            fail(errors, f"{row_id}.extractionDate must be 2026-07-03")
        if row.get("modelAdmissionDecision") != (
            "blocked-pending-manual-extraction-independent-fresh-review-and-reviewed-artifact-gates"
        ):
            fail(errors, f"{row_id}.modelAdmissionDecision must remain blocked")
        if set(require_string_list(row.get("blockedUses"), f"{row_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{row_id}.blockedUses must match required blocked uses")
        triggers = require_string_list(row.get("downgradeTriggers"), f"{row_id}.downgradeTriggers", errors, min_len=3)
        if not any("Block" in trigger or "block" in trigger for trigger in triggers):
            fail(errors, f"{row_id}.downgradeTriggers must include blocking language")
        validate_model_position(row.get("modelPosition"), f"{row_id}.modelPosition", errors)
        validate_evidence_trace(row.get("sourceEvidenceTrace"), f"{row_id}.sourceEvidenceTrace", errors)
        readiness = row.get("artifactPromotionReadiness")
        if row_id in EXPECTED_READY_ROWS:
            if not isinstance(readiness, str) or not readiness.startswith("bounded-fresh-review-candidate"):
                fail(errors, f"{row_id}.artifactPromotionReadiness must be bounded fresh-review candidate")
        elif row_id in EXPECTED_BLOCKED_ROWS:
            if not isinstance(readiness, str) or "no-direct-artifact" not in readiness:
                fail(errors, f"{row_id}.artifactPromotionReadiness must preserve no-direct-artifact boundary")
        else:
            fail(errors, f"{row_id} is not expected in ready or blocked rows")
        valid_rows.append(row)
    if set(candidates_by_id) != seen_candidates:
        fail(errors, "manualExtractionRows must cover every source-resolution candidate exactly once")
    if seen_ids != EXPECTED_READY_ROWS | EXPECTED_BLOCKED_ROWS:
        fail(errors, "manualExtractionRows IDs must match expected C2-LT-B4 manual extraction rows")
    return valid_rows


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"{relative_path} missing register link {REGISTER_LINK}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} missing script link {SCRIPT_LINK}")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "manual fulltext extraction register")
    source_resolution = load_json(SOURCE_RESOLUTION_PATH, errors, "source-resolution register")
    if not register or not source_resolution:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "top-level blockedUses must match required blocked uses")
    validate_source_of_truth(register, errors)
    candidates_by_id = source_resolution_candidates(source_resolution, errors)
    rows = validate_rows(register, candidates_by_id, errors)
    validate_scope(register, rows, errors)
    validate_summary(register, errors)
    validate_index_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "C2-LT-B4 manual/fulltext extraction register audit ok: "
        f"rows={len(rows)} ready={len(EXPECTED_READY_ROWS)} blocked={len(EXPECTED_BLOCKED_ROWS)} model=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
