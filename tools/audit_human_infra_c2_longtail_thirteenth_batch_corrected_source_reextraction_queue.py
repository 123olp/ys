#!/usr/bin/env python3
"""审计 C2-LT-B13 corrected source re-extraction 队列。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json"
SOURCE_RESOLUTION_PATH = ROOT / "docs/reference/human-infra-c2-longtail-thirteenth-batch-source-resolution-register.json"

SCHEMA = "human-infra.c2ltb13-corrected-source-reextraction-queue.v1"
STATUS = "active-c2ltb13-corrected-source-reextraction-queue-model-blocked"
BATCH_ID = "C2-LT-B13"
TASK_ID = "C2LTB13-CREXT-001"
ORIGIN_TASK_ID = "C2LTB13-EXT-021"
SOURCE_RESOLUTION_ID = "C2LTB13-SRR-003"
CANDIDATE_ID = "C2LTB13-SRR-003-CAND-02"
CORRECTED_URL = "https://pubmed.ncbi.nlm.nih.gov/22193141/"
BLOCKED_PRIOR_URL = "https://pubmed.ncbi.nlm.nih.gov/26428404/"
QUEUE_LINK = "human-infra-c2-longtail-thirteenth-batch-corrected-source-reextraction-queue.json"
SCRIPT_LINK = "audit_human_infra_c2_longtail_thirteenth_batch_corrected_source_reextraction_queue.py"

SOURCE_OF_TRUTH_KEYS = {
    "sourceResolutionRegister",
    "sourceExtractionRegister",
    "localReviewRegister",
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
    "sourceResolutionId",
    "domainId",
    "localDomainPath",
    "candidateId",
    "candidateRole",
    "sourceTitle",
    "sourceUrl",
    "sourceType",
    "reextractionRole",
    "reextractionAction",
    "sourceResolutionFinding",
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
    "docs/AGENTS.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "docs/reference/human-infra-maturity-gap-register.json",
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


def source_resolution_candidate(errors: list[str]) -> dict[str, Any]:
    register = load_json(SOURCE_RESOLUTION_PATH, errors, "C2-LT-B13 source-resolution register")
    rows = register.get("resolutionRows")
    if not isinstance(rows, list):
        fail(errors, "source-resolution register must contain resolutionRows")
        return {}
    for row in rows:
        if isinstance(row, dict) and row.get("taskId") == ORIGIN_TASK_ID:
            if row.get("sourceResolutionStatus") != "candidate-correction-prepared-reextraction-required-not-fresh-reviewed":
                fail(errors, "source-resolution row must remain pending corrected re-extraction")
            for candidate in row.get("sourceResolutionCandidates", []):
                if isinstance(candidate, dict) and candidate.get("candidateId") == CANDIDATE_ID:
                    return candidate
    fail(errors, f"missing corrected candidate {CANDIDATE_ID} in source-resolution register")
    return {}


def validate_source_of_truth(queue: dict[str, Any], errors: list[str]) -> None:
    source = queue.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != SOURCE_OF_TRUTH_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key in SOURCE_OF_TRUTH_KEYS:
        if key in source:
            repo_path(source[key], f"sourceOfTruth.{key}", errors)


def validate_scope(queue: dict[str, Any], errors: list[str]) -> None:
    scope = queue.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected = {
        "sourceResolutionIssueRowCount": 3,
        "titleDomainMismatchRowCount": 1,
        "correctedSourceCandidateCount": 1,
        "derivedTaskCount": 1,
        "directArtifactFillTaskCount": 0,
        "modelAdmissionOpenedTaskCount": 0,
    }
    if scope.get("batchId") != BATCH_ID:
        fail(errors, f"scope.batchId must be {BATCH_ID}")
    if scope.get("queueLevel") != "c2ltb13-corrected-source-reextraction-v0.1":
        fail(errors, "scope.queueLevel is invalid")
    for key, expected_value in expected.items():
        actual = require_int(scope.get(key), f"scope.{key}", errors)
        if actual is not None and actual != expected_value:
            fail(errors, f"scope.{key} must equal {expected_value}")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, min_len=4)


def validate_defaults(queue: dict[str, Any], errors: list[str]) -> None:
    defaults = queue.get("queueDefaults")
    if not isinstance(defaults, dict):
        fail(errors, "queueDefaults must be an object")
        return
    expected = {
        "taskStatus": "queued-corrected-source-reextraction-required",
        "reviewState": "source-resolution-candidate-correction-not-reextracted",
        "artifactPromotionDecision": "blocked-pending-corrected-source-reextraction-independent-fresh-review-and-reviewed-artifact-gates",
        "modelAdmissionDecision": "blocked",
    }
    for key, value in expected.items():
        if defaults.get(key) != value:
            fail(errors, f"queueDefaults.{key} must be {value}")
    if set(require_string_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, "queueDefaults.blockedUses must match required blocked uses")
    require_string(defaults.get("minimumReextractionQuestion"), "queueDefaults.minimumReextractionQuestion", errors)


def validate_task(queue: dict[str, Any], candidate: dict[str, Any], errors: list[str]) -> None:
    tasks = queue.get("reextractionTasks")
    if not isinstance(tasks, list) or len(tasks) != 1:
        fail(errors, "reextractionTasks must contain exactly one task")
        return
    task = tasks[0]
    if not isinstance(task, dict):
        fail(errors, "reextractionTasks[0] must be an object")
        return
    missing = REQUIRED_TASK_FIELDS - set(task)
    if missing:
        fail(errors, f"reextraction task missing fields: {sorted(missing)}")
    expected = {
        "taskId": TASK_ID,
        "batchId": BATCH_ID,
        "originTaskId": ORIGIN_TASK_ID,
        "sourceResolutionId": SOURCE_RESOLUTION_ID,
        "candidateId": CANDIDATE_ID,
        "sourceUrl": CORRECTED_URL,
        "taskStatus": "queued-corrected-source-reextraction-required",
        "reviewState": "source-resolution-candidate-correction-not-reextracted",
        "artifactPromotionDecision": "blocked-pending-corrected-source-reextraction-independent-fresh-review-and-reviewed-artifact-gates",
        "modelAdmissionDecision": "blocked",
    }
    for key, value in expected.items():
        if task.get(key) != value:
            fail(errors, f"{TASK_ID}.{key} must be {value}")
    if candidate and task.get("sourceTitle") != candidate.get("title"):
        fail(errors, f"{TASK_ID}.sourceTitle must match source-resolution candidate")
    if candidate and task.get("sourceUrl") != candidate.get("url"):
        fail(errors, f"{TASK_ID}.sourceUrl must match source-resolution candidate")
    repo_path(task.get("localDomainPath", ""), f"{TASK_ID}.localDomainPath", errors)
    slots = set(require_string_list(task.get("requiredReextractionSlots"), f"{TASK_ID}.requiredReextractionSlots", errors))
    if slots != REQUIRED_REEXTRACTION_SLOTS:
        fail(errors, f"{TASK_ID}.requiredReextractionSlots must match required slots")
    questions = require_string_list(task.get("reextractionQuestions"), f"{TASK_ID}.reextractionQuestions", errors, min_len=8)
    if not any("blocked uses" in question.lower() or "prohibited" in question.lower() for question in questions):
        fail(errors, f"{TASK_ID}.reextractionQuestions must ask about blocked/prohibited uses")
    if set(require_string_list(task.get("blockedUses"), f"{TASK_ID}.blockedUses", errors)) != REQUIRED_BLOCKED_USES:
        fail(errors, f"{TASK_ID}.blockedUses must match required blocked uses")
    boundary = " ".join(
        require_string(task.get(key), f"{TASK_ID}.{key}", errors)
        for key in ["useBoundary", "sourceResolutionFinding", "nextAction"]
    )
    for phrase in ["no skin-care advice", "no", "model admission"]:
        if phrase not in boundary:
            fail(errors, f"{TASK_ID} boundary text must preserve phrase: {phrase}")


def validate_summary(queue: dict[str, Any], errors: list[str]) -> None:
    summary = queue.get("derivedQueueSummary")
    if not isinstance(summary, dict):
        fail(errors, "derivedQueueSummary must be an object")
        return
    if summary.get("derivedTaskCount") != 1:
        fail(errors, "derivedQueueSummary.derivedTaskCount must equal 1")
    if summary.get("originTaskIds") != [ORIGIN_TASK_ID]:
        fail(errors, "derivedQueueSummary.originTaskIds must contain only C2LTB13-EXT-021")
    if summary.get("correctedCandidateIds") != [CANDIDATE_ID]:
        fail(errors, "derivedQueueSummary.correctedCandidateIds must contain only corrected IAD candidate")
    if summary.get("blockedPriorSourceUrls") != [BLOCKED_PRIOR_URL]:
        fail(errors, "derivedQueueSummary.blockedPriorSourceUrls must preserve invalid PMID route")
    if summary.get("correctedSourceUrls") != [CORRECTED_URL]:
        fail(errors, "derivedQueueSummary.correctedSourceUrls must preserve corrected PMID route")
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
        if QUEUE_LINK not in text:
            fail(errors, f"index file does not reference corrected re-extraction queue: {relative_path}")
    for relative_path in ["Makefile", "tools/README.md", "tools/AGENTS.md"]:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if SCRIPT_LINK not in text:
            fail(errors, f"{relative_path} does not reference audit script")


def main() -> int:
    errors: list[str] = []
    queue = load_json(QUEUE_PATH, errors, "C2-LT-B13 corrected source re-extraction queue")
    candidate = source_resolution_candidate(errors)
    if queue:
        if queue.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if queue.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(queue.get("queueId"), "queueId", errors)
        require_string(queue.get("purpose"), "purpose", errors)
        validate_source_of_truth(queue, errors)
        validate_scope(queue, errors)
        validate_defaults(queue, errors)
        validate_task(queue, candidate, errors)
        validate_summary(queue, errors)
        require_string_list(queue.get("nonClaims"), "nonClaims", errors, min_len=4)
        validate_index_links(queue, errors)

    if errors:
        print("C2-LT-B13 corrected source re-extraction queue audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("C2-LT-B13 corrected source re-extraction queue audit ok: tasks=1 model=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
