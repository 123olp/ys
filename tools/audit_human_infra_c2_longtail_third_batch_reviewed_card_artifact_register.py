#!/usr/bin/env python3
"""审计 C2-LT-B3 reviewed card artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json"
ORIGINAL_VERDICT_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-third-batch-independent-fresh-review-verdict-register.json"
)
ORIGINAL_EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-third-batch-source-extraction-register.json"
CORRECTED_VERDICT_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-third-batch-corrected-source-fresh-review-verdict-register.json"
)
CORRECTED_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-third-batch-corrected-source-reextraction-register.json"
)

SCHEMA = "human-infra.c2ltb3-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb3-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-third-batch-reviewed-card-artifact-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_third_batch_reviewed_card_artifact_register.py"
BATCH_ID = "C2-LT-B3"

ORIGINAL_ELIGIBLE_DECISION = "eligible-for-bounded-artifact-fill"
CORRECTED_ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
ORIGINAL_ARTIFACT_DECISION = "filled-from-eligible-original-fresh-review"
CORRECTED_ARTIFACT_DECISION = "filled-from-eligible-corrected-source-fresh-review"
MODEL_DECISION = "blocked-pending-c2ltb3-reviewed-artifact-gates-and-calibrated-model-validation"

SOURCE_OF_TRUTH_KEYS = {
    "originalIndependentFreshReviewVerdictRegister",
    "originalSourceExtractionRegister",
    "correctedSourceFreshReviewVerdictRegister",
    "correctedSourceReextractionRegister",
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

BASE_ARTIFACT_FIELDS = {
    "artifactId",
    "artifactType",
    "artifactStatus",
    "sourceRowKind",
    "domainId",
    "localDomainPath",
    "sourceTitle",
    "sourceUrl",
    "reviewerVerdict",
    "artifactPromotionDecision",
    "sourceVerdictDecision",
    "modelAdmissionDecision",
    "blockedUses",
    "freshReviewEvidenceUrls",
    "registeredExactClaimUse",
    "registeredTransferBoundary",
    "content",
}

ORIGINAL_ARTIFACT_FIELDS = BASE_ARTIFACT_FIELDS | {
    "taskId",
    "sourceRefId",
    "sourceRole",
}

CORRECTED_ARTIFACT_FIELDS = BASE_ARTIFACT_FIELDS | {
    "reextractionTaskId",
    "originTaskId",
    "sourceResolutionId",
    "correctedFreshReviewId",
    "candidateId",
    "sourceAccessStatus",
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


def load_rows(path: Path, key: str, id_field: str, errors: list[str], context: str) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    data = load_json(path, errors, context)
    rows = data.get(key)
    if not isinstance(rows, list):
        fail(errors, f"{context}.{key} must be a list")
        return [], {}
    result_list: list[dict[str, Any]] = []
    result_map: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        row_id = require_string(row.get(id_field), f"{context}.{key}[{index}].{id_field}", errors)
        if row_id:
            result_map[row_id] = row
        result_list.append(row)
    return result_list, result_map


def evidence_urls(items: Any, key: str, context: str, errors: list[str]) -> list[str]:
    if not isinstance(items, list) or not items:
        fail(errors, f"{context}.{key} must be a non-empty list")
        return []
    urls: list[str] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}.{key}[{index}].url", errors)
        if url:
            urls.append(url)
    return urls


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


def validate_scope(
    register: dict[str, Any],
    original_reviews: list[dict[str, Any]],
    corrected_reviews: list[dict[str, Any]],
    artifacts: list[Any],
    blocked_rows: list[Any],
    errors: list[str],
) -> tuple[set[str], set[str], set[str], set[str]]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set(), set(), set(), set()
    original_eligible = {
        row["taskId"]
        for row in original_reviews
        if row.get("artifactPromotionDecision") == ORIGINAL_ELIGIBLE_DECISION
        and isinstance(row.get("taskId"), str)
    }
    original_blocked = {
        row["taskId"]
        for row in original_reviews
        if row.get("artifactPromotionDecision") == "downgrade-before-fill"
        and isinstance(row.get("taskId"), str)
    }
    corrected_eligible = {
        row["reextractionTaskId"]
        for row in corrected_reviews
        if row.get("artifactPromotionDecision") == CORRECTED_ELIGIBLE_DECISION
        and isinstance(row.get("reextractionTaskId"), str)
    }
    corrected_blocked = {
        row["reextractionTaskId"]
        for row in corrected_reviews
        if row.get("artifactPromotionDecision") != CORRECTED_ELIGIBLE_DECISION
        and isinstance(row.get("reextractionTaskId"), str)
    }
    eligible_count = len(original_eligible) + len(corrected_eligible)
    expected = {
        "batchId": BATCH_ID,
        "artifactLevel": "c2ltb3-original-and-corrected-fresh-review-verdict-to-reviewed-card-artifact",
        "originalFreshReviewRowCount": len(original_reviews),
        "eligibleOriginalFreshReviewRowCount": len(original_eligible),
        "sourceResolutionOriginalRowCount": sum(
            1 for row in original_reviews if row.get("artifactPromotionDecision") == "eligible-for-corrected-source-reextraction"
        ),
        "downgradeBeforeFillOriginalRowCount": len(original_blocked),
        "correctedFreshReviewRowCount": len(corrected_reviews),
        "eligibleCorrectedFreshReviewRowCount": len(corrected_eligible),
        "blockedCorrectedFreshReviewRowCount": len(corrected_blocked),
        "eligibleRowCount": eligible_count,
        "blockedRowCount": len(original_blocked) + len(corrected_blocked),
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": eligible_count * len(ARTIFACT_TYPES),
    }
    for key, value in expected.items():
        if scope.get(key) != value:
            fail(errors, f"scope.{key} must equal {value!r}")
    if set(scope.get("artifactTypes", [])) != set(ARTIFACT_TYPES):
        fail(errors, "scope.artifactTypes must match required artifact types")
    if len(artifacts) != expected["reviewedArtifactCount"]:
        fail(errors, f"reviewedArtifacts must contain {expected['reviewedArtifactCount']} artifacts")
    if len(blocked_rows) != expected["blockedRowCount"]:
        fail(errors, f"blockedRows must contain {expected['blockedRowCount']} rows")
    for field in ["selectionRule", "blockedRowRule", "artifactStatusRule", "modelAdmissionRule"]:
        require_string(scope.get(field), f"scope.{field}", errors)
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4))
    for phrase in ["not model-ready", "does not authorize individual advice", "does not fill rows", "does not mark the remaining C2"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")
    return original_eligible, original_blocked, corrected_eligible, corrected_blocked


def validate_content(content: Any, artifact_id: str, artifact_type: str, errors: list[str]) -> None:
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
                else:
                    fail(errors, f"{context}[{index}] must be a string or object")
        elif isinstance(value, dict):
            if not value:
                fail(errors, f"{context} must be a non-empty object")
        else:
            fail(errors, f"{context} must be string, list or object")


def validate_original_artifact(
    artifact: dict[str, Any],
    review: dict[str, Any],
    extraction: dict[str, Any],
    artifact_id: str,
    errors: list[str],
) -> None:
    missing = ORIGINAL_ARTIFACT_FIELDS - set(artifact)
    if missing:
        fail(errors, f"{artifact_id} missing original fields: {sorted(missing)}")
    for field in ["domainId", "localDomainPath", "sourceRefId", "sourceTitle", "sourceUrl"]:
        if artifact.get(field) != extraction.get(field):
            fail(errors, f"{artifact_id}.{field} must match original extraction row")
    if artifact.get("sourceRole") != review.get("registeredSourceRole"):
        fail(errors, f"{artifact_id}.sourceRole must match original fresh-review role")
    if artifact.get("sourceVerdictDecision") != ORIGINAL_ELIGIBLE_DECISION:
        fail(errors, f"{artifact_id}.sourceVerdictDecision must preserve original eligible verdict")
    if artifact.get("artifactPromotionDecision") != ORIGINAL_ARTIFACT_DECISION:
        fail(errors, f"{artifact_id}.artifactPromotionDecision must be {ORIGINAL_ARTIFACT_DECISION}")
    if artifact.get("registeredExactClaimUse") != review.get("registeredExactClaimUse"):
        fail(errors, f"{artifact_id}.registeredExactClaimUse must match original fresh review")
    if artifact.get("registeredTransferBoundary") != review.get("registeredTransferBoundary"):
        fail(errors, f"{artifact_id}.registeredTransferBoundary must match original fresh review")
    if sorted(artifact.get("freshReviewEvidenceUrls", [])) != sorted(
        evidence_urls(review.get("freshReviewEvidence"), "freshReviewEvidence", artifact_id, errors)
    ):
        fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must match original fresh-review evidence")


def validate_corrected_artifact(
    artifact: dict[str, Any],
    review: dict[str, Any],
    extraction: dict[str, Any],
    artifact_id: str,
    errors: list[str],
) -> None:
    missing = CORRECTED_ARTIFACT_FIELDS - set(artifact)
    if missing:
        fail(errors, f"{artifact_id} missing corrected fields: {sorted(missing)}")
    for artifact_field, review_field in {
        "originTaskId": "originTaskId",
        "sourceResolutionId": "sourceResolutionId",
        "correctedFreshReviewId": "reviewId",
        "domainId": "domainId",
        "localDomainPath": "localDomainPath",
        "candidateId": "candidateId",
        "sourceTitle": "sourceTitle",
        "sourceUrl": "sourceUrl",
    }.items():
        if artifact.get(artifact_field) != review.get(review_field):
            fail(errors, f"{artifact_id}.{artifact_field} must match corrected fresh-review row")
    if artifact.get("sourceAccessStatus") != extraction.get("sourceAccessStatus"):
        fail(errors, f"{artifact_id}.sourceAccessStatus must match corrected extraction row")
    if artifact.get("sourceVerdictDecision") != CORRECTED_ELIGIBLE_DECISION:
        fail(errors, f"{artifact_id}.sourceVerdictDecision must preserve corrected eligible verdict")
    if artifact.get("artifactPromotionDecision") != CORRECTED_ARTIFACT_DECISION:
        fail(errors, f"{artifact_id}.artifactPromotionDecision must be {CORRECTED_ARTIFACT_DECISION}")
    if artifact.get("registeredExactClaimUse") != extraction.get("exactClaimUse"):
        fail(errors, f"{artifact_id}.registeredExactClaimUse must match corrected extraction exactClaimUse")
    if artifact.get("registeredTransferBoundary") != extraction.get("transferBoundary"):
        fail(errors, f"{artifact_id}.registeredTransferBoundary must match corrected extraction transferBoundary")
    if sorted(artifact.get("freshReviewEvidenceUrls", [])) != sorted(
        evidence_urls(review.get("reviewEvidenceTrace"), "reviewEvidenceTrace", artifact_id, errors)
    ):
        fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must match corrected fresh-review evidence")


def validate_artifacts(
    register: dict[str, Any],
    original_reviews: dict[str, dict[str, Any]],
    original_extractions: dict[str, dict[str, Any]],
    corrected_reviews: dict[str, dict[str, Any]],
    corrected_extractions: dict[str, dict[str, Any]],
    original_eligible: set[str],
    corrected_eligible: set[str],
    errors: list[str],
) -> tuple[int, int]:
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(artifacts, list):
        fail(errors, "reviewedArtifacts must be a list")
        return 0, 0
    seen_ids: set[str] = set()
    seen_pairs: set[tuple[str, str, str]] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        artifact_id = require_string(artifact.get("artifactId"), f"reviewedArtifacts[{index}].artifactId", errors)
        artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
        row_kind = require_string(artifact.get("sourceRowKind"), f"{artifact_id}.sourceRowKind", errors)
        if artifact_id in seen_ids:
            fail(errors, f"duplicate artifactId: {artifact_id}")
        seen_ids.add(artifact_id)
        if artifact_type not in ARTIFACT_TYPES:
            fail(errors, f"{artifact_id}.artifactType is invalid")
            continue
        if artifact.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"{artifact_id}.modelAdmissionDecision must remain blocked")
        if set(artifact.get("blockedUses", [])) != BLOCKED_USES:
            fail(errors, f"{artifact_id}.blockedUses must match required blocked uses")
        if artifact.get("reviewerVerdict") is None:
            fail(errors, f"{artifact_id}.reviewerVerdict is required")
        validate_content(artifact.get("content"), artifact_id, artifact_type, errors)

        if row_kind == "original-fresh-review-row":
            task_id = require_string(artifact.get("taskId"), f"{artifact_id}.taskId", errors)
            if task_id not in original_eligible:
                fail(errors, f"{artifact_id} is attached to non-eligible original row {task_id}")
            pair = (row_kind, task_id, artifact_type)
            review = original_reviews.get(task_id, {})
            extraction = original_extractions.get(task_id, {})
            if artifact.get("reviewerVerdict") != review.get("reviewerVerdict"):
                fail(errors, f"{artifact_id}.reviewerVerdict must match original fresh-review row")
            validate_original_artifact(artifact, review, extraction, artifact_id, errors)
        elif row_kind == "corrected-source-fresh-review-row":
            task_id = require_string(artifact.get("reextractionTaskId"), f"{artifact_id}.reextractionTaskId", errors)
            if task_id not in corrected_eligible:
                fail(errors, f"{artifact_id} is attached to non-eligible corrected row {task_id}")
            pair = (row_kind, task_id, artifact_type)
            review = corrected_reviews.get(task_id, {})
            extraction = corrected_extractions.get(task_id, {})
            if artifact.get("reviewerVerdict") != review.get("reviewerVerdict"):
                fail(errors, f"{artifact_id}.reviewerVerdict must match corrected fresh-review row")
            validate_corrected_artifact(artifact, review, extraction, artifact_id, errors)
        else:
            fail(errors, f"{artifact_id}.sourceRowKind is invalid")
            continue
        if pair in seen_pairs:
            fail(errors, f"duplicate artifact pair: {pair}")
        seen_pairs.add(pair)

    expected_pairs = {
        ("original-fresh-review-row", task_id, artifact_type)
        for task_id in original_eligible
        for artifact_type in ARTIFACT_TYPES
    } | {
        ("corrected-source-fresh-review-row", task_id, artifact_type)
        for task_id in corrected_eligible
        for artifact_type in ARTIFACT_TYPES
    }
    if seen_pairs != expected_pairs:
        fail(errors, "reviewedArtifacts must contain exactly one artifact of each type for every eligible original and corrected row")
    return len(seen_pairs), len(seen_ids)


def validate_blocked_rows(
    register: dict[str, Any],
    original_reviews: dict[str, dict[str, Any]],
    corrected_reviews: dict[str, dict[str, Any]],
    original_blocked: set[str],
    corrected_blocked: set[str],
    errors: list[str],
) -> None:
    rows = register.get("blockedRows")
    if not isinstance(rows, list):
        fail(errors, "blockedRows must be a list")
        return
    seen_original: set[str] = set()
    seen_corrected: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"blockedRows[{index}] must be an object")
            continue
        row_kind = require_string(row.get("blockedRowKind"), f"blockedRows[{index}].blockedRowKind", errors)
        if set(row.get("blockedUses", [])) != BLOCKED_USES:
            fail(errors, f"blockedRows[{index}].blockedUses must match required blocked uses")
        require_string(row.get("blockReason"), f"blockedRows[{index}].blockReason", errors)
        require_string(row.get("nextAction"), f"blockedRows[{index}].nextAction", errors)
        if "blocked" not in str(row.get("modelAdmissionDecision", "")):
            fail(errors, f"blockedRows[{index}].modelAdmissionDecision must remain blocked")
        if row_kind == "original-downgrade-before-fill":
            task_id = require_string(row.get("taskId"), f"blockedRows[{index}].taskId", errors)
            seen_original.add(task_id)
            review = original_reviews.get(task_id, {})
            if task_id not in original_blocked:
                fail(errors, f"blockedRows[{index}] is not an original downgrade-before-fill row")
            for field in ["domainId", "reviewerVerdict", "artifactPromotionDecision"]:
                if row.get(field) != review.get(field):
                    fail(errors, f"blockedRows[{index}].{field} must match original fresh-review row")
        elif row_kind == "corrected-duplicate-split-route":
            task_id = require_string(row.get("reextractionTaskId"), f"blockedRows[{index}].reextractionTaskId", errors)
            seen_corrected.add(task_id)
            review = corrected_reviews.get(task_id, {})
            if task_id not in corrected_blocked:
                fail(errors, f"blockedRows[{index}] is not a corrected blocked row")
            for row_field, review_field in {
                "reviewId": "reviewId",
                "originTaskId": "originTaskId",
                "sourceResolutionId": "sourceResolutionId",
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
        else:
            fail(errors, f"blockedRows[{index}].blockedRowKind is invalid")
    if seen_original != original_blocked:
        fail(errors, "blockedRows must preserve every original downgrade-before-fill row")
    if seen_corrected != corrected_blocked:
        fail(errors, "blockedRows must preserve every corrected blocked row")


def validate_indexes(register: dict[str, Any], errors: list[str]) -> None:
    paths = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if set(paths) != set(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must contain every required index file")
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements entry {relative_path}", errors)
        if target and REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {REGISTER_LINK}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        target = repo_path(relative_path, f"script index {relative_path}", errors)
        if target and SCRIPT_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {SCRIPT_LINK}")


def validate_summary(
    register: dict[str, Any],
    original_reviews: list[dict[str, Any]],
    corrected_reviews: list[dict[str, Any]],
    original_eligible: set[str],
    original_blocked: set[str],
    corrected_eligible: set[str],
    corrected_blocked: set[str],
    errors: list[str],
) -> None:
    summary = register.get("summary")
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if not isinstance(artifacts, list):
        artifacts = []
    type_counts = Counter(artifact.get("artifactType") for artifact in artifacts if isinstance(artifact, dict))
    expected_counts = {artifact_type: len(original_eligible) + len(corrected_eligible) for artifact_type in ARTIFACT_TYPES}
    checks = {
        "originalReviewerVerdictCounts": dict(Counter(row.get("reviewerVerdict") for row in original_reviews)),
        "originalArtifactPromotionDecisionCounts": dict(Counter(row.get("artifactPromotionDecision") for row in original_reviews)),
        "correctedReviewerVerdictCounts": dict(Counter(row.get("reviewerVerdict") for row in corrected_reviews)),
        "correctedArtifactPromotionDecisionCounts": dict(Counter(row.get("artifactPromotionDecision") for row in corrected_reviews)),
        "eligibleOriginalRows": sorted(original_eligible),
        "eligibleCorrectedRows": sorted(corrected_eligible),
        "blockedOriginalRows": sorted(original_blocked),
        "blockedCorrectedRows": sorted(corrected_blocked),
        "artifactTypeCounts": expected_counts,
        "reviewedArtifactsCreated": len(artifacts),
        "blockedRowsPreserved": len(original_blocked) + len(corrected_blocked),
        "modelAdmissionDecision": MODEL_DECISION,
    }
    for key, expected in checks.items():
        if summary.get(key) != expected:
            fail(errors, f"summary.{key} must match expected value")
    if type_counts != Counter(expected_counts):
        fail(errors, "reviewedArtifacts type counts must match summary artifactTypeCounts")
    require_string(summary.get("nextWorkOrder"), "summary.nextWorkOrder", errors)


def validate_register(errors: list[str]) -> tuple[int, int]:
    register = load_json(REGISTER_PATH, errors, "C2-LT-B3 reviewed card artifact register")
    original_review_rows, original_reviews = load_rows(
        ORIGINAL_VERDICT_PATH,
        "sourceTaskFreshReviews",
        "taskId",
        errors,
        "original independent fresh-review verdict register",
    )
    _, original_extractions = load_rows(
        ORIGINAL_EXTRACTION_PATH,
        "extractedRows",
        "taskId",
        errors,
        "original source extraction register",
    )
    corrected_review_rows, corrected_reviews = load_rows(
        CORRECTED_VERDICT_PATH,
        "correctedSourceFreshReviews",
        "reextractionTaskId",
        errors,
        "corrected source fresh-review verdict register",
    )
    _, corrected_extractions = load_rows(
        CORRECTED_EXTRACTION_PATH,
        "extractedRows",
        "reextractionTaskId",
        errors,
        "corrected source re-extraction register",
    )
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
    original_eligible, original_blocked, corrected_eligible, corrected_blocked = validate_scope(
        register,
        original_review_rows,
        corrected_review_rows,
        artifacts,
        blocked_rows,
        errors,
    )
    pair_count, artifact_count = validate_artifacts(
        register,
        original_reviews,
        original_extractions,
        corrected_reviews,
        corrected_extractions,
        original_eligible,
        corrected_eligible,
        errors,
    )
    validate_blocked_rows(register, original_reviews, corrected_reviews, original_blocked, corrected_blocked, errors)
    validate_indexes(register, errors)
    validate_summary(
        register,
        original_review_rows,
        corrected_review_rows,
        original_eligible,
        original_blocked,
        corrected_eligible,
        corrected_blocked,
        errors,
    )
    return pair_count, artifact_count


def main() -> int:
    errors: list[str] = []
    pair_count, artifact_count = validate_register(errors)
    if errors:
        print("C2-LT-B3 reviewed card artifact audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"C2-LT-B3 reviewed card artifact audit ok: artifacts={artifact_count} task_type_pairs={pair_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
