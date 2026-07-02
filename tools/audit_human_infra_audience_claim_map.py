#!/usr/bin/env python3
"""审计 Human Infra 受众-主张映射与邻近项目边界账本。"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-audience-claim-map.json"
CORE_MATRIX_PATH = ROOT / "docs/reference/human-infra-core-claim-evidence-matrix.md"

SCHEMA = "human-infra.audience-claim-map.v1"
STATUS = "active-value-clarity-gate"
REGISTER_LINK = "human-infra-audience-claim-map.json"

SOURCE_OF_TRUTH_KEYS = [
    "coreClaimEvidenceMatrix",
    "valueLenses",
    "projectBoundary",
    "pageClaimConsistency",
    "maturityGapRegister",
]

REQUIRED_AUDIENCE_IDS = {
    "researchers",
    "builders",
    "longevity-readers",
    "infrastructure-readers",
    "governance-reviewers",
    "modelers",
}

REQUIRED_ADJACENT_TYPE_IDS = {
    "health-management-app",
    "longevity-knowledge-base",
    "ai-toolbox",
    "policy-encyclopedia",
    "clinical-decision-support",
    "productivity-time-management",
}

REQUIRED_VALUE_LENS_IDS = {
    "subject-continuity",
    "resource-budget-expansion",
    "anti-scarcity-engineering",
}

REQUIRED_GLOBAL_BOUNDARY_PHRASES = {
    "不是医疗建议",
    "不输出个体死亡日期",
    "不证明具体技术已经实现有效永生",
}

REQUIRED_INDEX_FILES = [
    "README.md",
    "docs/reference/README.md",
    "docs/reference/human-infra-maturity-roadmap.md",
    "tools/README.md",
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


def known_claim_ids(errors: list[str]) -> set[str]:
    if not CORE_MATRIX_PATH.exists():
        fail(errors, "missing core claim matrix")
        return set()
    text = CORE_MATRIX_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"HI-CL\d+", text))


def validate_source_of_truth(data: dict[str, Any], errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in SOURCE_OF_TRUTH_KEYS:
        value = require_string(source.get(key), f"sourceOfTruth.{key}", errors)
        if value:
            repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_scope(data: dict[str, Any], audiences: list[dict[str, Any]], boundaries: list[dict[str, Any]], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        fail(errors, "scope must be an object")
        return

    audience_ids = {audience.get("audienceId") for audience in audiences if isinstance(audience.get("audienceId"), str)}
    boundary_ids = {boundary.get("adjacentTypeId") for boundary in boundaries if isinstance(boundary.get("adjacentTypeId"), str)}

    counts = {
        "audienceCount": len(audiences),
        "adjacentBoundaryCount": len(boundaries),
    }
    for key, expected in counts.items():
        value = require_int(scope.get(key), f"scope.{key}", errors)
        if value is not None and value != expected:
            fail(errors, f"scope.{key} must equal {expected}")

    required_audience_ids = set(require_string_list(scope.get("requiredAudienceIds"), "scope.requiredAudienceIds", errors, len(REQUIRED_AUDIENCE_IDS)))
    if required_audience_ids != REQUIRED_AUDIENCE_IDS:
        fail(errors, "scope.requiredAudienceIds must contain every required audience id")
    if audience_ids != REQUIRED_AUDIENCE_IDS:
        fail(errors, "audiences must cover exactly the required audience ids")

    required_boundary_ids = set(require_string_list(scope.get("requiredAdjacentTypeIds"), "scope.requiredAdjacentTypeIds", errors, len(REQUIRED_ADJACENT_TYPE_IDS)))
    if required_boundary_ids != REQUIRED_ADJACENT_TYPE_IDS:
        fail(errors, "scope.requiredAdjacentTypeIds must contain every required adjacent type id")
    if boundary_ids != REQUIRED_ADJACENT_TYPE_IDS:
        fail(errors, "adjacentProjectBoundaries must cover exactly the required adjacent type ids")

    lens_ids = set(require_string_list(scope.get("requiredValueLensIds"), "scope.requiredValueLensIds", errors, len(REQUIRED_VALUE_LENS_IDS)))
    if lens_ids != REQUIRED_VALUE_LENS_IDS:
        fail(errors, "scope.requiredValueLensIds must contain every required value lens id")

    boundary_phrases = set(require_string_list(scope.get("globalBoundaryPhrases"), "scope.globalBoundaryPhrases", errors, len(REQUIRED_GLOBAL_BOUNDARY_PHRASES)))
    if boundary_phrases != REQUIRED_GLOBAL_BOUNDARY_PHRASES:
        fail(errors, "scope.globalBoundaryPhrases must contain every global boundary phrase")
    require_string(scope.get("selectionRule"), "scope.selectionRule", errors)


def validate_audience(audience: Any, index: int, claims: set[str], errors: list[str]) -> None:
    if not isinstance(audience, dict):
        fail(errors, f"audiences[{index}] must be an object")
        return
    audience_id = require_string(audience.get("audienceId"), f"audiences[{index}].audienceId", errors)
    for field in ["audienceLabel", "primaryQuestion", "valueTranslation", "nextReaderAction"]:
        require_string(audience.get(field), f"{audience_id}.{field}", errors)

    claim_ids = set(require_string_list(audience.get("claimIds"), f"{audience_id}.claimIds", errors, 3))
    unknown_claims = claim_ids - claims
    if unknown_claims:
        fail(errors, f"{audience_id}.claimIds contains unknown claims: {', '.join(sorted(unknown_claims))}")
    if "HI-CL6" not in claim_ids and audience_id in {"longevity-readers", "governance-reviewers", "modelers"}:
        fail(errors, f"{audience_id}.claimIds must include HI-CL6 boundary claim")

    lens_ids = set(require_string_list(audience.get("valueLensIds"), f"{audience_id}.valueLensIds", errors, 1))
    if not lens_ids.issubset(REQUIRED_VALUE_LENS_IDS):
        fail(errors, f"{audience_id}.valueLensIds contains unknown lens ids")

    for entry_index, relative_path in enumerate(require_string_list(audience.get("entryPointFiles"), f"{audience_id}.entryPointFiles", errors, 1)):
        repo_path(relative_path, f"{audience_id}.entryPointFiles[{entry_index}]", errors)

    must_not_infer = require_string_list(audience.get("mustNotInfer"), f"{audience_id}.mustNotInfer", errors, 2)
    joined = " ".join(must_not_infer)
    if audience_id in {"longevity-readers", "governance-reviewers", "modelers"} and not any(
        phrase in joined for phrase in REQUIRED_GLOBAL_BOUNDARY_PHRASES
    ):
        fail(errors, f"{audience_id}.mustNotInfer must include at least one global boundary phrase")


def validate_boundary(boundary: Any, index: int, errors: list[str]) -> None:
    if not isinstance(boundary, dict):
        fail(errors, f"adjacentProjectBoundaries[{index}] must be an object")
        return
    boundary_id = require_string(boundary.get("adjacentTypeId"), f"adjacentProjectBoundaries[{index}].adjacentTypeId", errors)
    for field in ["adjacentLabel", "overlap", "humanInfraDistinction", "acceptedBorrowing", "prohibitedMisread"]:
        require_string(boundary.get(field), f"{boundary_id}.{field}", errors)
    prohibited = boundary.get("prohibitedMisread", "")
    if not any(marker in prohibited for marker in ["不能", "不输出", "不是"]):
        fail(errors, f"{boundary_id}.prohibitedMisread must be phrased as a clear negative boundary")


def validate_non_claims(data: dict[str, Any], errors: list[str]) -> None:
    non_claims = require_string_list(data.get("nonClaims"), "nonClaims", errors, 4)
    joined = " ".join(non_claims)
    for phrase in ["medical advice", "individual death-date", "calibration", "Claim IDs"]:
        if phrase not in joined:
            fail(errors, f"nonClaims must explicitly mention {phrase}")


def validate_index_requirements(data: dict[str, Any], errors: list[str]) -> None:
    index_requirements = require_string_list(data.get("indexRequirements"), "indexRequirements", errors, len(REQUIRED_INDEX_FILES))
    if sorted(index_requirements) != sorted(REQUIRED_INDEX_FILES):
        fail(errors, "indexRequirements must list the required index files")
    for relative_path in REQUIRED_INDEX_FILES:
        target = repo_path(relative_path, f"indexRequirements.{relative_path}", errors)
        if target and REGISTER_LINK not in target.read_text(encoding="utf-8"):
            fail(errors, f"{relative_path} must link {REGISTER_LINK}")


def validate_register(data: dict[str, Any], errors: list[str]) -> tuple[int, int]:
    if data.get("schemaVersion") != SCHEMA:
        fail(errors, f"schemaVersion must be {SCHEMA}")
    if data.get("status") != STATUS:
        fail(errors, f"status must be {STATUS}")
    require_string(data.get("registerId"), "registerId", errors)
    require_string(data.get("purpose"), "purpose", errors)

    claims = known_claim_ids(errors)
    validate_source_of_truth(data, errors)

    audiences = data.get("audiences")
    if not isinstance(audiences, list) or not audiences:
        fail(errors, "audiences must be a non-empty list")
        audiences = []
    boundaries = data.get("adjacentProjectBoundaries")
    if not isinstance(boundaries, list) or not boundaries:
        fail(errors, "adjacentProjectBoundaries must be a non-empty list")
        boundaries = []

    typed_audiences = [audience for audience in audiences if isinstance(audience, dict)]
    typed_boundaries = [boundary for boundary in boundaries if isinstance(boundary, dict)]
    validate_scope(data, typed_audiences, typed_boundaries, errors)

    seen_audiences: set[str] = set()
    for index, audience in enumerate(audiences):
        validate_audience(audience, index, claims, errors)
        if isinstance(audience, dict) and isinstance(audience.get("audienceId"), str):
            audience_id = audience["audienceId"]
            if audience_id in seen_audiences:
                fail(errors, f"duplicate audienceId: {audience_id}")
            seen_audiences.add(audience_id)

    seen_boundaries: set[str] = set()
    for index, boundary in enumerate(boundaries):
        validate_boundary(boundary, index, errors)
        if isinstance(boundary, dict) and isinstance(boundary.get("adjacentTypeId"), str):
            boundary_id = boundary["adjacentTypeId"]
            if boundary_id in seen_boundaries:
                fail(errors, f"duplicate adjacentTypeId: {boundary_id}")
            seen_boundaries.add(boundary_id)

    validate_non_claims(data, errors)
    validate_index_requirements(data, errors)
    return len(seen_audiences), len(seen_boundaries)


def main() -> int:
    errors: list[str] = []
    data = load_json(REGISTER_PATH, errors, "audience claim map")
    audience_count = boundary_count = 0
    if data:
        audience_count, boundary_count = validate_register(data, errors)

    if errors:
        print("audience claim map audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"audience claim map audit ok: audiences={audience_count} boundaries={boundary_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
