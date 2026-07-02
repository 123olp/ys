#!/usr/bin/env python3
"""审计域-来源字段行晋升队列契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-domain-source-card-promotion-queue.json"
REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-source-specific-extraction-register.json"

SCHEMA = "human-infra.domain-source-card-promotion-queue.v1"
STATUS = "active-promotion-queue-fresh-review-required"
REGISTER_LINK = "human-infra-domain-source-card-promotion-queue.json"

SOURCE_OF_TRUTH_KEYS = [
    "domainSourceSpecificExtractionRegister",
    "domainSourceSpecificExtractionQueue",
    "sourceCardSystem",
    "lifePathPredictionModelContract",
    "maturityGapRegister",
]

REQUIRED_TASK_FIELDS = [
    "promotionTaskId",
    "domainId",
    "domainClaimId",
    "fieldCardId",
    "sourceCardId",
    "sourceRole",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSample",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "sourceContextReviewStatus",
    "sourceContextReviewQuestion",
    "variableCardStatus",
    "endpointCardStatus",
    "uncertaintyCardStatus",
    "transferBoundaryCardStatus",
    "downgradeCheckStatus",
    "modelAdmissionDecision",
    "blockedUses",
    "nextAction",
]

REQUIRED_DEFAULTS = {
    "sourceContextReviewStatus": "queued-fresh-review-required",
    "variableCardStatus": "queued-variable-card-promotion",
    "endpointCardStatus": "queued-endpoint-card-promotion",
    "uncertaintyCardStatus": "queued-uncertainty-card-promotion",
    "transferBoundaryCardStatus": "queued-transfer-boundary-card-promotion",
    "downgradeCheckStatus": "queued-downgrade-check-required",
    "modelAdmissionDecision": "blocked-until-fresh-review-and-card-promotion",
}

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-recommendation",
    "individual-death-date-output",
    "intervention-ranking",
    "domain-claim-upgrade",
}

REQUIRED_PROMOTION_STAGES = {
    "source-context-fresh-review",
    "source-card-promotion",
    "variable-card-promotion",
    "endpoint-card-promotion",
    "uncertainty-card-promotion",
    "transfer-boundary-card-promotion",
    "downgrade-check-registration",
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


def load_register_rows(errors: list[str]) -> dict[tuple[str, str], dict[str, Any]]:
    data = load_json(REGISTER_PATH, errors, "domain-source extraction register")
    rows = data.get("completedRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "domain-source extraction register completedRows must be a list")
        return {}
    result: dict[tuple[str, str], dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"completedRows[{index}] must be an object")
            continue
        domain_id = require_string(row.get("domainId"), f"completedRows[{index}].domainId", errors)
        source_id = require_string(row.get("sourceCardId"), f"{domain_id}.sourceCardId", errors)
        if not domain_id or not source_id:
            continue
        key = (domain_id, source_id)
        if key in result:
            fail(errors, f"duplicate completed row in register: {domain_id}/{source_id}")
        result[key] = row
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


def validate_scope(scope: Any, register_rows: dict[tuple[str, str], dict[str, Any]], errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    if scope.get("promotionLevel") != "completed-field-extraction-to-fresh-review-and-card-promotion":
        fail(errors, "scope.promotionLevel must be completed-field-extraction-to-fresh-review-and-card-promotion")
    if scope.get("derivedTaskUnit") != "domainId + sourceCardId":
        fail(errors, "scope.derivedTaskUnit must be domainId + sourceCardId")

    domains = {domain_id for domain_id, _ in register_rows}
    fields = {row.get("fieldCardId") for row in register_rows.values() if isinstance(row.get("fieldCardId"), str)}
    sources = {source_id for _, source_id in register_rows}
    expected_counts = {
        "sourceExtractionRowCount": len(register_rows),
        "promotionTaskCount": len(register_rows),
        "coveredDomainCount": len(domains),
        "coveredFieldRowCount": len(fields),
        "coveredSourceAnchorCount": len(sources),
    }
    for key, expected in expected_counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")

    stages = set(require_string_list(scope.get("promotionStages"), "scope.promotionStages", errors, len(REQUIRED_PROMOTION_STAGES)))
    if stages != REQUIRED_PROMOTION_STAGES:
        fail(errors, "scope.promotionStages must contain every required promotion stage")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 4)


def validate_required_fields(fields: Any, errors: list[str]) -> None:
    actual = require_string_list(fields, "requiredPerPromotionTaskFields", errors, len(REQUIRED_TASK_FIELDS))
    if actual != REQUIRED_TASK_FIELDS:
        fail(errors, "requiredPerPromotionTaskFields must exactly match the promotion contract")


def validate_defaults(defaults: Any, errors: list[str]) -> None:
    if not isinstance(defaults, dict):
        fail(errors, "queueDefaults must be an object")
        return
    for key, expected in REQUIRED_DEFAULTS.items():
        if defaults.get(key) != expected:
            fail(errors, f"queueDefaults.{key} must be {expected}")
    blocked = set(require_string_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors, len(REQUIRED_BLOCKED_USES)))
    if not REQUIRED_BLOCKED_USES.issubset(blocked):
        fail(errors, "queueDefaults.blockedUses must include every required blocked use")
    require_string(defaults.get("minimumPromotionQuestion"), "queueDefaults.minimumPromotionQuestion", errors)


def validate_summary(summary: Any, register_rows: dict[tuple[str, str], dict[str, Any]], errors: list[str]) -> None:
    if not isinstance(summary, dict):
        fail(errors, "promotionSummary must be an object")
        return
    domains = {domain_id for domain_id, _ in register_rows}
    fields = {row.get("fieldCardId") for row in register_rows.values() if isinstance(row.get("fieldCardId"), str)}
    sources = {source_id for _, source_id in register_rows}
    expected_counts = {
        "sourceExtractionRowCount": len(register_rows),
        "promotionTaskCount": len(register_rows),
        "coveredDomainCount": len(domains),
        "coveredFieldRowCount": len(fields),
        "coveredSourceAnchorCount": len(sources),
    }
    for key, expected in expected_counts.items():
        value = require_int(summary.get(key), f"promotionSummary.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"promotionSummary.{key} must equal {expected}")
    if summary.get("promotionCompletionState") != "queued-not-reviewed":
        fail(errors, "promotionSummary.promotionCompletionState must be queued-not-reviewed")
    require_string_list(summary.get("remainingWork"), "promotionSummary.remainingWork", errors, 4)


def validate_tasks(tasks: Any, register_rows: dict[tuple[str, str], dict[str, Any]], errors: list[str]) -> None:
    if not isinstance(tasks, list):
        fail(errors, "promotionTasks must be a list")
        return
    seen: set[tuple[str, str]] = set()
    if len(tasks) != len(register_rows):
        fail(errors, f"promotionTasks must contain exactly {len(register_rows)} tasks")

    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            fail(errors, f"promotionTasks[{index}] must be an object")
            continue
        for field in REQUIRED_TASK_FIELDS:
            if field == "blockedUses":
                require_string_list(task.get(field), f"promotionTasks[{index}].{field}", errors, 5)
            else:
                require_string(task.get(field), f"promotionTasks[{index}].{field}", errors)

        domain_id = task.get("domainId")
        source_id = task.get("sourceCardId")
        if not isinstance(domain_id, str) or not isinstance(source_id, str):
            continue
        key = (domain_id, source_id)
        if key in seen:
            fail(errors, f"duplicate promotion task: {domain_id}/{source_id}")
        seen.add(key)
        row = register_rows.get(key)
        if row is None:
            fail(errors, f"promotion task is not backed by completed row: {domain_id}/{source_id}")
            continue

        for copied_field in [
            "domainClaimId",
            "fieldCardId",
            "sourceRole",
            "exactClaimUse",
            "endpointDefinition",
            "populationOrSample",
            "effectOrMechanismSignal",
            "uncertaintyOrBias",
            "transferBoundary",
        ]:
            if task.get(copied_field) != row.get(copied_field):
                fail(errors, f"{domain_id}/{source_id}.{copied_field} must match completed row")

        for status_field, expected in REQUIRED_DEFAULTS.items():
            if task.get(status_field) != expected:
                fail(errors, f"{domain_id}/{source_id}.{status_field} must be {expected}")
        blocked = set(require_string_list(task.get("blockedUses"), f"{domain_id}/{source_id}.blockedUses", errors, 5))
        row_blocked = set(row.get("blockedUses", [])) if isinstance(row.get("blockedUses"), list) else set()
        if not row_blocked.issubset(blocked):
            fail(errors, f"{domain_id}/{source_id}.blockedUses must preserve completed-row blocked uses")
        if not REQUIRED_BLOCKED_USES.issubset(blocked):
            fail(errors, f"{domain_id}/{source_id}.blockedUses must include promotion blocked uses")

    if seen != set(register_rows):
        missing = sorted(set(register_rows) - seen)
        fail(errors, f"promotionTasks missing completed row pairs: {missing[:5]}")


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_string_list(paths, "indexRequirements", errors, 2):
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link promotion queue: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(QUEUE_PATH, errors, "domain-source card promotion queue")
    register_rows = load_register_rows(errors)

    if not data:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("queueId"), "queueId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    validate_source_of_truth(data, errors)
    validate_scope(data.get("scope"), register_rows, errors)
    validate_required_fields(data.get("requiredPerPromotionTaskFields"), errors)
    validate_defaults(data.get("queueDefaults"), errors)
    validate_summary(data.get("promotionSummary"), register_rows, errors)
    validate_tasks(data.get("promotionTasks"), register_rows, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    validate_index_links(data.get("indexRequirements"), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    domains = {domain_id for domain_id, _ in register_rows}
    sources = {source_id for _, source_id in register_rows}
    print(
        "domain-source card promotion queue audit ok: "
        f"tasks={len(register_rows)} domains={len(domains)} sources={len(sources)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
