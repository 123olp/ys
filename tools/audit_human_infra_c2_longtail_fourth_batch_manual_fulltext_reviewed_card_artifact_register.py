#!/usr/bin/env python3
"""审计 C2-LT-B4 manual/fulltext reviewed artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json"
)
VERDICT_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-fresh-review-verdict-register.json"
)
MANUAL_EXTRACTION_PATH = (
    ROOT / "docs/reference/human-infra-c2-longtail-fourth-batch-manual-fulltext-extraction-register.json"
)

SCHEMA = "human-infra.c2ltb4-manual-fulltext-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb4-manual-fulltext-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-fourth-batch-manual-fulltext-reviewed-card-artifact-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_fourth_batch_manual_fulltext_reviewed_card_artifact_register.py"
BATCH_ID = "C2-LT-B4"
ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
ARTIFACT_DECISION = "filled-from-eligible-manual-fulltext-fresh-review"
MODEL_DECISION = "blocked-pending-c2ltb4-reviewed-artifact-gates-and-calibrated-model-validation"

SOURCE_OF_TRUTH_KEYS = {
    "manualFulltextFreshReviewVerdictRegister",
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
    "manualExtractionId",
    "originTaskId",
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


def load_rows(path: Path, key: str, id_field: str, errors: list[str], context: str) -> dict[str, dict[str, Any]]:
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


def validate_scope(
    register: dict[str, Any],
    reviews: dict[str, dict[str, Any]],
    artifacts: list[dict[str, Any]],
    blocked_rows: list[dict[str, Any]],
    errors: list[str],
) -> tuple[set[str], set[str]]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set(), set()
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("artifactLevel") != "c2ltb4-manual-fulltext-fresh-review-verdict-to-reviewed-card-artifact":
        fail(errors, "scope.artifactLevel is invalid")
    eligible = {row_id for row_id, row in reviews.items() if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION}
    blocked = set(reviews) - eligible
    expected = {
        "manualFulltextFreshReviewRowCount": len(reviews),
        "eligibleManualFulltextFreshReviewRowCount": len(eligible),
        "blockedManualFulltextFreshReviewRowCount": len(blocked),
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": len(eligible) * len(ARTIFACT_TYPES),
        "blockedRowCount": len(blocked),
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
    return eligible, blocked


def validate_artifacts(
    artifacts: list[dict[str, Any]],
    eligible: set[str],
    reviews: dict[str, dict[str, Any]],
    manual_rows: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    seen_ids: set[str] = set()
    pairs: Counter[tuple[str, str]] = Counter()
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
        manual_id = require_string(artifact.get("manualExtractionId"), f"{artifact_id}.manualExtractionId", errors)
        if manual_id not in eligible:
            fail(errors, f"{artifact_id} references non-eligible manual extraction row: {manual_id}")
        review = reviews.get(manual_id, {})
        manual_row = manual_rows.get(manual_id, {})
        for key in (
            "reviewId",
            "originTaskId",
            "sourceResolutionId",
            "candidateId",
            "domainId",
            "localDomainPath",
            "sourceTitle",
            "sourceUrl",
        ):
            if artifact.get(key) != review.get(key):
                fail(errors, f"{artifact_id}.{key} does not match fresh-review verdict row")
        if artifact.get("candidateRole") != manual_row.get("candidateRole"):
            fail(errors, f"{artifact_id}.candidateRole does not match manual extraction row")
        if artifact.get("artifactStatus") != "filled-reviewed-c2ltb4-manual-fulltext-artifact-model-blocked":
            fail(errors, f"{artifact_id}.artifactStatus is invalid")
        if artifact.get("sourceRowKind") != "manual-fulltext-fresh-review-row":
            fail(errors, f"{artifact_id}.sourceRowKind is invalid")
        if artifact.get("artifactPromotionDecision") != ARTIFACT_DECISION:
            fail(errors, f"{artifact_id}.artifactPromotionDecision is invalid")
        if artifact.get("sourceVerdictDecision") != ELIGIBLE_DECISION:
            fail(errors, f"{artifact_id}.sourceVerdictDecision must be eligible")
        if artifact.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"{artifact_id}.modelAdmissionDecision is invalid")
        if set(require_string_list(artifact.get("blockedUses"), f"{artifact_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{artifact_id}.blockedUses must match required blocked uses")
        if artifact.get("freshReviewEvidenceUrls") != evidence_urls(review, errors):
            fail(errors, f"{artifact_id}.freshReviewEvidenceUrls does not match reviewEvidenceTrace URLs")
        if artifact.get("registeredExactClaimUse") != manual_row.get("exactClaimUse"):
            fail(errors, f"{artifact_id}.registeredExactClaimUse does not match manual extraction row")
        if artifact.get("registeredTransferBoundary") != manual_row.get("transferBoundary"):
            fail(errors, f"{artifact_id}.registeredTransferBoundary does not match manual extraction row")
        content = artifact.get("content")
        if not isinstance(content, dict):
            fail(errors, f"{artifact_id}.content must be an object")
            continue
        required_content = TYPE_CONTENT_FIELDS.get(artifact_type, set())
        missing_content = required_content - set(content)
        if missing_content:
            fail(errors, f"{artifact_id}.content missing fields: {sorted(missing_content)}")
        pairs[(manual_id, artifact_type)] += 1
    for manual_id in eligible:
        for artifact_type in ARTIFACT_TYPES:
            if pairs[(manual_id, artifact_type)] != 1:
                fail(errors, f"eligible row {manual_id} must have exactly one {artifact_type}")


def validate_blocked_rows(
    rows: list[dict[str, Any]],
    blocked: set[str],
    reviews: dict[str, dict[str, Any]],
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
        if manual_id not in blocked:
            fail(errors, f"blockedRows[{index}] references non-blocked manual row: {manual_id}")
        review = reviews.get(manual_id, {})
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
            "nextAction",
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
    if seen != blocked:
        fail(errors, "blockedRows must cover exactly every non-eligible fresh-review row")


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
        actual = Counter(artifact["artifactType"] for artifact in artifacts if isinstance(artifact, dict) and "artifactType" in artifact)
        if counts != dict(actual):
            fail(errors, "summary.artifactTypeCounts must match reviewedArtifacts")
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
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "B4 manual/fulltext reviewed artifact register")
    reviews = load_rows(VERDICT_PATH, "manualFulltextFreshReviews", "manualExtractionId", errors, "fresh-review verdict register")
    manual_rows = load_rows(MANUAL_EXTRACTION_PATH, "manualExtractionRows", "manualExtractionId", errors, "manual/fulltext extraction register")

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
        eligible, blocked = validate_scope(register, reviews, artifacts, blocked_rows, errors)
        validate_artifacts(artifacts, eligible, reviews, manual_rows, errors)
        validate_blocked_rows(blocked_rows, blocked, reviews, errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        validate_summary(register, artifacts, blocked_rows, errors)
        validate_index_links(register, errors)

    if errors:
        print("C2-LT-B4 manual/fulltext reviewed artifact audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B4 manual/fulltext reviewed artifact audit ok: artifacts=18 blocked=5 model=blocked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
