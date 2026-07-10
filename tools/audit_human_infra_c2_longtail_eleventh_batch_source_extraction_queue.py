#!/usr/bin/env python3
"""审计 C2 长尾第十一批 source-specific 深读任务队列。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json"
PROMOTION_QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eleventh-batch-promotion-queue.json"

SCHEMA = "human-infra.c2-longtail-eleventh-batch-source-extraction-queue.v1"
STATUS = "active-c2ltb11-source-specific-extraction-queue-model-blocked"
BATCH_ID = "C2-LT-B11"
EXPECTED_DOMAINS = 12
EXPECTED_TASKS = 24
TASK_ID_RE = re.compile(r"^C2LTB11-EXT-(\d{3})$")

REQUIRED_TASK_FIELDS = {
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
}
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
REQUIRED_INDEX_LINKS = {
    "docs/AGENTS.md": "human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json",
    "docs/reference/README.md": "human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json",
    "docs/reference/human-infra-maturity-roadmap.md": "human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json",
    "docs/reference/human-infra-maturity-gap-register.json": "human-infra-c2-longtail-eleventh-batch-source-extraction-queue.json",
    "Makefile": "c2-longtail-eleventh-batch-source-extraction-audit",
    "tools/README.md": "audit_human_infra_c2_longtail_eleventh_batch_source_extraction_queue.py",
    "tools/AGENTS.md": "audit_human_infra_c2_longtail_eleventh_batch_source_extraction_queue.py",
}


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


def require_list(value: Any, path: str, errors: list[str], min_len: int = 0) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{path} must be a list with at least {min_len} item(s)")
        return []
    return value


def repo_path(relative_path: Any, path: str, errors: list[str]) -> Path | None:
    rel = require_string(relative_path, path, errors)
    if not rel:
        return None
    if rel.startswith(("http://", "https://")):
        fail(errors, f"{path} must be repository-local path")
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
            if isinstance(source, dict) and isinstance(source.get("sourceRefId"), str):
                source_map[(domain_id, source["sourceRefId"])] = source
    return domain_map, source_map


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        if needle not in path.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must reference {needle}")


def validate_scope(data: dict[str, Any], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "batchId": BATCH_ID,
        "derivedTaskUnit": "domainId + sourceRefId",
        "coveredDomainCount": EXPECTED_DOMAINS,
        "candidateSourceCount": EXPECTED_TASKS,
        "expectedTaskCount": EXPECTED_TASKS,
    }
    for key, value in expected.items():
        if scope.get(key) != value:
            fail(errors, f"scope.{key} must equal {value!r}")
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
    if "blocked" not in require_string(defaults.get("modelAdmissionDecision"), "queueDefaults.modelAdmissionDecision", errors):
        fail(errors, "queueDefaults.modelAdmissionDecision must contain blocked")
    if set(require_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "queueDefaults.blockedUses must match required blocked-use set")
    require_string(defaults.get("minimumExtractionQuestion"), "queueDefaults.minimumExtractionQuestion", errors)


def validate_task(
    task: Any,
    index: int,
    domain_map: dict[str, dict[str, Any]],
    source_map: dict[tuple[str, str], dict[str, Any]],
    seen_task_ids: set[str],
    seen_pairs: set[tuple[str, str]],
    errors: list[str],
) -> None:
    if not isinstance(task, dict):
        fail(errors, f"extractionTasks[{index}] must be an object")
        return
    missing = REQUIRED_TASK_FIELDS - set(task)
    if missing:
        fail(errors, f"extractionTasks[{index}] missing required fields: {sorted(missing)}")
    task_id = require_string(task.get("taskId"), f"extractionTasks[{index}].taskId", errors)
    match = TASK_ID_RE.match(task_id)
    if not match:
        fail(errors, f"extractionTasks[{index}].taskId must match C2LTB11-EXT-###")
    elif int(match.group(1)) != index + 1:
        fail(errors, f"extractionTasks[{index}].taskId sequence must be {index + 1:03d}")
    if task_id in seen_task_ids:
        fail(errors, f"duplicate taskId: {task_id}")
    seen_task_ids.add(task_id)
    if task.get("batchId") != BATCH_ID:
        fail(errors, f"{task_id}.batchId must be {BATCH_ID}")
    domain_id = require_string(task.get("domainId"), f"{task_id}.domainId", errors)
    source_id = require_string(task.get("sourceRefId"), f"{task_id}.sourceRefId", errors)
    pair = (domain_id, source_id)
    if pair in seen_pairs:
        fail(errors, f"duplicate domain/source task pair: {pair}")
    seen_pairs.add(pair)
    promotion_row = domain_map.get(domain_id)
    source_ref = source_map.get(pair)
    if not promotion_row:
        fail(errors, f"{task_id} references unknown promotion domain: {domain_id}")
    if not source_ref:
        fail(errors, f"{task_id} references unknown promotion source: {source_id}")
    if promotion_row and task.get("domainClaimSeed") != promotion_row.get("claimSeed"):
        fail(errors, f"{task_id}.domainClaimSeed must match promotion claimSeed")
    if promotion_row and task.get("variableSeed") != promotion_row.get("variableSeed"):
        fail(errors, f"{task_id}.variableSeed must match promotion variableSeed")
    if source_ref:
        if task.get("sourceTitle") != source_ref.get("title"):
            fail(errors, f"{task_id}.sourceTitle must match promotion source title")
        if task.get("sourceUrl") != source_ref.get("url"):
            fail(errors, f"{task_id}.sourceUrl must match promotion source URL")
        if task.get("evidenceRole") != source_ref.get("evidenceRole"):
            fail(errors, f"{task_id}.evidenceRole must match promotion evidenceRole")
    if set(require_list(task.get("requiredExtractionSlots"), f"{task_id}.requiredExtractionSlots", errors)) != REQUIRED_EXTRACTION_SLOTS:
        fail(errors, f"{task_id}.requiredExtractionSlots must match required slot set")
    if len(require_list(task.get("extractionQuestions"), f"{task_id}.extractionQuestions", errors, 7)) < 7:
        fail(errors, f"{task_id}.extractionQuestions must contain at least 7 questions")
    if task.get("taskStatus") != "queued-source-specific-extraction-required":
        fail(errors, f"{task_id}.taskStatus must be queued-source-specific-extraction-required")
    if task.get("reviewState") != "not-read-source-context":
        fail(errors, f"{task_id}.reviewState must be not-read-source-context")
    if "blocked" not in require_string(task.get("modelAdmissionDecision"), f"{task_id}.modelAdmissionDecision", errors):
        fail(errors, f"{task_id}.modelAdmissionDecision must contain blocked")
    require_string(task.get("nextAction"), f"{task_id}.nextAction", errors)


def main() -> int:
    errors: list[str] = []
    data = load_json(QUEUE_PATH, errors, "C2-LT-B11 source extraction queue")
    promotion = load_json(PROMOTION_QUEUE_PATH, errors, "C2-LT-B11 promotion queue")
    domain_map, source_map = promotion_maps(promotion, errors)

    if data:
        if data.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if data.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        source = data.get("sourceOfTruth")
        if not isinstance(source, dict) or not source:
            fail(errors, "sourceOfTruth must be a non-empty object")
        else:
            for key, value in source.items():
                repo_path(value, f"sourceOfTruth.{key}", errors)
        validate_scope(data, errors)
        validate_defaults(data, errors)
        if set(require_list(data.get("requiredPerTaskFields"), "requiredPerTaskFields", errors)) != REQUIRED_TASK_FIELDS:
            fail(errors, "requiredPerTaskFields must match required task field set")
        tasks = data.get("extractionTasks")
        if not isinstance(tasks, list) or len(tasks) != EXPECTED_TASKS:
            fail(errors, f"extractionTasks must contain {EXPECTED_TASKS} tasks")
            tasks = []
        seen_task_ids: set[str] = set()
        seen_pairs: set[tuple[str, str]] = set()
        for index, task in enumerate(tasks):
            validate_task(task, index, domain_map, source_map, seen_task_ids, seen_pairs, errors)
        if set(seen_pairs) != set(source_map):
            missing = sorted(set(source_map) - seen_pairs)
            extra = sorted(seen_pairs - set(source_map))
            fail(errors, f"task pairs must equal promotion source pairs; missing={missing} extra={extra}")
        summary = data.get("derivedQueueSummary")
        if not isinstance(summary, dict):
            fail(errors, "derivedQueueSummary must be an object")
        else:
            expected = {"coveredDomainCount": EXPECTED_DOMAINS, "derivedTaskCount": EXPECTED_TASKS, "uniqueSourceRefCount": EXPECTED_TASKS}
            for key, value in expected.items():
                if summary.get(key) != value:
                    fail(errors, f"derivedQueueSummary.{key} must equal {value}")
            if summary.get("modelAdmission") != "blocked":
                fail(errors, "derivedQueueSummary.modelAdmission must be blocked")
        non_claims = " ".join(str(item) for item in require_list(data.get("nonClaims"), "nonClaims", errors, 3))
        for phrase in ["does not mean the sources have been read in context", "does not create reviewed artifacts", "does not resolve any prior B1-B10 blocked row"]:
            if phrase not in non_claims:
                fail(errors, f"nonClaims missing phrase: {phrase}")

    validate_index_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"C2-LT-B11 source extraction queue audit ok: domains={EXPECTED_DOMAINS} tasks={EXPECTED_TASKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
