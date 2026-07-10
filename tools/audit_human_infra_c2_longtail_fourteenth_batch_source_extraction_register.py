#!/usr/bin/env python3
"""审计 C2 长尾第十四批来源抽取完成寄存器。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-c2-longtail-fourteenth-batch-source-extraction-register.json"
QUEUE_PATH = ROOT / "docs/reference/human-infra-c2-longtail-fourteenth-batch-source-extraction-queue.json"

SCHEMA = "human-infra.c2-longtail-fourteenth-batch-source-extraction-register.v1"
STATUS = "active-c2ltb14-source-extractions-pending-local-review-and-fresh-review"
REGISTER_LINK = "human-infra-c2-longtail-fourteenth-batch-source-extraction-register.json"
AUDIT_SCRIPT = "audit_human_infra_c2_longtail_fourteenth_batch_source_extraction_register.py"
AUDIT_TARGET = "c2-longtail-fourteenth-batch-source-extraction-register-audit"
EXPECTED_TASK_IDS = [f"C2LTB14-EXT-{index:03d}" for index in range(1, 33)]
REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
    "domain-claim-upgrade",
    "energy-infrastructure-advice",
    "vision-care-advice",
    "dental-or-oral-health-advice",
    "burn-prevention-advice",
    "genetic-or-neurodegenerative-advice",
    "immunization-record-advice",
    "indoor-environment-remediation-advice",
    "respiratory-or-allergy-advice",
    "employment-or-leave-legal-advice",
    "court-access-legal-advice",
    "reproductive-tissue-governance-advice",
    "skin-care-supplies-advice",
    "chemical-exposure-advice",
    "synthetic-data-validity-claim",
    "synthetic-media-authenticity-claim",
    "nutrition-benefit-advice",
}
REQUIRED_ROW_FIELDS = [
    "taskId",
    "domainId",
    "localDomainPath",
    "sourceRefId",
    "sourceTitle",
    "sourceUrl",
    "extractionStatus",
    "sourceAccessStatus",
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


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in ["sourceExtractionQueue", "promotionQueue", "sourceCardSystem", "maturityGapRegister", "maturityRoadmap"]:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(scope: Any, rows: list[dict[str, Any]], queue_count: int, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    expected_counts = {
        "queueTaskCount": queue_count,
        "extractedTaskCount": len(rows),
        "remainingTaskCount": queue_count - len(rows),
        "coveredDomainCount": len({row.get("domainId") for row in rows if isinstance(row.get("domainId"), str)}),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    selected = require_string_list(scope.get("selectedTaskIds"), "scope.selectedTaskIds", errors, len(EXPECTED_TASK_IDS))
    if selected != EXPECTED_TASK_IDS:
        fail(errors, "scope.selectedTaskIds must equal all 32 C2LTB14 extraction task IDs")
    if require_string(scope.get("batchId"), "scope.batchId", errors) != "C2-LT-B14":
        fail(errors, "scope.batchId must be C2-LT-B14")
    require_string(scope.get("extractionDepth"), "scope.extractionDepth", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def queue_tasks(errors: list[str]) -> dict[str, dict[str, Any]]:
    queue = load_json(QUEUE_PATH, errors, "C2 fourteenth-batch source extraction queue")
    tasks = queue.get("extractionTasks") if queue else None
    if not isinstance(tasks, list):
        fail(errors, "queue.extractionTasks must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"queue.extractionTasks[{index}] must be an object")
            continue
        task_id = task.get("taskId")
        if not isinstance(task_id, str) or not task_id.strip():
            fail(errors, f"queue.extractionTasks[{index}].taskId missing")
            continue
        result[task_id] = task
    return result


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context}.modelPosition must be an object")
        return
    require_string(value.get("primaryLocation"), f"{context}.modelPosition.primaryLocation", errors)
    require_string_list(value.get("variables"), f"{context}.modelPosition.variables", errors, 1)
    require_string(value.get("admissibleUse"), f"{context}.modelPosition.admissibleUse", errors)


def validate_rows(rows: Any, task_map: dict[str, dict[str, Any]], errors: list[str]) -> list[dict[str, Any]]:
    if not isinstance(rows, list):
        fail(errors, "extractedRows must be a list")
        return []
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    access_counts = {"200": 0, "403": 0, "404": 0}
    for index, row in enumerate(rows):
        context = f"extractedRows[{index}]"
        if not isinstance(row, dict):
            fail(errors, f"{context} must be an object")
            continue
        result.append(row)
        for field in REQUIRED_ROW_FIELDS:
            if field not in row:
                fail(errors, f"{context}.{field} missing")
        task_id = require_string(row.get("taskId"), f"{context}.taskId", errors)
        if task_id in seen:
            fail(errors, f"duplicate extracted taskId: {task_id}")
        seen.add(task_id)
        task = task_map.get(task_id)
        if task is None:
            fail(errors, f"{context}.taskId has no queue task: {task_id}")
            continue
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
        if row.get("extractionStatus") != "completed-c2ltb14-source-context-extraction":
            fail(errors, f"{task_id}.extractionStatus must be completed-c2ltb14-source-context-extraction")
        for field in [
            "sourceAccessStatus",
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
        access = str(row.get("sourceAccessStatus", ""))
        if "status-200" in access:
            access_counts["200"] += 1
        if "status-403" in access:
            access_counts["403"] += 1
        if "status-404" in access:
            access_counts["404"] += 1
        if "blocked" not in str(row.get("modelAdmissionDecision", "")):
            fail(errors, f"{task_id}.modelAdmissionDecision must keep model admission blocked")
        blocked = set(require_string_list(row.get("blockedUses"), f"{task_id}.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
        if blocked != REQUIRED_BLOCKED_USES:
            fail(errors, f"{task_id}.blockedUses must match required prohibited uses")
        require_string_list(row.get("downgradeTriggers"), f"{task_id}.downgradeTriggers", errors, 5)
        validate_model_position(row.get("modelPosition"), task_id, errors)
    if [row.get("taskId") for row in result] != EXPECTED_TASK_IDS:
        fail(errors, "extractedRows must be ordered as C2LTB14-EXT-001 through C2LTB14-EXT-032")
    if access_counts != {"200": 24, "403": 7, "404": 1}:
        fail(errors, f"sourceAccessStatus counts must be 24x200, 7x403 and 1x404; got {access_counts}")
    return result


def validate_index_links(data: dict[str, Any], errors: list[str]) -> None:
    requirements = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 5)
    link_targets = [
        "docs/AGENTS.md",
        "docs/reference/README.md",
        "docs/reference/human-infra-maturity-roadmap.md",
        "docs/reference/human-infra-maturity-gap-register.json",
        "tools/README.md",
        "tools/AGENTS.md",
    ]
    for relative_path in link_targets:
        target = ROOT / relative_path
        if not target.exists():
            fail(errors, f"missing index target: {relative_path}")
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index target does not link extraction register: {relative_path}")
    makefile = ROOT / "Makefile"
    if not makefile.exists():
        fail(errors, "missing index target: Makefile")
    else:
        make_text = makefile.read_text(encoding="utf-8")
        if AUDIT_TARGET not in make_text:
            fail(errors, "Makefile does not expose fourteenth-batch source extraction register audit target")
        if AUDIT_SCRIPT not in make_text:
            fail(errors, "Makefile does not run fourteenth-batch source extraction register audit script")
    if len(requirements) < 5:
        fail(errors, "indexRequirements must list at least five index targets")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "C2 fourteenth-batch source extraction register")
    task_map = queue_tasks(errors)

    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)
    validate_source_of_truth(data, errors)
    rows = validate_rows(data.get("extractedRows"), task_map, errors)
    validate_scope(data.get("scope"), rows, len(task_map), errors)
    notes = " ".join(require_string_list(data.get("sourceAccessNotes"), "sourceAccessNotes", errors, 3))
    for phrase in ["24 public HTTP 200", "7 HTTP 403", "HTTP 404"]:
        if phrase not in notes:
            fail(errors, f"sourceAccessNotes must mention {phrase}")
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    validate_index_links(data, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "C2 longtail fourteenth-batch source extraction register audit ok: "
        f"batch={data['scope']['batchId']} extracted={len(rows)} remaining={data['scope']['remainingTaskCount']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
