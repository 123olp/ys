#!/usr/bin/env python3
"""审计 C2 长尾第十二批 bounded reviewed artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-twelfth-batch-reviewed-card-artifact-register.json"
VERDICT_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-twelfth-batch-independent-fresh-review-verdict-register.json"
)

SCHEMA = "human-infra.c2-longtail-twelfth-batch-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb12-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-twelfth-batch-reviewed-card-artifact-register.json"
AUDIT_SCRIPT = "audit_human_infra_c2_longtail_twelfth_batch_reviewed_card_artifact_register.py"
AUDIT_TARGET = "c2-longtail-twelfth-batch-reviewed-card-artifact-audit"
MODEL_DECISION = "blocked-pending-b12-reviewed-artifact-gates-and-calibrated-model-validation"
ELIGIBLE_DECISION = "eligible-for-bounded-reviewed-artifact-prep"
ARTIFACT_DECISION = "filled-from-eligible-c2ltb12-independent-fresh-review"
BLOCKED_DECISION = "blocked-cannot-evaluate"
BLOCKED_ARTIFACT_DECISION = "blocked-no-reviewed-artifact-fill-from-pubmed-only-route"
ARTIFACT_TYPES = [
    "reviewed-source-card",
    "reviewed-variable-card",
    "reviewed-endpoint-card",
    "reviewed-uncertainty-card",
    "reviewed-transfer-boundary-card",
    "reviewed-downgrade-check",
]
SOURCE_OF_TRUTH_KEYS = {
    "independentFreshReviewVerdictRegister",
    "sourceExtractionRegister",
    "evidencePolicy",
    "maturityGapRegister",
}
BASE_FIELDS = {
    "artifactId",
    "artifactType",
    "artifactStatus",
    "sourceRowKind",
    "reviewId",
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
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
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "docs/reference/human-infra-maturity-gap-register.json",
    "tools/README.md",
    "tools/AGENTS.md",
    "Makefile",
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


def verdict_rows(errors: list[str]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    data = load_json(VERDICT_PATH, errors, "C2-LT-B12 independent fresh review verdict register")
    rows = data.get("freshReviewVerdicts") if data else None
    if not isinstance(rows, list):
        fail(errors, "freshReviewVerdicts must be a list")
        return {}, {}
    eligible: dict[str, dict[str, Any]] = {}
    blocked: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"freshReviewVerdicts[{index}] must be an object")
            continue
        review_id = require_string(row.get("reviewId"), f"freshReviewVerdicts[{index}].reviewId", errors)
        if row.get("reviewerVerdict") == ELIGIBLE_DECISION and review_id:
            eligible[review_id] = row
        elif row.get("reviewerVerdict") == BLOCKED_DECISION and review_id:
            blocked[review_id] = row
    if len(eligible) != 20:
        fail(errors, "verdict register must contain 20 eligible rows")
    if len(blocked) != 4:
        fail(errors, "verdict register must contain 4 blocked PubMed-only rows")
    return eligible, blocked


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


def validate_scope(register: dict[str, Any], errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "eligibleReviewRowCount": 20,
        "artifactTypesPerEligibleRow": 6,
        "reviewedArtifactCount": 120,
        "blockedRowCount": 4,
        "modelAdmissionCount": 0,
        "adviceUseAdmissionCount": 0,
    }
    if scope.get("batchId") != "C2-LT-B12":
        fail(errors, "scope.batchId must be C2-LT-B12")
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")


def validate_artifacts(
    register: dict[str, Any],
    eligible: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(artifacts, list):
        fail(errors, "reviewedArtifacts must be a list")
        return
    if len(artifacts) != 120:
        fail(errors, "reviewedArtifacts must contain 120 artifacts")

    blocked_uses = set(require_string_list(register.get("blockedUses"), "blockedUses", errors, 20))
    per_review: Counter[str] = Counter()
    per_type: Counter[str] = Counter()
    seen: set[str] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        missing = BASE_FIELDS - set(artifact)
        if missing:
            fail(errors, f"reviewedArtifacts[{index}] missing fields: {sorted(missing)}")
        artifact_id = require_string(artifact.get("artifactId"), f"reviewedArtifacts[{index}].artifactId", errors)
        if artifact_id in seen:
            fail(errors, f"duplicate artifactId: {artifact_id}")
        seen.add(artifact_id)
        artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
        if artifact_type not in ARTIFACT_TYPES:
            fail(errors, f"{artifact_id}.artifactType must be one of required artifact types")
        review_id = require_string(artifact.get("reviewId"), f"{artifact_id}.reviewId", errors)
        source = eligible.get(review_id)
        if not source:
            fail(errors, f"{artifact_id}.reviewId has no eligible verdict row: {review_id}")
            continue
        per_review[review_id] += 1
        per_type[artifact_type] += 1
        for field in ["taskId", "domainId", "localDomainPath", "sourceRefId", "sourceTitle", "sourceUrl"]:
            if artifact.get(field) != source.get(field):
                fail(errors, f"{artifact_id}.{field} must match verdict row")
        if artifact.get("artifactStatus") != "bounded-reviewed-artifact-model-blocked":
            fail(errors, f"{artifact_id}.artifactStatus must be bounded-reviewed-artifact-model-blocked")
        if artifact.get("reviewerVerdict") != ELIGIBLE_DECISION:
            fail(errors, f"{artifact_id}.reviewerVerdict must remain eligible bounded prep")
        if artifact.get("artifactPromotionDecision") != ARTIFACT_DECISION:
            fail(errors, f"{artifact_id}.artifactPromotionDecision must be {ARTIFACT_DECISION}")
        if artifact.get("modelAdmissionDecision") != MODEL_DECISION:
            fail(errors, f"{artifact_id}.modelAdmissionDecision must keep model admission blocked")
        if set(require_string_list(artifact.get("blockedUses"), f"{artifact_id}.blockedUses", errors, 20)) != blocked_uses:
            fail(errors, f"{artifact_id}.blockedUses must match register blockedUses")
        if not require_string_list(artifact.get("freshReviewEvidenceUrls"), f"{artifact_id}.freshReviewEvidenceUrls", errors, 4):
            fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must include evidence links")
        content = artifact.get("content")
        if not isinstance(content, dict):
            fail(errors, f"{artifact_id}.content must be an object")
            continue
        missing_content = TYPE_CONTENT_FIELDS.get(artifact_type, set()) - set(content)
        if missing_content:
            fail(errors, f"{artifact_id}.content missing fields: {sorted(missing_content)}")
    for review_id in eligible:
        if per_review[review_id] != 6:
            fail(errors, f"{review_id} must have exactly 6 artifacts")
    for artifact_type in ARTIFACT_TYPES:
        if per_type[artifact_type] != 20:
            fail(errors, f"{artifact_type} must have exactly 20 artifacts")


def validate_blocked_rows(
    register: dict[str, Any],
    blocked: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    rows = register.get("blockedRows")
    if not isinstance(rows, list):
        fail(errors, "blockedRows must be a list")
        return
    if len(rows) != 4:
        fail(errors, "blockedRows must contain 4 PubMed-only rows")
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"blockedRows[{index}] must be an object")
            continue
        review_id = require_string(row.get("reviewId"), f"blockedRows[{index}].reviewId", errors)
        source = blocked.get(review_id)
        if not source:
            fail(errors, f"blockedRows[{index}].reviewId has no blocked verdict row: {review_id}")
            continue
        if review_id in seen:
            fail(errors, f"duplicate blocked row: {review_id}")
        seen.add(review_id)
        for field in ["taskId", "domainId", "localDomainPath", "sourceRefId", "sourceTitle", "sourceUrl"]:
            if row.get(field) != source.get(field):
                fail(errors, f"{review_id}.{field} must match blocked verdict row")
        if row.get("reviewerVerdict") != BLOCKED_DECISION:
            fail(errors, f"{review_id}.reviewerVerdict must remain blocked-cannot-evaluate")
        if row.get("artifactPromotionDecision") != BLOCKED_ARTIFACT_DECISION:
            fail(errors, f"{review_id}.artifactPromotionDecision must block artifact fill")
        text = " ".join(str(row.get(field, "")) for field in ["blockedReason", "nextAction"])
        for phrase in ["PubMed", "full-context", "blocked"]:
            if phrase not in text:
                fail(errors, f"{review_id} must preserve PubMed-only blocked boundary with {phrase}")


def validate_index_links(register: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if not target:
            continue
        text = target.read_text(encoding="utf-8")
        if relative_path == "Makefile":
            if AUDIT_TARGET not in text:
                fail(errors, "Makefile must expose twelfth-batch reviewed artifact audit target")
            if AUDIT_SCRIPT not in text:
                fail(errors, "Makefile must run twelfth-batch reviewed artifact audit script")
        elif REGISTER_LINK not in text:
            fail(errors, f"{relative_path} must link {REGISTER_LINK}")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "C2-LT-B12 reviewed card artifact register")
    eligible, blocked = verdict_rows(errors)
    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        validate_scope(register, errors)
        validate_artifacts(register, eligible, errors)
        validate_blocked_rows(register, blocked, errors)
        validate_index_links(register, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "C2 longtail twelfth-batch reviewed artifact audit ok: "
        "artifacts=120 eligible_rows=20 blocked_pubmed_only=4 model_admission=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
