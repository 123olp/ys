#!/usr/bin/env python3
"""审计 arXiv-style 论文页的强主张、反证条件和禁止用途边界。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-paper-claim-register.json"

REQUIRED_SCHEMA = "human-infra.paper-claim-register.v1"
REQUIRED_STATUS = "active-paper-claim-gate"
REGISTER_LINK = "human-infra-paper-claim-register.json"
CLAIM_RE = re.compile(r"\bHI-CL\d+\b")
PAPER_CLAIM_RE = re.compile(r"^HIPAPER-CL\d+$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing register: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "register must be a JSON object")
        return {}
    return data


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
    return value


def require_string_list(value: Any, context: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not value:
        fail(errors, f"{context} must be a non-empty list")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def require_optional_string_list(value: Any, context: str, errors: list[str]) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        fail(errors, f"{context} must be a list")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, errors: list[str], context: str) -> Path | None:
    if not isinstance(relative_path, str) or not relative_path.strip():
        fail(errors, f"{context} must be a non-empty local path")
        return None
    if relative_path.startswith(("http://", "https://")):
        fail(errors, f"{context} must be local, not URL: {relative_path}")
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


def collect_paper_reader_pages() -> set[str]:
    pages: set[str] = set()
    for page in (ROOT / "web/src/pages").rglob("*.astro"):
        text = page.read_text(encoding="utf-8")
        if "PaperReaderLayout" in text:
            pages.add(str(page.relative_to(ROOT)))
    return pages


def known_core_claims(errors: list[str], core_matrix: str) -> set[str]:
    path = repo_path(core_matrix, errors, "coreMatrix")
    if path is None:
        return set()
    claims = set(CLAIM_RE.findall(path.read_text(encoding="utf-8")))
    expected = {f"HI-CL{index}" for index in range(1, 8)}
    missing = sorted(expected - claims)
    if missing:
        fail(errors, f"core matrix missing expected claims: {', '.join(missing)}")
    return claims


def validate_claim_ids(
    claims: list[str],
    known_claims: set[str],
    context: str,
    errors: list[str],
) -> None:
    for claim in claims:
        if claim not in known_claims:
            fail(errors, f"{context} references unknown core claim: {claim}")


def combined_source_text(page_path: Path, source_paths: list[str], errors: list[str], context: str) -> str:
    chunks = [page_path.read_text(encoding="utf-8")]
    for relative_path in source_paths:
        source = repo_path(relative_path, errors, f"{context}.sourceDataPaths")
        if source is not None:
            chunks.append(source.read_text(encoding="utf-8"))
    return "\n".join(chunks)


def validate_falsifier(falsifier: Any, context: str, errors: list[str]) -> int:
    if not isinstance(falsifier, dict):
        fail(errors, f"{context} must be an object")
        return 0
    for key in ("condition", "downgradeAction", "evidenceNeeded"):
        require_string(falsifier.get(key), f"{context}.{key}", errors)
    return 1


def validate_strong_claim(
    claim: Any,
    known_claims: set[str],
    claim_ids: set[str],
    context: str,
    errors: list[str],
) -> tuple[int, int]:
    if not isinstance(claim, dict):
        fail(errors, f"{context} must be an object")
        return (0, 0)

    claim_id = require_string(claim.get("claimId"), f"{context}.claimId", errors)
    if claim_id:
        if not PAPER_CLAIM_RE.match(claim_id):
            fail(errors, f"{context}.claimId must match HIPAPER-CL<number>: {claim_id}")
        if claim_id in claim_ids:
            fail(errors, f"duplicate paper claimId: {claim_id}")
        claim_ids.add(claim_id)

    require_string(claim.get("claimText"), f"{context}.claimText", errors)
    require_string(claim.get("modelPosition"), f"{context}.modelPosition", errors)

    linked_claims = require_string_list(claim.get("linkedCoreClaims"), f"{context}.linkedCoreClaims", errors)
    validate_claim_ids(linked_claims, known_claims, f"{context}.linkedCoreClaims", errors)

    prohibited = require_string_list(claim.get("prohibitedUses"), f"{context}.prohibitedUses", errors)
    if len(prohibited) < 2:
        fail(errors, f"{context}.prohibitedUses must contain at least two boundaries")

    falsifiers = claim.get("falsifiers")
    if not isinstance(falsifiers, list) or len(falsifiers) < 2:
        fail(errors, f"{context}.falsifiers must contain at least two falsifier rows")
        return (1, 0)

    count = 0
    for index, falsifier in enumerate(falsifiers):
        count += validate_falsifier(falsifier, f"{context}.falsifiers[{index}]", errors)
    return (1, count)


def validate_paper(
    paper: Any,
    known_claims: set[str],
    paper_ids: set[str],
    paper_paths: set[str],
    claim_ids: set[str],
    errors: list[str],
) -> tuple[int, int]:
    if not isinstance(paper, dict):
        fail(errors, "papers[] must contain objects")
        return (0, 0)

    paper_id = require_string(paper.get("paperId"), "paper.paperId", errors)
    if paper_id:
        if paper_id in paper_ids:
            fail(errors, f"duplicate paperId: {paper_id}")
        paper_ids.add(paper_id)

    relative_path = require_string(paper.get("path"), f"{paper_id}.path", errors)
    page_path = repo_path(relative_path, errors, f"{paper_id}.path") if relative_path else None
    if relative_path:
        if relative_path in paper_paths:
            fail(errors, f"duplicate paper path: {relative_path}")
        paper_paths.add(relative_path)

    paper_type = require_string(paper.get("paperType"), f"{paper_id}.paperType", errors)
    if paper_type != "arxiv-style-working-paper":
        fail(errors, f"{paper_id}.paperType must be arxiv-style-working-paper")

    arxiv_id = require_string(paper.get("arxivId"), f"{paper_id}.arxivId", errors)
    source_paths = require_optional_string_list(paper.get("sourceDataPaths"), f"{paper_id}.sourceDataPaths", errors)
    required_claims = require_string_list(paper.get("requiredClaims"), f"{paper_id}.requiredClaims", errors)
    required_phrases = require_string_list(
        paper.get("requiredBoundaryPhrases"),
        f"{paper_id}.requiredBoundaryPhrases",
        errors,
    )
    validate_claim_ids(required_claims, known_claims, f"{paper_id}.requiredClaims", errors)

    if page_path is None:
        return (0, 0)

    text = combined_source_text(page_path, source_paths, errors, paper_id)
    page_only_text = page_path.read_text(encoding="utf-8")
    if "PaperReaderLayout" not in page_only_text:
        fail(errors, f"{relative_path} is registered as paper but does not use PaperReaderLayout")
    if arxiv_id and arxiv_id not in text:
        fail(errors, f"{relative_path} or sourceDataPaths missing arxivId: {arxiv_id}")
    for claim in required_claims:
        if claim not in page_only_text:
            fail(errors, f"{relative_path} missing required core claim ID: {claim}")
    for phrase in required_phrases:
        if phrase not in page_only_text:
            fail(errors, f"{relative_path} missing required boundary phrase: {phrase}")

    strong_claims = paper.get("strongClaims")
    if not isinstance(strong_claims, list) or len(strong_claims) < 2:
        fail(errors, f"{paper_id}.strongClaims must contain at least two claims")
        return (0, 0)

    claim_count = 0
    falsifier_count = 0
    for index, strong_claim in enumerate(strong_claims):
        claim_inc, falsifier_inc = validate_strong_claim(
            strong_claim,
            known_claims,
            claim_ids,
            f"{paper_id}.strongClaims[{index}]",
            errors,
        )
        claim_count += claim_inc
        falsifier_count += falsifier_inc
    return (claim_count, falsifier_count)


def validate_index_links(paths: list[str], errors: list[str]) -> None:
    for relative_path in paths:
        target = repo_path(relative_path, errors, f"indexRequirements:{relative_path}")
        if target is None:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index does not link paper claim register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors)
    if not data:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if data.get("schemaVersion") != REQUIRED_SCHEMA:
        fail(errors, f"schemaVersion must be {REQUIRED_SCHEMA}")
    if data.get("status") != REQUIRED_STATUS:
        fail(errors, f"status must be {REQUIRED_STATUS}")

    known_claims = known_core_claims(errors, require_string(data.get("coreMatrix"), "coreMatrix", errors))
    for linked_register in ("pageConsistencyRegister", "domainFalsifierRegister", "maturityGapRegister"):
        path = require_string(data.get(linked_register), linked_register, errors)
        if path:
            repo_path(path, errors, linked_register)

    require_string_list(data.get("globalRequiredBoundaryPhrases"), "globalRequiredBoundaryPhrases", errors)
    non_claims = require_string_list(data.get("nonClaims"), "nonClaims", errors)
    if len(non_claims) < 3:
        fail(errors, "nonClaims must contain at least three boundary statements")

    papers = data.get("papers")
    if not isinstance(papers, list) or len(papers) < 5:
        fail(errors, "papers must contain at least five arXiv-style paper entries")
        papers = []

    paper_ids: set[str] = set()
    paper_paths: set[str] = set()
    claim_ids: set[str] = set()
    total_strong_claims = 0
    total_falsifiers = 0
    for paper in papers:
        claim_count, falsifier_count = validate_paper(
            paper,
            known_claims,
            paper_ids,
            paper_paths,
            claim_ids,
            errors,
        )
        total_strong_claims += claim_count
        total_falsifiers += falsifier_count

    actual_paper_pages = collect_paper_reader_pages()
    missing_from_register = sorted(actual_paper_pages - paper_paths)
    stale_register_paths = sorted(paper_paths - actual_paper_pages)
    if missing_from_register:
        fail(errors, f"PaperReaderLayout pages missing from paper register: {', '.join(missing_from_register)}")
    if stale_register_paths:
        fail(errors, f"registered paper paths no longer use PaperReaderLayout: {', '.join(stale_register_paths)}")

    index_paths = require_string_list(data.get("indexRequirements"), "indexRequirements", errors)
    validate_index_links(index_paths, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "paper claim register audit ok: "
        f"papers={len(papers)} strong_claims={total_strong_claims} falsifiers={total_falsifiers}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
