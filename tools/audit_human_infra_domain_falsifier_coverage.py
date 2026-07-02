#!/usr/bin/env python3
"""审计 C1/C2 优先研究域的反证与降级条件覆盖。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-falsifier-coverage.json"
CORE_MATRIX_PATH = ROOT / "docs/reference/human-infra-core-claim-evidence-matrix.md"

SCHEMA = "human-infra.domain-falsifier-coverage.v1"
STATUS = "active-priority-domain-gate"
CLAIM_RE = re.compile(r"\bHI-CL\d+\b")
REGISTER_LINK = "human-infra-domain-falsifier-coverage.json"
REQUIRED_TOP_LEVEL_FILES = [
    "coreMatrix",
    "pageConsistencyRegister",
    "maturityGapRegister",
]
ALLOWED_TIERS = {"C1", "C2"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_register(errors: list[str]) -> dict[str, Any]:
    if not REGISTER_PATH.exists():
        fail(errors, f"missing register: {REGISTER_PATH.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(REGISTER_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "register must be a JSON object")
        return {}
    return data


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


def require_string(value: Any, context: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{context} must be a non-empty string")
        return ""
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


def known_claim_ids(errors: list[str]) -> set[str]:
    if not CORE_MATRIX_PATH.exists():
        fail(errors, f"missing core matrix: {CORE_MATRIX_PATH.relative_to(ROOT)}")
        return set()
    claims = set(CLAIM_RE.findall(CORE_MATRIX_PATH.read_text(encoding="utf-8")))
    expected = {f"HI-CL{index}" for index in range(1, 8)}
    missing = sorted(expected - claims)
    if missing:
        fail(errors, f"core matrix missing expected claims: {', '.join(missing)}")
    return claims


def discover_c1_domain_paths() -> set[str]:
    root = ROOT / "domains/c1-boundary-rewriting"
    return {
        str(path.relative_to(ROOT))
        for path in sorted(root.iterdir())
        if path.is_dir() and (path / "README.md").exists() and (path / "AGENTS.md").exists()
    }


def validate_scope(scope: Any, errors: list[str]) -> tuple[set[str], int]:
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return (set(), 0)
    require_string(scope.get("c1Coverage"), "scope.c1Coverage", errors)
    priority_min = scope.get("priorityC2Minimum")
    if not isinstance(priority_min, int) or priority_min < 1:
        fail(errors, "scope.priorityC2Minimum must be a positive integer")
        priority_min = 0
    priority_c2 = set(require_string_list(scope.get("priorityC2Domains"), "scope.priorityC2Domains", errors, 1))
    if len(priority_c2) < priority_min:
        fail(errors, "scope.priorityC2Domains is smaller than priorityC2Minimum")
    require_string_list(scope.get("currentLimitations"), "scope.currentLimitations", errors, 2)
    return (priority_c2, priority_min)


def validate_variables(value: Any, domain_id: str, errors: list[str]) -> None:
    if not isinstance(value, dict):
        fail(errors, f"{domain_id}.variables must be an object")
        return
    for key in ["inputs", "mediators", "outputs"]:
        require_string_list(value.get(key), f"{domain_id}.variables.{key}", errors, 2)


def validate_falsifiers(value: Any, domain_id: str, errors: list[str]) -> int:
    if not isinstance(value, list) or len(value) < 2:
        fail(errors, f"{domain_id}.falsifiers must contain at least 2 falsifier objects")
        return 0
    for index, item in enumerate(value):
        if not isinstance(item, dict):
            fail(errors, f"{domain_id}.falsifiers[{index}] must be an object")
            continue
        require_string(item.get("condition"), f"{domain_id}.falsifiers[{index}].condition", errors)
        require_string(item.get("downgradeAction"), f"{domain_id}.falsifiers[{index}].downgradeAction", errors)
        require_string(item.get("evidenceNeeded"), f"{domain_id}.falsifiers[{index}].evidenceNeeded", errors)
    return len(value)


def validate_entry(
    entry: Any,
    claims: set[str],
    priority_c2: set[str],
    errors: list[str],
) -> tuple[str, str, int]:
    if not isinstance(entry, dict):
        fail(errors, "entries[] must contain objects")
        return ("", "", 0)

    domain_id = require_string(entry.get("domainId"), "entry.domainId", errors)
    tier = require_string(entry.get("tier"), f"{domain_id}.tier", errors)
    if tier and tier not in ALLOWED_TIERS:
        fail(errors, f"{domain_id}.tier must be one of {sorted(ALLOWED_TIERS)}")

    path_value = require_string(entry.get("path"), f"{domain_id}.path", errors)
    target = repo_path(path_value, f"{domain_id}.path", errors) if path_value else None
    if target is not None:
        if not (target / "README.md").exists():
            fail(errors, f"{domain_id} missing README.md")
        if not (target / "AGENTS.md").exists():
            fail(errors, f"{domain_id} missing AGENTS.md")
        if target.name != domain_id:
            fail(errors, f"{domain_id}.path basename must match domainId")

    if tier == "C2" and domain_id not in priority_c2:
        fail(errors, f"{domain_id} is C2 but absent from scope.priorityC2Domains")

    required_claims = require_string_list(entry.get("requiredClaims"), f"{domain_id}.requiredClaims", errors, 2)
    for claim in required_claims:
        if claim not in claims:
            fail(errors, f"{domain_id} references unknown claim: {claim}")

    require_string(entry.get("strongClaim"), f"{domain_id}.strongClaim", errors)
    require_string(entry.get("modelPosition"), f"{domain_id}.modelPosition", errors)
    validate_variables(entry.get("variables"), domain_id, errors)
    falsifier_count = validate_falsifiers(entry.get("falsifiers"), domain_id, errors)
    require_string_list(entry.get("prohibitedUses"), f"{domain_id}.prohibitedUses", errors, 2)
    require_string(entry.get("nextEvidenceAction"), f"{domain_id}.nextEvidenceAction", errors)
    return (path_value, tier, falsifier_count)


def validate_index_links(paths: list[str], errors: list[str]) -> None:
    for relative_path in paths:
        target = repo_path(relative_path, f"indexRequirements:{relative_path}", errors)
        if target is None:
            continue
        if REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"index does not link domain falsifier register: {relative_path}")


def main() -> int:
    errors: list[str] = []
    data = load_register(errors)
    claims = known_claim_ids(errors)
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
    for key in REQUIRED_TOP_LEVEL_FILES:
        value = require_string(data.get(key), key, errors)
        if value:
            repo_path(value, key, errors)

    priority_c2, priority_min = validate_scope(data.get("scope"), errors)

    entries = data.get("entries")
    entry_paths: set[str] = set()
    entry_ids: set[str] = set()
    c2_count = 0
    falsifier_count = 0
    if not isinstance(entries, list) or len(entries) < 10:
        fail(errors, "entries must contain at least 10 priority domain entries")
    else:
        for entry in entries:
            path_value, tier, count = validate_entry(entry, claims, priority_c2, errors)
            domain_id = entry.get("domainId") if isinstance(entry, dict) else ""
            if isinstance(domain_id, str):
                if domain_id in entry_ids:
                    fail(errors, f"duplicate domainId: {domain_id}")
                entry_ids.add(domain_id)
            if path_value:
                if path_value in entry_paths:
                    fail(errors, f"duplicate domain path: {path_value}")
                entry_paths.add(path_value)
            if tier == "C2":
                c2_count += 1
            falsifier_count += count

    missing_c1 = sorted(discover_c1_domain_paths() - entry_paths)
    if missing_c1:
        fail(errors, f"C1 domains missing from coverage: {', '.join(missing_c1)}")
    missing_priority_c2 = sorted(priority_c2 - entry_ids)
    if missing_priority_c2:
        fail(errors, f"priority C2 domains missing from entries: {', '.join(missing_priority_c2)}")
    if c2_count < priority_min:
        fail(errors, f"C2 entry count {c2_count} below priority minimum {priority_min}")

    index_paths = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, 1)
    validate_index_links(index_paths, errors)
    require_string_list(data.get("nonClaims"), "nonClaims", errors, 2)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "domain falsifier coverage audit ok: "
        f"entries={len(entries)} c2_priority={c2_count} falsifiers={falsifier_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
