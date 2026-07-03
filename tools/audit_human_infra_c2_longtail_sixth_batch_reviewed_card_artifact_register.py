#!/usr/bin/env python3
"""审计 C2-LT-B6 reviewed card artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json"
VERDICT_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-sixth-batch-independent-fresh-review-verdict-register.json"
)
SOURCE_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-source-extraction-register.json"
)
MANUAL_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-sixth-batch-manual-fulltext-extraction-register.json"
)

SCHEMA = "human-infra.c2ltb6-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb6-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-sixth-batch-reviewed-card-artifact-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_sixth_batch_reviewed_card_artifact_register.py"
BATCH_ID = "C2-LT-B6"
ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
ARTIFACT_DECISION = "filled-from-eligible-c2ltb6-fresh-review"
ARTIFACT_STATUS = "filled-reviewed-c2ltb6-artifact-model-blocked"
MODEL_DECISION = "blocked-pending-c2ltb6-reviewed-artifact-gates-and-calibrated-model-validation"

SOURCE_OF_TRUTH_KEYS = {
    "independentFreshReviewVerdictRegister",
    "sourceExtractionRegister",
    "manualFulltextExtractionRegister",
    "sourceResolutionRegister",
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

REQUIRED_BLOCKED_USES = {
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
    "reviewId",
    "sourceExtractionTaskId",
    "manualExtractionId",
    "sourceResolutionId",
    "candidateId",
    "candidateRole",
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
    "freshReviewFinding",
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


def load_rows(
    path: Path,
    key: str,
    id_field: str,
    errors: list[str],
    context: str,
) -> dict[str, dict[str, Any]]:
    data = load_json(path, errors, context)
    rows = data.get(key)
    if not isinstance(rows, list):
        fail(errors, f"{context}.{key} must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"{context}.{key}[{index}] must be an object")
            continue
        row_id = require_string(row.get(id_field), f"{context}.{key}[{index}].{id_field}", errors)
        if row_id in result:
            fail(errors, f"duplicate {id_field}: {row_id}")
        result[row_id] = row
    return result


def evidence_urls(review: dict[str, Any], errors: list[str]) -> list[str]:
    items = review.get("reviewEvidenceTrace")
    if not isinstance(items, list) or not items:
        fail(errors, f"{review.get('reviewId')}.reviewEvidenceTrace must be a non-empty list")
        return []
    urls: list[str] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            fail(errors, f"{review.get('reviewId')}.reviewEvidenceTrace[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{review.get('reviewId')}.reviewEvidenceTrace[{index}].url", errors)
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


def split_reviews(verdict: dict[str, Any], errors: list[str]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], set[str], set[str], set[str]]:
    source_reviews = verdict.get("sourceExtractionFreshReviews")
    manual_reviews = verdict.get("manualFulltextFreshReviews")
    if not isinstance(source_reviews, list):
        fail(errors, "sourceExtractionFreshReviews must be a list")
        source_reviews = []
    if not isinstance(manual_reviews, list):
        fail(errors, "manualFulltextFreshReviews must be a list")
        manual_reviews = []

    source_by_task: dict[str, dict[str, Any]] = {}
    manual_by_id: dict[str, dict[str, Any]] = {}
    for index, review in enumerate(source_reviews):
        if not isinstance(review, dict):
            fail(errors, f"sourceExtractionFreshReviews[{index}] must be an object")
            continue
        task_id = require_string(review.get("originTaskId"), f"sourceReview[{index}].originTaskId", errors)
        source_by_task[task_id] = review
    for index, review in enumerate(manual_reviews):
        if not isinstance(review, dict):
            fail(errors, f"manualFulltextFreshReviews[{index}] must be an object")
            continue
        manual_id = require_string(review.get("manualExtractionId"), f"manualReview[{index}].manualExtractionId", errors)
        manual_by_id[manual_id] = review

    eligible_source = {
        task_id
        for task_id, row in source_by_task.items()
        if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION
    }
    eligible_manual = {
        manual_id
        for manual_id, row in manual_by_id.items()
        if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION
    }
    blocked_manual = set(manual_by_id) - eligible_manual
    return source_by_task, manual_by_id, eligible_source, eligible_manual, blocked_manual


def validate_scope(
    register: dict[str, Any],
    source_reviews: dict[str, dict[str, Any]],
    manual_reviews: dict[str, dict[str, Any]],
    artifacts: list[dict[str, Any]],
    blocked_rows: list[dict[str, Any]],
    errors: list[str],
) -> tuple[set[str], set[str], set[str]]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set(), set(), set()
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("artifactLevel") != "c2ltb6-independent-fresh-review-verdict-to-reviewed-card-artifact":
        fail(errors, "scope.artifactLevel is invalid")

    eligible_source = {
        task_id
        for task_id, row in source_reviews.items()
        if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION
    }
    eligible_manual = {
        manual_id
        for manual_id, row in manual_reviews.items()
        if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION
    }
    blocked_manual = set(manual_reviews) - eligible_manual
    expected = {
        "sourceExtractionFreshReviewRowCount": len(source_reviews),
        "manualFulltextFreshReviewRowCount": len(manual_reviews),
        "eligibleSourceExtractionFreshReviewRowCount": len(eligible_source),
        "eligibleManualFulltextFreshReviewRowCount": len(eligible_manual),
        "blockedManualFulltextFreshReviewRowCount": len(blocked_manual),
        "eligibleFreshReviewRowCount": len(eligible_source) + len(eligible_manual),
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": (len(eligible_source) + len(eligible_manual)) * len(ARTIFACT_TYPES),
        "blockedRowCount": len(blocked_manual),
    }
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    if scope.get("artifactTypes") != ARTIFACT_TYPES:
        fail(errors, "scope.artifactTypes must match required artifact types")
    if len(artifacts) != expected["reviewedArtifactCount"]:
        fail(errors, f"reviewedArtifacts must contain {expected['reviewedArtifactCount']} artifacts")
    if len(blocked_rows) != expected["blockedRowCount"]:
        fail(errors, f"blockedRows must contain {expected['blockedRowCount']} rows")
    text = "\n".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, min_len=4))
    for phrase in ("not model-ready", "does not authorize individual advice", "does not fill rows", "does not mark remaining"):
        if phrase not in text:
            fail(errors, f"scope.nonClaims missing phrase: {phrase}")
    return eligible_source, eligible_manual, blocked_manual


def expected_source_row_kind(artifact: dict[str, Any]) -> str:
    if artifact.get("manualExtractionId") == "not-applicable":
        return "source-extraction-fresh-review-row"
    return "manual-fulltext-fresh-review-row"


def review_for_artifact(
    artifact: dict[str, Any],
    source_reviews: dict[str, dict[str, Any]],
    manual_reviews: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    manual_id = artifact.get("manualExtractionId")
    if manual_id and manual_id != "not-applicable":
        return manual_reviews.get(manual_id, {})
    return source_reviews.get(artifact.get("sourceExtractionTaskId"), {})


def source_row_for_artifact(
    artifact: dict[str, Any],
    source_rows: dict[str, dict[str, Any]],
    manual_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    manual_id = artifact.get("manualExtractionId")
    if manual_id and manual_id != "not-applicable":
        return manual_rows.get(manual_id, {})
    return source_rows.get(artifact.get("sourceExtractionTaskId"), {})


def validate_artifacts(
    artifacts: list[dict[str, Any]],
    eligible_source: set[str],
    eligible_manual: set[str],
    source_reviews: dict[str, dict[str, Any]],
    manual_reviews: dict[str, dict[str, Any]],
    source_rows: dict[str, dict[str, Any]],
    manual_rows: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    seen_ids: set[str] = set()
    pairs: Counter[tuple[str, str]] = Counter()
    eligible_keys = {f"source:{task_id}" for task_id in eligible_source} | {
        f"manual:{manual_id}" for manual_id in eligible_manual
    }
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        missing = BASE_ARTIFACT_FIELDS - set(artifact)
        if missing:
            fail(errors, f"artifact[{index}] missing fields: {sorted(missing)}")
        artifact_id = require_string(artifact.get("artifactId"), f"artifact[{index}].artifactId", errors)
        if artifact_id in seen_ids:
            fail(errors, f"duplicate artifactId: {artifact_id}")
        seen_ids.add(artifact_id)
        artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
        if artifact_type not in ARTIFACT_TYPES:
            fail(errors, f"{artifact_id}.artifactType is invalid")
        if artifact.get("artifactStatus") != ARTIFACT_STATUS:
            fail(errors, f"{artifact_id}.artifactStatus is invalid")
        if artifact.get("sourceRowKind") != expected_source_row_kind(artifact):
            fail(errors, f"{artifact_id}.sourceRowKind is invalid")

        row_key = (
            f"manual:{artifact.get('manualExtractionId')}"
            if artifact.get("manualExtractionId") != "not-applicable"
            else f"source:{artifact.get('sourceExtractionTaskId')}"
        )
        if row_key not in eligible_keys:
            fail(errors, f"{artifact_id} references non-eligible fresh-review row: {row_key}")

        review = review_for_artifact(artifact, source_reviews, manual_reviews)
        source_row = source_row_for_artifact(artifact, source_rows, manual_rows)
        if not review:
            fail(errors, f"{artifact_id} has no matching fresh-review row")
        if not source_row:
            fail(errors, f"{artifact_id} has no matching source/manual extraction row")
        if review:
            for key in ("reviewId", "domainId", "localDomainPath", "sourceTitle", "sourceUrl", "reviewerVerdict"):
                if artifact.get(key) != review.get(key):
                    fail(errors, f"{artifact_id}.{key} does not match fresh-review row")
            if artifact.get("sourceVerdictDecision") != review.get("artifactPromotionDecision"):
                fail(errors, f"{artifact_id}.sourceVerdictDecision must match fresh-review promotion decision")
            if artifact.get("freshReviewEvidenceUrls") != evidence_urls(review, errors):
                fail(errors, f"{artifact_id}.freshReviewEvidenceUrls does not match reviewEvidenceTrace URLs")
            if artifact.get("freshReviewFinding") != review.get("freshReviewFinding"):
                fail(errors, f"{artifact_id}.freshReviewFinding does not match fresh-review row")
        if source_row:
            if artifact.get("registeredExactClaimUse") != source_row.get("exactClaimUse"):
                fail(errors, f"{artifact_id}.registeredExactClaimUse does not match extraction row")
            if artifact.get("registeredTransferBoundary") != source_row.get("transferBoundary"):
                fail(errors, f"{artifact_id}.registeredTransferBoundary does not match extraction row")
        if artifact.get("artifactPromotionDecision") != ARTIFACT_DECISION:
            fail(errors, f"{artifact_id}.artifactPromotionDecision is invalid")
        if artifact.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"{artifact_id}.modelAdmissionDecision is invalid")
        if set(require_string_list(artifact.get("blockedUses"), f"{artifact_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{artifact_id}.blockedUses must match required blocked uses")
        content = artifact.get("content")
        if not isinstance(content, dict):
            fail(errors, f"{artifact_id}.content must be an object")
            continue
        required_content = TYPE_CONTENT_FIELDS.get(artifact_type, set())
        missing_content = required_content - set(content)
        if missing_content:
            fail(errors, f"{artifact_id}.content missing fields: {sorted(missing_content)}")
        pairs[(row_key, artifact_type)] += 1
    for row_key in eligible_keys:
        for artifact_type in ARTIFACT_TYPES:
            if pairs[(row_key, artifact_type)] != 1:
                fail(errors, f"eligible row {row_key} must have exactly one {artifact_type}")


def validate_blocked_rows(
    rows: list[dict[str, Any]],
    blocked_manual: set[str],
    manual_reviews: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"blockedRows[{index}] must be an object")
            continue
        manual_id = require_string(row.get("manualExtractionId"), f"blockedRows[{index}].manualExtractionId", errors)
        if manual_id in seen:
            fail(errors, f"duplicate blocked manualExtractionId: {manual_id}")
        seen.add(manual_id)
        if manual_id not in blocked_manual:
            fail(errors, f"blockedRows[{index}] references non-blocked manual row: {manual_id}")
        review = manual_reviews.get(manual_id, {})
        for key in (
            "reviewId",
            "originTaskId",
            "sourceResolutionId",
            "candidateId",
            "domainId",
            "localDomainPath",
            "sourceTitle",
            "sourceUrl",
            "reviewerVerdict",
            "artifactPromotionDecision",
            "modelAdmissionDecision",
        ):
            if row.get(key) != review.get(key):
                fail(errors, f"blocked row {manual_id}.{key} does not match fresh-review verdict row")
        if set(require_string_list(row.get("blockedUses"), f"blocked row {manual_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"blocked row {manual_id}.blockedUses must match required blocked uses")
        if row.get("freshReviewEvidenceUrls") != evidence_urls(review, errors):
            fail(errors, f"blocked row {manual_id}.freshReviewEvidenceUrls does not match reviewEvidenceTrace URLs")
        require_string(row.get("blockedRowKind"), f"blocked row {manual_id}.blockedRowKind", errors)
        require_string(row.get("blockReason"), f"blocked row {manual_id}.blockReason", errors)
        require_string(row.get("requiredBeforeArtifactFill"), f"blocked row {manual_id}.requiredBeforeArtifactFill", errors)
    if seen != blocked_manual:
        fail(errors, "blockedRows must cover exactly every non-eligible manual fresh-review row")


def validate_summary(register: dict[str, Any], artifacts: list[dict[str, Any]], blocked_rows: list[dict[str, Any]], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    if summary.get("reviewedArtifactsCreated") != len(artifacts):
        fail(errors, "summary.reviewedArtifactsCreated must match artifact count")
    if summary.get("blockedRowsPreserved") != len(blocked_rows):
        fail(errors, "summary.blockedRowsPreserved must match blocked row count")
    if summary.get("modelAdmissionDecision") != MODEL_DECISION:
        fail(errors, "summary.modelAdmissionDecision is invalid")
    counts = summary.get("artifactTypeCounts")
    if not isinstance(counts, dict):
        fail(errors, "summary.artifactTypeCounts must be an object")
    else:
        actual = Counter(
            artifact["artifactType"]
            for artifact in artifacts
            if isinstance(artifact, dict) and "artifactType" in artifact
        )
        if counts != dict(actual):
            fail(errors, "summary.artifactTypeCounts must match reviewedArtifacts")
    for key in ("eligibleSourceExtractionRows", "eligibleManualFulltextRows", "blockedManualFulltextRows"):
        require_string_list(summary.get(key), f"summary.{key}", errors)
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
            fail(errors, f"index file does not reference reviewed artifact register: {relative_path}")
    for relative_path in ("Makefile", "tools/README.md", "tools/AGENTS.md"):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "B6 reviewed artifact register")
    verdict = load_json(VERDICT_PATH, errors, "B6 independent fresh-review verdict register")
    source_rows = load_rows(SOURCE_EXTRACTION_PATH, "extractedRows", "taskId", errors, "source extraction register")
    manual_rows = load_rows(MANUAL_EXTRACTION_PATH, "manualExtractionRows", "manualExtractionId", errors, "manual/fulltext extraction register")
    source_reviews, manual_reviews, _, _, _ = split_reviews(verdict, errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        artifacts = register.get("reviewedArtifacts")
        blocked_rows = register.get("blockedRows")
        if not isinstance(artifacts, list):
            fail(errors, "reviewedArtifacts must be a list")
            artifacts = []
        if not isinstance(blocked_rows, list):
            fail(errors, "blockedRows must be a list")
            blocked_rows = []
        eligible_source, eligible_manual, blocked_manual = validate_scope(
            register, source_reviews, manual_reviews, artifacts, blocked_rows, errors
        )
        validate_artifacts(
            artifacts,
            eligible_source,
            eligible_manual,
            source_reviews,
            manual_reviews,
            source_rows,
            manual_rows,
            errors,
        )
        validate_blocked_rows(blocked_rows, blocked_manual, manual_reviews, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        validate_summary(register, artifacts, blocked_rows, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B6 reviewed artifact audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B6 reviewed artifact audit ok: artifacts=144 blocked=12 model=blocked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
