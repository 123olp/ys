#!/usr/bin/env python3
"""审计 C2-LT-B7 manual/fulltext fresh-review 判定账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-register.json"
)
MANUAL_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-seventh-batch-manual-fulltext-extraction-register.json"
)

SCHEMA = "human-infra.c2ltb7-manual-fulltext-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb7-manual-fulltext-fresh-review-verdict-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-seventh-batch-manual-fulltext-fresh-review-verdict-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_seventh_batch_manual_fulltext_fresh_review_verdict_register.py"
BATCH_ID = "C2-LT-B7"

SOURCE_OF_TRUTH_KEYS = {
    "manualFulltextExtractionRegister",
    "sourceResolutionRegister",
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

REQUIRED_REVIEW_FIELDS = {
    "reviewId",
    "batchId",
    "manualExtractionId",
    "originTaskId",
    "sourceResolutionId",
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
    "blocked-dynamic-registration-no-direct-artifact-fill",
    "blocked-access-restricted-no-direct-artifact-fill",
    "blocked-duplicate-lineage-no-direct-artifact-fill",
    "blocked-index-route-no-direct-artifact-fill",
}

EXPECTED_ELIGIBLE_ROWS = {
    "C2LTB7-MFEXT-001",
    "C2LTB7-MFEXT-002",
    "C2LTB7-MFEXT-006",
}

EXPECTED_BLOCKED_ROWS = {
    "C2LTB7-MFEXT-003",
    "C2LTB7-MFEXT-004",
    "C2LTB7-MFEXT-005",
    "C2LTB7-MFEXT-007",
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


def manual_rows(register: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    rows = register.get("manualExtractionRows")
    if not isinstance(rows, list):
        fail(errors, "manual/fulltext extraction register missing manualExtractionRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"manualExtractionRows[{index}] must be an object")
            continue
        row_id = require_string(row.get("manualExtractionId"), f"manualExtractionRows[{index}].manualExtractionId", errors)
        if row_id in result:
            fail(errors, f"duplicate manualExtractionId: {row_id}")
        result[row_id] = row
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


def validate_reviews(
    register: dict[str, Any], rows_by_manual_id: dict[str, dict[str, Any]], errors: list[str]
) -> list[dict[str, Any]]:
    reviews = register.get("manualFulltextFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "manualFulltextFreshReviews must be a list")
        return []

    seen: set[str] = set()
    valid_reviews: list[dict[str, Any]] = []
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"manualFulltextFreshReviews[{index}] must be an object")
            continue
        missing = REQUIRED_REVIEW_FIELDS - set(review)
        if missing:
            fail(errors, f"review[{index}] missing fields: {sorted(missing)}")

        review_id = require_string(review.get("reviewId"), f"review[{index}].reviewId", errors)
        if review_id and review_id != f"C2LTB7-MFFRV-{index + 1:03d}":
            fail(errors, f"{review_id} must follow sequential C2LTB7-MFFRV-### order")

        manual_id = require_string(review.get("manualExtractionId"), f"{review_id}.manualExtractionId", errors)
        if manual_id in seen:
            fail(errors, f"duplicate manualExtractionId: {manual_id}")
        seen.add(manual_id)

        source_row = rows_by_manual_id.get(manual_id)
        if not source_row:
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
                if review.get(key) != source_row.get(key):
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
        blocked_uses = set(require_string_list(review.get("blockedUses"), f"{review_id}.blockedUses", errors))
        if blocked_uses != REQUIRED_BLOCKED_USES:
            fail(errors, f"{review_id}.blockedUses must match required blocked uses")

        decision = require_string(review.get("artifactPromotionDecision"), f"{review_id}.artifactPromotionDecision", errors)
        allowed = review.get("allowedArtifactTypes")
        if manual_id in EXPECTED_ELIGIBLE_ROWS:
            if decision != "eligible-for-bounded-reviewed-artifact-prep":
                fail(errors, f"{review_id}.artifactPromotionDecision must be eligible")
            if review.get("reviewerVerdict") != "support-with-boundary":
                fail(errors, f"{review_id}.reviewerVerdict must be support-with-boundary")
            if allowed != ALLOWED_ARTIFACT_TYPES:
                fail(errors, f"{review_id}.allowedArtifactTypes must contain all reviewed artifact types")
        elif manual_id in EXPECTED_BLOCKED_ROWS:
            if decision not in BLOCKED_PROMOTION_DECISIONS:
                fail(errors, f"{review_id}.artifactPromotionDecision must be one of blocked decisions")
            if review.get("reviewerVerdict") != "blocked-or-context-only":
                fail(errors, f"{review_id}.reviewerVerdict must be blocked-or-context-only")
            if allowed != []:
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
        valid_reviews.append(review)

    if seen != set(rows_by_manual_id):
        fail(errors, "manualFulltextFreshReviews must cover exactly every manual extraction row")
    return valid_reviews


def validate_scope(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("reviewLevel") != "c2ltb7-manual-fulltext-fresh-review-v0.1":
        fail(errors, "scope.reviewLevel is invalid")
    eligible = [r for r in reviews if r.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep"]
    blocked = [r for r in reviews if r.get("artifactPromotionDecision") in BLOCKED_PROMOTION_DECISIONS]
    expected = {
        "manualExtractionRowCount": len(reviews),
        "reviewedManualExtractionRowCount": len(reviews),
        "eligibleForArtifactPrepRowCount": len(eligible),
        "blockedOrContextOnlyRowCount": len(blocked),
        "directReviewedArtifactRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    non_claims = "\n".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4))
    for phrase in ("does not create reviewed artifacts", "does not open model admission", "does not authorize"):
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")


def validate_summary(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    reviewed = require_int(summary.get("reviewedManualExtractionRows"), "summary.reviewedManualExtractionRows", errors)
    if reviewed is not None and reviewed != len(reviews):
        fail(errors, "summary.reviewedManualExtractionRows must equal review count")
    eligible = [
        review["manualExtractionId"]
        for review in reviews
        if review.get("artifactPromotionDecision") == "eligible-for-bounded-reviewed-artifact-prep"
    ]
    blocked = [
        review["manualExtractionId"]
        for review in reviews
        if review.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep"
    ]
    if set(eligible) != EXPECTED_ELIGIBLE_ROWS:
        fail(errors, "summary eligible rows must match expected manual/fulltext fresh-review decisions")
    if set(blocked) != EXPECTED_BLOCKED_ROWS:
        fail(errors, "summary blocked rows must match expected manual/fulltext fresh-review decisions")
    if summary.get("eligibleForArtifactPrepRows") != eligible:
        fail(errors, "summary.eligibleForArtifactPrepRows does not match reviews")
    if summary.get("blockedOrContextOnlyRows") != blocked:
        fail(errors, "summary.blockedOrContextOnlyRows does not match reviews")
    if summary.get("directReviewedArtifactsCreated") != 0:
        fail(errors, "summary.directReviewedArtifactsCreated must be 0")
    if summary.get("modelAdmissionDecision") != "blocked":
        fail(errors, "summary.modelAdmissionDecision must be blocked")
    new_facts = "\n".join(require_string_list(summary.get("newFreshReviewFacts"), "summary.newFreshReviewFacts", errors, min_len=4))
    for phrase in ("CDC", "FDA HCT/P", "Donate Life", "RegisterMe", "xenotransplantation", "index"):
        if phrase not in new_facts:
            fail(errors, f"summary.newFreshReviewFacts must include: {phrase}")
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
            fail(errors, f"index file does not reference manual/fulltext fresh-review verdict register: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "manual/fulltext fresh-review verdict register")
    manual_register = load_json(MANUAL_EXTRACTION_PATH, errors, "manual/fulltext extraction register")
    rows_by_manual_id = manual_rows(manual_register, errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        reviews = validate_reviews(register, rows_by_manual_id, errors)
        validate_scope(register, reviews, errors)
        blocked_uses = set(require_string_list(register.get("blockedUses"), "blockedUses", errors))
        if blocked_uses != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        validate_summary(register, reviews, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B7 manual/fulltext fresh-review verdict audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B7 manual/fulltext fresh-review verdict audit ok: reviewed=7 eligible=3 blocked=4 model=blocked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
