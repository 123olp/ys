#!/usr/bin/env python3
"""审计 C2 长尾第八批本地来源语境复核账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-local-review-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-queue.json"
EXTRACTION_REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-eighth-batch-source-extraction-register.json"

SCHEMA = "human-infra.c2-longtail-eighth-batch-local-review-register.v1"
STATUS = "complete-local-source-context-review-independent-fresh-review-required"
REGISTER_LINK = "human-infra-c2-longtail-eighth-batch-local-review-register.json"
EXPECTED_TASK_IDS = [f"C2LTB8-EXT-{index:03d}" for index in range(1, 25)]
EXPECTED_SOURCE_RESOLUTION_IDS = [
    "C2LTB8-EXT-006",
    "C2LTB8-EXT-008",
    "C2LTB8-EXT-011",
    "C2LTB8-EXT-014",
    "C2LTB8-EXT-021",
    "C2LTB8-EXT-022",
    "C2LTB8-EXT-024",
]
REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
}
REQUIRED_NEXT_ARTIFACTS = {
    "c2ltb8-independent-fresh-review-protocol",
    "c2ltb8-independent-fresh-review-verdict-register",
    "c2ltb8-source-resolution-register-for-pubmed-fulltext-issue-rows",
    "reviewed-source-card",
    "variable-card",
    "endpoint-card",
    "uncertainty-card",
    "transfer-boundary-card",
    "downgrade-check-row",
}
REQUIRED_ROW_FIELDS = [
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "sourceTitle",
    "sourceUrl",
    "sourceRole",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSetting",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "downgradeTriggers",
    "modelPosition",
    "modelAdmissionDecision",
    "blockedUses",
    "nextAction",
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


def load_queue(errors: list[str]) -> dict[str, dict[str, Any]]:
    queue = load_json(QUEUE_PATH, errors, "C2-LT-B8 source extraction queue")
    tasks = queue.get("extractionTasks") if queue else None
    if not isinstance(tasks, list):
        fail(errors, "queue.extractionTasks must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"queue.extractionTasks[{index}] must be an object")
            continue
        task_id = require_string(task.get("taskId"), f"queue.extractionTasks[{index}].taskId", errors)
        if task_id:
            result[task_id] = task
    if list(result) != EXPECTED_TASK_IDS:
        fail(errors, "queue task IDs must be C2LTB8-EXT-001 through C2LTB8-EXT-024")
    return result


def load_extraction_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    register = load_json(EXTRACTION_REGISTER_PATH, errors, "C2-LT-B8 source extraction register")
    rows = register.get("extractedRows") if register else None
    if not isinstance(rows, list):
        fail(errors, "source extraction register extractedRows must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"extractedRows[{index}] must be an object")
            continue
        task_id = require_string(row.get("taskId"), f"extractedRows[{index}].taskId", errors)
        if task_id in result:
            fail(errors, f"duplicate extracted row taskId: {task_id}")
        if task_id:
            result[task_id] = row
    if list(result) != EXPECTED_TASK_IDS:
        fail(errors, "source extraction register rows must be ordered as all 24 C2LTB8 task IDs")
    return result


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in ["sourceExtractionQueue", "sourceExtractionRegister", "sourceCardSystem", "maturityGapRegister"]:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(scope: Any, task_map: dict[str, dict[str, Any]], errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if require_string(scope.get("batchId"), "scope.batchId", errors) != "C2-LT-B8":
        fail(errors, "scope.batchId must be C2-LT-B8")
    if require_string(scope.get("reviewLevel"), "scope.reviewLevel", errors) != "source-extraction-row-local-context-review":
        fail(errors, "scope.reviewLevel must be source-extraction-row-local-context-review")
    expected_counts = {
        "sourceExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "localReviewedExtractionTaskCount": len(EXPECTED_TASK_IDS),
        "coveredDomainCount": len({task.get("domainId") for task in task_map.values()}),
        "reviewBatchCount": 2,
        "sourceResolutionIssueCount": len(EXPECTED_SOURCE_RESOLUTION_IDS),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    selected = require_string_list(
        scope.get("reviewedExtractionTaskIds"),
        "scope.reviewedExtractionTaskIds",
        errors,
        len(EXPECTED_TASK_IDS),
    )
    if selected != EXPECTED_TASK_IDS:
        fail(errors, "scope.reviewedExtractionTaskIds must equal all 24 C2LTB8 task IDs")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 5)


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context}.modelPosition must be an object")
        return
    require_string(value.get("primaryLocation"), f"{context}.modelPosition.primaryLocation", errors)
    require_string_list(value.get("variables"), f"{context}.modelPosition.variables", errors, 1)
    require_string(value.get("admissibleUse"), f"{context}.modelPosition.admissibleUse", errors)


def validate_extraction_row(row: dict[str, Any], task: dict[str, Any], errors: list[str]) -> None:
    task_id = str(row.get("taskId", "unknown"))
    for field in REQUIRED_ROW_FIELDS:
        if field not in row:
            fail(errors, f"{task_id}.{field} missing")
    for field in ["domainId", "localDomainPath", "sourceRefId", "sourceTitle", "sourceUrl"]:
        if row.get(field) != task.get(field):
            fail(errors, f"{task_id}.{field} must match queue")
    local_path = row.get("localDomainPath")
    if isinstance(local_path, str):
        path = repo_path(local_path, f"{task_id}.localDomainPath", errors)
        if path:
            for required in ["README.md", "AGENTS.md"]:
                if not (path / required).exists():
                    fail(errors, f"{task_id}.localDomainPath missing {required}")
    if row.get("extractionStatus") != "completed-c2ltb8-source-context-extraction":
        fail(errors, f"{task_id}.extractionStatus must be completed-c2ltb8-source-context-extraction")
    for field in [
        "sourceRole",
        "exactClaimUse",
        "endpointDefinition",
        "populationOrSetting",
        "effectOrMechanismSignal",
        "uncertaintyOrBias",
        "transferBoundary",
        "modelAdmissionDecision",
        "nextAction",
    ]:
        require_string(row.get(field), f"{task_id}.{field}", errors)
    if "blocked" not in str(row.get("modelAdmissionDecision", "")):
        fail(errors, f"{task_id}.modelAdmissionDecision must keep model admission blocked")
    blocked = set(require_string_list(row.get("blockedUses"), f"{task_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, f"{task_id}.blockedUses must match required prohibited uses")
    require_string_list(row.get("downgradeTriggers"), f"{task_id}.downgradeTriggers", errors, 3)
    validate_model_position(row.get("modelPosition"), task_id, errors)


def validate_batches(
    batches: Any,
    task_map: dict[str, dict[str, Any]],
    extraction_rows: dict[str, dict[str, Any]],
    errors: list[str],
) -> None:
    if not isinstance(batches, list) or len(batches) != 2:
        fail(errors, "reviewBatches must contain exactly two batch objects")
        return
    covered: list[str] = []
    for index, batch in enumerate(batches):
        context = f"reviewBatches[{index}]"
        if not isinstance(batch, dict):
            fail(errors, f"{context} must be an object")
            continue
        require_string(batch.get("reviewBatchId"), f"{context}.reviewBatchId", errors)
        require_string(batch.get("reviewLabel"), f"{context}.reviewLabel", errors)
        task_ids = require_string_list(batch.get("taskIds"), f"{context}.taskIds", errors, 1)
        task_count = require_int(batch.get("taskCount"), f"{context}.taskCount", errors)
        if task_count is not None and task_count != len(task_ids):
            fail(errors, f"{context}.taskCount must equal len(taskIds)")
        if require_string(batch.get("reviewDecision"), f"{context}.reviewDecision", errors) != "local-review-pass-for-independent-fresh-review-only":
            fail(errors, f"{context}.reviewDecision must pass only for independent fresh review")
        require_string(batch.get("nextReviewMode"), f"{context}.nextReviewMode", errors)
        domain_ids = set(require_string_list(batch.get("domainIds"), f"{context}.domainIds", errors, 1))
        actual_domains = {str(task_map.get(task_id, {}).get("domainId")) for task_id in task_ids}
        if domain_ids != actual_domains:
            fail(errors, f"{context}.domainIds must match task domain IDs")
        for task_id in task_ids:
            task = task_map.get(task_id)
            row = extraction_rows.get(task_id)
            if task is None:
                fail(errors, f"{context}.{task_id} missing from queue")
                continue
            if row is None:
                fail(errors, f"{context}.{task_id} missing from extraction register")
                continue
            validate_extraction_row(row, task, errors)
        covered.extend(task_ids)
    if covered != EXPECTED_TASK_IDS:
        fail(errors, "reviewBatches must cover all 24 task IDs exactly once in order")


def validate_source_resolution_findings(findings: Any, extraction_rows: dict[str, dict[str, Any]], errors: list[str]) -> None:
    if not isinstance(findings, list):
        fail(errors, "sourceResolutionFindings must be a list")
        return
    task_ids: list[str] = []
    for index, finding in enumerate(findings):
        context = f"sourceResolutionFindings[{index}]"
        if not isinstance(finding, dict):
            fail(errors, f"{context} must be an object")
            continue
        task_id = require_string(finding.get("taskId"), f"{context}.taskId", errors)
        if task_id:
            task_ids.append(task_id)
            row = extraction_rows.get(task_id)
            if row is None:
                fail(errors, f"{context}.taskId has no extraction row")
            else:
                source_context = " ".join(
                    str(row.get(field, "")) for field in ["sourceAccessStatus", "sourceRole", "uncertaintyOrBias", "transferBoundary"]
                )
                markers = ["PubMed", "pubmed", "fulltext", "route", "manual", "living", "sentience", "source-resolution"]
                if not any(marker in source_context for marker in markers):
                    fail(errors, f"{task_id} must preserve PubMed/fulltext/source-resolution context")
        for field in ["issueType", "reviewDisposition", "correctionCandidate", "reason"]:
            require_string(finding.get(field), f"{context}.{field}", errors)
        disposition = str(finding.get("reviewDisposition", ""))
        if not any(marker in disposition for marker in ["source-resolution", "manual-fulltext", "manual-route", "bounded-fresh-review", "fulltext", "overclaim"]):
            fail(errors, f"{context}.reviewDisposition must preserve source-resolution/manual-fulltext boundary")
    if task_ids != EXPECTED_SOURCE_RESOLUTION_IDS:
        fail(errors, "sourceResolutionFindings must list the seven expected C2-LT-B8 issue rows in order")


def validate_register_fields(data: dict[str, Any], errors: list[str]) -> None:
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)
    require_string_list(data.get("requiredExtractionFieldsReviewed"), "requiredExtractionFieldsReviewed", errors, len(REQUIRED_ROW_FIELDS))
    for field in ["localReviewVerdict", "promotionDecision", "sourceResolutionDecision", "modelAdmissionDecision"]:
        require_string(data.get(field), field, errors)
    if "independent-fresh-review" not in str(data.get("localReviewVerdict", "")):
        fail(errors, "localReviewVerdict must route only to independent fresh review")
    if "independent-fresh-review" not in str(data.get("promotionDecision", "")):
        fail(errors, "promotionDecision must route only to independent fresh review")
    if "blocked" not in str(data.get("modelAdmissionDecision", "")):
        fail(errors, "modelAdmissionDecision must remain blocked")
    blocked = set(require_string_list(data.get("blockedUses"), "blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if blocked != REQUIRED_BLOCKED_USES:
        fail(errors, "blockedUses must match required prohibited uses")
    next_artifacts = set(require_string_list(data.get("requiredNextArtifacts"), "requiredNextArtifacts", errors, len(REQUIRED_NEXT_ARTIFACTS)))
    missing = REQUIRED_NEXT_ARTIFACTS - next_artifacts
    if missing:
        fail(errors, f"requiredNextArtifacts missing: {sorted(missing)}")
    if "c2ltb8-source-resolution-register-for-pubmed-fulltext-issue-rows" not in next_artifacts:
        fail(errors, "requiredNextArtifacts must include source-resolution register for C2-LT-B8 PubMed/fulltext issue rows")
    require_string_list(data.get("localReviewChecks"), "localReviewChecks", errors, 7)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 5)
    require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 4)


def validate_index_links(errors: list[str]) -> None:
    for relative_path in [
        "README.md",
        "docs/reference/README.md",
        "docs/reference/human-infra-maturity-roadmap.md",
        "tools/README.md",
    ]:
        target = ROOT / relative_path
        if not target.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index target does not link local review register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2-LT-B8 local review register")
    task_map = load_queue(errors)
    extraction_rows = load_extraction_rows(errors)
    if data:
        validate_register_fields(data, errors)
        validate_source_of_truth(data, errors)
        validate_scope(data.get("scope"), task_map, errors)
        validate_batches(data.get("reviewBatches"), task_map, extraction_rows, errors)
        validate_source_resolution_findings(data.get("sourceResolutionFindings"), extraction_rows, errors)
        validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "C2 longtail eighth-batch local review register audit ok: "
        "batch=C2-LT-B8 reviewed=24 domains=12 source_resolution_issues=7"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
