#!/usr/bin/env python3
"""审计域 Source Card 字段抽取账本的 endpoint / population / uncertainty / transfer-boundary 槽位。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-source-card-field-extraction.json"
DOMAIN_MATRIX_PATH = ROOT / "docs/reference/human-infra-domain-claim-evidence-matrix.json"
DOMAIN_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-falsifier-coverage.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-extraction.json"

SCHEMA = "human-infra.domain-source-card-field-extraction.v1"
STATUS = "active-domain-field-extraction-gate"
REGISTER_LINK = "human-infra-domain-source-card-field-extraction.json"
FIELD_ID_RE = re.compile(r"^HIDOM-FLD\d{3}$")
CLAIM_ID_RE = re.compile(r"^HIDOM-CL\d{3}$")

SOURCE_OF_TRUTH_KEYS = [
    "domainClaimEvidenceMatrix",
    "domainFalsifierRegister",
    "sourceCardExtractionRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

DEFAULT_KEYS = [
    "claimFieldSource",
    "endpointFieldSource",
    "populationBoundary",
    "uncertaintyChannels",
    "transferBoundary",
    "fieldExtractionStatus",
    "blockedUses",
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


def domain_matrix_rows(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(DOMAIN_MATRIX_PATH, errors, "domain claim-evidence matrix")
    if data.get("status") != "active-domain-claim-evidence-matrix-gate":
        fail(errors, "domain claim-evidence matrix status must be active-domain-claim-evidence-matrix-gate")
    rows = data.get("domainClaimRows") if data else None
    if not isinstance(rows, list):
        fail(errors, "domain claim-evidence matrix domainClaimRows must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"domainClaimRows[{index}] must be an object")
            continue
        domain_id = row.get("domainId")
        if not isinstance(domain_id, str) or not domain_id.strip():
            fail(errors, f"domainClaimRows[{index}].domainId missing")
            continue
        result[domain_id] = row
    return result


def domain_register_entries(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(DOMAIN_REGISTER_PATH, errors, "domain falsifier register")
    entries = data.get("entries") if data else None
    if not isinstance(entries, list):
        fail(errors, "domain falsifier register entries must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(errors, f"domain register entries[{index}] must be an object")
            continue
        domain_id = entry.get("domainId")
        if not isinstance(domain_id, str) or not domain_id.strip():
            fail(errors, f"domain register entries[{index}].domainId missing")
            continue
        result[domain_id] = entry
    return result


def extracted_source_ids(errors: list[str]) -> set[str]:
    data = load_json(EXTRACTION_PATH, errors, "source-card extraction register")
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


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(scope: Any, row_count: int, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    require_string(scope.get("coverageLevel"), "scope.coverageLevel", errors)
    covered_count = require_int(scope.get("coveredDomainCount"), "scope.coveredDomainCount", errors)
    if covered_count is not None and covered_count != row_count:
        fail(errors, f"scope.coveredDomainCount must equal row count ({row_count})")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_defaults(defaults: Any, errors: list[str]) -> None:
    if not isinstance(defaults, dict):
        fail(errors, "rowDefaults must be an object")
        return
    for key in DEFAULT_KEYS:
        if key in {"uncertaintyChannels", "blockedUses"}:
            require_string_list(defaults.get(key), f"rowDefaults.{key}", errors, 4)
        else:
            require_string(defaults.get(key), f"rowDefaults.{key}", errors)
    blocked = set(defaults.get("blockedUses", [])) if isinstance(defaults.get("blockedUses"), list) else set()
    for required in {"calibrated-prediction", "individual-recommendation", "individual-death-date-output"}:
        if required not in blocked:
            fail(errors, f"rowDefaults.blockedUses missing {required}")


def validate_rows(
    rows: Any,
    matrix_rows: dict[str, dict[str, Any]],
    domain_entries: dict[str, dict[str, Any]],
    extracted_sources: set[str],
    errors: list[str],
) -> tuple[int, int, int]:
    if not isinstance(rows, list):
        fail(errors, "fieldRows must be a list")
        return (0, 0, 0)

    domain_ids: set[str] = set()
    field_ids: set[str] = set()
    source_refs: set[str] = set()
    endpoint_count = 0

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"fieldRows[{index}] must be an object")
            continue
        field_id = require_string(row.get("fieldCardId"), f"fieldRows[{index}].fieldCardId", errors)
        if field_id and not FIELD_ID_RE.match(field_id):
            fail(errors, f"{field_id} must match HIDOM-FLD###")
        if field_id in field_ids:
            fail(errors, f"duplicate fieldCardId: {field_id}")
        field_ids.add(field_id)

        claim_id = require_string(row.get("domainClaimId"), f"{field_id}.domainClaimId", errors)
        if claim_id and not CLAIM_ID_RE.match(claim_id):
            fail(errors, f"{claim_id} must match HIDOM-CL###")

        domain_id = require_string(row.get("domainId"), f"{field_id}.domainId", errors)
        if not domain_id:
            continue
        if domain_id in domain_ids:
            fail(errors, f"duplicate fieldRows domainId: {domain_id}")
        domain_ids.add(domain_id)

        matrix_row = matrix_rows.get(domain_id)
        domain_entry = domain_entries.get(domain_id)
        if matrix_row is None:
            fail(errors, f"{domain_id} missing from domain Claim-Evidence Matrix")
            continue
        if domain_entry is None:
            fail(errors, f"{domain_id} missing from domain falsifier register")
            continue
        if claim_id and claim_id != matrix_row.get("domainClaimId"):
            fail(errors, f"{domain_id}.domainClaimId must match domain Claim-Evidence Matrix")

        source_ids = require_string_list(row.get("sourceCardIds"), f"{domain_id}.sourceCardIds", errors, 1)
        if source_ids != matrix_row.get("sourceCardIds"):
            fail(errors, f"{domain_id}.sourceCardIds must match domain Claim-Evidence Matrix")
        for source_id in source_ids:
            source_refs.add(source_id)
            if source_id not in extracted_sources:
                fail(errors, f"{domain_id} references source without field extraction: {source_id}")

        variables = domain_entry.get("variables")
        expected_outputs = variables.get("outputs") if isinstance(variables, dict) else None
        endpoints = require_string_list(row.get("endpointCandidates"), f"{domain_id}.endpointCandidates", errors, 2)
        if endpoints != expected_outputs:
            fail(errors, f"{domain_id}.endpointCandidates must match domain variables.outputs")
        endpoint_count += len(endpoints)

        expected_action = domain_entry.get("nextEvidenceAction")
        action = require_string(row.get("nextFieldExtractionAction"), f"{domain_id}.nextFieldExtractionAction", errors)
        if isinstance(expected_action, str) and action != expected_action:
            fail(errors, f"{domain_id}.nextFieldExtractionAction must match domain nextEvidenceAction")

    expected_domains = set(matrix_rows)
    missing = sorted(expected_domains - domain_ids)
    stale = sorted(domain_ids - expected_domains)
    if missing:
        fail(errors, f"field register missing domains: {', '.join(missing)}")
    if stale:
        fail(errors, f"field register has stale domains: {', '.join(stale)}")
    return (len(domain_ids), len(source_refs), endpoint_count)


def validate_summary(summary: Any, domain_count: int, source_count: int, endpoint_count: int, errors: list[str]) -> None:
    if not isinstance(summary, dict):
        fail(errors, "coverageSummary must be an object")
        return
    for key, expected in {
        "coveredDomainCount": domain_count,
        "coveredFieldRowCount": domain_count,
        "coveredEndpointCandidateCount": endpoint_count,
        "coveredSourceAnchorCount": source_count,
    }.items():
        value = require_int(summary.get(key), f"coverageSummary.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"coverageSummary.{key} must equal {expected}")
    require_string(summary.get("fieldCompletionState"), "coverageSummary.fieldCompletionState", errors)
    require_string_list(summary.get("remainingWork"), "coverageSummary.remainingWork", errors, 3)


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_string_list(paths, "indexRequirements", errors, 2):
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link domain source-card field extraction register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "domain source-card field extraction register")
    matrix_rows = domain_matrix_rows(errors)
    domain_entries = domain_register_entries(errors)
    source_ids = extracted_source_ids(errors)

    if not data:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    rows = data.get("fieldRows")
    row_count = len(rows) if isinstance(rows, list) else 0
    validate_source_of_truth(data, errors)
    validate_scope(data.get("scope"), row_count, errors)
    validate_defaults(data.get("rowDefaults"), errors)
    domain_count, source_count, endpoint_count = validate_rows(rows, matrix_rows, domain_entries, source_ids, errors)
    validate_summary(data.get("coverageSummary"), domain_count, source_count, endpoint_count, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 3)
    validate_index_links(data.get("indexRequirements"), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "domain source-card field extraction audit ok: "
        f"rows={domain_count} source_refs={source_count} endpoint_candidates={endpoint_count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
