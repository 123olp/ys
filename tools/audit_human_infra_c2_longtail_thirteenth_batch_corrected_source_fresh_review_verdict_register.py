#!/usr/bin/env python3
"""审计 C2-LT-B13 corrected source fresh-review 判定账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-register.json"
)
REEXTRACTION_REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-register.json"
)

SCHEMA = "human-infra.c2ltb13-corrected-source-fresh-review-verdict-register.v1"
STATUS = "active-c2ltb13-corrected-source-fresh-review-verdict-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-thirteenth-batch-corrected-source-fresh-review-verdict-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_fresh_review_verdict_register.py"
BATCH_ID = "C2-LT-B13"
REVIEW_ID = "C2LTB13-CFRV-001"
TASK_ID = "C2LTB13-CREXT-001"
SOURCE_URL = "https://pubmed.ncbi.nlm.nih.gov/22193141/"
BLOCKED_PRIOR_SOURCE_URL = "https://pubmed.ncbi.nlm.nih.gov/26428404/"

SOURCE_OF_TRUTH_KEYS = {
    "correctedSourceReextractionRegister",
    "correctedSourceReextractionQueue",
    "sourceResolutionRegister",
    "sourceExtractionRegister",
    "evidencePolicy",
    "maturityGapRegister",
}

REQUIRED_REVIEW_FIELDS = {
    "reviewId",
    "batchId",
    "reextractionTaskId",
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

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
    "clinical-advice",
    "skin-care-advice",
    "dermatology-care-advice",
    "wound-care-advice",
    "incontinence-care-advice",
    "product-advice",
}

ALLOWED_ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]

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


def extraction_row(register: dict[str, Any], errors: list[str]) -> dict[str, Any]:
    rows = register.get("extractedRows")
    if not isinstance(rows, list) or len(rows) != 1:
        fail(errors, "corrected re-extraction register must contain exactly one extractedRows item")
        return {}
    row = rows[0]
    if not isinstance(row, dict):
        fail(errors, "corrected re-extraction row must be an object")
        return {}
    if row.get("reextractionTaskId") != TASK_ID:
        fail(errors, f"corrected re-extraction row must be {TASK_ID}")
    return row


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, f"sourceOfTruth must contain exactly {sorted(SOURCE_OF_TRUTH_KEYS)}")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = source.get(key)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_evidence_trace(value: Any, errors: list[str]) -> None:
    if not isinstance(value, list) or len(value) != 3:
        fail(errors, "reviewEvidenceTrace must contain exactly PubMed, ESummary and EFetch evidence")
        return
    text = json.dumps(value, ensure_ascii=False)
    for url_fragment in [
        "pubmed.ncbi.nlm.nih.gov/22193141",
        "esummary.fcgi?db=pubmed&id=22193141",
        "efetch.fcgi?db=pubmed&id=22193141",
    ]:
        if url_fragment not in text:
            fail(errors, f"reviewEvidenceTrace missing {url_fragment}")
    for phrase in [
        "2012",
        "review",
        "10.1097/WON.0b013e31823fe246",
        "research remains limited",
        "additional studies are needed",
    ]:
        if phrase not in text:
            fail(errors, f"reviewEvidenceTrace missing phrase: {phrase}")
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"reviewEvidenceTrace[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"reviewEvidenceTrace[{index}].url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"reviewEvidenceTrace[{index}].url must be https")
        require_string(item.get("evidenceType"), f"reviewEvidenceTrace[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"reviewEvidenceTrace[{index}].finding", errors)


def validate_review(register: dict[str, Any], source_row: dict[str, Any], errors: list[str]) -> list[dict[str, Any]]:
    reviews = register.get("correctedSourceFreshReviews")
    if not isinstance(reviews, list) or len(reviews) != 1:
        fail(errors, "correctedSourceFreshReviews must contain exactly one item")
        return []
    review = reviews[0]
    if not isinstance(review, dict):
        fail(errors, "correctedSourceFreshReviews[0] must be an object")
        return []

    missing = REQUIRED_REVIEW_FIELDS - set(review)
    if missing:
        fail(errors, f"{REVIEW_ID} missing fields: {sorted(missing)}")
    if review.get("reviewId") != REVIEW_ID:
        fail(errors, f"reviewId must be {REVIEW_ID}")
    if review.get("batchId") != BATCH_ID:
        fail(errors, f"batchId must be {BATCH_ID}")
    if review.get("reextractionTaskId") != TASK_ID:
        fail(errors, f"reextractionTaskId must be {TASK_ID}")
    if review.get("sourceUrl") != SOURCE_URL:
        fail(errors, f"sourceUrl must be {SOURCE_URL}")
    if review.get("freshReviewDate") != "2026-07-11":
        fail(errors, "freshReviewDate must be 2026-07-11")
    if review.get("freshReviewMode") != "corrected-source-reextraction-independent-fresh-review":
        fail(errors, "freshReviewMode is invalid")

    for review_key, source_key in {
        "originTaskId": "originTaskId",
        "sourceResolutionId": "sourceResolutionId",
        "domainId": "domainId",
        "localDomainPath": "localDomainPath",
        "candidateId": "candidateId",
        "sourceTitle": "sourceTitle",
        "sourceUrl": "sourceUrl",
    }.items():
        if source_row and review.get(review_key) != source_row.get(source_key):
            fail(errors, f"{REVIEW_ID}.{review_key} does not match corrected re-extraction row")

    if review.get("reviewerVerdict") != "support-with-boundary":
        fail(errors, "reviewerVerdict must be support-with-boundary")
    if review.get("artifactPromotionDecision") != "eligible-for-bounded-reviewed-artifact-prep":
        fail(errors, "artifactPromotionDecision must be eligible for bounded artifact prep")
    if review.get("allowedArtifactTypes") != ALLOWED_ARTIFACT_TYPES:
        fail(errors, "allowedArtifactTypes must contain every bounded reviewed artifact type")
    if review.get("modelAdmissionDecision") != "blocked":
        fail(errors, "modelAdmissionDecision must remain blocked")
    if set(require_string_list(review.get("blockedUses"), "review.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "review.blockedUses must match required blocked uses")
    if review.get("transferBoundaryVerdict") != "transfer-boundary-present-and-required":
        fail(errors, "transferBoundaryVerdict must preserve the boundary")

    review_text = json.dumps(review, ensure_ascii=False)
    required_phrases = [
        "2012",
        "currentness",
        "research remains limited",
        "additional studies",
        "background",
        "moisture exposure",
        "skin-barrier",
        "infection-entry",
        "clinical guidance",
        "product advice",
        "calibrated risk",
        "clinical/product/advice uses",
    ]
    for phrase in required_phrases:
        if phrase not in review_text:
            fail(errors, f"{REVIEW_ID} missing required review boundary phrase: {phrase}")
    for phrase in [
        "clinical-advice",
        "skin-care-advice",
        "dermatology-care-advice",
        "wound-care-advice",
        "incontinence-care-advice",
        "product-advice",
    ]:
        if phrase not in review_text:
            fail(errors, f"{REVIEW_ID} missing blocked-use phrase: {phrase}")
    validate_evidence_trace(review.get("reviewEvidenceTrace"), errors)
    return [review]


def validate_scope(register: dict[str, Any], reviews: list[dict[str, Any]], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "batchId": BATCH_ID,
        "reviewLevel": "c2ltb13-corrected-source-fresh-review-v0.1",
        "correctedExtractionRowCount": 1,
        "reviewedCorrectedExtractionRowCount": len(reviews),
        "eligibleForArtifactPrepRowCount": 1,
        "blockedOrContextOnlyRowCount": 0,
        "directReviewedArtifactRowCount": 0,
        "modelAdmissionOpenedRowCount": 0,
    }
    for key, expected_value in expected.items():
        if isinstance(expected_value, int):
            actual = require_int(scope.get(key), f"scope.{key}", errors)
            if actual is not None and actual != expected_value:
                fail(errors, f"scope.{key} must equal {expected_value}")
        elif scope.get(key) != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    non_claims = "\n".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4))
    for phrase in [
        "does not create reviewed artifacts",
        "does not open model admission",
        "does not authorize clinical advice",
        "does not override currentness",
    ]:
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
    if summary.get("eligibleForArtifactPrepRows") != [TASK_ID]:
        fail(errors, "summary.eligibleForArtifactPrepRows must list only C2LTB13-CREXT-001")
    if summary.get("blockedOrContextOnlyRows") != []:
        fail(errors, "summary.blockedOrContextOnlyRows must be empty")
    if summary.get("directReviewedArtifactsCreated") != 0:
        fail(errors, "summary.directReviewedArtifactsCreated must be 0")
    if summary.get("modelAdmissionDecision") != "blocked":
        fail(errors, "summary.modelAdmissionDecision must remain blocked")
    facts = "\n".join(require_string_list(summary.get("newFreshReviewFacts"), "summary.newFreshReviewFacts", errors, min_len=3))
    for phrase in ["PMID 22193141", "2012 review", "research remains limited", "product selection", "calibrated model"]:
        if phrase not in facts:
            fail(errors, f"summary.newFreshReviewFacts missing phrase: {phrase}")
    next_work = require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)
    for phrase in ["bounded reviewed artifacts", "product advice", "model admission"]:
        if phrase not in next_work:
            fail(errors, f"summary.nextWorkOrder missing phrase: {phrase}")


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
            fail(errors, f"{relative_path} does not reference corrected source fresh-review verdict register")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "B13 corrected source fresh-review verdict register")
    reextraction_register = load_json(REEXTRACTION_REGISTER_PATH, errors, "B13 corrected source re-extraction register")
    source_row = extraction_row(reextraction_register, errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        purpose = require_string(register.get("purpose"), "purpose", errors)
        if "PMID 22193141" not in purpose or "model admission blocked" not in purpose:
            fail(errors, "purpose must name PMID 22193141 and model blocking")
        validate_source_of_truth(register, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "top-level blockedUses must match required blocked uses")
        if set(require_string_list(register.get("verdictTaxonomy"), "verdictTaxonomy", errors)) != {
            "support-with-boundary",
            "blocked-or-context-only",
        }:
            fail(errors, "verdictTaxonomy is invalid")
        if set(require_string_list(register.get("artifactPromotionDecisions"), "artifactPromotionDecisions", errors)) != {
            "eligible-for-bounded-reviewed-artifact-prep",
            "blocked-context-only-no-direct-artifact-fill",
            "blocked-cannot-evaluate",
        }:
            fail(errors, "artifactPromotionDecisions is invalid")
        required_review_fields = set(require_string_list(register.get("requiredReviewFields"), "requiredReviewFields", errors))
        if not required_review_fields.issubset(REQUIRED_REVIEW_FIELDS):
            fail(errors, "requiredReviewFields must be a subset of required review fields")
        reviews = validate_review(register, source_row, errors)
        validate_scope(register, reviews, errors)
        validate_summary(register, reviews, errors)
        validate_index_links(register, errors)

    # Ensure the corrected verdict did not silently erase the original bad source boundary.
    source_resolution = (ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json").read_text(
        encoding="utf-8"
    )
    if BLOCKED_PRIOR_SOURCE_URL not in source_resolution:
        fail(errors, f"source-resolution register must still retain blocked prior source {BLOCKED_PRIOR_SOURCE_URL}")

    if errors:
        print("C2-LT-B13 corrected source fresh-review verdict audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B13 corrected source fresh-review verdict audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
