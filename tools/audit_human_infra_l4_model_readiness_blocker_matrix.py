#!/usr/bin/env python3
"""审计 Human Infra L4 模型准入阻塞矩阵。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "docs/reference/human-infra-l4-model-readiness-blocker-matrix.json"

SCHEMA = "human-infra.l4-model-readiness-blocker-matrix.v1"
STATUS = "active-l4-admission-blocked-readiness-matrix"
REGISTER_LINK = "human-infra-l4-model-readiness-blocker-matrix.json"
SCRIPT_LINK = "audit_human_infra_l4_model_readiness_blocker_matrix.py"

REQUIRED_SOURCE_KEYS = {
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "l4UnblockExecutionPlan",
    "maturityGapRegister",
    "maturityRoadmap",
    "nhanesWeightedDomainOutputReadiness",
    "nhanesLocalRunEvidenceManifest",
    "nhanesDisclosureReviewExecutionRegister",
    "nhatsL4ReadinessRunway",
    "publicWebNoRealValuesGate",
}
REQUIRED_BLOCKERS = {
    "L4B-01-governed-data-access",
    "L4B-02-exact-field-value-confirmation",
    "L4B-03-real-extraction-cohort-flow",
    "L4B-04-disclosure-review-public-output",
    "L4B-05-survey-design-weighted-estimates",
    "L4B-06-validation-calibration",
}
REQUIRED_CANDIDATES = {
    "L4C-NHANES-PUBLIC-LMF-WEIGHTED-DOMAIN",
    "L4C-NHATS-R13-R14-FUNCTIONAL-SURVIVAL",
}
REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-prediction",
    "individual-death-date-output",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "docs/reference/human-infra-model-admission-candidate-registry.json": REGISTER_LINK,
    "Makefile": "l4-model-readiness-blocker-matrix-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
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
        fail(errors, f"invalid {context} JSON: {exc}")
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


def require_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[Any]:
    if not isinstance(value, list) or len(value) < min_len:
        fail(errors, f"{context} must be a list with at least {min_len} item(s)")
        return []
    return value


def require_string_list(value: Any, context: str, errors: list[str], min_len: int = 1) -> list[str]:
    result: list[str] = []
    for index, item in enumerate(require_list(value, context, errors, min_len)):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"{context}[{index}] must be a non-empty string")
            continue
        result.append(item)
    return result


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
        return None
    if value.startswith(("http://", "https://")):
        fail(errors, f"{context} must be a local repository path, not URL")
        return None
    target = (ROOT / value).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        fail(errors, f"{context} escapes repository: {value}")
        return None
    if not target.exists():
        fail(errors, f"{context} does not exist: {value}")
        return None
    return target


def validate_source_of_truth(matrix: dict[str, Any], errors: list[str]) -> None:
    source = matrix.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(matrix: dict[str, Any], errors: list[str]) -> None:
    decision = matrix.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if "L3" not in require_string(decision.get("highestCurrentModelLevel"), "currentDecision.highestCurrentModelLevel", errors):
        fail(errors, "currentDecision.highestCurrentModelLevel must remain L3")
    for key in [
        "l4AggregateCalibratedAdmissionAllowed",
        "publicWeightedDomainOutputAllowed",
        "calibratedPredictionAvailable",
        "individualUseAllowed",
    ]:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in ["NHANES", "NHATS", "calibration"]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase}")


def validate_candidates(matrix: dict[str, Any], errors: list[str]) -> None:
    candidates = matrix.get("candidatePaths")
    if not isinstance(candidates, list):
        fail(errors, "candidatePaths must be a list")
        return
    ids: set[str] = set()
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            fail(errors, f"candidatePaths[{index}] must be an object")
            continue
        candidate_id = require_string(candidate.get("candidateId"), f"candidatePaths[{index}].candidateId", errors)
        ids.add(candidate_id)
        if "L4" not in require_string(candidate.get("targetLevel"), f"{candidate_id}.targetLevel", errors):
            fail(errors, f"{candidate_id}.targetLevel must target L4")
        if require_bool(candidate.get("admissionAllowed"), f"{candidate_id}.admissionAllowed", errors) is not False:
            fail(errors, f"{candidate_id}.admissionAllowed must be false")
        for path_index, path in enumerate(require_string_list(candidate.get("evidencePaths"), f"{candidate_id}.evidencePaths", errors, min_len=2)):
            repo_path(path, f"{candidate_id}.evidencePaths[{path_index}]", errors)
        require_string(candidate.get("blockingReason"), f"{candidate_id}.blockingReason", errors)
    missing = REQUIRED_CANDIDATES - ids
    if missing:
        fail(errors, f"candidatePaths missing required candidates: {sorted(missing)}")


def validate_blockers(matrix: dict[str, Any], errors: list[str]) -> None:
    blockers = matrix.get("blockers")
    if not isinstance(blockers, list):
        fail(errors, "blockers must be a list")
        return
    blocker_ids: set[str] = set()
    for index, blocker in enumerate(blockers):
        if not isinstance(blocker, dict):
            fail(errors, f"blockers[{index}] must be an object")
            continue
        blocker_id = require_string(blocker.get("blockerId"), f"blockers[{index}].blockerId", errors)
        blocker_ids.add(blocker_id)
        if blocker.get("status") != "blocked":
            fail(errors, f"{blocker_id}.status must be blocked")
        if require_bool(blocker.get("blocksAdmission"), f"{blocker_id}.blocksAdmission", errors) is not True:
            fail(errors, f"{blocker_id}.blocksAdmission must be true")
        candidates = set(require_string_list(blocker.get("appliesToCandidates"), f"{blocker_id}.appliesToCandidates", errors))
        if not candidates <= REQUIRED_CANDIDATES:
            fail(errors, f"{blocker_id}.appliesToCandidates contains unknown candidate")
        require_string_list(blocker.get("admissionGateRefs"), f"{blocker_id}.admissionGateRefs", errors)
        for path_index, path in enumerate(require_string_list(blocker.get("evidencePaths"), f"{blocker_id}.evidencePaths", errors, min_len=2)):
            repo_path(path, f"{blocker_id}.evidencePaths[{path_index}]", errors)
        require_string_list(blocker.get("requiredBeforeUnblock"), f"{blocker_id}.requiredBeforeUnblock", errors, min_len=2)
        blocked_uses = set(require_string_list(blocker.get("blockedUses"), f"{blocker_id}.blockedUses", errors))
        missing_uses = REQUIRED_BLOCKED_USES - blocked_uses
        if missing_uses:
            fail(errors, f"{blocker_id}.blockedUses missing {sorted(missing_uses)}")
    missing = REQUIRED_BLOCKERS - blocker_ids
    if missing:
        fail(errors, f"blockers missing required blockers: {sorted(missing)}")


def validate_work_orders(matrix: dict[str, Any], errors: list[str]) -> None:
    orders = matrix.get("nextWorkOrders")
    if not isinstance(orders, list) or len(orders) < 3:
        fail(errors, "nextWorkOrders must contain at least three items")
        return
    known_blockers = REQUIRED_BLOCKERS
    for index, order in enumerate(orders):
        if not isinstance(order, dict):
            fail(errors, f"nextWorkOrders[{index}] must be an object")
            continue
        if order.get("priority") != index + 1:
            fail(errors, f"nextWorkOrders[{index}].priority must be {index + 1}")
        require_string(order.get("item"), f"nextWorkOrders[{index}].item", errors)
        unblocks = set(require_string_list(order.get("unblocks"), f"nextWorkOrders[{index}].unblocks", errors))
        if not unblocks <= known_blockers:
            fail(errors, f"nextWorkOrders[{index}].unblocks contains unknown blocker")


def validate_boundaries(matrix: dict[str, Any], errors: list[str]) -> None:
    boundaries = set(require_string_list(matrix.get("hardBoundaries"), "hardBoundaries", errors, min_len=5))
    required_phrases = [
        "No individual death-date output.",
        "No individual medical advice.",
        "No calibration claim before validation and calibration diagnostics.",
    ]
    for phrase in required_phrases:
        if phrase not in boundaries:
            fail(errors, f"hardBoundaries missing {phrase!r}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} missing reference to {needle}")


def main() -> int:
    errors: list[str] = []
    matrix = load_json(MATRIX_PATH, errors, "L4 model readiness blocker matrix")
    if matrix:
        if matrix.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if matrix.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(matrix.get("matrixId"), "matrixId", errors)
        require_string(matrix.get("purpose"), "purpose", errors)
        validate_source_of_truth(matrix, errors)
        validate_current_decision(matrix, errors)
        validate_candidates(matrix, errors)
        validate_blockers(matrix, errors)
        validate_work_orders(matrix, errors)
        validate_boundaries(matrix, errors)
    validate_index_links(errors)

    if errors:
        print("L4 model readiness blocker matrix audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "L4 model readiness blocker matrix audit ok: "
        f"candidates={len(matrix.get('candidatePaths', []))} "
        f"blockers={len(matrix.get('blockers', []))} l4=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
