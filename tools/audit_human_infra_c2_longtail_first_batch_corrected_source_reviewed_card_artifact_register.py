#!/usr/bin/env python3
"""审计 C2-LT-B1 corrected source reviewed artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json"
)
FRESH_REVIEW_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-fresh-review-verdict-register.json"
)
REEXTRACTION_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json"
)

SCHEMA = "human-infra.c2ltb1-corrected-source-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb1-corrected-source-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-corrected-source-reviewed-card-artifact-register.json"
SCRIPT_LINK = (
    "audit_human_infra_c2_longtail_first_batch_corrected_source_reviewed_card_artifact_register.py"
)
BATCH_ID = "C2-LT-B1"
ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
ARTIFACT_STATUS = "filled-reviewed-c2ltb1-corrected-source-artifact-model-blocked"
MODEL_ADMISSION_DECISION = "blocked-pending-corrected-source-reviewed-artifact-gates-and-calibrated-model-validation"
ARTIFACT_PROMOTION_DECISION = "filled-from-eligible-corrected-source-fresh-review"

SOURCE_OF_TRUTH_KEYS = {
    "correctedSourceFreshReviewVerdictRegister",
    "correctedSourceReextractionRegister",
    "correctedSourceReextractionQueue",
    "originalReviewedCardArtifactRegister",
    "evidencePolicy",
    "maturityGapRegister",
}

ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]

BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}

REQUIRED_ARTIFACT_FIELDS = {
    "artifactId",
    "artifactType",
    "artifactStatus",
    "reextractionTaskId",
    "originTaskId",
    "sourceResolutionReviewId",
    "correctedFreshReviewId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "sourceTitle",
    "sourceUrl",
    "sourceAccessStatus",
    "reviewerVerdict",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
    "freshReviewEvidenceUrls",
    "registeredExactClaimUse",
    "registeredTransferBoundary",
    "content",
}

TYPE_CONTENT_FIELDS = {
    "reviewed-source-card": {
        "sourceIdentity",
        "sourceRole",
        "exactClaimUse",
        "transferBoundary",
        "freshReviewEvidence",
        "reviewerNote",
    },
    "reviewed-variable-card": {
        "variableQuestion",
        "variableSeed",
        "sourceExtractedVariables",
        "modelPosition",
        "admissibleUse",
        "promotionBoundary",
    },
    "reviewed-endpoint-card": {
        "endpointQuestion",
        "endpointDefinition",
        "populationOrSetting",
        "endpointBoundary",
        "modelPosition",
        "blockedEndpointUses",
    },
    "reviewed-uncertainty-card": {
        "uncertaintyQuestion",
        "uncertaintyOrBias",
        "uncertaintyBoundaryVerdict",
        "evidenceLimit",
        "downgradeTriggers",
    },
    "reviewed-transfer-boundary-card": {
        "transferBoundaryQuestion",
        "domainTransferVerdict",
        "registeredTransferBoundary",
        "sourceExtractionTransferBoundary",
        "blockedTransferUses",
    },
    "reviewed-downgrade-check": {
        "downgradeQuestion",
        "downgradeVerdict",
        "reviewerVerdict",
        "downgradeRequiredWhen",
        "blockedSiblingPolicy",
    },
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


def validate_source_of_truth(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def load_review_rows(errors: list[str]) -> list[dict[str, Any]]:
    data = load_json(FRESH_REVIEW_PATH, errors, "corrected source fresh-review verdict register")
    rows = data.get("correctedSourceFreshReviews")
    if not isinstance(rows, list):
        fail(errors, "corrected source fresh-review verdict register must contain correctedSourceFreshReviews")
        return []
    result: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"correctedSourceFreshReviews[{index}] must be an object")
            continue
        result.append(row)
    return result


def load_extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(REEXTRACTION_PATH, errors, "corrected source re-extraction register")
    rows = data.get("extractedRows")
    if not isinstance(rows, list):
        fail(errors, "corrected source re-extraction register must contain extractedRows")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("reextractionTaskId"), f"extractedRows[{index}].reextractionTaskId", errors)
        if task_id:
            result[task_id] = row
    return result


def evidence_urls(review: dict[str, Any], context: str, errors: list[str]) -> list[str]:
    trace = review.get("reviewEvidenceTrace")
    if not isinstance(trace, list) or not trace:
        fail(errors, f"{context}.reviewEvidenceTrace must be a non-empty list")
        return []
    urls: list[str] = []
    for index, item in enumerate(trace):
        if not isinstance(item, dict):
            fail(errors, f"{context}.reviewEvidenceTrace[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}.reviewEvidenceTrace[{index}].url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}.reviewEvidenceTrace[{index}].url must be https")
        if url:
            urls.append(url)
    return urls


def validate_scope(
    register: dict[str, Any],
    reviews: list[dict[str, Any]],
    artifacts: list[Any],
    blocked_rows: list[Any],
    errors: list[str],
) -> tuple[set[str], set[str]]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set(), set()
    eligible = {
        row["reextractionTaskId"]
        for row in reviews
        if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION
        and isinstance(row.get("reextractionTaskId"), str)
    }
    blocked = {
        row["reextractionTaskId"]
        for row in reviews
        if row.get("artifactPromotionDecision") != ELIGIBLE_DECISION
        and isinstance(row.get("reextractionTaskId"), str)
    }
    expected = {
        "batchId": BATCH_ID,
        "artifactLevel": "c2ltb1-corrected-source-fresh-review-verdict-to-reviewed-card-artifact",
        "correctedFreshReviewRowCount": len(reviews),
        "eligibleCorrectedFreshReviewRowCount": len(eligible),
        "blockedCorrectedFreshReviewRowCount": len(blocked),
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": len(eligible) * len(ARTIFACT_TYPES),
    }
    for key, value in expected.items():
        if scope.get(key) != value:
            fail(errors, f"scope.{key} must equal {value!r}")
    if set(scope.get("artifactTypes", [])) != set(ARTIFACT_TYPES):
        fail(errors, "scope.artifactTypes must match required artifact types")
    if len(artifacts) != expected["reviewedArtifactCount"]:
        fail(errors, f"reviewedArtifacts must contain {expected['reviewedArtifactCount']} artifacts")
    if len(blocked_rows) != len(blocked):
        fail(errors, f"blockedRows must contain {len(blocked)} rows")
    for field in ["selectionRule", "blockedRowRule", "artifactStatusRule", "modelAdmissionRule"]:
        require_string(scope.get(field), f"scope.{field}", errors)
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4))
    for phrase in ["not model-ready", "does not authorize individual advice", "does not fill rows", "does not mark the remaining C2"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")
    return eligible, blocked


def validate_content(content: Any, artifact_id: str, artifact_type: str, extraction: dict[str, Any], errors: list[str]) -> None:
    if not isinstance(content, dict):
        fail(errors, f"{artifact_id}.content must be an object")
        return
    expected = TYPE_CONTENT_FIELDS[artifact_type]
    if set(content) != expected:
        fail(errors, f"{artifact_id}.content must contain exact fields for {artifact_type}")
    for key, value in content.items():
        context = f"{artifact_id}.content.{key}"
        if isinstance(value, str):
            require_string(value, context, errors)
        elif isinstance(value, list):
            if not value:
                fail(errors, f"{context} must be a non-empty list")
            for index, item in enumerate(value):
                if isinstance(item, str):
                    require_string(item, f"{context}[{index}]", errors)
                elif isinstance(item, dict):
                    if not item:
                        fail(errors, f"{context}[{index}] must be a non-empty object")
                    for item_key, item_value in item.items():
                        if isinstance(item_value, str):
                            require_string(item_value, f"{context}[{index}].{item_key}", errors)
                else:
                    fail(errors, f"{context}[{index}] must be a string or object")
        elif isinstance(value, dict):
            if not value:
                fail(errors, f"{context} must be a non-empty object")
        else:
            fail(errors, f"{context} must be string, list or object")
    if artifact_type == "reviewed-variable-card":
        extracted = content.get("sourceExtractedVariables")
        expected_variables = extraction.get("modelPosition", {}).get("variables")
        if extracted != expected_variables:
            fail(errors, f"{artifact_id}.content.sourceExtractedVariables must match extraction modelPosition.variables")


def validate_artifacts(
    register: dict[str, Any],
    reviews_by_task: dict[str, dict[str, Any]],
    extractions_by_task: dict[str, dict[str, Any]],
    eligible: set[str],
    errors: list[str],
) -> tuple[int, int]:
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(artifacts, list):
        fail(errors, "reviewedArtifacts must be a list")
        return 0, 0

    seen_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        missing = REQUIRED_ARTIFACT_FIELDS - set(artifact)
        if missing:
            fail(errors, f"reviewedArtifacts[{index}] missing fields: {sorted(missing)}")
        artifact_id = require_string(artifact.get("artifactId"), f"reviewedArtifacts[{index}].artifactId", errors)
        artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
        task_id = require_string(artifact.get("reextractionTaskId"), f"{artifact_id}.reextractionTaskId", errors)
        if artifact_id in seen_ids:
            fail(errors, f"duplicate artifactId: {artifact_id}")
        seen_ids.add(artifact_id)
        if artifact_type not in ARTIFACT_TYPES:
            fail(errors, f"{artifact_id}.artifactType is invalid")
            continue
        if task_id not in eligible:
            fail(errors, f"{artifact_id} is attached to non-eligible corrected row {task_id}")
        pair = (task_id, artifact_type)
        if pair in seen_pairs:
            fail(errors, f"duplicate artifact type for corrected row: {task_id} {artifact_type}")
        seen_pairs.add(pair)

        review = reviews_by_task.get(task_id, {})
        extraction = extractions_by_task.get(task_id, {})
        for artifact_field, review_field in {
            "originTaskId": "originTaskId",
            "sourceResolutionReviewId": "sourceResolutionReviewId",
            "correctedFreshReviewId": "reviewId",
            "domainId": "domainId",
            "localDomainPath": "localDomainPath",
            "candidateId": "candidateId",
            "sourceTitle": "sourceTitle",
            "sourceUrl": "sourceUrl",
            "reviewerVerdict": "reviewerVerdict",
        }.items():
            if artifact.get(artifact_field) != review.get(review_field):
                fail(errors, f"{artifact_id}.{artifact_field} must match corrected fresh-review row")
        if review.get("artifactPromotionDecision") != ELIGIBLE_DECISION:
            fail(errors, f"{artifact_id} must originate from an eligible corrected fresh-review row")
        if artifact.get("artifactPromotionDecision") != ARTIFACT_PROMOTION_DECISION:
            fail(errors, f"{artifact_id}.artifactPromotionDecision must be {ARTIFACT_PROMOTION_DECISION}")
        if artifact.get("sourceAccessStatus") != extraction.get("sourceAccessStatus"):
            fail(errors, f"{artifact_id}.sourceAccessStatus must match corrected extraction row")
        if artifact.get("artifactStatus") != ARTIFACT_STATUS:
            fail(errors, f"{artifact_id}.artifactStatus must be {ARTIFACT_STATUS}")
        if artifact.get("modelAdmissionDecision") != MODEL_ADMISSION_DECISION:
            fail(errors, f"{artifact_id}.modelAdmissionDecision must remain blocked")
        if set(artifact.get("blockedUses", [])) != BLOCKED_USES:
            fail(errors, f"{artifact_id}.blockedUses must match required blocked uses")
        if sorted(artifact.get("freshReviewEvidenceUrls", [])) != sorted(evidence_urls(review, artifact_id, errors)):
            fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must match review evidence trace")
        if artifact.get("registeredExactClaimUse") != extraction.get("exactClaimUse"):
            fail(errors, f"{artifact_id}.registeredExactClaimUse must match corrected extraction exactClaimUse")
        if artifact.get("registeredTransferBoundary") != extraction.get("transferBoundary"):
            fail(errors, f"{artifact_id}.registeredTransferBoundary must match corrected extraction transferBoundary")
        validate_content(artifact.get("content"), artifact_id, artifact_type, extraction, errors)

    expected_pairs = {(task_id, artifact_type) for task_id in eligible for artifact_type in ARTIFACT_TYPES}
    if seen_pairs != expected_pairs:
        fail(errors, "reviewedArtifacts must contain exactly one artifact of each type for every eligible corrected row")
    return len(seen_pairs), len(seen_ids)


def validate_blocked_rows(
    register: dict[str, Any],
    reviews_by_task: dict[str, dict[str, Any]],
    blocked: set[str],
    errors: list[str],
) -> None:
    rows = register.get("blockedRows")
    if not isinstance(rows, list):
        fail(errors, "blockedRows must be a list")
        return
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"blockedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("reextractionTaskId"), f"blockedRows[{index}].reextractionTaskId", errors)
        seen.add(task_id)
        review = reviews_by_task.get(task_id, {})
        if task_id not in blocked:
            fail(errors, f"blockedRows[{index}] is not a blocked corrected fresh-review row")
        for row_field, review_field in {
            "reviewId": "reviewId",
            "originTaskId": "originTaskId",
            "sourceResolutionReviewId": "sourceResolutionReviewId",
            "domainId": "domainId",
            "localDomainPath": "localDomainPath",
            "candidateId": "candidateId",
            "sourceTitle": "sourceTitle",
            "sourceUrl": "sourceUrl",
            "reviewerVerdict": "reviewerVerdict",
            "artifactPromotionDecision": "artifactPromotionDecision",
        }.items():
            if row.get(row_field) != review.get(review_field):
                fail(errors, f"blockedRows[{index}].{row_field} must match corrected fresh-review row")
        if row.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"blockedRows[{index}].modelAdmissionDecision must remain blocked")
        if set(row.get("blockedUses", [])) != BLOCKED_USES:
            fail(errors, f"blockedRows[{index}].blockedUses must match required blocked uses")
        require_string(row.get("blockReason"), f"blockedRows[{index}].blockReason", errors)
        require_string(row.get("nextAction"), f"blockedRows[{index}].nextAction", errors)
    if seen != blocked:
        fail(errors, "blockedRows must match every non-eligible corrected fresh-review row")


def validate_indexes(register: dict[str, Any], errors: list[str]) -> None:
    paths = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if set(paths) != set(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must contain every required index file")
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements entry {relative_path}", errors)
        if not target:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"{relative_path} must reference {REGISTER_LINK}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        target = repo_path(relative_path, f"script index {relative_path}", errors)
        if target and SCRIPT_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {SCRIPT_LINK}")


def validate_summary(register: dict[str, Any], eligible: set[str], blocked: set[str], errors: list[str]) -> None:
    summary = register.get("summary")
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if not isinstance(artifacts, list):
        artifacts = []
    type_counts = Counter(artifact.get("artifactType") for artifact in artifacts if isinstance(artifact, dict))
    expected_counts = {artifact_type: len(eligible) for artifact_type in ARTIFACT_TYPES}
    if summary.get("eligibleCorrectedRows") != sorted(eligible):
        fail(errors, "summary.eligibleCorrectedRows must match eligible corrected rows")
    if summary.get("blockedCorrectedRows") != sorted(blocked):
        fail(errors, "summary.blockedCorrectedRows must match blocked corrected rows")
    if summary.get("artifactTypeCounts") != expected_counts:
        fail(errors, "summary.artifactTypeCounts must match artifact counts")
    if type_counts != Counter(expected_counts):
        fail(errors, "reviewedArtifacts type counts must match expected artifact counts")
    if summary.get("reviewedArtifactsCreated") != len(artifacts):
        fail(errors, "summary.reviewedArtifactsCreated must equal reviewedArtifacts length")
    if summary.get("blockedRowsPreserved") != len(blocked):
        fail(errors, "summary.blockedRowsPreserved must match blocked rows")
    if summary.get("modelAdmissionDecision") != MODEL_ADMISSION_DECISION:
        fail(errors, "summary.modelAdmissionDecision must remain blocked")
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def validate_register(errors: list[str]) -> tuple[int, int]:
    register = load_json(REGISTER_PATH, errors, "C2-LT-B1 corrected source reviewed card artifact register")
    reviews = load_review_rows(errors)
    extractions_by_task = load_extraction_rows(errors)
    reviews_by_task = {
        row["reextractionTaskId"]: row
        for row in reviews
        if isinstance(row.get("reextractionTaskId"), str)
    }
    if not register:
        return 0, 0

    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    validate_source_of_truth(register, errors)
    if set(register.get("blockedUses", [])) != BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")

    artifacts = register.get("reviewedArtifacts") if isinstance(register.get("reviewedArtifacts"), list) else []
    blocked_rows = register.get("blockedRows") if isinstance(register.get("blockedRows"), list) else []
    eligible, blocked = validate_scope(register, reviews, artifacts, blocked_rows, errors)
    pair_count, artifact_count = validate_artifacts(register, reviews_by_task, extractions_by_task, eligible, errors)
    validate_blocked_rows(register, reviews_by_task, blocked, errors)
    validate_indexes(register, errors)
    validate_summary(register, eligible, blocked, errors)
    return pair_count, artifact_count


def main() -> int:
    errors: list[str] = []
    pair_count, artifact_count = validate_register(errors)
    if errors:
        print("C2-LT-B1 corrected source reviewed artifact audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "C2-LT-B1 corrected source reviewed artifact audit ok: "
        f"artifacts={artifact_count} task_type_pairs={pair_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
