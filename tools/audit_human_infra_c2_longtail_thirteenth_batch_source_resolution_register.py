#!/usr/bin/env python3
"""审计 C2-LT-B13 source-resolution 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-source-extraction-queue.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-source-extraction-register.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-local-review-register.json"

SCHEMA = "human-infra.c2-longtail-thirteenth-batch-source-resolution-register.v1"
STATUS = "active-c2ltb13-source-resolution-register-independent-fresh-review-required"
REGISTER_LINK = "human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_thirteenth_batch_source_resolution_register.py"
AUDIT_TARGET = "c2-longtail-thirteenth-batch-source-resolution-audit"
EXPECTED_TASK_IDS = [
    "C2LTB13-EXT-004",
    "C2LTB13-EXT-017",
    "C2LTB13-EXT-021",
]
IDENTITY_MATCH_TASK_IDS = {
    "C2LTB13-EXT-004",
    "C2LTB13-EXT-017",
}
TITLE_DOMAIN_MISMATCH_TASK_IDS = {
    "C2LTB13-EXT-021",
}
EXPECTED_CANDIDATE_COUNT = 4
EXPECTED_VERIFICATION_IDS = {
    "C2LTB13-SR-VERIFY-NCBI-ESUMMARY-20260711",
    "C2LTB13-SR-VERIFY-NCBI-EFETCH-20260711",
    "C2LTB13-SR-VERIFY-NCBI-IAD-SEARCH-20260711",
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
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "docs/reference/human-infra-maturity-gap-register.json",
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
        "pubmedManualRouteIssueCount": 3,
        "pubmedIdentityMatchCount": len(IDENTITY_MATCH_TASK_IDS),
        "pubmedTitleDomainMismatchCount": len(TITLE_DOMAIN_MISMATCH_TASK_IDS),
        "correctedSourceCandidateCount": 1,
        "resolutionCandidateCount": EXPECTED_CANDIDATE_COUNT,
    }
    if scope.get("batchId") != "C2-LT-B13":
        fail(errors, "scope.batchId must be C2-LT-B13")
    if scope.get("resolutionLevel") != "c2ltb13-local-review-issue-row-source-resolution-v0.1":
        fail(errors, "scope.resolutionLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    candidate_count = sum(len(row.get("sourceResolutionCandidates", [])) for row in rows)
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        fail(errors, f"resolution candidate count must equal {EXPECTED_CANDIDATE_COUNT}")
    non_claims = require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 5)
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
    for field in ["observedTitle", "observedJournal", "observedDoi", "verificationEvidence", "result"]:
        require_string(check.get(field), f"resolutionRows[{index}].currentSourceCheck.{field}", errors)
    evidence = check.get("verificationEvidence")
    if isinstance(evidence, str) and evidence not in verification_ids:
        fail(errors, f"resolutionRows[{index}].currentSourceCheck.verificationEvidence must reference verificationSources")


def validate_candidates(row: dict[str, Any], index: int, verification_ids: set[str], errors: list[str]) -> int:
    candidates = row.get("sourceResolutionCandidates")
    if not isinstance(candidates, list) or not candidates:
        fail(errors, f"resolutionRows[{index}].sourceResolutionCandidates must be a non-empty list")
        return 0
    for candidate_index, candidate in enumerate(candidates):
        context = f"resolutionRows[{index}].sourceResolutionCandidates[{candidate_index}]"
        if not isinstance(candidate, dict):
            fail(errors, f"{context} must be an object")
            continue
        for field in REQUIRED_CANDIDATE_FIELDS:
            require_string(candidate.get(field), f"{context}.{field}", errors)
        url = candidate.get("url")
        if isinstance(url, str) and not url.startswith("https://"):
            fail(errors, f"{context}.url must be https")
        evidence = candidate.get("verificationEvidence")
        if isinstance(evidence, str) and evidence not in verification_ids:
            fail(errors, f"{context}.verificationEvidence must reference verificationSources")
        if "model admission" not in str(candidate.get("useBoundary", "")):
            fail(errors, f"{context}.useBoundary must keep model admission blocked")
    return len(candidates)


def validate_rows(
    data: dict[str, Any],
    verification_ids: set[str],
    queue_rows: dict[str, dict[str, Any]],
    extraction_rows: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    rows = data.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "resolutionRows must be a list")
        return []
    if [row.get("taskId") for row in rows if isinstance(row, dict)] != EXPECTED_TASK_IDS:
        fail(errors, "resolutionRows must preserve expected B13 issue task order")
    candidate_count = 0
    mismatch_found = False
    corrected_found = False
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"resolutionRows[{index}] must be an object")
            continue
        for field in REQUIRED_ROW_FIELDS:
            if field not in row:
                fail(errors, f"resolutionRows[{index}].{field} missing")
        task_id = require_string(row.get("taskId"), f"resolutionRows[{index}].taskId", errors)
        queue_row = queue_rows.get(task_id, {})
        extraction_row = extraction_rows.get(task_id, {})
        for field in ["domainId", "localDomainPath", "sourceRefId"]:
            if row.get(field) != queue_row.get(field):
                fail(errors, f"{task_id}.{field} must match source extraction queue")
        if row.get("originalRegisteredUrl") != extraction_row.get("sourceUrl"):
            fail(errors, f"{task_id}.originalRegisteredUrl must match source extraction register")
        local_path = row.get("localDomainPath")
        if isinstance(local_path, str):
            repo_path(local_path, f"{task_id}.localDomainPath", errors)
        validate_current_source_check(row, index, verification_ids, errors)
        candidate_count += validate_candidates(row, index, verification_ids, errors)
        if task_id in IDENTITY_MATCH_TASK_IDS:
            if "keep-registered-pubmed-route" not in str(row.get("sourceResolutionDecision", "")):
                fail(errors, f"{task_id}.sourceResolutionDecision must keep verified PubMed route")
        if task_id in TITLE_DOMAIN_MISMATCH_TASK_IDS:
            if "replace-mismatched-pmid" not in str(row.get("sourceResolutionDecision", "")):
                fail(errors, f"{task_id}.sourceResolutionDecision must require corrected source replacement")
            row_text = json.dumps(row, ensure_ascii=False)
            mismatch_found = "26428404" in row_text and "chemistry" in row_text.lower()
            corrected_found = "22193141" in row_text and "Incontinence-associated dermatitis" in row_text
        require_string_list(row.get("requiredFreshReviewActions"), f"{task_id}.requiredFreshReviewActions", errors, 5)
        if "blocked" not in str(row.get("artifactPromotionDecision", "")):
            fail(errors, f"{task_id}.artifactPromotionDecision must remain blocked")
        if "blocked" not in str(row.get("modelAdmissionDecision", "")):
            fail(errors, f"{task_id}.modelAdmissionDecision must remain blocked")
        blocked = set(require_string_list(row.get("blockedUses"), f"{task_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
        if blocked != REQUIRED_BLOCKED_USES:
            fail(errors, f"{task_id}.blockedUses must match required blocked uses")
    if candidate_count != EXPECTED_CANDIDATE_COUNT:
        fail(errors, f"total sourceResolutionCandidates must equal {EXPECTED_CANDIDATE_COUNT}")
    if not mismatch_found:
        fail(errors, "C2LTB13-EXT-021 must preserve PMID 26428404 chemistry mismatch evidence")
    if not corrected_found:
        fail(errors, "C2LTB13-EXT-021 must preserve corrected IAD candidate PMID 22193141")
    return [row for row in rows if isinstance(row, dict)]


def validate_top_level(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    for field in ["registerId", "purpose", "modelAdmissionDecision"]:
        require_string(data.get(field), field, errors)
    if "blocked" not in str(data.get("modelAdmissionDecision", "")):
        fail(errors, "modelAdmissionDecision must remain blocked")
    blocked = set(require_string_list(data.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    require_string_list(data.get("requiredNextArtifacts"), "requiredNextArtifacts", errors, 5)
    require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 5)


def validate_index_links(errors: list[str]) -> None:
    for relative_path in REQUIRED_INDEX_FILES:
        target = ROOT / relative_path
        if not target.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index target does not mention register: {relative_path}")
    makefile = ROOT / "Makefile"
    if not makefile.exists():
        fail(errors, "missing Makefile")
    else:
        make_text = makefile.read_text(encoding="utf-8")
        if AUDIT_TARGET not in make_text:
            fail(errors, "Makefile does not expose B13 source-resolution audit target")
        if SCRIPT_LINK not in make_text:
            fail(errors, "Makefile does not run B13 source-resolution audit script")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2-LT-B13 source-resolution register")
    queue_rows = task_rows(QUEUE_PATH, "extractionTasks", errors, "C2-LT-B13 source extraction queue")
    extraction_rows = task_rows(EXTRACTION_PATH, "extractedRows", errors, "C2-LT-B13 source extraction register")
    task_rows(LOCAL_REVIEW_PATH, "sourceResolutionFindings", errors, "C2-LT-B13 local review register")
    if data:
        validate_top_level(data, errors)
        validate_source_of_truth(data, errors)
        verification_ids = validate_verification_sources(data, errors)
        rows = validate_rows(data, verification_ids, queue_rows, extraction_rows, errors)
        validate_scope(data, rows, errors)
        validate_index_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "C2 longtail thirteenth-batch source-resolution register audit ok: "
        "batch=C2-LT-B13 issue_rows=3 identity_matches=2 title_domain_mismatches=1 candidates=4"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
