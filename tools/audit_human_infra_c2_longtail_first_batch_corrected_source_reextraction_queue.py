#!/usr/bin/env python3
"""审计 C2-LT-B1 corrected source re-extraction 队列。"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json"
SOURCE_RESOLUTION_REVIEW_PATH = (
    ROOT
    / "docs/reference/human-infra-c2-longtail-first-batch-source-resolution-fresh-review-verdict-register.json"
)

SCHEMA = "human-infra.c2ltb1-corrected-source-reextraction-queue.v1"
STATUS = "active-c2ltb1-corrected-source-reextraction-queue-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_queue.py"
BATCH_ID = "C2-LT-B1"
TASK_ID_RE = re.compile(r"^C2LTB1-CREXT-(\d{3})$")

SOURCE_OF_TRUTH_KEYS = {
    "sourceResolutionFreshReviewVerdictRegister",
    "blockedSourceResolutionRegister",
    "originalFreshReviewVerdictRegister",
    "sourceExtractionRegister",
    "reviewedCardArtifactRegister",
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

REQUIRED_REEXTRACTION_SLOTS = {
    "sourceIdentityCorrection",
    "currentnessBoundary",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSetting",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "downgradeTriggers",
    "modelPosition",
    "artifactPromotionReadiness",
}

REQUIRED_TASK_FIELDS = {
    "taskId",
    "batchId",
    "originTaskId",
    "sourceResolutionReviewId",
    "domainId",
    "localDomainPath",
    "priorReviewerVerdict",
    "priorArtifactPromotionDecision",
    "sourceResolutionReviewerVerdict",
    "candidateId",
    "candidateRole",
    "sourceTitle",
    "sourceUrl",
    "sourceType",
    "reextractionRole",
    "reextractionAction",
    "routeSplitPolicy",
    "sourceResolutionFinding",
    "freshReviewFinding",
    "useBoundary",
    "requiredReextractionSlots",
    "reextractionQuestions",
    "taskStatus",
    "reviewState",
    "artifactPromotionDecision",
    "modelAdmissionDecision",
    "blockedUses",
    "nextAction",
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


def validate_source_of_truth(queue: dict[str, Any], errors: list[str]) -> None:
    source = queue.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        value = source.get(key)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def selected_candidates(source_resolution_review: dict[str, Any], errors: list[str]) -> tuple[dict[tuple[str, str], dict[str, Any]], int, int]:
    reviews = source_resolution_review.get("sourceResolutionFreshReviews")
    if not isinstance(reviews, list):
        fail(errors, "source-resolution fresh review register missing reviews")
        return ({}, 0, 0)
    selected: dict[tuple[str, str], dict[str, Any]] = {}
    route_only_count = 0
    for review in reviews:
        if not isinstance(review, dict):
            continue
        route_only = review.get("routeOnlyOrContextCandidates")
        if isinstance(route_only, list):
            route_only_count += len(route_only)
        verdicts = {
            candidate.get("candidateId"): candidate
            for candidate in review.get("candidateVerdicts", [])
            if isinstance(candidate, dict)
        }
        for candidate_id in review.get("selectedResolutionCandidates", []):
            candidate = verdicts.get(candidate_id)
            if isinstance(candidate, dict):
                selected[(review.get("reviewId"), candidate_id)] = {
                    "review": review,
                    "candidate": candidate,
                }
    return (selected, len(reviews), route_only_count)


def validate_scope(
    queue: dict[str, Any],
    tasks: list[dict[str, Any]],
    review_count: int,
    route_only_count: int,
    errors: list[str],
) -> None:
    scope = queue.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("queueLevel") != "c2ltb1-corrected-source-reextraction-v0.1":
        fail(errors, "scope.queueLevel is invalid")
    expected = {
        "sourceResolutionReviewedRowCount": review_count,
        "selectedCorrectedCandidateCount": len(tasks),
        "routeOnlyOrContextCandidateCount": route_only_count,
        "derivedTaskCount": len(tasks),
        "directArtifactFillTaskCount": 0,
        "modelAdmissionOpenedTaskCount": 0,
    }
    candidate_total = require_int(scope.get("sourceResolutionCandidateCount"), "scope.sourceResolutionCandidateCount", errors)
    if candidate_total is not None and candidate_total != len(tasks) + route_only_count:
        fail(errors, "scope.sourceResolutionCandidateCount must equal selected + route-only counts")
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, min_len=4)


def validate_defaults(queue: dict[str, Any], errors: list[str]) -> None:
    defaults = queue.get("queueDefaults")
    if not isinstance(defaults, dict):
        fail(errors, "queueDefaults must be an object")
        return
    expected = {
        "taskStatus": "queued-corrected-source-reextraction-required",
        "reviewState": "source-resolution-fresh-reviewed-not-reextracted",
        "artifactPromotionDecision": "blocked-pending-corrected-source-reextraction-output-and-independent-review",
        "modelAdmissionDecision": "blocked",
    }
    for key, value in expected.items():
        if defaults.get(key) != value:
            fail(errors, f"queueDefaults.{key} must be {value}")
    blocked = set(require_string_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, "queueDefaults.blockedUses must match required blocked uses")
    require_string(defaults.get("minimumReextractionQuestion"), "queueDefaults.minimumReextractionQuestion", errors)


def validate_tasks(
    tasks: Any,
    selected: dict[tuple[str, str], dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    if not isinstance(tasks, list):
        fail(errors, "reextractionTasks must be a list")
        return []
    seen_task_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    valid_tasks: list[dict[str, Any]] = []
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"reextractionTasks[{index}] must be an object")
            continue
        missing = REQUIRED_TASK_FIELDS - set(task)
        if missing:
            fail(errors, f"reextractionTasks[{index}] missing fields: {sorted(missing)}")
        task_id = require_string(task.get("taskId"), f"reextractionTasks[{index}].taskId", errors)
        match = TASK_ID_RE.match(task_id)
        if not match:
            fail(errors, f"{task_id}.taskId must match C2LTB1-CREXT-###")
        elif int(match.group(1)) != index + 1:
            fail(errors, f"{task_id}.taskId sequence must be {index + 1:03d}")
        if task_id in seen_task_ids:
            fail(errors, f"duplicate taskId: {task_id}")
        seen_task_ids.add(task_id)

        if task.get("batchId") != BATCH_ID:
            fail(errors, f"{task_id}.batchId must be {BATCH_ID}")
        if task.get("taskStatus") != "queued-corrected-source-reextraction-required":
            fail(errors, f"{task_id}.taskStatus is invalid")
        if task.get("reviewState") != "source-resolution-fresh-reviewed-not-reextracted":
            fail(errors, f"{task_id}.reviewState is invalid")
        if task.get("artifactPromotionDecision") != "blocked-pending-corrected-source-reextraction-output-and-independent-review":
            fail(errors, f"{task_id}.artifactPromotionDecision must remain blocked")
        if task.get("modelAdmissionDecision") != "blocked":
            fail(errors, f"{task_id}.modelAdmissionDecision must be blocked")
        if set(require_string_list(task.get("blockedUses"), f"{task_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{task_id}.blockedUses must match required blocked uses")
        if set(require_string_list(task.get("requiredReextractionSlots"), f"{task_id}.requiredReextractionSlots", errors)) != REQUIRED_REEXTRACTION_SLOTS:
            fail(errors, f"{task_id}.requiredReextractionSlots must match required slots")
        require_string_list(task.get("reextractionQuestions"), f"{task_id}.reextractionQuestions", errors, min_len=10)
        source_url = require_string(task.get("sourceUrl"), f"{task_id}.sourceUrl", errors)
        if source_url and not source_url.startswith("https://"):
            fail(errors, f"{task_id}.sourceUrl must be https")

        review_id = require_string(task.get("sourceResolutionReviewId"), f"{task_id}.sourceResolutionReviewId", errors)
        candidate_id = require_string(task.get("candidateId"), f"{task_id}.candidateId", errors)
        pair = (review_id, candidate_id)
        if pair not in selected:
            fail(errors, f"{task_id} is not derived from selected source-resolution candidate")
        else:
            review = selected[pair]["review"]
            candidate = selected[pair]["candidate"]
            for task_key, review_key in {
                "originTaskId": "taskId",
                "domainId": "domainId",
                "localDomainPath": "localDomainPath",
                "priorReviewerVerdict": "priorReviewerVerdict",
                "priorArtifactPromotionDecision": "priorArtifactPromotionDecision",
                "sourceResolutionReviewerVerdict": "sourceResolutionReviewerVerdict",
                "sourceResolutionFinding": "sourceResolutionFinding",
            }.items():
                if task.get(task_key) != review.get(review_key):
                    fail(errors, f"{task_id}.{task_key} does not match source-resolution review")
            if task.get("candidateRole") != candidate.get("candidateRole"):
                fail(errors, f"{task_id}.candidateRole does not match source-resolution candidate")
            if task.get("freshReviewFinding") != candidate.get("freshReviewFinding"):
                fail(errors, f"{task_id}.freshReviewFinding does not match source-resolution candidate")
        if pair in seen_pairs:
            fail(errors, f"duplicate sourceResolutionReviewId+candidateId pair: {pair}")
        seen_pairs.add(pair)
        valid_tasks.append(task)

    if seen_pairs != set(selected):
        fail(errors, "reextractionTasks must cover exactly the selected source-resolution candidates")
    return valid_tasks


def validate_summary(
    queue: dict[str, Any],
    tasks: list[dict[str, Any]],
    review_count: int,
    route_only_count: int,
    errors: list[str],
) -> None:
    summary = queue.get("derivedQueueSummary")
    if not isinstance(summary, dict):
        fail(errors, "derivedQueueSummary must be an object")
        return
    expected = {
        "sourceResolutionReviewedRowCount": review_count,
        "derivedTaskCount": len(tasks),
        "uniqueOriginTaskCount": len({task.get("originTaskId") for task in tasks}),
        "selectedCorrectedCandidateCount": len(tasks),
        "routeOnlyOrContextCandidateCount": route_only_count,
        "domainCount": len({task.get("domainId") for task in tasks}),
    }
    for key, value in expected.items():
        actual = require_int(summary.get(key), f"derivedQueueSummary.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"derivedQueueSummary.{key} must equal {value}")
    if summary.get("reextractionRoleCounts") != dict(Counter(task.get("reextractionRole") for task in tasks)):
        fail(errors, "derivedQueueSummary.reextractionRoleCounts does not match tasks")
    if summary.get("originTaskCounts") != dict(Counter(task.get("originTaskId") for task in tasks)):
        fail(errors, "derivedQueueSummary.originTaskCounts does not match tasks")
    if summary.get("fieldCompletionState") != "queue-derived-not-corrected-source-reextracted":
        fail(errors, "derivedQueueSummary.fieldCompletionState is invalid")
    require_string_list(summary.get("remainingWork"), "derivedQueueSummary.remainingWork", errors, min_len=4)


def validate_index_links(queue: dict[str, Any], errors: list[str]) -> None:
    if queue.get("indexRequirements") != REQUIRED_INDEX_FILES:
        fail(errors, "indexRequirements must match required index file list")
    for relative_path in REQUIRED_INDEX_FILES:
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index file does not reference queue: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    queue = load_json(QUEUE_PATH, errors, "corrected source re-extraction queue")
    source_resolution_review = load_json(
        SOURCE_RESOLUTION_REVIEW_PATH,
        errors,
        "source-resolution fresh review verdict register",
    )
    selected, review_count, route_only_count = selected_candidates(source_resolution_review, errors)

    if queue:
        if queue.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if queue.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(queue.get("queueId"), "queueId", errors)
        require_string(queue.get("purpose"), "purpose", errors)
        validate_source_of_truth(queue, errors)
        tasks = validate_tasks(queue.get("reextractionTasks"), selected, errors)
        validate_scope(queue, tasks, review_count, route_only_count, errors)
        validate_defaults(queue, errors)
        validate_summary(queue, tasks, review_count, route_only_count, errors)
        validate_index_links(queue, errors)
        non_claims = "\n".join(require_string_list(queue.get("nonClaims"), "nonClaims", errors, min_len=4))
        for phrase in ("does not complete corrected source re-extraction", "does not create reviewed artifacts", "does not authorize"):
            if phrase not in non_claims:
                fail(errors, f"nonClaims missing phrase: {phrase}")

    if errors:
        print("C2-LT-B1 corrected source re-extraction queue audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B1 corrected source re-extraction queue audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
