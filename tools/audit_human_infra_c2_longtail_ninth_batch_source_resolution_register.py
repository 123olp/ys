#!/usr/bin/env python3
"""审计 C2 长尾第九批 source-resolution 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-ninth-batch-source-resolution-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-ninth-batch-source-extraction-queue.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-ninth-batch-source-extraction-register.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-ninth-batch-local-review-register.json"

SCHEMA = "human-infra.c2-longtail-ninth-batch-source-resolution-register.v1"
STATUS = "active-c2ltb9-source-resolution-register-independent-fresh-review-required"
REGISTER_LINK = "human-infra-c2-longtail-ninth-batch-source-resolution-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_ninth_batch_source_resolution_register.py"
EXPECTED_TASK_IDS = ["C2LTB9-EXT-008", "C2LTB9-EXT-011"]
EXPECTED_CANDIDATE_COUNT = 8
EXPECTED_VERIFICATION_IDS = {
    "C2LTB9-SR-VERIFY-IDSA-GUIDELINE-PAGE-20260704",
    "C2LTB9-SR-VERIFY-IDSA-PUBMED-CIAD527-20260704",
    "C2LTB9-SR-VERIFY-IDSA-DOI-CIAD527-20260704",
    "C2LTB9-SR-VERIFY-IWGDF-COMPANION-PUBMED-20260704",
    "C2LTB9-SR-VERIFY-MEDICAID-DENTAL-CANONICAL-20260704",
    "C2LTB9-SR-VERIFY-MEDICAID-DENTAL-INDEX-REDIRECT-20260704",
    "C2LTB9-SR-VERIFY-MEDICAID-ORAL-HEALTH-FACTSHEET-20260704",
    "C2LTB9-SR-VERIFY-MEDICAID-EPSDT-20260704",
}
SOURCE_OF_TRUTH_KEYS = {
    "sourceExtractionQueue",
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
    "medical-advice",
    "dental-advice",
    "rehabilitation-advice",
    "respiratory-equipment-advice",
    "vaccine-advice",
    "environmental-health-advice",
}
REQUIRED_ROW_FIELDS = {
    "resolutionId",
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "originalRegisteredTitle",
    "originalRegisteredUrl",
    "localReviewIssueType",
    "currentSourceCheck",
    "sourceResolutionDecision",
    "sourceResolutionStatus",
    "sourceResolutionCandidates",
    "requiredFreshReviewActions",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
}
REQUIRED_CANDIDATE_FIELDS = {
    "candidateId",
    "candidateRole",
    "title",
    "url",
    "sourceType",
    "sourceIdentityStatus",
    "verificationEvidence",
    "resolutionFinding",
    "useBoundary",
}
REQUIRED_INDEX_FILES = [
    "README.md",
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
    "tools/AGENTS.md",
]


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


def task_rows(path: Path, key: str, errors: list[str], context: str) -> dict[str, dict[str, Any]]:
    data = load_json(path, errors, context)
    rows = data.get(key) if data else None
    if not isinstance(rows, list):
        fail(errors, f"{context}.{key} must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"{context}.{key}[{index}].taskId", errors)
        if task_id:
            result[task_id] = row
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        if key in source:
            repo_path(source[key], f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], rows: list[dict[str, Any]], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "totalLocalReviewRowCount": 24,
        "issueRowCount": len(EXPECTED_TASK_IDS),
        "manualRouteIssueCount": len(EXPECTED_TASK_IDS),
        "idsaHttp525IssueCount": 1,
        "medicaidHttp403IssueCount": 1,
        "resolutionCandidateCount": EXPECTED_CANDIDATE_COUNT,
    }
    if scope.get("batchId") != "C2-LT-B9":
        fail(errors, "scope.batchId must be C2-LT-B9")
    if scope.get("resolutionLevel") != "c2ltb9-local-review-issue-row-source-resolution-v0.1":
        fail(errors, "scope.resolutionLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    candidate_count = sum(len(row.get("sourceResolutionCandidates", [])) for row in rows)
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        fail(errors, f"resolution candidate count must equal {EXPECTED_CANDIDATE_COUNT}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4)
    for phrase in ["does not change", "does not create reviewed artifacts", "does not authorize", "does not open"]:
        if not any(phrase in item for item in non_claims):
            fail(errors, f"scope.nonClaims must include phrase: {phrase}")


def validate_verification_sources(data: dict[str, Any], errors: list[str]) -> set[str]:
    sources = data.get("verificationSources")
    if not isinstance(sources, list):
        fail(errors, "verificationSources must be a list")
        return set()
    seen: set[str] = set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            fail(errors, f"verificationSources[{index}] must be an object")
            continue
        verification_id = require_string(source.get("verificationId"), f"verificationSources[{index}].verificationId", errors)
        if verification_id:
            seen.add(verification_id)
        for field in ["title", "url", "sourceType", "useBoundary"]:
            require_string(source.get(field), f"verificationSources[{index}].{field}", errors)
        url = source.get("url")
        if isinstance(url, str) and not url.startswith("https://"):
            fail(errors, f"verificationSources[{index}].url must be https")
    if seen != EXPECTED_VERIFICATION_IDS:
        fail(errors, "verificationSources must match expected verification IDs")
    return seen


def validate_current_source_check(row: dict[str, Any], index: int, verification_ids: set[str], errors: list[str]) -> None:
    check = row.get("currentSourceCheck")
    if not isinstance(check, dict):
        fail(errors, f"resolutionRows[{index}].currentSourceCheck must be an object")
        return
    for field in ["observedTitle", "result"]:
        require_string(check.get(field), f"resolutionRows[{index}].currentSourceCheck.{field}", errors)
    evidence = require_string_list(
        check.get("verificationEvidence"),
        f"resolutionRows[{index}].currentSourceCheck.verificationEvidence",
        errors,
        1,
    )
    for evidence_id in evidence:
        if evidence_id not in verification_ids:
            fail(errors, f"resolutionRows[{index}].currentSourceCheck unknown verificationEvidence: {evidence_id}")
    result = check.get("result")
    if isinstance(result, str) and "not-fresh-reviewed" not in result:
        fail(errors, f"resolutionRows[{index}].currentSourceCheck.result must preserve not-fresh-reviewed status")


def validate_candidates(row: dict[str, Any], index: int, verification_ids: set[str], errors: list[str]) -> None:
    candidates = row.get("sourceResolutionCandidates")
    if not isinstance(candidates, list) or not candidates:
        fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates must be a non-empty list")
        return
    resolution_id = row.get("resolutionId")
    if not isinstance(resolution_id, str):
        return
    for candidate_index, candidate in enumerate(candidates):
        context = f"resolutionRows[{index}].sourceResolutionCandidates[{candidate_index}]"
        if not isinstance(candidate, dict):
            fail(errors, f"{context} must be an object")
            continue
        missing = REQUIRED_CANDIDATE_FIELDS - set(candidate)
        if missing:
            fail(errors, f"{context} missing fields: {sorted(missing)}")
        candidate_id = require_string(candidate.get("candidateId"), f"{context}.candidateId", errors)
        if candidate_id and not candidate_id.startswith(f"{resolution_id}-CAND-"):
            fail(errors, f"{context}.candidateId must start with {resolution_id}-CAND-")
        url = require_string(candidate.get("url"), f"{context}.url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}.url must be https")
        evidence_id = require_string(candidate.get("verificationEvidence"), f"{context}.verificationEvidence", errors)
        if evidence_id and evidence_id not in verification_ids:
            fail(errors, f"{context}.verificationEvidence is unknown: {evidence_id}")
        status = require_string(candidate.get("sourceIdentityStatus"), f"{context}.sourceIdentityStatus", errors)
        if status and "not-fresh-reviewed" not in status:
            fail(errors, f"{context}.sourceIdentityStatus must preserve not-fresh-reviewed status")
        boundary = require_string(candidate.get("useBoundary"), f"{context}.useBoundary", errors)
        for forbidden in ["no ", "model admission"]:
            if boundary and forbidden not in boundary:
                fail(errors, f"{context}.useBoundary must include forbidden-use boundary phrase: {forbidden}")


def validate_rows(
    data: dict[str, Any],
    extraction_rows: dict[str, dict[str, Any]],
    local_rows: dict[str, dict[str, Any]],
    verification_ids: set[str],
    errors: list[str],
) -> None:
    rows = data.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "resolutionRows must be a list")
        return
    actual_ids = [row.get("taskId") for row in rows if isinstance(row, dict)]
    if actual_ids != EXPECTED_TASK_IDS:
        fail(errors, "resolutionRows task IDs must be C2LTB9-EXT-008 and C2LTB9-EXT-011 in order")
    seen_candidates: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(row)
        if missing:
            fail(errors, f"resolutionRows[{index}] missing fields: {sorted(missing)}")
        task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
        source_row = extraction_rows.get(task_id)
        local_row = local_rows.get(task_id)
        if not source_row:
            fail(errors, f"resolutionRows[{index}] references unknown extraction task: {task_id}")
        if not local_row:
            fail(errors, f"resolutionRows[{index}] references unknown local-review issue task: {task_id}")
        if source_row:
            field_pairs = {
                "domainId": "domainId",
                "localDomainPath": "localDomainPath",
                "sourceRefId": "sourceRefId",
                "originalRegisteredTitle": "sourceTitle",
                "originalRegisteredUrl": "sourceUrl",
            }
            for row_field, source_field in field_pairs.items():
                if row.get(row_field) != source_row.get(source_field):
                    fail(errors, f"resolutionRows[{index}].{row_field} must match extraction row {source_field}")
        if local_row and row.get("localReviewIssueType") != local_row.get("issueType"):
            fail(errors, f"resolutionRows[{index}].localReviewIssueType must match local review issueType")
        blocked_uses = row.get("blockedUses")
        if not isinstance(blocked_uses, list) or set(blocked_uses) != REQUIRED_BLOCKED_USES:
            fail(errors, f"resolutionRows[{index}].blockedUses must match required blocked uses")
        for field in ["artifactPromotionDecision", "modelAdmissionDecision", "sourceResolutionStatus"]:
            value = require_string(row.get(field), f"resolutionRows[{index}].{field}", errors)
            if value and not any(marker in value for marker in ["blocked", "not-fresh-reviewed"]):
                fail(errors, f"resolutionRows[{index}].{field} must preserve blocked/not-fresh-reviewed status")
        actions = require_string_list(row.get("requiredFreshReviewActions"), f"resolutionRows[{index}].requiredFreshReviewActions", errors, 3)
        if actions and not any("fresh review" in action for action in actions):
            fail(errors, f"resolutionRows[{index}].requiredFreshReviewActions must require fresh review")
        validate_current_source_check(row, index, verification_ids, errors)
        validate_candidates(row, index, verification_ids, errors)
        for candidate in row.get("sourceResolutionCandidates", []):
            if isinstance(candidate, dict):
                candidate_id = candidate.get("candidateId")
                if isinstance(candidate_id, str):
                    if candidate_id in seen_candidates:
                        fail(errors, f"duplicate candidateId: {candidate_id}")
                    seen_candidates.add(candidate_id)


def validate_global_boundaries(data: dict[str, Any], errors: list[str]) -> None:
    blocked_uses = data.get("blockedUses")
    if not isinstance(blocked_uses, list) or set(blocked_uses) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    required_next = require_string_list(data.get("requiredNextArtifacts"), "requiredNextArtifacts", errors, 5)
    for required in ["c2ltb9-manual-route-extraction-register", "c2ltb9-independent-fresh-review-verdict-register", "reviewed-source-card"]:
        if required not in required_next:
            fail(errors, f"requiredNextArtifacts missing {required}")
    decision = require_string(data.get("modelAdmissionDecision"), "modelAdmissionDecision", errors)
    if decision and "blocked" not in decision:
        fail(errors, "modelAdmissionDecision must remain blocked")


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"{relative_path} must link {REGISTER_LINK}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing tool index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text and relative_path != "Makefile":
            fail(errors, f"{relative_path} must mention {SCRIPT_LINK}")
        if "c2-longtail-ninth-batch-source-resolution-audit" not in text:
            fail(errors, f"{relative_path} must mention c2-longtail-ninth-batch-source-resolution-audit")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2-LT-B9 source-resolution register")
    extraction_rows = task_rows(EXTRACTION_PATH, "extractedRows", errors, "C2-LT-B9 source extraction register")
    local_review = load_json(LOCAL_REVIEW_PATH, errors, "C2-LT-B9 local review register")
    local_rows = {}
    if local_review:
        findings = local_review.get("sourceResolutionFindings")
        if not isinstance(findings, list):
            fail(errors, "localReview.sourceResolutionFindings must be a list")
        else:
            for finding in findings:
                if isinstance(finding, dict) and isinstance(finding.get("taskId"), str):
                    local_rows[finding["taskId"]] = finding
    queue = load_json(QUEUE_PATH, errors, "C2-LT-B9 source extraction queue")
    if queue and len(queue.get("extractionTasks", [])) != 24:
        fail(errors, "source extraction queue must contain 24 tasks")
    if data:
        if data.get("schemaVersion") != SCHEMA:
            fail(errors, "schemaVersion is invalid")
        if data.get("status") != STATUS:
            fail(errors, "status is invalid")
        require_string(data.get("purpose"), "purpose", errors)
        rows = data.get("resolutionRows") if isinstance(data.get("resolutionRows"), list) else []
        validate_source_of_truth(data, errors)
        validate_scope(data, rows, errors)
        verification_ids = validate_verification_sources(data, errors)
        validate_rows(data, extraction_rows, local_rows, verification_ids, errors)
        validate_global_boundaries(data, errors)
    validate_index_links(errors)
    if errors:
        print("C2-LT-B9 source-resolution register audit FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("C2-LT-B9 source-resolution register audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
