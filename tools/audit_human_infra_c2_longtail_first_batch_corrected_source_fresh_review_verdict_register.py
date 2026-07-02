#!/usr/bin/env python3
"""审计 C2-LT-B1 corrected source fresh-review 判定账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json"
)
EXTRACTION_REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json"
)

SCHEMA = "human-infra.c2ltb1-corrected-source-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb1-corrected-source-fresh-review-verdict-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_first_batch_corrected_source_fresh_review_verdict_register.py"
BATCH_ID = "C2-LT-B1"

SOURCE_OF_TRUTH_KEYS = {
    "correctedSourceReextractionRegister",
    "correctedSourceReextractionQueue",
    "sourceResolutionFreshReviewVerdictRegister",
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

REQUIRED_REVIEW_FIELDS = {
    "reviewId",
    "batchId",
    "reextractionTaskId",
    "originTaskId",
    "sourceResolutionReviewId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "sourceTitle",
    "sourceUrl",
    "freshReviewDate",
    "freshReviewMode",
    "sourceIdentityVerdict",
    "sourceAccessVerdict",
    "sourceContextVerdict",
    "currentnessVerdict",
    "exactClaimVerdict",
    "endpointVariableVerdict",
    "transferBoundaryVerdict",
    "reviewerVerdict",
    "freshReviewFinding",
    "downgradeOrBlockReason",
    "artifactPromotionDecision",
    "allowedArtifactTypes",
    "modelAdmissionDecision",
    "blockedUses",
    "reviewEvidenceTrace",
    "nextAction",
}

ALLOWED_ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]

BLOCKED_PROMOTION_DECISIONS = {
    "blocked-context-lineage-only-no-direct-artifact-fill",
    "blocked-direct-source-access-needed",
    "blocked-publisher-route-only",
    "blocked-directory-route-only",
    "blocked-fulltext-needed",
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


def extraction_rows(register: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    rows = register.get("extractedRows")
    if not isinstance(rows, list):
        fail(errors, "corrected extraction register missing extractedRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("reextractionTaskId"), f"extractedRows[{index}].reextractionTaskId", errors)
        result[task_id] = row
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
        if url and not url.startswith("https://"):
            fail(errors, f"{context}[{index}].url must be https")
        require_string(item.get("evidenceType"), f"{context}[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"{context}[{index}].finding", errors)


def validate_reviews(register: dict[str, Any], rows_by_task: dict[str, dict[str, Any]], errors: list[str]) -> list[dict[str, Any]]:
    reviews = register.get("correctedSourceFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "correctedSourceFreshReviews must be a list")
        return []
    seen: set[str] = set()
    valid_reviews: list[dict[str, Any]] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"correctedSourceFreshReviews[{index}] must be an object")
            continue
        missing = REQUIRED_REVIEW_FIELDS - set(review)
        if missing:
            fail(errors, f"review[{index}] missing fields: {sorted(missing)}")
        review_id = require_string(review.get("reviewId"), f"review[{index}].reviewId", errors)
        if review_id and review_id != f"C2LTB1-CFRV-{index + 1:03d}":
            fail(errors, f"{review_id} must follow sequential C2LTB1-CFRV-### order")
        task_id = require_string(review.get("reextractionTaskId"), f"{review_id}.reextractionTaskId", errors)
        if task_id in seen:
            fail(errors, f"duplicate reextractionTaskId: {task_id}")
        seen.add(task_id)
        source_row = rows_by_task.get(task_id)
        if not source_row:
            fail(errors, f"{review_id} references unknown corrected extraction row: {task_id}")
        else:
            for review_key, source_key in {
                "originTaskId": "originTaskId",
                "sourceResolutionReviewId": "sourceResolutionReviewId",
                "domainId": "domainId",
                "localDomainPath": "localDomainPath",
                "candidateId": "candidateId",
                "sourceUrl": "sourceUrl",
            }.items():
                if review.get(review_key) != source_row.get(source_key):
                    fail(errors, f"{review_id}.{review_key} does not match corrected extraction row")
        if review.get("batchId") != BATCH_ID:
            fail(errors, f"{review_id}.batchId must be {BATCH_ID}")
        if review.get("freshReviewDate") != "2026-07-02":
            fail(errors, f"{review_id}.freshReviewDate must be 2026-07-02")
        if review.get("freshReviewMode") != "corrected-source-reextraction-independent-fresh-review":
            fail(errors, f"{review_id}.freshReviewMode is invalid")
        if review.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"{review_id}.modelAdmissionDecision must remain blocked")
        if set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{review_id}.blockedUses must match required blocked uses")
        if review.get("transferBoundaryVerdict") != "transfer-boundary-present-and-required":
            fail(errors, f"{review_id}.transferBoundaryVerdict must preserve boundary")
        decision = require_string(review.get("artifactPromotionDecision"), f"{review_id}.artifactPromotionDecision", errors)
        allowed = review.get("allowedArtifactTypes")
        if decision == "eligible-for-bounded-reviewed-artifact-prep":
            if review.get("reviewerVerdict") != "support-with-boundary":
                fail(errors, f"{review_id}.reviewerVerdict must support eligible rows with boundary")
            if allowed != ALLOWED_ARTIFACT_TYPES:
                fail(errors, f"{review_id}.allowedArtifactTypes must contain all reviewed artifact types")
        elif decision in BLOCKED_PROMOTION_DECISIONS:
            if review.get("reviewerVerdict") != "blocked-or-context-only":
                fail(errors, f"{review_id}.reviewerVerdict must be blocked-or-context-only")
            if allowed != []:
                fail(errors, f"{review_id}.allowedArtifactTypes must be empty for blocked rows")
        else:
            fail(errors, f"{review_id}.artifactPromotionDecision is invalid: {decision}")
        validate_evidence_trace(review.get("reviewEvidenceTrace"), f"{review_id}.reviewEvidenceTrace", errors)
        require_string(review.get("freshReviewFinding"), f"{review_id}.freshReviewFinding", errors)
        require_string(review.get("downgradeOrBlockReason"), f"{review_id}.downgradeOrBlockReason", errors)
        require_string(review.get("nextAction"), f"{review_id}.nextAction", errors)
        valid_reviews.append(review)
    if seen != set(rows_by_task):
        fail(errors, "correctedSourceFreshReviews must cover exactly every corrected extraction row")
    return valid_reviews


def validate_scope(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("reviewLevel") != "c2ltb1-corrected-source-fresh-review-v0.1":
        fail(errors, "scope.reviewLevel is invalid")
    eligible = [review for review in reviews if review.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep"]
    blocked = [review for review in reviews if review.get("artifactPromotionDecision") in BLOCKED_PROMOTION_DECISIONS]
    expected = {
        "correctedExtractionRowCount": len(reviews),
        "reviewedCorrectedExtractionRowCount": len(reviews),
        "eligibleForArtifactPrepRowCount": len(eligible),
        "blockedOrContextOnlyRowCount": len(blocked),
        "directReviewedArtifactRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    non_claims = "\n".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4))
    for phrase in ("does not create reviewed artifacts", "does not open model admission", "does not authorize"):
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")


def validate_summary(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    actual_reviewed = require_int(summary.get("reviewedCorrectedRows"), "summary.reviewedCorrectedRows", errors)
    if actual_reviewed is not None and actual_reviewed != len(reviews):
        fail(errors, "summary.reviewedCorrectedRows must equal review count")
    eligible = [
        review["reextractionTaskId"]
        for review in reviews
        if review.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep"
    ]
    blocked = [
        review["reextractionTaskId"]
        for review in reviews
        if review.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep"
    ]
    if summary.get("eligibleForArtifactPrepRows") != eligible:
        fail(errors, "summary.eligibleForArtifactPrepRows does not match reviews")
    if summary.get("blockedOrContextOnlyRows") != blocked:
        fail(errors, "summary.blockedOrContextOnlyRows does not match reviews")
    if summary.get("directReviewedArtifactsCreated") != 0:
        fail(errors, "summary.directReviewedArtifactsCreated must be 0")
    if summary.get("modelAdmissionDecision") != "blocked":
        fail(errors, "summary.modelAdmissionDecision must be blocked")
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
            fail(errors, f"index file does not reference corrected fresh-review verdict register: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "corrected source fresh-review verdict register")
    extraction_register = load_json(EXTRACTION_REGISTER_PATH, errors, "corrected source re-extraction register")
    rows_by_task = extraction_rows(extraction_register, errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        reviews = validate_reviews(register, rows_by_task, errors)
        validate_scope(register, reviews, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        required_review_fields = set(require_string_list(register.get("requiredReviewFields"), "requiredReviewFields", errors))
        if not required_review_fields.issubset(REQUIRED_REVIEW_FIELDS):
            fail(errors, "requiredReviewFields must be a subset of required review fields")
        if set(require_string_list(register.get("verdictTaxonomy"), "verdictTaxonomy", errors)) != {
            "support-with-boundary",
            "blocked-or-context-only",
        }:
            fail(errors, "verdictTaxonomy is invalid")
        decisions = set(require_string_list(register.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors))
        if decisions != {"eligible-for-bounded-reviewed-artifact-prep"} | BLOCKED_PROMOTION_DECISIONS:
            fail(errors, "artifactPromotionDecisions is invalid")
        validate_summary(register, reviews, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B1 corrected source fresh-review verdict audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B1 corrected source fresh-review verdict audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
