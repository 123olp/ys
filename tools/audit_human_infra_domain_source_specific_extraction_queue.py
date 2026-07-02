#!/usr/bin/env python3
"""审计域-来源深读队列契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "docs/reference/human-infra-domain-source-specific-extraction-queue.json"
FIELD_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-source-card-field-extraction.json"
SOURCE_EXTRACTION_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-extraction.json"

SCHEMA = "human-infra.domain-source-specific-extraction-queue.v1"
STATUS = "active-source-specific-extraction-queue-gate"
REGISTER_LINK = "human-infra-domain-source-specific-extraction-queue.json"

SOURCE_OF_TRUTH_KEYS = [
    "domainSourceCardFieldExtraction",
    "domainClaimEvidenceMatrix",
    "sourceCardExtractionRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

REQUIRED_TASK_FIELDS = [
    "domainId",
    "domainClaimId",
    "fieldCardId",
    "sourceCardId",
    "exactClaimUse",
    "endpointDefinition",
    "populationOrSample",
    "effectOrMechanismSignal",
    "uncertaintyOrBias",
    "transferBoundary",
    "modelAdmissionDecision",
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


def extracted_source_ids(errors: list[str]) -> set[str]:
    data = load_json(SOURCE_EXTRACTION_PATH, errors, "source-card extraction register")
    cards = data.get("sourceCards") if data else None
    if not isinstance(cards, list):
        fail(errors, "source-card extraction sourceCards must be a list")
        return set()
    result: set[str] = set()
    for index, card in enumerate(cards):
        if not isinstance(card, dict):
            fail(errors, f"sourceCards[{index}] must be an object")
            continue
        source_id = card.get("sourceId")
        if not isinstance(source_id, str) or not source_id.strip():
            fail(errors, f"sourceCards[{index}].sourceId missing")
            continue
        result.add(source_id)
    return result


def derived_pairs(errors: list[str]) -> tuple[int, int, int, set[str]]:
    data = load_json(FIELD_REGISTER_PATH, errors, "domain source-card field extraction register")
    rows = data.get("fieldRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "domain field extraction fieldRows must be a list")
        return (0, 0, 0, set())

    pair_keys: set[tuple[str, str]] = set()
    domain_ids: set[str] = set()
    source_ids: set[str] = set()
    extracted = extracted_source_ids(errors)

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"fieldRows[{index}] must be an object")
            continue
        domain_id = require_string(row.get("domainId"), f"fieldRows[{index}].domainId", errors)
        require_string(row.get("domainClaimId"), f"{domain_id}.domainClaimId", errors)
        require_string(row.get("fieldCardId"), f"{domain_id}.fieldCardId", errors)
        source_cards = require_string_list(row.get("sourceCardIds"), f"{domain_id}.sourceCardIds", errors, 1)
        if domain_id:
            domain_ids.add(domain_id)
        for source_id in source_cards:
            pair_key = (domain_id, source_id)
            if pair_key in pair_keys:
                fail(errors, f"duplicate domain-source pair: {domain_id}/{source_id}")
            pair_keys.add(pair_key)
            source_ids.add(source_id)
            if source_id not in extracted:
                fail(errors, f"{domain_id} references source without field extraction: {source_id}")

    return (len(domain_ids), len(rows), len(pair_keys), source_ids)


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(scope: Any, domain_count: int, row_count: int, task_count: int, source_count: int, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    require_string(scope.get("coverageLevel"), "scope.coverageLevel", errors)
    if scope.get("derivedTaskUnit") != "domainId + sourceCardId":
        fail(errors, "scope.derivedTaskUnit must be domainId + sourceCardId")
    for key, expected in {
        "coveredDomainCount": domain_count,
        "coveredFieldRowCount": row_count,
        "expectedTaskCount": task_count,
        "expectedUniqueSourceAnchorCount": source_count,
    }.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_required_fields(fields: Any, errors: list[str]) -> None:
    actual = require_string_list(fields, "requiredPerTaskFields", errors, len(REQUIRED_TASK_FIELDS))
    if actual != REQUIRED_TASK_FIELDS:
        fail(errors, "requiredPerTaskFields must exactly match the source-specific extraction contract")


def validate_defaults(defaults: Any, errors: list[str]) -> None:
    if not isinstance(defaults, dict):
        fail(errors, "queueDefaults must be an object")
        return
    if defaults.get("taskStatus") != "queued-source-specific-extraction-required":
        fail(errors, "queueDefaults.taskStatus must be queued-source-specific-extraction-required")
    if defaults.get("modelAdmissionDecision") != "blocked-until-source-specific-fields-are-extracted":
        fail(errors, "queueDefaults.modelAdmissionDecision must block model admission")
    blocked = set(require_string_list(defaults.get("blockedUses"), "queueDefaults.blockedUses", errors, 4))
    for required in {"calibrated-prediction", "individual-recommendation", "individual-death-date-output", "domain-claim-upgrade"}:
        if required not in blocked:
            fail(errors, f"queueDefaults.blockedUses missing {required}")
    require_string(defaults.get("minimumExtractionQuestion"), "queueDefaults.minimumExtractionQuestion", errors)


def validate_summary(summary: Any, domain_count: int, row_count: int, task_count: int, source_count: int, errors: list[str]) -> None:
    if not isinstance(summary, dict):
        fail(errors, "derivedQueueSummary must be an object")
        return
    for key, expected in {
        "coveredDomainCount": domain_count,
        "coveredFieldRowCount": row_count,
        "derivedTaskCount": task_count,
        "uniqueSourceAnchorCount": source_count,
    }.items():
        value = require_int(summary.get(key), f"derivedQueueSummary.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"derivedQueueSummary.{key} must equal {expected}")
    require_string(summary.get("fieldCompletionState"), "derivedQueueSummary.fieldCompletionState", errors)
    require_string_list(summary.get("remainingWork"), "derivedQueueSummary.remainingWork", errors, 3)


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_string_list(paths, "indexRequirements", errors, 2):
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link domain-source queue: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(QUEUE_PATH, errors, "domain-source extraction queue")
    domain_count, row_count, task_count, source_ids = derived_pairs(errors)
    source_count = len(source_ids)

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
    validate_scope(data.get("scope"), domain_count, row_count, task_count, source_count, errors)
    validate_required_fields(data.get("requiredPerTaskFields"), errors)
    validate_defaults(data.get("queueDefaults"), errors)
    validate_summary(data.get("derivedQueueSummary"), domain_count, row_count, task_count, source_count, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 3)
    validate_index_links(data.get("indexRequirements"), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "domain-source extraction queue audit ok: "
        f"domains={domain_count} field_rows={row_count} tasks={task_count} source_refs={source_count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
