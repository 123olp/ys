#!/usr/bin/env python3
"""审计反证来源的字段级 Source Card 抽取账本。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-extraction.json"
BACKFILL_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-backfill.json"
DOMAIN_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-falsifier-coverage.json"
PAPER_REGISTER_PATH = ROOT / "docs/reference/human-infra-paper-claim-register.json"

SCHEMA = "human-infra.falsifier-source-card-extraction.v1"
STATUS = "active-field-source-card-extraction-gate"
REGISTER_LINK = "human-infra-falsifier-source-card-extraction.json"
CARD_STATUS = "field-extracted-v0.1"

REQUIRED_TOP_LEVEL_LOCAL_PATHS = [
    "backfillRegister",
    "sourceCardSystem",
    "domainFalsifierRegister",
    "paperClaimRegister",
    "maturityGapRegister",
    "humanReadablePack",
]

REQUIRED_MODEL_POSITION_KEYS = [
    "stateVariable",
    "stateTransition",
    "hazard",
    "observationProcess",
    "actionPolicy",
    "timeAccounting",
    "optionValue",
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


def backfill_sources(errors: list[str]) -> dict[str, dict[str, Any]]:
    data = load_json(BACKFILL_PATH, errors, "source-card backfill register")
    anchors = data.get("sourceAnchors") if data else None
    if not isinstance(anchors, list):
        fail(errors, "backfill register sourceAnchors must be a list")
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(anchors):
        if not isinstance(item, dict):
            fail(errors, f"backfill sourceAnchors[{index}] must be an object")
            continue
        source_id = item.get("sourceId")
        if not isinstance(source_id, str) or not source_id.strip():
            fail(errors, f"backfill sourceAnchors[{index}].sourceId missing")
            continue
        result[source_id] = item
    return result


def expected_domain_ids(errors: list[str]) -> set[str]:
    data = load_json(DOMAIN_REGISTER_PATH, errors, "domain falsifier register")
    entries = data.get("entries") if data else None
    if not isinstance(entries, list):
        fail(errors, "domain falsifier register entries must be a list")
        return set()
    result: set[str] = set()
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            fail(errors, f"domain register entries[{index}] must be an object")
            continue
        domain_id = entry.get("domainId")
        if isinstance(domain_id, str) and domain_id.strip():
            result.add(domain_id)
        else:
            fail(errors, f"domain register entries[{index}].domainId missing")
    return result


def expected_paper_claim_ids(errors: list[str]) -> set[str]:
    data = load_json(PAPER_REGISTER_PATH, errors, "paper claim register")
    papers = data.get("papers") if data else None
    if not isinstance(papers, list):
        fail(errors, "paper claim register papers must be a list")
        return set()
    result: set[str] = set()
    for paper_index, paper in enumerate(papers):
        if not isinstance(paper, dict):
            fail(errors, f"paper register papers[{paper_index}] must be an object")
            continue
        claims = paper.get("strongClaims")
        if not isinstance(claims, list):
            fail(errors, f"paper register papers[{paper_index}].strongClaims must be a list")
            continue
        for claim_index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                fail(errors, f"paper register papers[{paper_index}].strongClaims[{claim_index}] must be an object")
                continue
            claim_id = claim.get("claimId")
            if isinstance(claim_id, str) and claim_id.strip():
                result.add(claim_id)
            else:
                fail(errors, f"paper register papers[{paper_index}].strongClaims[{claim_index}].claimId missing")
    return result


def validate_scope(scope: Any, card_count: int, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    require_string(scope.get("coverageLevel"), "scope.coverageLevel", errors)
    selected_count = require_int(scope.get("selectedSourceAnchorCount"), "scope.selectedSourceAnchorCount", errors)
    if selected_count is not None and selected_count != card_count:
        fail(errors, f"scope.selectedSourceAnchorCount must equal sourceCards length ({card_count})")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_source_identity(
    identity: Any,
    context: str,
    backfill: dict[str, Any],
    errors: list[str],
) -> None:
    if not isinstance(identity, dict):
        fail(errors, f"{context}.sourceIdentity must be an object")
        return
    require_string(identity.get("title"), f"{context}.sourceIdentity.title", errors)
    require_string(identity.get("year"), f"{context}.sourceIdentity.year", errors)
    url = require_string(identity.get("url"), f"{context}.sourceIdentity.url", errors)
    if url and not url.startswith("https://"):
        fail(errors, f"{context}.sourceIdentity.url must start with https://")
    backfill_url = backfill.get("url")
    if isinstance(backfill_url, str) and url and url != backfill_url:
        fail(errors, f"{context}.sourceIdentity.url must match backfill URL")
    require_string(identity.get("sourceType"), f"{context}.sourceIdentity.sourceType", errors)


def validate_mapping(
    mapping: Any,
    context: str,
    domain_ids: set[str],
    paper_claim_ids: set[str],
    errors: list[str],
) -> tuple[int, int]:
    if not isinstance(mapping, dict):
        fail(errors, f"{context}.humanInfraMapping must be an object")
        return (0, 0)
    domains = require_string_list(mapping.get("domainIds"), f"{context}.humanInfraMapping.domainIds", errors, 1)
    claims = require_string_list(mapping.get("paperClaimIds"), f"{context}.humanInfraMapping.paperClaimIds", errors, 1)
    for domain_id in domains:
        if domain_id not in domain_ids:
            fail(errors, f"{context} references unknown domainId: {domain_id}")
    for claim_id in claims:
        if claim_id not in paper_claim_ids:
            fail(errors, f"{context} references unknown paper claimId: {claim_id}")
    require_string_list(
        mapping.get("subjectContinuityVariables"),
        f"{context}.humanInfraMapping.subjectContinuityVariables",
        errors,
        2,
    )
    require_string(mapping.get("valueLens"), f"{context}.humanInfraMapping.valueLens", errors)
    require_string(mapping.get("safetyBoundary"), f"{context}.humanInfraMapping.safetyBoundary", errors)
    return (len(domains), len(claims))


def validate_model_position(value: Any, context: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{context}.modelPosition must be an object")
        return
    for key in REQUIRED_MODEL_POSITION_KEYS:
        require_string(value.get(key), f"{context}.modelPosition.{key}", errors)


def validate_source_cards(
    value: Any,
    known_sources: dict[str, dict[str, Any]],
    domain_ids: set[str],
    paper_claim_ids: set[str],
    errors: list[str],
) -> tuple[list[str], int, int]:
    if not isinstance(value, list) or len(value) < 8:
        fail(errors, "sourceCards must contain at least 8 field-level cards")
        return ([], 0, 0)

    seen: set[str] = set()
    domain_ref_count = 0
    paper_claim_ref_count = 0
    ordered_ids: list[str] = []
    for index, item in enumerate(value):
        context = f"sourceCards[{index}]"
        if not isinstance(item, dict):
            fail(errors, f"{context} must be an object")
            continue
        source_id = require_string(item.get("sourceId"), f"{context}.sourceId", errors)
        if source_id:
            if source_id in seen:
                fail(errors, f"duplicate sourceId: {source_id}")
            seen.add(source_id)
            ordered_ids.append(source_id)
            if source_id not in known_sources:
                fail(errors, f"{context}.sourceId not found in backfill register: {source_id}")
        if item.get("cardStatus") != CARD_STATUS:
            fail(errors, f"{context}.cardStatus must be {CARD_STATUS}")

        backfill = known_sources.get(source_id, {})
        validate_source_identity(item.get("sourceIdentity"), context, backfill, errors)
        require_string(item.get("oneSentenceUse"), f"{context}.oneSentenceUse", errors)
        domains_count, claims_count = validate_mapping(
            item.get("humanInfraMapping"),
            context,
            domain_ids,
            paper_claim_ids,
            errors,
        )
        domain_ref_count += domains_count
        paper_claim_ref_count += claims_count
        validate_model_position(item.get("modelPosition"), context, errors)
        require_string_list(item.get("evidenceRoles"), f"{context}.evidenceRoles", errors, 2)
        require_string_list(item.get("keyExtracts"), f"{context}.keyExtracts", errors, 3)
        require_string(item.get("supportedUse"), f"{context}.supportedUse", errors)
        require_string(item.get("falsifierUse"), f"{context}.falsifierUse", errors)
        require_string(item.get("transferBoundary"), f"{context}.transferBoundary", errors)
        require_string_list(item.get("risksAndMisreadings"), f"{context}.risksAndMisreadings", errors, 2)
        require_string(item.get("repositoryAction"), f"{context}.repositoryAction", errors)
        require_string(item.get("nextExtractionStep"), f"{context}.nextExtractionStep", errors)

    missing = sorted(set(known_sources) - seen)
    stale = sorted(seen - set(known_sources))
    if missing:
        fail(errors, f"sourceCards missing backfill source anchors: {', '.join(missing)}")
    if stale:
        fail(errors, f"sourceCards contains stale source anchors: {', '.join(stale)}")
    return (ordered_ids, domain_ref_count, paper_claim_ref_count)


def validate_coverage_summary(value: Any, source_ids: list[str], errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, "coverageSummary must be an object")
        return
    selected = require_string_list(value.get("selectedSourceAnchors"), "coverageSummary.selectedSourceAnchors", errors, 1)
    if selected and selected != source_ids:
        fail(errors, "coverageSummary.selectedSourceAnchors must exactly match sourceCards order")
    remaining_count = require_int(value.get("remainingSourceAnchorCount"), "coverageSummary.remainingSourceAnchorCount", errors)
    if remaining_count not in (None, 0):
        fail(errors, "coverageSummary.remainingSourceAnchorCount must be 0 when all current anchors are extracted")
    require_string(value.get("remainingWork"), "coverageSummary.remainingWork", errors)


def validate_index_links(paths: list[str], errors: list[str]) -> None:
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link source-card extraction register: {relative_path}")


def validate_human_pack(path_value: str, source_ids: list[str], errors: list[str]) -> None:
    target = repo_path(path_value, "humanReadablePack", errors)
    if target is None:
        return
    text = target.read_text(encoding="utf-8")
    for source_id in source_ids:
        if source_id not in text:
            fail(errors, f"humanReadablePack does not mention sourceId: {source_id}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "source-card extraction register")
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
    for key in REQUIRED_TOP_LEVEL_LOCAL_PATHS:
        value = require_string(data.get(key), key, errors)
        if value:
            repo_path(value, key, errors)

    known_sources = backfill_sources(errors)
    domain_ids = expected_domain_ids(errors)
    paper_claim_ids = expected_paper_claim_ids(errors)

    source_ids, domain_ref_count, paper_claim_ref_count = validate_source_cards(
        data.get("sourceCards"),
        known_sources,
        domain_ids,
        paper_claim_ids,
        errors,
    )
    validate_scope(data.get("scope"), len(source_ids), errors)
    validate_coverage_summary(data.get("coverageSummary"), source_ids, errors)
    validate_human_pack(require_string(data.get("humanReadablePack"), "humanReadablePack", errors), source_ids, errors)

    index_paths = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 1)
    validate_index_links(index_paths, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 3)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "falsifier source-card extraction audit ok: "
        f"cards={len(source_ids)} domains={domain_ref_count} "
        f"paper_claim_refs={paper_claim_ref_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
