#!/usr/bin/env python3
"""审计 C2-LT-B6 independent fresh-review verdict 账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json"
)
SOURCE_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-register.json"
)
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-local-review-register.json"
MANUAL_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json"
)

SCHEMA = "human-infra.c2ltb6-independent-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb6-independent-fresh-review-verdict-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_sixth_batch_independent_fresh_review_verdict_register.py"
BATCH_ID = "C2-LT-B6"

SOURCE_OF_TRUTH_KEYS = {
    "sourceExtractionRegister",
    "localReviewRegister",
    "sourceResolutionRegister",
    "manualFulltextExtractionRegister",
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

ALLOWED_ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]

EXPECTED_MANUAL_ELIGIBLE_ROWS = {
    "C2LTB6-MFEXT-002",
    "C2LTB6-MFEXT-004",
    "C2LTB6-MFEXT-007",
    "C2LTB6-MFEXT-010",
    "C2LTB6-MFEXT-012",
    "C2LTB6-MFEXT-015",
    "C2LTB6-MFEXT-017",
}
EXPECTED_MANUAL_BLOCKED_ROWS = {
    "C2LTB6-MFEXT-001",
    "C2LTB6-MFEXT-003",
    "C2LTB6-MFEXT-005",
    "C2LTB6-MFEXT-006",
    "C2LTB6-MFEXT-008",
    "C2LTB6-MFEXT-009",
    "C2LTB6-MFEXT-011",
    "C2LTB6-MFEXT-013",
    "C2LTB6-MFEXT-014",
    "C2LTB6-MFEXT-016",
    "C2LTB6-MFEXT-018",
    "C2LTB6-MFEXT-019",
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


def source_extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(SOURCE_EXTRACTION_PATH, errors, "C2-LT-B6 source extraction register")
    rows = data.get("extractedRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register missing extractedRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"extractedRows[{index}].taskId", errors)
        if task_id in result:
            fail(errors, f"duplicate source extraction taskId: {task_id}")
        result[task_id] = row
    return result


def issue_task_ids(errors: list[str]) -> set[str]:
    data = load_json(LOCAL_REVIEW_PATH, errors, "C2-LT-B6 local review register")
    rows = data.get("sourceResolutionFindings") if data else None
    if not isinstance(rows, list):
        fail(errors, "local review register missing sourceResolutionFindings")
        return set()
    result = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"sourceResolutionFindings[{index}] must be an object")
            continue
        result.add(require_string(row.get("taskId"), f"sourceResolutionFindings[{index}].taskId", errors))
    return result


def manual_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(MANUAL_EXTRACTION_PATH, errors, "C2-LT-B6 manual/fulltext extraction register")
    rows = data.get("manualExtractionRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "manual/fulltext extraction register missing manualExtractionRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"manualExtractionRows[{index}] must be an object")
            continue
        manual_id = require_string(row.get("manualExtractionId"), f"manualExtractionRows[{index}].manualExtractionId", errors)
        if manual_id in result:
            fail(errors, f"duplicate manualExtractionId: {manual_id}")
        result[manual_id] = row
    return result


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = source.get(key)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_evidence_trace(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        fail(errors, f"{context} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"{context}[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}[{index}].url", errors)
        if url.startswith("https://"):
            pass
        elif url:
            repo_path(url, f"{context}[{index}].url", errors)
        require_string(item.get("evidenceType"), f"{context}[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"{context}[{index}].finding", errors)


def validate_source_reviews(
    register: dict[str, Any],
    extraction_by_id: dict[str, dict[str, Any]],
    issue_rows: set[str],
    errors: list[str],
) -> list[dict[str, Any]]:
    reviews = register.get("sourceExtractionFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "sourceExtractionFreshReviews must be a list")
        return []

    expected_task_ids = set(extraction_by_id) - issue_rows
    seen: set[str] = set()
    valid: list[dict[str, Any]] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"sourceExtractionFreshReviews[{index}] must be an object")
            continue
        review_id = require_string(review.get("reviewId"), f"sourceReview[{index}].reviewId", errors)
        if review_id and review_id != f"C2LTB6-FRV-{index + 1:03d}":
            fail(errors, f"{review_id} must follow sequential C2LTB6-FRV-### order")
        task_id = require_string(review.get("originTaskId"), f"{review_id}.originTaskId", errors)
        seen.add(task_id)
        source = extraction_by_id.get(task_id)
        if not source:
            fail(errors, f"{review_id} references unknown source extraction row: {task_id}")
        else:
            for key in ("domainId", "localDomainPath", "sourceTitle", "sourceUrl"):
                if review.get(key) != source.get(key):
                    fail(errors, f"{review_id}.{key} does not match source extraction row")
        if review.get("batchId") != BATCH_ID:
            fail(errors, f"{review_id}.batchId must be {BATCH_ID}")
        if review.get("freshReviewDate") != "2026-07-03":
            fail(errors, f"{review_id}.freshReviewDate must be 2026-07-03")
        if review.get("freshReviewMode") != "source-extraction-independent-fresh-review":
            fail(errors, f"{review_id}.freshReviewMode is invalid")
        if review.get("reviewerVerdict") != "support-with-boundary":
            fail(errors, f"{review_id}.reviewerVerdict must be support-with-boundary")
        if review.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep":
            fail(errors, f"{review_id}.artifactPromotionDecision must be eligible")
        if review.get("allowedArtifactTypes") != ALLOWED_ARTIFACT_TYPES:
            fail(errors, f"{review_id}.allowedArtifactTypes must contain all reviewed artifact types")
        if review.get("transferBoundaryVerdict") != "transfer-boundary-present-and-required":
            fail(errors, f"{review_id}.transferBoundaryVerdict must preserve boundary")
        if review.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"{review_id}.modelAdmissionDecision must remain blocked")
        if set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{review_id}.blockedUses must match required blocked uses")
        for key in (
            "sourceIdentityVerdict",
            "sourceAccessVerdict",
            "sourceContextVerdict",
            "currentnessVerdict",
            "exactClaimUseVerdict",
            "endpointVariableVerdict",
            "uncertaintyBoundaryVerdict",
            "freshReviewFinding",
            "downgradeOrBlockReason",
            "nextAction",
        ):
            require_string(review.get(key), f"{review_id}.{key}", errors)
        validate_evidence_trace(review.get("reviewEvidenceTrace"), f"{review_id}.reviewEvidenceTrace", errors)
        valid.append(review)

    if seen != expected_task_ids:
        fail(errors, "sourceExtractionFreshReviews must cover exactly non-issue extraction rows")
    return valid


def validate_manual_reviews(
    register: dict[str, Any],
    manual_by_id: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    reviews = register.get("manualFulltextFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "manualFulltextFreshReviews must be a list")
        return []
    seen: set[str] = set()
    valid: list[dict[str, Any]] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"manualFulltextFreshReviews[{index}] must be an object")
            continue
        review_id = require_string(review.get("reviewId"), f"manualReview[{index}].reviewId", errors)
        if review_id and review_id != f"C2LTB6-MFFRV-{index + 1:03d}":
            fail(errors, f"{review_id} must follow sequential C2LTB6-MFFRV-### order")
        manual_id = require_string(review.get("manualExtractionId"), f"{review_id}.manualExtractionId", errors)
        seen.add(manual_id)
        source = manual_by_id.get(manual_id)
        if not source:
            fail(errors, f"{review_id} references unknown manual extraction row: {manual_id}")
        else:
            for key in (
                "originTaskId",
                "sourceResolutionId",
                "domainId",
                "localDomainPath",
                "candidateId",
                "sourceTitle",
                "sourceUrl",
            ):
                if review.get(key) != source.get(key):
                    fail(errors, f"{review_id}.{key} does not match manual extraction row")
        if review.get("batchId") != BATCH_ID:
            fail(errors, f"{review_id}.batchId must be {BATCH_ID}")
        if review.get("freshReviewDate") != "2026-07-03":
            fail(errors, f"{review_id}.freshReviewDate must be 2026-07-03")
        if review.get("freshReviewMode") != "manual-fulltext-extraction-independent-fresh-review":
            fail(errors, f"{review_id}.freshReviewMode is invalid")
        if review.get("transferBoundaryVerdict") != "transfer-boundary-present-and-required":
            fail(errors, f"{review_id}.transferBoundaryVerdict must preserve boundary")
        if review.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"{review_id}.modelAdmissionDecision must remain blocked")
        if set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{review_id}.blockedUses must match required blocked uses")

        if manual_id in EXPECTED_MANUAL_ELIGIBLE_ROWS:
            if review.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep":
                fail(errors, f"{review_id}.artifactPromotionDecision must be eligible")
            if review.get("reviewerVerdict") != "support-with-boundary":
                fail(errors, f"{review_id}.reviewerVerdict must be support-with-boundary")
            if review.get("allowedArtifactTypes") != ALLOWED_ARTIFACT_TYPES:
                fail(errors, f"{review_id}.allowedArtifactTypes must contain all reviewed artifact types")
        elif manual_id in EXPECTED_MANUAL_BLOCKED_ROWS:
            if review.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep":
                fail(errors, f"{review_id}.artifactPromotionDecision must remain blocked/context-only")
            if review.get("reviewerVerdict") != "blocked-or-context-only":
                fail(errors, f"{review_id}.reviewerVerdict must be blocked-or-context-only")
            if review.get("allowedArtifactTypes") != []:
                fail(errors, f"{review_id}.allowedArtifactTypes must be empty for blocked rows")
        else:
            fail(errors, f"unexpected manual extraction row: {manual_id}")

        for key in (
            "sourceIdentityVerdict",
            "sourceAccessVerdict",
            "sourceContextVerdict",
            "currentnessVerdict",
            "exactClaimVerdict",
            "endpointVariableVerdict",
            "freshReviewFinding",
            "downgradeOrBlockReason",
            "nextAction",
        ):
            require_string(review.get(key), f"{review_id}.{key}", errors)
        validate_evidence_trace(review.get("reviewEvidenceTrace"), f"{review_id}.reviewEvidenceTrace", errors)
        valid.append(review)

    if seen != set(manual_by_id):
        fail(errors, "manualFulltextFreshReviews must cover exactly every manual extraction row")
    return valid


def validate_scope_and_summary(
    register: dict[str, Any],
    source_reviews: list[dict[str, Any]],
    manual_reviews: list[dict[str, Any]],
    errors: list[str],
) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    source_eligible = [r["originTaskId"] for r in source_reviews]
    manual_eligible = [
        r["manualExtractionId"]
        for r in manual_reviews
        if r.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep"
    ]
    manual_blocked = [
        r["manualExtractionId"]
        for r in manual_reviews
        if r.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep"
    ]
    expected_counts = {
        "sourceExtractionFreshReviewRowCount": len(source_reviews),
        "manualFulltextFreshReviewRowCount": len(manual_reviews),
        "reviewedFreshReviewRowCount": len(source_reviews) + len(manual_reviews),
        "eligibleForArtifactPrepRowCount": len(source_eligible) + len(manual_eligible),
        "blockedOrContextOnlyRowCount": len(manual_blocked),
        "directReviewedArtifactRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("reviewLevel") != "c2ltb6-independent-fresh-review-v0.1":
        fail(errors, "scope.reviewLevel is invalid")
    for key, expected in expected_counts.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    non_claims = "\n".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=5))
    for phrase in ("does not create reviewed artifacts", "does not open model admission", "Route-only"):
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")

    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if summary.get("reviewedSourceExtractionRows") != len(source_reviews):
        fail(errors, "summary.reviewedSourceExtractionRows must match source review count")
    if summary.get("reviewedManualFulltextRows") != len(manual_reviews):
        fail(errors, "summary.reviewedManualFulltextRows must match manual review count")
    if summary.get("eligibleSourceExtractionRows") != source_eligible:
        fail(errors, "summary.eligibleSourceExtractionRows must match source reviews")
    if summary.get("eligibleManualFulltextRows") != manual_eligible:
        fail(errors, "summary.eligibleManualFulltextRows must match manual reviews")
    if set(manual_eligible) != EXPECTED_MANUAL_ELIGIBLE_ROWS:
        fail(errors, "summary eligible manual rows must match expected B6 bounded routes")
    if set(manual_blocked) != EXPECTED_MANUAL_BLOCKED_ROWS:
        fail(errors, "summary blocked manual rows must match expected blocked/context rows")
    if summary.get("blockedOrContextOnlyManualFulltextRows") != manual_blocked:
        fail(errors, "summary blocked manual rows must match review order")
    if summary.get("directReviewedArtifactsCreated") != 0:
        fail(errors, "summary.directReviewedArtifactsCreated must be 0")
    if summary.get("modelAdmissionDecision") != "blocked":
        fail(errors, "summary.modelAdmissionDecision must be blocked")
    facts = "\n".join(require_string_list(summary.get("newFreshReviewFacts"), "summary.newFreshReviewFacts", errors, min_len=5))
    for phrase in ("Seventeen", "Seven manual/fulltext", "Twelve route-only", "calibrated prediction"):
        if phrase not in facts:
            fail(errors, f"summary.newFreshReviewFacts missing phrase: {phrase}")
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def validate_index_links(register: dict[str, Any], errors: list[str]) -> None:
    if register.get("indexRequirements") != REQUIRED_INDEX_FILES:
        fail(errors, "indexRequirements must match required index file list")
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index file does not reference B6 fresh-review verdict register: {relative_path}")
    for relative_path in ("Makefile", "tools/README.md", "tools/AGENTS.md"):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "C2-LT-B6 independent fresh-review verdict register")
    extraction_by_id = source_extraction_rows(errors)
    issues = issue_task_ids(errors)
    manual_by_id = manual_rows(errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        source_reviews = validate_source_reviews(register, extraction_by_id, issues, errors)
        manual_reviews = validate_manual_reviews(register, manual_by_id, errors)
        validate_scope_and_summary(register, source_reviews, manual_reviews, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B6 independent fresh-review verdict audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B6 independent fresh-review verdict audit ok: source=17 manual=19 eligible=24 blocked=12 model=blocked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
