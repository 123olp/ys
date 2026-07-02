#!/usr/bin/env python3
"""审计 Human Infra 主要页面的 Claim ID 与边界语言一致性。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-page-claim-consistency.json"

REQUIRED_SCHEMA = "human-infra.page-claim-consistency.v1"
REQUIRED_STATUS = "active-consistency-gate"
CLAIM_RE = re.compile(r"\bHI-CL\d+\b")
REGISTER_LINK = "human-infra-page-claim-consistency.json"


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


def validate_claims(claims: list[str], known_claims: set[str], context: str, errors: list[str]) -> None:
    for claim in claims:
        if claim not in known_claims:
            fail(errors, f"{context} references unknown claim: {claim}")


def validate_page(
    page: Any,
    known_claims: set[str],
    global_claims: set[str],
    page_ids: set[str],
    page_paths: set[str],
    errors: list[str],
) -> tuple[int, int]:
    if not isinstance(page, dict):
        fail(errors, "pages[] must contain objects")
        return (0, 0)

    page_id = require_string(page.get("pageId"), "page.pageId", errors)
    if page_id:
        if page_id in page_ids:
            fail(errors, f"duplicate pageId: {page_id}")
        page_ids.add(page_id)

    page_type = require_string(page.get("pageType"), f"{page_id}.pageType", errors)
    if not page_type:
        return (0, 0)

    relative_path = require_string(page.get("path"), f"{page_id}.path", errors)
    target = repo_path(relative_path, errors, f"{page_id}.path") if relative_path else None
    if relative_path:
        if relative_path in page_paths:
            fail(errors, f"duplicate page path: {relative_path}")
        page_paths.add(relative_path)

    required_claims = require_string_list(page.get("requiredClaims"), f"{page_id}.requiredClaims", errors)
    required_phrases = require_string_list(
        page.get("requiredBoundaryPhrases"),
        f"{page_id}.requiredBoundaryPhrases",
        errors,
    )
    label = require_string(page.get("claimSpineLabel"), f"{page_id}.claimSpineLabel", errors)

    validate_claims(required_claims, known_claims, f"{page_id}.requiredClaims", errors)

    if page_type in {"project-entry", "web-entry"}:
        missing_global = sorted(global_claims - set(required_claims))
        if missing_global:
            fail(errors, f"{page_id} missing global required claims: {', '.join(missing_global)}")

    if target is None:
        return (len(required_claims), len(required_phrases))

    text = target.read_text(encoding="utf-8")
    for claim in required_claims:
        if claim not in text:
            fail(errors, f"{relative_path} missing required claim ID: {claim}")
    for phrase in required_phrases:
        if phrase not in text:
            fail(errors, f"{relative_path} missing boundary phrase: {phrase}")
    if label and label not in text:
        fail(errors, f"{relative_path} missing claim spine label: {label}")

    return (len(required_claims), len(required_phrases))


def validate_index_links(paths: list[str], errors: list[str]) -> None:
    for relative_path in paths:
        target = repo_path(relative_path, errors, f"indexRequirements:{relative_path}")
        if target is None:
            continue
        text = target.read_text(encoding="utf-8")
        if REGISTER_LINK not in text:
            fail(errors, f"index does not link page claim consistency register: {relative_path}")


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

    core_matrix_rel = require_string(data.get("coreMatrix"), "coreMatrix", errors)
    core_matrix_path = repo_path(core_matrix_rel, errors, "coreMatrix") if core_matrix_rel else None
    known_claims: set[str] = set()
    if core_matrix_path is not None:
        matrix_text = core_matrix_path.read_text(encoding="utf-8")
        known_claims = set(CLAIM_RE.findall(matrix_text))
        expected_claims = {f"HI-CL{index}" for index in range(1, 8)}
        missing_expected = sorted(expected_claims - known_claims)
        if missing_expected:
            fail(errors, f"core matrix missing expected claims: {', '.join(missing_expected)}")

    maturity_gap = require_string(data.get("maturityGapRegister"), "maturityGapRegister", errors)
    if maturity_gap:
        repo_path(maturity_gap, errors, "maturityGapRegister")

    global_claims = set(require_string_list(data.get("globalRequiredClaims"), "globalRequiredClaims", errors))
    validate_claims(sorted(global_claims), known_claims, "globalRequiredClaims", errors)
    require_string_list(data.get("globalBoundaryPhrases"), "globalBoundaryPhrases", errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors)

    pages = data.get("pages")
    total_claim_refs = 0
    total_boundary_checks = 0
    page_ids: set[str] = set()
    page_paths: set[str] = set()
    if not isinstance(pages, list) or len(pages) < 6:
        fail(errors, "pages must contain at least six major page entries")
    else:
        for page in pages:
            claim_count, boundary_count = validate_page(
                page,
                known_claims,
                global_claims,
                page_ids,
                page_paths,
                errors,
            )
            total_claim_refs += claim_count
            total_boundary_checks += boundary_count

    index_paths = require_string_list(data.get("indexRequirements"), "indexRequirements", errors)
    validate_index_links(index_paths, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "page claim consistency audit ok: "
        f"pages={len(pages)} claim_refs={total_claim_refs} boundary_checks={total_boundary_checks}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
