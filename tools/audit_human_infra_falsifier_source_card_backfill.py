#!/usr/bin/env python3
"""审计论文强主张和优先域反证的 Source Card 锚点回填。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-falsifier-source-card-backfill.json"
DOMAIN_REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-falsifier-coverage.json"
PAPER_REGISTER_PATH = ROOT / "docs/reference/human-infra-paper-claim-register.json"

SCHEMA = "human-infra.falsifier-source-card-backfill.v1"
STATUS = "active-source-anchor-backfill-gate"
REGISTER_LINK = "human-infra-falsifier-source-card-backfill.json"

REQUIRED_TOP_LEVEL_LOCAL_PATHS = [
    "domainFalsifierRegister",
    "paperClaimRegister",
    "sourceCardSystem",
    "maturityGapRegister",
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


def require_bool(value: Any, context: str, errors: list[str]) -> bool | None:
    if not isinstance(value, bool):
        fail(errors, f"{context} must be boolean")
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


def validate_scope(scope: Any, errors: list[str]) -> None:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return
    require_string(scope.get("coverageLevel"), "scope.coverageLevel", errors)
    if require_bool(scope.get("coversAllCurrentDomainFalsifierEntries"), "scope.coversAllCurrentDomainFalsifierEntries", errors) is not True:
        fail(errors, "scope must declare all current domain falsifier entries covered")
    if require_bool(scope.get("coversAllCurrentPaperStrongClaims"), "scope.coversAllCurrentPaperStrongClaims", errors) is not True:
        fail(errors, "scope must declare all current paper strong claims covered")
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 3)


def validate_source_anchors(value: Any, errors: list[str]) -> set[str]:
    if not isinstance(value, list) or len(value) < 8:
        fail(errors, "sourceAnchors must contain at least 8 source-anchor objects")
        return set()
    seen: set[str] = set()
    for index, item in enumerate(value):
        context = f"sourceAnchors[{index}]"
        if not isinstance(item, dict):
            fail(errors, f"{context} must be an object")
            continue
        source_id = require_string(item.get("sourceId"), f"{context}.sourceId", errors)
        if source_id:
            if source_id in seen:
                fail(errors, f"duplicate sourceId: {source_id}")
            seen.add(source_id)
        require_string(item.get("sourceType"), f"{context}.sourceType", errors)
        require_string(item.get("title"), f"{context}.title", errors)
        url = require_string(item.get("url"), f"{context}.url", errors)
        if url and not url.startswith("https://"):
            fail(errors, f"{context}.url must start with https://")
        require_string(item.get("evidenceRole"), f"{context}.evidenceRole", errors)
        require_string_list(item.get("supports"), f"{context}.supports", errors, 2)
        require_string(item.get("transferBoundary"), f"{context}.transferBoundary", errors)
        require_string(item.get("localUse"), f"{context}.localUse", errors)
    return seen


def source_refs_exist(source_ids: list[str], known_sources: set[str], context: str, errors: list[str]) -> None:
    for source_id in source_ids:
        if source_id not in known_sources:
            fail(errors, f"{context} references unknown source anchor: {source_id}")


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


def expected_paper_claims(errors: list[str]) -> dict[str, set[str]]:
    data = load_json(PAPER_REGISTER_PATH, errors, "paper claim register")
    papers = data.get("papers") if data else None
    if not isinstance(papers, list):
        fail(errors, "paper claim register papers must be a list")
        return {}
    result: dict[str, set[str]] = {}
    for paper_index, paper in enumerate(papers):
        if not isinstance(paper, dict):
            fail(errors, f"paper register papers[{paper_index}] must be an object")
            continue
        paper_id = paper.get("paperId")
        if not isinstance(paper_id, str) or not paper_id.strip():
            fail(errors, f"paper register papers[{paper_index}].paperId missing")
            continue
        claims = paper.get("strongClaims")
        if not isinstance(claims, list):
            fail(errors, f"{paper_id}.strongClaims must be a list")
            continue
        result[paper_id] = set()
        for claim_index, claim in enumerate(claims):
            if not isinstance(claim, dict):
                fail(errors, f"{paper_id}.strongClaims[{claim_index}] must be an object")
                continue
            claim_id = claim.get("claimId")
            if isinstance(claim_id, str) and claim_id.strip():
                result[paper_id].add(claim_id)
            else:
                fail(errors, f"{paper_id}.strongClaims[{claim_index}].claimId missing")
    return result


def validate_domain_coverage(
    value: Any,
    expected_ids: set[str],
    known_sources: set[str],
    errors: list[str],
) -> int:
    if not isinstance(value, list) or not value:
        fail(errors, "domainCoverage must be a non-empty list")
        return 0
    seen: set[str] = set()
    for index, item in enumerate(value):
        context = f"domainCoverage[{index}]"
        if not isinstance(item, dict):
            fail(errors, f"{context} must be an object")
            continue
        domain_id = require_string(item.get("domainId"), f"{context}.domainId", errors)
        if domain_id:
            if domain_id in seen:
                fail(errors, f"duplicate domainCoverage domainId: {domain_id}")
            seen.add(domain_id)
        anchors = require_string_list(item.get("sourceAnchors"), f"{context}.sourceAnchors", errors, 2)
        source_refs_exist(anchors, known_sources, context, errors)
        require_string(item.get("supportedUse"), f"{context}.supportedUse", errors)
        require_string(item.get("transferBoundary"), f"{context}.transferBoundary", errors)
        require_string(item.get("remainingGap"), f"{context}.remainingGap", errors)
        require_string(item.get("nextAction"), f"{context}.nextAction", errors)

    missing = sorted(expected_ids - seen)
    stale = sorted(seen - expected_ids)
    if missing:
        fail(errors, f"domainCoverage missing domains: {', '.join(missing)}")
    if stale:
        fail(errors, f"domainCoverage contains stale domains: {', '.join(stale)}")
    return len(seen)


def validate_paper_claim_coverage(
    value: Any,
    expected_claims: dict[str, set[str]],
    known_sources: set[str],
    errors: list[str],
) -> tuple[int, int]:
    if not isinstance(value, list) or not value:
        fail(errors, "paperClaimCoverage must be a non-empty list")
        return (0, 0)
    seen_papers: set[str] = set()
    covered_claims: dict[str, set[str]] = {}
    for index, item in enumerate(value):
        context = f"paperClaimCoverage[{index}]"
        if not isinstance(item, dict):
            fail(errors, f"{context} must be an object")
            continue
        paper_id = require_string(item.get("paperId"), f"{context}.paperId", errors)
        if paper_id:
            if paper_id in seen_papers:
                fail(errors, f"duplicate paperClaimCoverage paperId: {paper_id}")
            seen_papers.add(paper_id)
        claim_ids = set(require_string_list(item.get("paperClaimIds"), f"{context}.paperClaimIds", errors, 1))
        covered_claims[paper_id] = claim_ids
        anchors = require_string_list(item.get("sourceAnchors"), f"{context}.sourceAnchors", errors, 2)
        source_refs_exist(anchors, known_sources, context, errors)
        require_string(item.get("supportedUse"), f"{context}.supportedUse", errors)
        require_string(item.get("transferBoundary"), f"{context}.transferBoundary", errors)
        require_string(item.get("remainingGap"), f"{context}.remainingGap", errors)
        require_string(item.get("nextAction"), f"{context}.nextAction", errors)

    missing_papers = sorted(set(expected_claims) - seen_papers)
    stale_papers = sorted(seen_papers - set(expected_claims))
    if missing_papers:
        fail(errors, f"paperClaimCoverage missing papers: {', '.join(missing_papers)}")
    if stale_papers:
        fail(errors, f"paperClaimCoverage contains stale papers: {', '.join(stale_papers)}")

    total_claims = 0
    for paper_id, expected_ids in expected_claims.items():
        actual_ids = covered_claims.get(paper_id, set())
        missing = sorted(expected_ids - actual_ids)
        stale = sorted(actual_ids - expected_ids)
        if missing:
            fail(errors, f"{paper_id} missing paper claim coverage: {', '.join(missing)}")
        if stale:
            fail(errors, f"{paper_id} contains stale paper claim coverage: {', '.join(stale)}")
        total_claims += len(actual_ids)
    return (len(seen_papers), total_claims)


def validate_index_links(paths: list[str], errors: list[str]) -> None:
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link source-card backfill register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "source-card backfill register")
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
    validate_scope(data.get("scope"), errors)

    expected_domains = expected_domain_ids(errors)
    expected_claims = expected_paper_claims(errors)
    known_sources = validate_source_anchors(data.get("sourceAnchors"), errors)
    domain_count = validate_domain_coverage(data.get("domainCoverage"), expected_domains, known_sources, errors)
    paper_count, paper_claim_count = validate_paper_claim_coverage(
        data.get("paperClaimCoverage"),
        expected_claims,
        known_sources,
        errors,
    )

    index_paths = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 1)
    validate_index_links(index_paths, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 3)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "falsifier source-card backfill audit ok: "
        f"source_anchors={len(known_sources)} domains={domain_count} "
        f"papers={paper_count} paper_claims={paper_claim_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
