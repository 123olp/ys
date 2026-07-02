#!/usr/bin/env python3
"""审计 C2-LT-B1 reviewed card artifact 账本。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json"
VERDICT_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-independent-fresh-review-verdict-register.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-source-extraction-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json"

SCHEMA = "human-infra.c2ltb1-reviewed-card-artifact-register.v1"
STATUS = "active-c2ltb1-reviewed-card-artifact-register-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-reviewed-card-artifact-register.json"
ELIGIBLE_DECISION = "eligible-for-bounded-artifact-fill"

SOURCE_OF_TRUTH_KEYS = {
    "promotionQueue",
    "sourceExtractionRegister",
    "localReviewRegister",
    "independentFreshReviewVerdictRegister",
    "evidencePolicy",
    "maturityGapRegister",
}

ARTIFACT_TYPES = {
    "reviewed-source-card",
    "variable-card",
    "endpoint-card",
    "uncertainty-card",
    "transfer-boundary-card",
    "downgrade-check",
}

REQUIRED_BLOCKED_USES = {
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
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "sourceTitle",
    "sourceUrl",
    "sourceRole",
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
    "variable-card": {
        "variableQuestion",
        "variableSeed",
        "sourceExtractedVariables",
        "modelPosition",
        "admissibleUse",
        "promotionBoundary",
    },
    "endpoint-card": {
        "endpointQuestion",
        "endpointDefinition",
        "populationOrSetting",
        "endpointBoundary",
        "modelPosition",
        "blockedEndpointUses",
    },
    "uncertainty-card": {
        "uncertaintyQuestion",
        "uncertaintyOrBias",
        "uncertaintyBoundaryVerdict",
        "evidenceLimit",
        "downgradeTriggers",
    },
    "transfer-boundary-card": {
        "transferBoundaryQuestion",
        "domainTransferVerdict",
        "registeredTransferBoundary",
        "sourceExtractionTransferBoundary",
        "blockedTransferUses",
    },
    "downgrade-check": {
        "downgradeQuestion",
        "downgradeVerdict",
        "reviewerVerdict",
        "downgradeRequiredWhen",
        "nonEligibleSiblingPolicy",
    },
}

REQUIRED_INDEX_FILES = [
    "README.md",
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


def load_rows(path: Path, key: str, errors: list[str], context: str) -> dict[str, dict[str, Any]]:
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
    reviews: list[dict[str, Any]],
    artifacts: list[dict[str, Any]],
    blocked_rows: list[dict[str, Any]],
    errors: list[str],
) -> tuple[set[str], set[str]]:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return set(), set()
    if scope.get("batchId") != "C2-LT-B1":
        fail(errors, "scope.batchId must be C2-LT-B1")
    if scope.get("artifactLevel") != "c2ltb1-fresh-review-verdict-row-to-reviewed-card-artifact":
        fail(errors, "scope.artifactLevel is invalid")

    eligible = {row["taskId"] for row in reviews if row.get("artifactPromotionDecision") == ELIGIBLE_DECISION}
    blocked = {row["taskId"] for row in reviews if row.get("artifactPromotionDecision") != ELIGIBLE_DECISION}
    expected = {
        "totalFreshReviewVerdictRowCount": len(reviews),
        "eligibleFreshReviewVerdictRowCount": len(eligible),
        "downgradeBeforeFillRowCount": sum(1 for row in reviews if row.get("artifactPromotionDecision") == "downgrade-before-fill"),
        "blockedCannotEvaluateRowCount": sum(1 for row in reviews if row.get("artifactPromotionDecision") == "blocked-cannot-evaluate"),
        "eligibleDomainCount": len({row["domainId"] for row in reviews if row.get("taskId") in eligible}),
        "totalDomainCount": len({row["domainId"] for row in reviews}),
        "artifactTypeCount": len(ARTIFACT_TYPES),
        "reviewedArtifactCount": len(eligible) * len(ARTIFACT_TYPES),
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    if len(artifacts) != expected["reviewedArtifactCount"]:
        fail(errors, f"reviewedArtifacts must contain {expected['reviewedArtifactCount']} artifacts")
    if len(blocked_rows) != len(blocked):
        fail(errors, f"blockedRows must contain {len(blocked)} rows")
    if set(scope.get("artifactTypes", [])) != ARTIFACT_TYPES:
        fail(errors, "scope.artifactTypes must contain every artifact type")
    for field in ["selectionRule", "blockedRowRule", "artifactStatusRule", "modelAdmissionRule"]:
        require_string(scope.get(field), f"scope.{field}", errors)
    non_claims = " ".join(require_string_list(scope.get("nonClaims"), "scope.nonClaims", errors, 4))
    for phrase in ["not model-ready", "does not authorize individual advice", "does not fill rows", "does not mark the remaining 184"]:
        if phrase not in non_claims:
            fail(errors, f"scope.nonClaims must mention {phrase!r}")
    return eligible, blocked


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


def validate_artifacts(
    register: dict[str, Any],
    reviews_by_task: dict[str, dict[str, Any]],
    extraction_by_task: dict[str, dict[str, Any]],
    eligible: set[str],
    errors: list[str],
) -> tuple[int, int]:
    artifacts = register.get("reviewedArtifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail(errors, "reviewedArtifacts must be a non-empty list")
        return 0, 0

    seen_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for index, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(errors, f"reviewedArtifacts[{index}] must be an object")
            continue
        for field in REQUIRED_ARTIFACT_FIELDS:
            if field not in artifact:
                fail(errors, f"reviewedArtifacts[{index}] missing {field}")
        artifact_id = require_string(artifact.get("artifactId"), f"reviewedArtifacts[{index}].artifactId", errors)
        artifact_type = require_string(artifact.get("artifactType"), f"{artifact_id}.artifactType", errors)
        task_id = require_string(artifact.get("taskId"), f"{artifact_id}.taskId", errors)
        if artifact_id in seen_ids:
            fail(errors, f"duplicate artifactId: {artifact_id}")
        seen_ids.add(artifact_id)
        if artifact_type not in ARTIFACT_TYPES:
            fail(errors, f"{artifact_id}.artifactType is invalid")
            continue
        if task_id not in eligible:
            fail(errors, f"{artifact_id} is attached to non-eligible task {task_id}")
        pair = (task_id, artifact_type)
        if pair in seen_pairs:
            fail(errors, f"duplicate artifact type for task: {task_id} {artifact_type}")
        seen_pairs.add(pair)

        review = reviews_by_task.get(task_id, {})
        extraction = extraction_by_task.get(task_id, {})
        for field in ["domainId", "sourceRefId", "sourceTitle", "sourceUrl"]:
            if artifact.get(field) != extraction.get(field):
                fail(errors, f"{artifact_id}.{field} must match extraction row")
        if artifact.get("sourceRole") != review.get("registeredSourceRole"):
            fail(errors, f"{artifact_id}.sourceRole must match fresh-review registeredSourceRole")
        if artifact.get("reviewerVerdict") != review.get("reviewerVerdict"):
            fail(errors, f"{artifact_id}.reviewerVerdict must match fresh review")
        if artifact.get("artifactPromotionDecision") != ELIGIBLE_DECISION:
            fail(errors, f"{artifact_id}.artifactPromotionDecision must be {ELIGIBLE_DECISION}")
        if "blocked" not in require_string(artifact.get("modelAdmissionDecision"), f"{artifact_id}.modelAdmissionDecision", errors):
            fail(errors, f"{artifact_id}.modelAdmissionDecision must remain blocked")
        if set(artifact.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{artifact_id}.blockedUses must match required blocked uses")
        expected_urls = sorted(item["url"] for item in review.get("freshReviewEvidence", []))
        if sorted(artifact.get("freshReviewEvidenceUrls", [])) != expected_urls:
            fail(errors, f"{artifact_id}.freshReviewEvidenceUrls must match fresh-review evidence URLs")
        if artifact.get("registeredExactClaimUse") != review.get("registeredExactClaimUse"):
            fail(errors, f"{artifact_id}.registeredExactClaimUse must match fresh review")
        if artifact.get("registeredTransferBoundary") != review.get("registeredTransferBoundary"):
            fail(errors, f"{artifact_id}.registeredTransferBoundary must match fresh review")
        validate_content(artifact.get("content"), artifact_id, artifact_type, errors)

    expected_pairs = {(task_id, artifact_type) for task_id in eligible for artifact_type in ARTIFACT_TYPES}
    if seen_pairs != expected_pairs:
        fail(errors, "reviewedArtifacts must contain exactly one artifact of each type for every eligible task")
    return len(seen_pairs), len(seen_ids)


def validate_blocked_rows(register: dict[str, Any], reviews_by_task: dict[str, dict[str, Any]], blocked: set[str], errors: list[str]) -> None:
    rows = register.get("blockedRows")
    if not isinstance(rows, list):
        fail(errors, "blockedRows must be a list")
        return
    seen = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"blockedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"blockedRows[{index}].taskId", errors)
        seen.add(task_id)
        review = reviews_by_task.get(task_id, {})
        if task_id not in blocked:
            fail(errors, f"blockedRows[{index}] is not a blocked verdict row")
        for field in ["domainId", "reviewerVerdict", "artifactPromotionDecision"]:
            if row.get(field) != review.get(field):
                fail(errors, f"blockedRows[{index}].{field} must match fresh review")
        if "blocked" not in str(row.get("modelAdmissionDecision", "")):
            fail(errors, f"blockedRows[{index}].modelAdmissionDecision must remain blocked")
        require_string(row.get("blockReason"), f"blockedRows[{index}].blockReason", errors)
        require_string(row.get("requiredBeforeArtifactFill"), f"blockedRows[{index}].requiredBeforeArtifactFill", errors)
    if seen != blocked:
        fail(errors, "blockedRows must match every non-eligible fresh-review row")


def validate_indexes(register: dict[str, Any], errors: list[str]) -> None:
    paths = require_string_list(register.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if set(paths) != set(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must contain every required index file")
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements entry {relative_path}", errors)
        if target and REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {REGISTER_LINK}")


def validate_register(errors: list[str]) -> tuple[int, int]:
    register = load_json(REGISTER_PATH, errors, "C2-LT-B1 reviewed card artifact register")
    verdict = load_json(VERDICT_PATH, errors, "C2-LT-B1 independent fresh-review verdict register")
    extraction_by_task = load_rows(EXTRACTION_PATH, "extractedRows", errors, "source extraction register")
    queue = load_json(QUEUE_PATH, errors, "C2-LT-B1 promotion queue")
    if not register:
        return 0, 0

    if register.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if register.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(register.get("registerId"), "registerId", errors)
    require_string(register.get("purpose"), "purpose", errors)
    validate_source_of_truth(register, errors)

    reviews = verdict.get("sourceTaskFreshReviews") if isinstance(verdict, dict) else []
    if not isinstance(reviews, list) or len(reviews) != 48:
        fail(errors, "fresh-review verdict register must contain 48 sourceTaskFreshReviews")
        reviews = []
    reviews_by_task = {row["taskId"]: row for row in reviews if isinstance(row, dict) and isinstance(row.get("taskId"), str)}

    artifacts = register.get("reviewedArtifacts") if isinstance(register.get("reviewedArtifacts"), list) else []
    blocked_rows = register.get("blockedRows") if isinstance(register.get("blockedRows"), list) else []
    eligible, blocked = validate_scope(register, reviews, artifacts, blocked_rows, errors)
    if set(register.get("blockedUses", [])) != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required blocked uses")
    pair_count, artifact_count = validate_artifacts(register, reviews_by_task, extraction_by_task, eligible, errors)
    validate_blocked_rows(register, reviews_by_task, blocked, errors)
    validate_indexes(register, errors)

    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
    else:
        if summary.get("reviewerVerdictCounts") != dict(Counter(row.get("reviewerVerdict") for row in reviews)):
            fail(errors, "summary.reviewerVerdictCounts must match fresh review")
        if summary.get("artifactPromotionDecisionCounts") != dict(Counter(row.get("artifactPromotionDecision") for row in reviews)):
            fail(errors, "summary.artifactPromotionDecisionCounts must match fresh review")
        if "blocked" not in str(summary.get("modelAdmissionDecision", "")):
            fail(errors, "summary.modelAdmissionDecision must remain blocked")
    if queue and queue.get("scope", {}).get("batchId") != "C2-LT-B1":
        fail(errors, "promotion queue scope.batchId must be C2-LT-B1")
    return pair_count, artifact_count


def main() -> int:
    errors: list[str] = []
    pair_count, artifact_count = validate_register(errors)
    if errors:
        print("C2-LT-B1 reviewed card artifact audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"C2-LT-B1 reviewed card artifact audit ok: artifacts={artifact_count} task_type_pairs={pair_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
