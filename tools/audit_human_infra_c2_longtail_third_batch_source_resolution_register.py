#!/usr/bin/env python3
"""审计 C2-LT-B3 source-resolution 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-resolution-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-extraction-queue.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-local-review-register.json"

SCHEMA = "human-infra.c2-longtail-third-batch-source-resolution-register.v1"
STATUS = "active-c2ltb3-source-resolution-register-independent-fresh-review-required"
REGISTER_LINK = "human-infra-c2-longtail-third-batch-source-resolution-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_third_batch_source_resolution_register.py"

EXPECTED_TASK_IDS = [
    "C2LTB3-EXT-007",
    "C2LTB3-EXT-010",
    "C2LTB3-EXT-011",
    "C2LTB3-EXT-012",
    "C2LTB3-EXT-020",
]
EXPECTED_CANDIDATE_COUNT = 7
EXPECTED_VERIFICATION_IDS = {
    "C2LTB3-SR-VERIFY-NCBI-ESUMMARY-20260703",
    "C2LTB3-SR-VERIFY-AAOHNS-ROUTE-20260703",
    "C2LTB3-SR-VERIFY-PUBMED-SSNHL-20260703",
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
    "AGENTS.md",
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
        "pubmedTitleMismatchCount": 3,
        "pubmedPartMismatchCount": 1,
        "publisherAccessOrRouteIssueCount": 1,
        "resolutionCandidateCount": EXPECTED_CANDIDATE_COUNT,
    }
    if scope.get("batchId") != "C2-LT-B3":
        fail(errors, "scope.batchId must be C2-LT-B3")
    if scope.get("resolutionLevel") != "c2ltb3-local-review-issue-row-source-resolution-v0.1":
        fail(errors, "scope.resolutionLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    candidate_count = sum(len(row.get("sourceResolutionCandidates", [])) for row in rows)
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        fail(errors, f"resolution candidate count must equal {EXPECTED_CANDIDATE_COUNT}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4)
    for phrase in ["does not change", "does not create reviewed artifacts", "does not authorize"]:
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
    for field in ["observedTitle", "verificationEvidence", "result"]:
        require_string(check.get(field), f"resolutionRows[{index}].currentSourceCheck.{field}", errors)
    evidence = check.get("verificationEvidence")
    if isinstance(evidence, str) and evidence not in verification_ids:
        fail(errors, f"resolutionRows[{index}].currentSourceCheck.verificationEvidence unknown: {evidence}")


def validate_candidates(row: dict[str, Any], row_index: int, verification_ids: set[str], errors: list[str]) -> None:
    candidates = row.get("sourceResolutionCandidates")
    if not isinstance(candidates, list) or not candidates:
        fail(errors, f"resolutionRows[{row_index}].sourceResolutionCandidates must be a non-empty list")
        return
    seen: set[str] = set()
    for candidate_index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            fail(errors, f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}] must be an object")
            continue
        missing = REQUIRED_CANDIDATE_FIELDS - set(candidate)
        if missing:
            fail(
                errors,
                f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}] missing: {sorted(missing)}",
            )
        candidate_id = require_string(
            candidate.get("candidateId"),
            f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].candidateId",
            errors,
        )
        if candidate_id in seen:
            fail(errors, f"duplicate candidateId in resolutionRows[{row_index}]: {candidate_id}")
        seen.add(candidate_id)
        url = require_string(
            candidate.get("url"),
            f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].url",
            errors,
        )
        if url and not url.startswith("https://"):
            fail(errors, f"candidate URL must be https: {url}")
        evidence = require_string(
            candidate.get("verificationEvidence"),
            f"resolutionRows[{row_index}].sourceResolutionCandidates[{candidate_index}].verificationEvidence",
            errors,
        )
        if evidence and evidence not in verification_ids:
            fail(errors, f"candidate verificationEvidence unknown: {evidence}")
        if "individual" not in str(candidate.get("useBoundary", "")) and "artifact" not in str(candidate.get("useBoundary", "")):
            fail(errors, f"candidate useBoundary must preserve individual-use or artifact boundary: {candidate_id}")


def validate_row(
    row: dict[str, Any],
    index: int,
    queue: dict[str, dict[str, Any]],
    extraction: dict[str, dict[str, Any]],
    local_findings: dict[str, dict[str, Any]],
    verification_ids: set[str],
    errors: list[str],
) -> None:
    missing = REQUIRED_ROW_FIELDS - set(row)
    if missing:
        fail(errors, f"resolutionRows[{index}] missing fields: {sorted(missing)}")
    task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
    if not task_id:
        return
    if task_id not in EXPECTED_TASK_IDS:
        fail(errors, f"unexpected resolution row taskId: {task_id}")
    task = queue.get(task_id)
    extracted = extraction.get(task_id)
    finding = local_findings.get(task_id)
    if not task:
        fail(errors, f"{task_id} missing from queue")
        return
    if not extracted:
        fail(errors, f"{task_id} missing from extraction register")
        return
    if not finding:
        fail(errors, f"{task_id} missing from local review findings")
        return
    mappings = {
        "domainId": task.get("domainId"),
        "localDomainPath": task.get("localDomainPath"),
        "sourceRefId": task.get("sourceRefId"),
        "originalRegisteredTitle": task.get("sourceTitle"),
        "originalRegisteredUrl": task.get("sourceUrl"),
        "localReviewIssueType": finding.get("issueType"),
    }
    for field, expected in mappings.items():
        if row.get(field) != expected:
            fail(errors, f"{task_id}.{field} must match source queue/local-review finding")
    local_path = row.get("localDomainPath")
    if isinstance(local_path, str):
        path = repo_path(local_path, f"{task_id}.localDomainPath", errors)
        if path:
            for required in ["README.md", "AGENTS.md"]:
                if not (path / required).exists():
                    fail(errors, f"{task_id}.localDomainPath missing {required}")
    if "mismatch" not in str(extracted.get("sourceAccessStatus", "")) and "forbidden" not in str(extracted.get("sourceAccessStatus", "")):
        fail(errors, f"{task_id} extraction row must preserve source issue status")
    if row.get("sourceResolutionStatus") != "candidate-resolution-prepared-not-fresh-reviewed":
        fail(errors, f"{task_id}.sourceResolutionStatus must remain candidate-resolution-prepared-not-fresh-reviewed")
    if row.get("artifactPromotionDecision") != "blocked-pending-resolution-fresh-review":
        fail(errors, f"{task_id}.artifactPromotionDecision must remain blocked")
    if "blocked" not in str(row.get("modelAdmissionDecision", "")):
        fail(errors, f"{task_id}.modelAdmissionDecision must remain blocked")
    blocked = set(require_string_list(row.get("blockedUses"), f"{task_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, f"{task_id}.blockedUses must match required prohibited uses")
    require_string(row.get("sourceResolutionDecision"), f"{task_id}.sourceResolutionDecision", errors)
    require_string_list(row.get("requiredFreshReviewActions"), f"{task_id}.requiredFreshReviewActions", errors, 4)
    validate_current_source_check(row, index, verification_ids, errors)
    validate_candidates(row, index, verification_ids, errors)


def validate_rows(
    data: dict[str, Any],
    queue: dict[str, dict[str, Any]],
    extraction: dict[str, dict[str, Any]],
    local_findings: dict[str, dict[str, Any]],
    verification_ids: set[str],
    errors: list[str],
) -> None:
    rows = data.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "resolutionRows must be a list")
        return
    if [row.get("taskId") for row in rows if isinstance(row, dict)] != EXPECTED_TASK_IDS:
        fail(errors, "resolutionRows must cover expected C2-LT-B3 issue task IDs in order")
    seen_resolution_ids: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        resolution_id = require_string(row.get("resolutionId"), f"resolutionRows[{index}].resolutionId", errors)
        if resolution_id in seen_resolution_ids:
            fail(errors, f"duplicate resolutionId: {resolution_id}")
        seen_resolution_ids.add(resolution_id)
        validate_row(row, index, queue, extraction, local_findings, verification_ids, errors)


def validate_top_level(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    for field in ["registerId", "purpose", "modelAdmissionDecision"]:
        require_string(data.get(field), field, errors)
    blocked = set(require_string_list(data.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required prohibited uses")
    required_next = require_string_list(data.get("requiredNextArtifacts"), "requiredNextArtifacts", errors, 5)
    if not any("fresh-review" in item for item in required_next):
        fail(errors, "requiredNextArtifacts must include fresh review next step")
    if not any("corrected-source" in item for item in required_next):
        fail(errors, "requiredNextArtifacts must include corrected source next step")
    require_string_list(data.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index target does not link source-resolution register: {relative_path}")
        if relative_path.startswith("tools/") and SCRIPT_LINK not in text:
            fail(errors, f"tools index target does not link audit script: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2-LT-B3 source-resolution register")
    queue = task_rows(QUEUE_PATH, "extractionTasks", errors, "source extraction queue")
    extraction = task_rows(EXTRACTION_PATH, "extractedRows", errors, "source extraction register")
    local_review = load_json(LOCAL_REVIEW_PATH, errors, "local review register")
    findings = {
        row.get("taskId"): row
        for row in local_review.get("sourceResolutionFindings", [])
        if isinstance(row, dict) and isinstance(row.get("taskId"), str)
    }

    if data:
        validate_top_level(data, errors)
        validate_source_of_truth(data, errors)
        verification_ids = validate_verification_sources(data, errors)
        rows = data.get("resolutionRows") if isinstance(data.get("resolutionRows"), list) else []
        validate_scope(data, rows, errors)
        validate_rows(data, queue, extraction, findings, verification_ids, errors)
        validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("C2-LT-B3 source-resolution register audit ok: rows=5 candidates=7 model=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
