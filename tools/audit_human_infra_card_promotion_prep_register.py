#!/usr/bin/env python3
"""审计卡片晋升预注册账本契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-card-promotion-prep-register.json"
PROMOTION_QUEUE_PATH = ROOT / "docs/reference/human-infra-domain-source-card-promotion-queue.json"
LOCAL_REVIEW_PATH = ROOT / "docs/reference/human-infra-source-context-local-review-register.json"

SCHEMA = "human-infra.card-promotion-prep-register.v1"
STATUS = "active-card-promotion-prep-independent-review-required"
REGISTER_LINK = "human-infra-card-promotion-prep-register.json"

SOURCE_OF_TRUTH_KEYS = [
    "domainSourceCardPromotionQueue",
    "sourceContextLocalReviewRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

REQUIRED_PACKET_FIELDS = [
    "promotionTaskId",
    "domainId",
    "domainClaimId",
    "fieldCardId",
    "sourceCardId",
    "sourceRole",
    "sourceContextLocalReviewVerdict",
    "sourceContextLocalReviewEvidenceUrls",
    "independentFreshReviewStatus",
    "artifactPackStatus",
    "artifactIds",
    "promotionQuestions",
    "requiredReviewerVerdicts",
    "blockedUses",
    "modelAdmissionDecision",
    "nextAction",
]

REQUIRED_ARTIFACT_ID_FIELDS = {
    "reviewedSourceCardId",
    "variableCardId",
    "endpointCardId",
    "uncertaintyCardId",
    "transferBoundaryCardId",
    "downgradeCheckId",
}

REQUIRED_PROMOTION_QUESTION_FIELDS = {
    "sourceSupportQuestion",
    "variableQuestion",
    "endpointQuestion",
    "uncertaintyQuestion",
    "transferBoundaryQuestion",
    "downgradeQuestion",
}

REQUIRED_REVIEWER_VERDICTS = {
    "support-with-boundary",
    "bounded-support",
    "downgrade-required",
    "reject-source-context-mismatch",
    "cannot-evaluate-insufficient-context",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-recommendation",
    "individual-death-date-output",
    "intervention-ranking",
    "domain-claim-upgrade",
    "clinical-validity-claim",
}

REQUIRED_ARTIFACT_TYPES = {
    "reviewed-source-card",
    "variable-card",
    "endpoint-card",
    "uncertainty-card",
    "transfer-boundary-card",
    "downgrade-check",
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


def load_promotion_tasks(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(PROMOTION_QUEUE_PATH, errors, "domain-source card promotion queue")
    tasks = data.get("promotionTasks") if data else None
    if not isinstance(tasks, list):
        fail(errors, "domain-source card promotion queue promotionTasks must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"promotionTasks[{index}] must be an object")
            continue
        task_id = require_string(task.get("promotionTaskId"), f"promotionTasks[{index}].promotionTaskId", errors)
        if task_id:
            if task_id in result:
                fail(errors, f"duplicate promotion task: {task_id}")
            result[task_id] = task
    return result


def load_local_reviews(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(LOCAL_REVIEW_PATH, errors, "source-context local review register")
    reviews = data.get("localReviews") if data else None
    if not isinstance(reviews, list):
        fail(errors, "source-context local review register localReviews must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            fail(errors, f"localReviews[{index}] must be an object")
            continue
        source_id = require_string(review.get("sourceCardId"), f"localReviews[{index}].sourceCardId", errors)
        if source_id:
            if source_id in result:
                fail(errors, f"duplicate local review sourceCardId: {source_id}")
            result[source_id] = review
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


def validate_scope(
    data: dict[str, Any],
    packets: list[dict[str, Any]],
    promotion_tasks: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("prepLevel") != "locally-reviewed-promotion-task-to-card-artifact-pack":
        fail(errors, "scope.prepLevel must be locally-reviewed-promotion-task-to-card-artifact-pack")

    task_ids = {packet.get("promotionTaskId") for packet in packets if isinstance(packet.get("promotionTaskId"), str)}
    domains = {packet.get("domainId") for packet in packets if isinstance(packet.get("domainId"), str)}
    fields = {packet.get("fieldCardId") for packet in packets if isinstance(packet.get("fieldCardId"), str)}
    sources = {packet.get("sourceCardId") for packet in packets if isinstance(packet.get("sourceCardId"), str)}
    expected_counts = {
        "promotionTaskCount": len(promotion_tasks),
        "coveredDomainCount": len(domains),
        "coveredFieldRowCount": len(fields),
        "coveredSourceAnchorCount": len(sources),
        "artifactTypeCount": len(REQUIRED_ARTIFACT_TYPES),
        "artifactPackCount": len(task_ids),
        "preparedArtifactCount": len(task_ids) * len(REQUIRED_ARTIFACT_TYPES),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    if task_ids != set(promotion_tasks):
        fail(errors, "scope packets must cover exactly the promotion queue task ids")

    artifact_types = set(require_string_list(scope.get("artifactTypes"), "scope.artifactTypes", errors, len(REQUIRED_ARTIFACT_TYPES)))
    if artifact_types != REQUIRED_ARTIFACT_TYPES:
        fail(errors, "scope.artifactTypes must contain every required artifact type")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 4)


def validate_required_fields(data: dict[str, Any], errors: list[str]) -> None:
    fields = require_string_list(
        data.get("requiredPerPromotionPacketFields"),
        "requiredPerPromotionPacketFields",
        errors,
        len(REQUIRED_PACKET_FIELDS),
    )
    if fields != REQUIRED_PACKET_FIELDS:
        fail(errors, "requiredPerPromotionPacketFields must exactly match the prep contract")

    contract = data.get("artifactContract")
    if not isinstance(contract, dict):
        fail(errors, "artifactContract must be an object")
        return
    checks = [
        ("requiredArtifactIdFields", REQUIRED_ARTIFACT_ID_FIELDS),
        ("requiredPromotionQuestionFields", REQUIRED_PROMOTION_QUESTION_FIELDS),
        ("requiredReviewerVerdicts", REQUIRED_REVIEWER_VERDICTS),
        ("requiredBlockedUses", REQUIRED_BLOCKED_USES),
    ]
    for key, expected in checks:
        actual = set(require_string_list(contract.get(key), f"artifactContract.{key}", errors, len(expected)))
        if actual != expected:
            fail(errors, f"artifactContract.{key} must contain every required value")


def validate_packet(
    packet: Any,
    index: int,
    promotion_tasks: dict[str, dict[str, Any]],
    local_reviews: dict[str, dict[str, Any]],
    seen_tasks: set[str],
    seen_artifacts: set[str],
    errors: list[str],
) -> None:
    if not isinstance(packet, dict):
        fail(errors, f"promotionPackets[{index}] must be an object")
        return
    missing = [field for field in REQUIRED_PACKET_FIELDS if field not in packet]
    if missing:
        fail(errors, f"promotionPackets[{index}] missing required fields: {', '.join(missing)}")

    task_id = require_string(packet.get("promotionTaskId"), f"promotionPackets[{index}].promotionTaskId", errors)
    if not task_id:
        return
    if task_id in seen_tasks:
        fail(errors, f"duplicate promotion packet: {task_id}")
    seen_tasks.add(task_id)

    source_task = promotion_tasks.get(task_id)
    if source_task is None:
        fail(errors, f"{task_id} has no matching promotion task")
        return
    for field in ["domainId", "domainClaimId", "fieldCardId", "sourceCardId", "sourceRole"]:
        if packet.get(field) != source_task.get(field):
            fail(errors, f"{task_id}.{field} must match promotion queue")

    source_id = require_string(packet.get("sourceCardId"), f"{task_id}.sourceCardId", errors)
    local_review = local_reviews.get(source_id)
    if local_review is None:
        fail(errors, f"{task_id}.sourceCardId has no local source-context review: {source_id}")
    else:
        if packet.get("sourceContextLocalReviewVerdict") != local_review.get("sourceContextVerdict"):
            fail(errors, f"{task_id}.sourceContextLocalReviewVerdict must match local review")
        expected_urls = sorted(
            item.get("url")
            for item in local_review.get("reviewEvidence", [])
            if isinstance(item, dict) and isinstance(item.get("url"), str)
        )
        actual_urls = sorted(require_string_list(packet.get("sourceContextLocalReviewEvidenceUrls"), f"{task_id}.sourceContextLocalReviewEvidenceUrls", errors, 1))
        if actual_urls != expected_urls:
            fail(errors, f"{task_id}.sourceContextLocalReviewEvidenceUrls must match local review evidence URLs")

    if packet.get("independentFreshReviewStatus") != "required-not-complete":
        fail(errors, f"{task_id}.independentFreshReviewStatus must be required-not-complete")
    if packet.get("artifactPackStatus") != "prepared-not-promoted":
        fail(errors, f"{task_id}.artifactPackStatus must be prepared-not-promoted")
    if packet.get("modelAdmissionDecision") != "blocked-pending-independent-review-card-promotion-downgrade-check-and-model-gates":
        fail(errors, f"{task_id}.modelAdmissionDecision must keep model admission blocked")

    artifact_ids = packet.get("artifactIds")
    if not isinstance(artifact_ids, dict):
        fail(errors, f"{task_id}.artifactIds must be an object")
    else:
        if set(artifact_ids) != REQUIRED_ARTIFACT_ID_FIELDS:
            fail(errors, f"{task_id}.artifactIds must contain every required artifact id field")
        for key, value in artifact_ids.items():
            artifact_id = require_string(value, f"{task_id}.artifactIds.{key}", errors)
            if artifact_id:
                if artifact_id in seen_artifacts:
                    fail(errors, f"duplicate artifact id: {artifact_id}")
                seen_artifacts.add(artifact_id)

    questions = packet.get("promotionQuestions")
    if not isinstance(questions, dict):
        fail(errors, f"{task_id}.promotionQuestions must be an object")
    else:
        if set(questions) != REQUIRED_PROMOTION_QUESTION_FIELDS:
            fail(errors, f"{task_id}.promotionQuestions must contain every required question field")
        for key in REQUIRED_PROMOTION_QUESTION_FIELDS:
            require_string(questions.get(key), f"{task_id}.promotionQuestions.{key}", errors)

    verdicts = set(require_string_list(packet.get("requiredReviewerVerdicts"), f"{task_id}.requiredReviewerVerdicts", errors, len(REQUIRED_REVIEWER_VERDICTS)))
    if verdicts != REQUIRED_REVIEWER_VERDICTS:
        fail(errors, f"{task_id}.requiredReviewerVerdicts must contain every required reviewer verdict")
    blocked = set(require_string_list(packet.get("blockedUses"), f"{task_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, f"{task_id}.blockedUses must contain every required blocked use")
    require_string(packet.get("nextAction"), f"{task_id}.nextAction", errors)


def validate_non_claims(data: dict[str, Any], errors: list[str]) -> None:
    non_claims = require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    joined = " ".join(non_claims)
    for phrase in [
        "independent fresh review",
        "prepared card artifact",
        "calibrated prediction",
        "model gates",
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

    promotion_tasks = load_promotion_tasks(errors)
    local_reviews = load_local_reviews(errors)

    validate_source_of_truth(data, errors)
    validate_required_fields(data, errors)

    packets = data.get("promotionPackets")
    if not isinstance(packets, list) or not packets:
        fail(errors, "promotionPackets must be a non-empty list")
        packets = []
    typed_packets = [packet for packet in packets if isinstance(packet, dict)]
    validate_scope(data, typed_packets, promotion_tasks, errors)

    seen_tasks: set[str] = set()
    seen_artifacts: set[str] = set()
    for index, packet in enumerate(packets):
        validate_packet(packet, index, promotion_tasks, local_reviews, seen_tasks, seen_artifacts, errors)
    if seen_tasks != set(promotion_tasks):
        fail(errors, "promotionPackets must cover exactly every promotion task")

    validate_non_claims(data, errors)
    validate_index_requirements(data, errors)
    domains = {packet.get("domainId") for packet in typed_packets if isinstance(packet.get("domainId"), str)}
    return len(seen_tasks), len(seen_artifacts), len(domains)


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "card promotion prep register")
    task_count = artifact_count = domain_count = 0
    if data:
        task_count, artifact_count, domain_count = validate_register(data, errors)

    if errors:
        print("card promotion prep register audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "card promotion prep register audit ok: "
        f"tasks={task_count} artifacts={artifact_count} domains={domain_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
