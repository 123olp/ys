#!/usr/bin/env python3
"""审计 C2 长尾第一批 source-specific 深读任务队列。"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-source-extraction-queue.json"
PROMOTION_QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-promotion-queue.json"

SCHEMA = "human-infra.c2-longtail-first-batch-source-extraction-queue.v1"
STATUS = "active-c2ltb1-source-specific-extraction-queue-model-blocked"
BATCH_ID = "C2-LT-B1"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-source-extraction-queue.json"

REQUIRED_TASK_FIELDS = [
    "taskId",
    "domainId",
    "sourceRefId",
    "sourceTitle",
    "sourceUrl",
    "evidenceRole",
    "domainClaimSeed",
    "variableSeed",
    "requiredExtractionSlots",
    "extractionQuestions",
    "taskStatus",
    "reviewState",
    "modelAdmissionDecision",
    "nextAction",
]

REQUIRED_EXTRACTION_SLOTS = {
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSetting",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "downgradeTriggers",
    "modelPosition",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}

TASK_ID_RE = re.compile(r"^C2LTB1-EXT-(\d{3})$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {label}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON in {label}: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{label} must be a JSON object")
        return {}
    return data


def require_string(value: Any, path: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{path} must be a non-empty string")
        return ""
    return value


def require_int(value: Any, path: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{path} must be integer")
        return None
    return value


def require_list(value: Any, path: str, errors: list[str], min_len: int = 0) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{path} must be a list with at least {min_len} item(s)")
        return []
    return value


def repo_path(relative_path: str, path: str, errors: list[str]) -> Path | None:
    rel = require_string(relative_path, path, errors)
    if not rel:
        return None
    if rel.startswith(("http://", "https://")):
        fail(errors, f"{path} must be a repository-local path")
        return None
    target = (ROOT / rel).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{path} escapes repository: {rel}")
        return None
    if not target.exists():
        fail(errors, f"{path} does not exist: {rel}")
        return None
    return target


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict) or not source:
        fail(errors, "sourceOfTruth must be a non-empty object")
        return
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def promotion_maps(promotion: dict[str, Any], errors: list[str]) -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], dict[str, Any]]]:
    rows = promotion.get("batchRows")
    if not isinstance(rows, list) or not rows:
        fail(errors, "promotion queue batchRows must be a non-empty list")
        return ({}, {})
    domain_map: dict[str, dict[str, Any]] = {}
    source_map: dict[tuple[str, str], dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"promotion batchRows[{index}] must be an object")
            continue
        domain_id = row.get("domainId")
        if not isinstance(domain_id, str) or not domain_id:
            fail(errors, f"promotion batchRows[{index}].domainId missing")
            continue
        domain_map[domain_id] = row
        sources = row.get("candidateSourceRefs")
        if not isinstance(sources, list) or not sources:
            fail(errors, f"{domain_id}.candidateSourceRefs must be non-empty")
            continue
        for source in sources:
            if not isinstance(source, dict):
                fail(errors, f"{domain_id}.candidateSourceRefs contains non-object")
                continue
            source_id = source.get("sourceRefId")
            if not isinstance(source_id, str) or not source_id:
                fail(errors, f"{domain_id}.candidateSourceRefs sourceRefId missing")
                continue
            source_map[(domain_id, source_id)] = source
    return (domain_map, source_map)


def validate_scope(data: dict[str, Any], domains: int, tasks: int, errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("derivedTaskUnit") != "domainId + sourceRefId":
        fail(errors, "scope.derivedTaskUnit must be domainId + sourceRefId")
    expected = {
        "coveredDomainCount": domains,
        "candidateSourceCount": tasks,
        "expectedTaskCount": tasks,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    require_string(scope.get("coverageLevel"), "scope.coverageLevel", errors)
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_defaults(data: dict[str, Any], errors: list[str]) -> None:
    defaults = data.get("queueDefaults")
    if not isinstance(defaults, dict):
        fail(errors, "queueDefaults must be an object")
        return
    if defaults.get("taskStatus") != "queued-source-specific-extraction-required":
        fail(errors, "queueDefaults.taskStatus must be queued-source-specific-extraction-required")
    if defaults.get("reviewState") != "not-read-source-context":
        fail(errors, "queueDefaults.reviewState must be not-read-source-context")
    decision = require_string(defaults.get("modelAdmissionDecision"), "queueDefaults.modelAdmissionDecision", errors)
    if decision and "blocked" not in decision:
        fail(errors, "queueDefaults.modelAdmissionDecision must contain blocked")
    blocked = set(require_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors, 4))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, f"queueDefaults.blockedUses must be {sorted(REQUIRED_BLOCKED_USES)}")
    require_string(defaults.get("minimumExtractionQuestion"), "queueDefaults.minimumExtractionQuestion", errors)


def validate_summary(
    data: dict[str, Any],
    domains: int,
    tasks: int,
    domain_map: dict[str, dict[str, Any]],
    rows: list[dict[str, Any]],
    errors: list[str],
) -> None:
    summary = data.get("derivedQueueSummary")
    if not isinstance(summary, dict):
        fail(errors, "derivedQueueSummary must be an object")
        return
    expected = {
        "coveredDomainCount": domains,
        "derivedTaskCount": tasks,
        "uniqueSourceRefCount": tasks,
    }
    for key, value in expected.items():
        actual = require_int(summary.get(key), f"derivedQueueSummary.{key}", errors)
        if actual != value:
            fail(errors, f"derivedQueueSummary.{key} must equal {value}")
    triage_counts = Counter(row.get("triageBucket") for row in domain_map.values())
    if summary.get("triageBucketCounts") != dict(triage_counts):
        fail(errors, "derivedQueueSummary.triageBucketCounts does not match tasks")
    role_counts = Counter(row.get("evidenceRole") for row in rows)
    if summary.get("sourceRoleCounts") != dict(role_counts):
        fail(errors, "derivedQueueSummary.sourceRoleCounts does not match tasks")
    require_string(summary.get("fieldCompletionState"), "derivedQueueSummary.fieldCompletionState", errors)
    require_list(summary.get("remainingWork"), "derivedQueueSummary.remainingWork", errors, 3)


def validate_task(
    task: Any,
    index: int,
    domain_map: dict[str, dict[str, Any]],
    source_map: dict[tuple[str, str], dict[str, Any]],
    seen_task_ids: set[str],
    seen_pairs: set[tuple[str, str]],
    errors: list[str],
) -> dict[str, Any] | None:
    path = f"extractionTasks[{index}]"
    if not isinstance(task, dict):
        fail(errors, f"{path} must be an object")
        return None
    task_id = require_string(task.get("taskId"), f"{path}.taskId", errors)
    match = TASK_ID_RE.match(task_id)
    if not match:
        fail(errors, f"{path}.taskId must match C2LTB1-EXT-###")
    elif int(match.group(1)) != index + 1:
        fail(errors, f"{path}.taskId sequence must be {index + 1:03d}")
    if task_id in seen_task_ids:
        fail(errors, f"duplicate taskId: {task_id}")
    seen_task_ids.add(task_id)

    if task.get("batchId") != BATCH_ID:
        fail(errors, f"{path}.batchId must be {BATCH_ID}")
    domain_id = require_string(task.get("domainId"), f"{path}.domainId", errors)
    source_id = require_string(task.get("sourceRefId"), f"{path}.sourceRefId", errors)
    if not domain_id or not source_id:
        return None
    pair = (domain_id, source_id)
    if pair in seen_pairs:
        fail(errors, f"duplicate domain/source task: {domain_id}/{source_id}")
    seen_pairs.add(pair)

    domain = domain_map.get(domain_id)
    source = source_map.get(pair)
    if domain is None:
        fail(errors, f"{path}.domainId not found in promotion queue: {domain_id}")
        return None
    if source is None:
        fail(errors, f"{path}.sourceRefId not found under promotion domain: {domain_id}/{source_id}")
        return None

    for key in ["triageBucket", "localDomainPath"]:
        if task.get(key) != domain.get(key):
            fail(errors, f"{path}.{key} does not match promotion queue")
    domain_dir = repo_path(task.get("localDomainPath"), f"{path}.localDomainPath", errors)
    if domain_dir is not None:
        for filename in ["README.md", "AGENTS.md"]:
            if not (domain_dir / filename).exists():
                fail(errors, f"{domain_id} missing {filename}")
    if task.get("promotionPriorityRank") != domain.get("priorityRank"):
        fail(errors, f"{path}.promotionPriorityRank does not match promotion queue")
    if task.get("sourceTitle") != source.get("title"):
        fail(errors, f"{path}.sourceTitle does not match promotion queue")
    if task.get("sourceUrl") != source.get("url"):
        fail(errors, f"{path}.sourceUrl does not match promotion queue")
    if task.get("evidenceRole") != source.get("evidenceRole"):
        fail(errors, f"{path}.evidenceRole does not match promotion queue")
    if task.get("sourceCandidateStatus") != source.get("reviewStatus"):
        fail(errors, f"{path}.sourceCandidateStatus does not match promotion queue")
    if task.get("domainClaimSeed") != domain.get("claimSeed"):
        fail(errors, f"{path}.domainClaimSeed does not match promotion queue")
    if task.get("variableSeed") != domain.get("variableSeed"):
        fail(errors, f"{path}.variableSeed does not match promotion queue")

    url = require_string(task.get("sourceUrl"), f"{path}.sourceUrl", errors)
    if url and not url.startswith(("https://", "http://")):
        fail(errors, f"{path}.sourceUrl must be a URL")
    if set(require_list(task.get("requiredExtractionSlots"), f"{path}.requiredExtractionSlots", errors, 8)) != REQUIRED_EXTRACTION_SLOTS:
        fail(errors, f"{path}.requiredExtractionSlots must be {sorted(REQUIRED_EXTRACTION_SLOTS)}")
    questions = require_list(task.get("extractionQuestions"), f"{path}.extractionQuestions", errors, 8)
    if len(questions) != len(REQUIRED_EXTRACTION_SLOTS):
        fail(errors, f"{path}.extractionQuestions must match extraction slot count")
    if task.get("taskStatus") != "queued-source-specific-extraction-required":
        fail(errors, f"{path}.taskStatus must be queued-source-specific-extraction-required")
    if task.get("reviewState") != "not-read-source-context":
        fail(errors, f"{path}.reviewState must be not-read-source-context")
    require_string(task.get("urlAccessPolicy"), f"{path}.urlAccessPolicy", errors)
    if set(require_list(task.get("blockedUses"), f"{path}.blockedUses", errors, 4)) != REQUIRED_BLOCKED_USES:
        fail(errors, f"{path}.blockedUses must be {sorted(REQUIRED_BLOCKED_USES)}")
    decision = require_string(task.get("modelAdmissionDecision"), f"{path}.modelAdmissionDecision", errors)
    if decision and "blocked" not in decision:
        fail(errors, f"{path}.modelAdmissionDecision must contain blocked")
    require_string(task.get("nextAction"), f"{path}.nextAction", errors)
    return task


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_list(paths, "indexRequirements", errors, 2):
        if not isinstance(relative_path, str):
            fail(errors, "indexRequirements must contain strings")
            continue
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index does not link source extraction queue: {relative_path}")


def main() -> int:
    errors: list[str] = []
    queue = load_json(QUEUE_PATH, errors, "C2 longtail first-batch source extraction queue")
    promotion = load_json(PROMOTION_QUEUE_PATH, errors, "C2 longtail first-batch promotion queue")
    domain_map, source_map = promotion_maps(promotion, errors)

    if queue:
        if queue.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if queue.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(queue.get("queueId"), "queueId", errors)
        require_string(queue.get("purpose"), "purpose", errors)
        validate_source_of_truth(queue, errors)

    tasks_raw = queue.get("extractionTasks") if queue else None
    if not isinstance(tasks_raw, list) or not tasks_raw:
        fail(errors, "extractionTasks must be a non-empty list")
        tasks_raw = []
    if len(tasks_raw) != len(source_map):
        fail(errors, f"extractionTasks must derive exactly {len(source_map)} promotion sources")

    rows: list[dict[str, Any]] = []
    seen_task_ids: set[str] = set()
    seen_pairs: set[tuple[str, str]] = set()
    for index, task in enumerate(tasks_raw):
        valid = validate_task(task, index, domain_map, source_map, seen_task_ids, seen_pairs, errors)
        if valid is not None:
            rows.append(valid)

    if set(seen_pairs) != set(source_map):
        missing = sorted(set(source_map) - set(seen_pairs))
        extra = sorted(set(seen_pairs) - set(source_map))
        if missing:
            fail(errors, f"missing promotion source tasks: {missing[:5]}")
        if extra:
            fail(errors, f"extra source tasks not in promotion queue: {extra[:5]}")

    if queue:
        validate_scope(queue, len(domain_map), len(source_map), errors)
        if require_list(queue.get("requiredPerTaskFields"), "requiredPerTaskFields", errors, len(REQUIRED_TASK_FIELDS)) != REQUIRED_TASK_FIELDS:
            fail(errors, "requiredPerTaskFields must exactly match the extraction queue contract")
        validate_defaults(queue, errors)
        validate_summary(queue, len(domain_map), len(source_map), domain_map, rows, errors)
        non_claims = require_list(queue.get("nonClaims"), "nonClaims", errors, 4)
        joined = " ".join(str(item) for item in non_claims)
        for phrase in ["does not complete source-specific reading", "does not complete independent fresh review", "does not authorize calibrated prediction"]:
            if phrase not in joined:
                fail(errors, f"nonClaims must include phrase: {phrase}")
        validate_index_links(queue.get("indexRequirements"), errors)

    if errors:
        for message in errors:
            print(f"ERROR: {message}", file=sys.stderr)
        return 1

    print(
        "C2 longtail first-batch source extraction queue audit ok: "
        f"batch={BATCH_ID} domains={len(domain_map)} tasks={len(rows)} sources={len(source_map)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
