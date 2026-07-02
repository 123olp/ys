#!/usr/bin/env python3
"""审计 C2-LT-B1 corrected source re-extraction 完成寄存器。"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-first-batch-corrected-source-reextraction-queue.json"

SCHEMA = "human-infra.c2ltb1-corrected-source-reextraction-register.v1"
STATUS = "active-c2ltb1-corrected-source-reextracted-model-blocked"
REGISTER_LINK = "human-infra-c2-longtail-first-batch-corrected-source-reextraction-register.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_first_batch_corrected_source_reextraction_register.py"
BATCH_ID = "C2-LT-B1"

SOURCE_OF_TRUTH_KEYS = {
    "correctedSourceReextractionQueue",
    "sourceResolutionFreshReviewVerdictRegister",
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

REQUIRED_ROW_FIELDS = {
    "reextractionTaskId",
    "originTaskId",
    "sourceResolutionReviewId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "sourceTitle",
    "sourceUrl",
    "extractionStatus",
    "sourceAccessStatus",
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
    "modelAdmissionDecision",
    "blockedUses",
    "sourceEvidenceTrace",
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

ROUTE_ONLY_PROMOTION_STATES = {
    "route-only-no-direct-artifact-promotion",
    "fulltext-needed-no-direct-artifact-promotion",
    "downgraded-source-index-only-independent-direct-review-required",
    "context-only-independent-review-required-no-direct-artifact-fill",
}


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


def queue_tasks(queue: dict[str, Any], errors: list[str]) -> dict[str, dict[str, Any]]:
    tasks = queue.get("reextractionTasks")
    if not isinstance(tasks, list):
        fail(errors, "queue.reextractionTasks must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"queue.reextractionTasks[{index}] must be an object")
            continue
        task_id = require_string(task.get("taskId"), f"queue.reextractionTasks[{index}].taskId", errors)
        if task_id in result:
            fail(errors, f"duplicate queue taskId: {task_id}")
        result[task_id] = task
    return result


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


def validate_scope(register: dict[str, Any], rows: list[dict[str, Any]], queue_task_count: int, errors: list[str]) -> None:
    scope = register.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    expected = {
        "queueTaskCount": queue_task_count,
        "reextractedRowCount": len(rows),
        "directArtifactFillCount": 0,
        "modelAdmissionOpenedCount": 0,
    }
    for key, value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != value:
            fail(errors, f"scope.{key} must equal {value}")
    candidate_count = require_int(scope.get("boundedFreshReviewCandidateCount"), "scope.boundedFreshReviewCandidateCount", errors)
    route_count = require_int(scope.get("routeOrIndexOnlyCount"), "scope.routeOrIndexOnlyCount", errors)
    if candidate_count is not None and route_count is not None and candidate_count + route_count != len(rows):
        fail(errors, "scope bounded candidate + route-only counts must equal row count")
    require_string(scope.get("extractionLimit"), "scope.extractionLimit", errors)


def validate_evidence_trace(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        fail(errors, f"{context} must be a non-empty list")
        return
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"{context}[{index}] must be an object")
            continue
        url = require_string(item.get("url"), f"{context}[{index}].url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}[{index}].url must be https")
        require_string(item.get("evidenceType"), f"{context}[{index}].evidenceType", errors)
        require_string(item.get("finding"), f"{context}[{index}].finding", errors)


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context} must be an object")
        return
    require_string(value.get("primaryLocation"), f"{context}.primaryLocation", errors)
    require_string_list(value.get("variables"), f"{context}.variables", errors, min_len=2)
    require_string(value.get("admissibleUse"), f"{context}.admissibleUse", errors)


def validate_rows(register: dict[str, Any], queued: dict[str, dict[str, Any]], errors: list[str]) -> list[dict[str, Any]]:
    rows = register.get("extractedRows")
    if not isinstance(rows, list):
        fail(errors, "extractedRows must be a list")
        return []
    seen: set[str] = set()
    valid_rows: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        missing = REQUIRED_ROW_FIELDS - set(row)
        if missing:
            fail(errors, f"extractedRows[{index}] missing fields: {sorted(missing)}")
        task_id = require_string(row.get("reextractionTaskId"), f"extractedRows[{index}].reextractionTaskId", errors)
        if task_id in seen:
            fail(errors, f"duplicate reextractionTaskId: {task_id}")
        seen.add(task_id)
        queued_task = queued.get(task_id)
        if not queued_task:
            fail(errors, f"{task_id} is not derived from corrected source re-extraction queue")
        else:
            for row_key, queue_key in {
                "originTaskId": "originTaskId",
                "sourceResolutionReviewId": "sourceResolutionReviewId",
                "domainId": "domainId",
                "localDomainPath": "localDomainPath",
                "candidateId": "candidateId",
                "sourceUrl": "sourceUrl",
            }.items():
                if row.get(row_key) != queued_task.get(queue_key):
                    fail(errors, f"{task_id}.{row_key} does not match queue")
        for key in REQUIRED_ROW_FIELDS:
            if key in {"downgradeTriggers", "modelPosition", "blockedUses", "sourceEvidenceTrace"}:
                continue
            require_string(row.get(key), f"{task_id}.{key}", errors)
        if set(require_string_list(row.get("blockedUses"), f"{task_id}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, f"{task_id}.blockedUses must match required blocked uses")
        if row.get("modelAdmissionDecision") != "blocked-pending-corrected-extraction-independent-review-and-artifact-gates":
            fail(errors, f"{task_id}.modelAdmissionDecision must remain blocked")
        triggers = require_string_list(row.get("downgradeTriggers"), f"{task_id}.downgradeTriggers", errors, min_len=3)
        if not any("Block" in trigger or "block" in trigger for trigger in triggers):
            fail(errors, f"{task_id}.downgradeTriggers must include a blocking condition")
        validate_model_position(row.get("modelPosition"), f"{task_id}.modelPosition", errors)
        validate_evidence_trace(row.get("sourceEvidenceTrace"), f"{task_id}.sourceEvidenceTrace", errors)
        readiness = row.get("artifactPromotionReadiness")
        source_access = row.get("sourceAccessStatus", "")
        if any(marker in source_access for marker in ("403", "index-only", "no-abstract", "route-only")):
            if readiness not in ROUTE_ONLY_PROMOTION_STATES:
                fail(errors, f"{task_id}.artifactPromotionReadiness must remain route/index/fulltext limited")
        valid_rows.append(row)
    if seen != set(queued):
        fail(errors, "extractedRows must cover exactly the queued corrected re-extraction tasks")
    return valid_rows


def validate_summary(register: dict[str, Any], rows: list[dict[str, Any]], errors: list[str]) -> None:
    summary = register.get("summary")
    if not isinstance(summary, dict):
        fail(errors, "summary must be an object")
        return
    row_count = require_int(summary.get("reextractedRowCount"), "summary.reextractedRowCount", errors)
    if row_count is not None and row_count != len(rows):
        fail(errors, "summary.reextractedRowCount must equal extractedRows length")
    expected_candidate = [
        row["reextractionTaskId"]
        for row in rows
        if row.get("artifactPromotionReadiness") == "eligible-for-independent-fresh-review-before-bounded-artifact-promotion"
    ]
    expected_route = [
        row["reextractionTaskId"]
        for row in rows
        if row.get("artifactPromotionReadiness") != "eligible-for-independent-fresh-review-before-bounded-artifact-promotion"
    ]
    if summary.get("freshReviewCandidateTaskIds") != expected_candidate:
        fail(errors, "summary.freshReviewCandidateTaskIds does not match rows")
    if summary.get("routeOrIndexOnlyTaskIds") != expected_route:
        fail(errors, "summary.routeOrIndexOnlyTaskIds does not match rows")
    require_string_list(summary.get("remainingWork"), "summary.remainingWork", errors, min_len=4)


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
            fail(errors, f"index file does not reference corrected extraction register: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        path = ROOT / relative_path
        text = path.read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "corrected source re-extraction register")
    queue = load_json(QUEUE_PATH, errors, "corrected source re-extraction queue")
    queued = queue_tasks(queue, errors)

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(register.get("registerId"), "registerId", errors)
        require_string(register.get("purpose"), "purpose", errors)
        validate_source_of_truth(register, errors)
        rows = validate_rows(register, queued, errors)
        validate_scope(register, rows, len(queued), errors)
        if set(require_string_list(register.get("blockedUses"), "blockedUses", errors)) != REQUIRED_BLOCKED_USES:
            fail(errors, "blockedUses must match required blocked uses")
        required = register.get("requiredPerRowFields")
        if not isinstance(required, list) or not set(required).issubset(REQUIRED_ROW_FIELDS):
            fail(errors, "requiredPerRowFields must be a subset of required row fields")
        validate_summary(register, rows, errors)
        validate_index_links(register, errors)
        non_claims = "\n".join(require_string_list(register.get("nonClaims"), "nonClaims", errors, min_len=4))
        for phrase in ("does not create reviewed", "does not authorize", "remain blocked"):
            if phrase not in non_claims:
                fail(errors, f"nonClaims missing phrase: {phrase}")
        status_counts = Counter(row.get("artifactPromotionReadiness") for row in rows)
        if status_counts["eligible-for-independent-fresh-review-before-bounded-artifact-promotion"] < 1:
            fail(errors, "at least one row should be eligible for independent fresh review candidate status")
        if not any(row.get("artifactPromotionReadiness") in ROUTE_ONLY_PROMOTION_STATES for row in rows):
            fail(errors, "at least one row should preserve route/index/fulltext-needed blocking")

    if errors:
        print("C2-LT-B1 corrected source re-extraction register audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("C2-LT-B1 corrected source re-extraction register audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
