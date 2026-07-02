#!/usr/bin/env python3
"""审计来源语境本地复核账本契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-source-context-local-review-register.json"
PROMOTION_QUEUE_PATH = ROOT / "docs/reference/human-infra-domain-source-card-promotion-queue.json"

SCHEMA = "human-infra.source-context-local-review-register.v1"
STATUS = "partial-local-review-method-anchors-complete-independent-fresh-review-required"
REGISTER_LINK = "human-infra-source-context-local-review-register.json"

SOURCE_OF_TRUTH_KEYS = [
    "domainSourceCardPromotionQueue",
    "domainSourceSpecificExtractionRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

REQUIRED_REVIEW_FIELDS = [
    "sourceCardId",
    "reviewedSourceTitle",
    "reviewedSourceAuthors",
    "reviewedSourceYear",
    "sourceType",
    "reviewDate",
    "reviewMode",
    "sourceContextVerdict",
    "reviewEvidence",
    "supports",
    "doesNotSupport",
    "reviewerBoundary",
    "affectedPromotionTaskCount",
    "affectedPromotionTaskIds",
    "affectedDomainIds",
    "affectedFieldCardIds",
    "promotionDecision",
    "modelAdmissionDecision",
    "requiredNextArtifacts",
    "blockedUses",
]

REQUIRED_NEXT_ARTIFACTS = {
    "reviewed-source-card",
    "variable-card",
    "endpoint-card",
    "uncertainty-card",
    "transfer-boundary-card",
    "downgrade-check-row",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-recommendation",
    "individual-death-date-output",
    "intervention-ranking",
    "domain-claim-upgrade",
    "clinical-validity-claim",
}

REQUIRED_INDEX_FILES = [
    "README.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
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
    if not isinstance(relative_path, str) or not relative_path.strip():
        fail(errors, f"{context} must be a non-empty local path")
        return None
    if relative_path.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local path, not URL")
        return None
    target = (ROOT / relative_path).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {relative_path}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {relative_path}")
        return None
    return target


def load_promotion_tasks(errors: list[str]) -> list[dict[str, Any]]:
    data = load_json(PROMOTION_QUEUE_PATH, errors, "domain-source promotion queue")
    tasks = data.get("promotionTasks") if data else None
    if not isinstance(tasks, list):
        fail(errors, "domain-source promotion queue promotionTasks must be a list")
        return []
    result: list[dict[str, Any]] = []
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"promotionTasks[{index}] must be an object")
            continue
        result.append(task)
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_required_fields(data: dict[str, Any], errors: list[str]) -> None:
    fields = require_string_list(
        data.get("requiredPerReviewFields"),
        "requiredPerReviewFields",
        errors,
        len(REQUIRED_REVIEW_FIELDS),
    )
    if fields != REQUIRED_REVIEW_FIELDS:
        fail(errors, "requiredPerReviewFields must exactly match the source-context review contract")


def validate_scope(data: dict[str, Any], reviews: list[dict[str, Any]], tasks_by_source: dict[str, list[dict[str, Any]]], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("reviewLevel") != "source-anchor-local-context-review":
        fail(errors, "scope.reviewLevel must be source-anchor-local-context-review")

    source_ids = sorted(review.get("sourceCardId") for review in reviews if isinstance(review.get("sourceCardId"), str))
    affected_tasks = [task for source_id in source_ids for task in tasks_by_source.get(source_id, [])]
    affected_domains = sorted({task.get("domainId") for task in affected_tasks if isinstance(task.get("domainId"), str)})

    expected_counts = {
        "reviewedSourceAnchorCount": len(source_ids),
        "affectedPromotionTaskCount": len(affected_tasks),
        "affectedDomainCount": len(affected_domains),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")

    reviewed = require_string_list(scope.get("reviewedSourceAnchors"), "scope.reviewedSourceAnchors", errors, len(source_ids))
    if sorted(reviewed) != source_ids:
        fail(errors, "scope.reviewedSourceAnchors must match localReviews.sourceCardId")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 4)


def validate_review_evidence(review: dict[str, Any], index: int, errors: list[str]) -> None:
    evidence = review.get("reviewEvidence")
    if not isinstance(evidence, list) or not evidence:
        fail(errors, f"localReviews[{index}].reviewEvidence must be a non-empty list")
        return
    for evidence_index, item in enumerate(evidence):
        if not isinstance(item, dict):
            fail(errors, f"localReviews[{index}].reviewEvidence[{evidence_index}] must be an object")
            continue
        url = require_string(item.get("url"), f"localReviews[{index}].reviewEvidence[{evidence_index}].url", errors)
        if url and not url.startswith(("http://", "https://")):
            fail(errors, f"localReviews[{index}].reviewEvidence[{evidence_index}].url must be an HTTP(S) source URL")
        require_string(item.get("evidenceType"), f"localReviews[{index}].reviewEvidence[{evidence_index}].evidenceType", errors)
        require_string(item.get("finding"), f"localReviews[{index}].reviewEvidence[{evidence_index}].finding", errors)


def validate_review(
    review: Any,
    index: int,
    tasks_by_source: dict[str, list[dict[str, Any]]],
    seen_sources: set[str],
    errors: list[str],
) -> None:
    if not isinstance(review, dict):
        fail(errors, f"localReviews[{index}] must be an object")
        return
    missing = [field for field in REQUIRED_REVIEW_FIELDS if field not in review]
    if missing:
        fail(errors, f"localReviews[{index}] missing required fields: {', '.join(missing)}")

    source_id = require_string(review.get("sourceCardId"), f"localReviews[{index}].sourceCardId", errors)
    if not source_id:
        return
    if source_id in seen_sources:
        fail(errors, f"duplicate local review sourceCardId: {source_id}")
    seen_sources.add(source_id)

    tasks = tasks_by_source.get(source_id, [])
    if not tasks:
        fail(errors, f"localReviews[{index}] sourceCardId has no matching promotion tasks: {source_id}")

    for field in [
        "reviewedSourceTitle",
        "reviewedSourceAuthors",
        "reviewedSourceYear",
        "sourceType",
        "reviewDate",
        "reviewMode",
        "sourceContextVerdict",
        "reviewerBoundary",
        "promotionDecision",
        "modelAdmissionDecision",
    ]:
        require_string(review.get(field), f"localReviews[{index}].{field}", errors)

    if review.get("reviewMode") != "local-source-context-review-from-primary-or-registry-sources":
        fail(errors, f"{source_id}.reviewMode must be local-source-context-review-from-primary-or-registry-sources")
    if review.get("sourceContextVerdict") != "local-review-pass-with-boundaries-requires-independent-fresh-review":
        fail(errors, f"{source_id}.sourceContextVerdict must keep independent fresh review required")
    if review.get("promotionDecision") != "eligible-for-card-drafting-only-after-independent-review":
        fail(errors, f"{source_id}.promotionDecision must keep card drafting gated by independent review")
    if review.get("modelAdmissionDecision") != "blocked-pending-card-promotion-independent-review-and-model-gates":
        fail(errors, f"{source_id}.modelAdmissionDecision must keep model admission blocked")

    validate_review_evidence(review, index, errors)
    require_string_list(review.get("supports"), f"{source_id}.supports", errors, 2)
    require_string_list(review.get("doesNotSupport"), f"{source_id}.doesNotSupport", errors, 2)

    expected_task_ids = sorted(task.get("promotionTaskId") for task in tasks if isinstance(task.get("promotionTaskId"), str))
    expected_domain_ids = sorted({task.get("domainId") for task in tasks if isinstance(task.get("domainId"), str)})
    expected_field_ids = sorted({task.get("fieldCardId") for task in tasks if isinstance(task.get("fieldCardId"), str)})

    actual_count = require_int(review.get("affectedPromotionTaskCount"), f"{source_id}.affectedPromotionTaskCount", errors)
    if actual_count is not None and actual_count != len(tasks):
        fail(errors, f"{source_id}.affectedPromotionTaskCount must equal {len(tasks)}")

    actual_task_ids = sorted(require_string_list(review.get("affectedPromotionTaskIds"), f"{source_id}.affectedPromotionTaskIds", errors, len(expected_task_ids)))
    if actual_task_ids != expected_task_ids:
        fail(errors, f"{source_id}.affectedPromotionTaskIds must match promotion queue")

    actual_domain_ids = sorted(require_string_list(review.get("affectedDomainIds"), f"{source_id}.affectedDomainIds", errors, len(expected_domain_ids)))
    if actual_domain_ids != expected_domain_ids:
        fail(errors, f"{source_id}.affectedDomainIds must match promotion queue")

    actual_field_ids = sorted(require_string_list(review.get("affectedFieldCardIds"), f"{source_id}.affectedFieldCardIds", errors, len(expected_field_ids)))
    if actual_field_ids != expected_field_ids:
        fail(errors, f"{source_id}.affectedFieldCardIds must match promotion queue")

    next_artifacts = set(require_string_list(review.get("requiredNextArtifacts"), f"{source_id}.requiredNextArtifacts", errors, len(REQUIRED_NEXT_ARTIFACTS)))
    if next_artifacts != REQUIRED_NEXT_ARTIFACTS:
        fail(errors, f"{source_id}.requiredNextArtifacts must contain every required artifact")

    blocked_uses = set(require_string_list(review.get("blockedUses"), f"{source_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked_uses != REQUIRED_BLOCKED_USES:
        fail(errors, f"{source_id}.blockedUses must contain every required blocked use")


def validate_non_claims(data: dict[str, Any], errors: list[str]) -> None:
    non_claims = require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    joined = " ".join(non_claims)
    for phrase in [
        "independent fresh review",
        "calibrated prediction",
        "domain intervention effects",
        "Source Cards",
    ]:
        if phrase not in joined:
            fail(errors, f"nonClaims must explicitly mention {phrase}")


def validate_index_requirements(data: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {REGISTER_LINK}")


def validate_register(data: dict[str, Any], errors: list[str]) -> tuple[int, int, int]:
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    validate_source_of_truth(data, errors)
    validate_required_fields(data, errors)

    promotion_tasks = load_promotion_tasks(errors)
    tasks_by_source: dict[str, list[dict[str, Any]]] = {}
    for task in promotion_tasks:
        source_id = task.get("sourceCardId")
        if isinstance(source_id, str) and source_id.strip():
            tasks_by_source.setdefault(source_id, []).append(task)

    reviews = data.get("localReviews")
    if not isinstance(reviews, list) or not reviews:
        fail(errors, "localReviews must be a non-empty list")
        reviews = []

    seen_sources: set[str] = set()
    for index, review in enumerate(reviews):
        validate_review(review, index, tasks_by_source, seen_sources, errors)

    typed_reviews = [review for review in reviews if isinstance(review, dict)]
    validate_scope(data, typed_reviews, tasks_by_source, errors)
    validate_non_claims(data, errors)
    validate_index_requirements(data, errors)

    affected_tasks = [task for source_id in seen_sources for task in tasks_by_source.get(source_id, [])]
    affected_domains = {task.get("domainId") for task in affected_tasks if isinstance(task.get("domainId"), str)}
    return len(seen_sources), len(affected_tasks), len(affected_domains)


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "source-context local review register")
    source_count = task_count = domain_count = 0
    if data:
        source_count, task_count, domain_count = validate_register(data, errors)

    if errors:
        print("source-context local review register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "source-context local review register audit ok: "
        f"sources={source_count} tasks={task_count} domains={domain_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
