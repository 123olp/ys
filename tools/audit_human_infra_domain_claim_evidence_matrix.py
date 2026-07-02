#!/usr/bin/env python3
"""审计域级 Claim-Evidence Matrix 的覆盖、来源锚点和边界契约。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "docs/reference/human-infra-domain-claim-evidence-matrix.json"
DOMAIN_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-falsifier-coverage.json"
BACKFILL_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-backfill.json"
EXTRACTION_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-extraction.json"

SCHEMA = "human-infra.domain-claim-evidence-matrix.v1"
STATUS = "active-domain-claim-evidence-matrix-gate"
REGISTER_LINK = "human-infra-domain-claim-evidence-matrix.json"
CLAIM_ID_RE = re.compile(r"^HIDOM-CL\d{3}$")

SOURCE_OF_TRUTH_KEYS = [
    "domainFalsifierRegister",
    "sourceCardBackfillRegister",
    "sourceCardExtractionRegister",
    "sourceCardSystem",
    "maturityGapRegister",
]

ROW_DEFAULT_KEYS = [
    "claimSource",
    "variableContractSource",
    "modelPositionSource",
    "falsifierSource",
    "evidenceBoundary",
    "modelUseAllowed",
    "modelUseBlocked",
    "nextExtractionStep",
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


def domain_entries(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(DOMAIN_REGISTER_PATH, errors, "domain falsifier register")
    if data.get("status") != "active-priority-domain-gate":
        fail(errors, "domain falsifier register status must be active-priority-domain-gate")
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
        if domain_id in result:
            fail(errors, f"duplicate domain register entry: {domain_id}")
        result[domain_id] = entry
    return result


def backfill_domain_sources(errors: list[str]) -> dict[str, list[str]]:
    data = load_json(BACKFILL_PATH, errors, "source-card backfill register")
    coverage = data.get("domainCoverage") if data else None
    if not isinstance(coverage, list):
        fail(errors, "source-card backfill domainCoverage must be a list")
        return {}
    result: dict[str, list[str]] = {}
    for index, item in enumerate(coverage):
        if not isinstance(item, dict):
            fail(errors, f"domainCoverage[{index}] must be an object")
            continue
        domain_id = item.get("domainId")
        if not isinstance(domain_id, str) or not domain_id.strip():
            fail(errors, f"domainCoverage[{index}].domainId missing")
            continue
        source_ids = require_string_list(item.get("sourceAnchors"), f"{domain_id}.sourceAnchors", errors, 1)
        if domain_id in result:
            fail(errors, f"duplicate backfill domainCoverage entry: {domain_id}")
        result[domain_id] = source_ids
    return result


def extracted_source_ids(errors: list[str]) -> set[str]:
    data = load_json(EXTRACTION_PATH, errors, "source-card extraction register")
    if data.get("status") != "active-field-source-card-extraction-gate":
        fail(errors, "source-card extraction register status must be active-field-source-card-extraction-gate")
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
        if source_id in result:
            fail(errors, f"duplicate extracted sourceId: {source_id}")
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
    for key in ROW_DEFAULT_KEYS:
        if key in {"modelUseAllowed", "modelUseBlocked"}:
            require_string_list(defaults.get(key), f"rowDefaults.{key}", errors, 3)
        else:
            require_string(defaults.get(key), f"rowDefaults.{key}", errors)


def validate_domain_contract(domain_id: str, entry: dict[str, Any], errors: list[str]) -> int:
    require_string(entry.get("strongClaim"), f"{domain_id}.strongClaim", errors)
    require_string(entry.get("modelPosition"), f"{domain_id}.modelPosition", errors)
    variables = entry.get("variables")
    if not isinstance(variables, dict):
        fail(errors, f"{domain_id}.variables must be an object")
    else:
        for key in ["inputs", "mediators", "outputs"]:
            require_string_list(variables.get(key), f"{domain_id}.variables.{key}", errors, 2)
    falsifiers = entry.get("falsifiers")
    if not isinstance(falsifiers, list) or len(falsifiers) < 2:
        fail(errors, f"{domain_id}.falsifiers must contain at least 2 falsifiers")
        falsifier_count = 0
    else:
        falsifier_count = len(falsifiers)
        for index, falsifier in enumerate(falsifiers):
            if not isinstance(falsifier, dict):
                fail(errors, f"{domain_id}.falsifiers[{index}] must be an object")
                continue
            require_string(falsifier.get("condition"), f"{domain_id}.falsifiers[{index}].condition", errors)
            require_string(
                falsifier.get("downgradeAction"),
                f"{domain_id}.falsifiers[{index}].downgradeAction",
                errors,
            )
            require_string(falsifier.get("evidenceNeeded"), f"{domain_id}.falsifiers[{index}].evidenceNeeded", errors)
    require_string_list(entry.get("prohibitedUses"), f"{domain_id}.prohibitedUses", errors, 2)
    require_string(entry.get("nextEvidenceAction"), f"{domain_id}.nextEvidenceAction", errors)
    return falsifier_count


def validate_rows(
    rows: Any,
    domains: dict[str, dict[str, Any]],
    backfill: dict[str, list[str]],
    extracted_sources: set[str],
    errors: list[str],
) -> tuple[int, int, int]:
    if not isinstance(rows, list):
        fail(errors, "domainClaimRows must be a list")
        return (0, 0, 0)

    row_domain_ids: set[str] = set()
    claim_ids: set[str] = set()
    source_refs: set[str] = set()
    falsifier_total = 0

    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"domainClaimRows[{index}] must be an object")
            continue
        claim_id = require_string(row.get("domainClaimId"), f"domainClaimRows[{index}].domainClaimId", errors)
        if claim_id and not CLAIM_ID_RE.match(claim_id):
            fail(errors, f"{claim_id} must match HIDOM-CL###")
        if claim_id in claim_ids:
            fail(errors, f"duplicate domainClaimId: {claim_id}")
        claim_ids.add(claim_id)

        domain_id = require_string(row.get("domainId"), f"{claim_id}.domainId", errors)
        if not domain_id:
            continue
        if domain_id in row_domain_ids:
            fail(errors, f"duplicate domainClaimRows domainId: {domain_id}")
        row_domain_ids.add(domain_id)

        if domain_id not in domains:
            fail(errors, f"{domain_id} missing from domain falsifier register")
            continue
        if domain_id not in backfill:
            fail(errors, f"{domain_id} missing from source-card backfill domainCoverage")
            continue

        source_ids = require_string_list(row.get("sourceCardIds"), f"{domain_id}.sourceCardIds", errors, 1)
        expected_sources = backfill[domain_id]
        if source_ids != expected_sources:
            fail(errors, f"{domain_id}.sourceCardIds must exactly match backfill sourceAnchors")
        for source_id in source_ids:
            source_refs.add(source_id)
            if source_id not in extracted_sources:
                fail(errors, f"{domain_id} references source without field extraction: {source_id}")

        falsifier_total += validate_domain_contract(domain_id, domains[domain_id], errors)

    expected_domains = set(domains)
    missing_domains = sorted(expected_domains - row_domain_ids)
    stale_domains = sorted(row_domain_ids - expected_domains)
    if missing_domains:
        fail(errors, f"matrix missing domain rows: {', '.join(missing_domains)}")
    if stale_domains:
        fail(errors, f"matrix has stale domain rows: {', '.join(stale_domains)}")

    backfill_domains = set(backfill)
    if row_domain_ids != backfill_domains:
        missing = sorted(backfill_domains - row_domain_ids)
        stale = sorted(row_domain_ids - backfill_domains)
        if missing:
            fail(errors, f"matrix missing backfill domains: {', '.join(missing)}")
        if stale:
            fail(errors, f"matrix has domains absent from backfill: {', '.join(stale)}")

    return (len(row_domain_ids), len(source_refs), falsifier_total)


def validate_summary(summary: Any, row_count: int, source_count: int, errors: list[str]) -> None:
    if not isinstance(summary, dict):
        fail(errors, "coverageSummary must be an object")
        return
    covered_domains = require_int(summary.get("coveredDomainCount"), "coverageSummary.coveredDomainCount", errors)
    if covered_domains is not None and covered_domains != row_count:
        fail(errors, f"coverageSummary.coveredDomainCount must equal row count ({row_count})")
    covered_sources = require_int(summary.get("coveredSourceAnchorCount"), "coverageSummary.coveredSourceAnchorCount", errors)
    if covered_sources is not None and covered_sources != source_count:
        fail(errors, f"coverageSummary.coveredSourceAnchorCount must equal unique source refs ({source_count})")
    if summary.get("domainRegisterStatus") != "active-priority-domain-gate":
        fail(errors, "coverageSummary.domainRegisterStatus must be active-priority-domain-gate")
    if summary.get("sourceCardExtractionStatus") != "active-field-source-card-extraction-gate":
        fail(errors, "coverageSummary.sourceCardExtractionStatus must be active-field-source-card-extraction-gate")
    require_string(summary.get("matrixCompletionState"), "coverageSummary.matrixCompletionState", errors)
    require_string_list(summary.get("remainingWork"), "coverageSummary.remainingWork", errors, 2)


def validate_index_links(paths: Any, errors: list[str]) -> None:
    for relative_path in require_string_list(paths, "indexRequirements", errors, 2):
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link domain claim-evidence matrix: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(MATRIX_PATH, errors, "domain claim-evidence matrix")
    domains = domain_entries(errors)
    backfill = backfill_domain_sources(errors)
    extracted_sources = extracted_source_ids(errors)

    if not data:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("matrixId"), "matrixId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    validate_source_of_truth(data, errors)
    rows = data.get("domainClaimRows")
    row_count = len(rows) if isinstance(rows, list) else 0
    validate_scope(data.get("scope"), row_count, errors)
    validate_defaults(data.get("rowDefaults"), errors)
    domain_count, source_count, falsifier_count = validate_rows(rows, domains, backfill, extracted_sources, errors)
    validate_summary(data.get("coverageSummary"), domain_count, source_count, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 3)
    validate_index_links(data.get("indexRequirements"), errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "domain claim-evidence matrix audit ok: "
        f"rows={domain_count} source_refs={source_count} falsifiers={falsifier_count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
