#!/usr/bin/env python3
"""审计 Human Infra 模型准入契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs/reference/human-infra-model-admission-contract.json"

SCHEMA = "human-infra.model-admission-contract.v1"
STATUS = "active-model-admission-contract-calibrated-admission-blocked"
REGISTER_LINK = "human-infra-model-admission-contract.json"
SCRIPT_LINK = "audit_human_infra_model_admission_contract.py"

REQUIRED_LEVELS = ["L0", "L1", "L2", "L3", "L4", "L5"]
REQUIRED_GATE_IDS = {
    "MAC-G1-source-review",
    "MAC-G2-model-location",
    "MAC-G3-estimand",
    "MAC-G4-data-access",
    "MAC-G5-variable-confirmation",
    "MAC-G6-extraction-and-cohort-flow",
    "MAC-G7-validation-calibration",
    "MAC-G8-governance-boundary",
}
REQUIRED_ABORT_IDS = {
    "ABORT-1-no-source-identity",
    "ABORT-2-biomarker-to-lifespan-leap",
    "ABORT-3-animal-to-human-effect-leap",
    "ABORT-4-no-comparator-or-time-zero",
    "ABORT-5-individual-output",
    "ABORT-6-raw-data-exposure",
}
REQUIRED_BLOCKED_USES = {
    "individual-death-date-output",
    "individual-advice",
    "calibrated-prediction",
    "intervention-ranking",
    "clinical-validity-claim",
}
REQUIRED_SOURCE_KEYS = {
    "predictionModelContract",
    "predictionModelGovernance",
    "maturityGapRegister",
    "maturityRoadmap",
    "calibrationReadiness",
    "firstEstimandProtocol",
    "variableConfirmationMatrix",
    "publicMortalityAnchor",
    "reviewedArtifactRegisters",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "model-admission-contract-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing contract: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, "contract must be a JSON object")
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


def validate_source_of_truth(contract: dict[str, Any], errors: list[str]) -> None:
    source = contract.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        if key == "reviewedArtifactRegisters":
            if not isinstance(value, list) or len(value) < 10:
                fail(errors, "sourceOfTruth.reviewedArtifactRegisters must include cumulative and current C2 long-tail reviewed registers")
                continue
            for index, item in enumerate(value):
                repo_path(item, f"sourceOfTruth.reviewedArtifactRegisters[{index}]", errors)
            continue
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_levels(contract: dict[str, Any], errors: list[str]) -> None:
    levels = contract.get("admissionLevels")
    if not isinstance(levels, list):
        fail(errors, "admissionLevels must be a list")
        return
    actual = [item.get("level") for item in levels if isinstance(item, dict)]
    if actual != REQUIRED_LEVELS:
        fail(errors, f"admissionLevels must be ordered {REQUIRED_LEVELS}, got {actual}")
    for item in levels:
        if not isinstance(item, dict):
            fail(errors, "admissionLevels[] must contain objects")
            continue
        level = require_string(item.get("level"), "admissionLevels[].level", errors)
        require_string(item.get("name"), f"{level}.name", errors)
        require_string(item.get("allowedUse"), f"{level}.allowedUse", errors)
        require_string_list(item.get("minimumEvidence"), f"{level}.minimumEvidence", errors, min_len=3)
        blocked = set(require_string_list(item.get("blockedUses"), f"{level}.blockedUses", errors))
        if level in {"L1", "L4", "L5"} and not (blocked & REQUIRED_BLOCKED_USES):
            fail(errors, f"{level}.blockedUses must include at least one required high-risk blocked use")
        if level == "L5" and "Blocked by default" not in item.get("allowedUse", ""):
            fail(errors, "L5.allowedUse must explicitly be blocked by default")


def validate_gates(contract: dict[str, Any], errors: list[str]) -> None:
    gates = contract.get("minimumAdmissionGates")
    if not isinstance(gates, list):
        fail(errors, "minimumAdmissionGates must be a list")
        return
    gate_ids = set()
    for gate in gates:
        if not isinstance(gate, dict):
            fail(errors, "minimumAdmissionGates[] must contain objects")
            continue
        gate_id = require_string(gate.get("gateId"), "minimumAdmissionGates[].gateId", errors)
        if gate_id in gate_ids:
            fail(errors, f"duplicate gateId: {gate_id}")
        gate_ids.add(gate_id)
        require_string(gate.get("name"), f"{gate_id}.name", errors)
        require_string(gate.get("passCondition"), f"{gate_id}.passCondition", errors)
        levels = set(require_string_list(gate.get("requiredForLevels"), f"{gate_id}.requiredForLevels", errors))
        if not levels <= set(REQUIRED_LEVELS):
            fail(errors, f"{gate_id}.requiredForLevels contains unknown level(s)")
    missing = REQUIRED_GATE_IDS - gate_ids
    if missing:
        fail(errors, f"missing admission gates: {sorted(missing)}")


def validate_abort_gates(contract: dict[str, Any], errors: list[str]) -> None:
    gates = contract.get("hardAbortGates")
    if not isinstance(gates, list):
        fail(errors, "hardAbortGates must be a list")
        return
    abort_ids = set()
    for gate in gates:
        if not isinstance(gate, dict):
            fail(errors, "hardAbortGates[] must contain objects")
            continue
        abort_id = require_string(gate.get("abortId"), "hardAbortGates[].abortId", errors)
        if abort_id in abort_ids:
            fail(errors, f"duplicate abortId: {abort_id}")
        abort_ids.add(abort_id)
        require_string(gate.get("condition"), f"{abort_id}.condition", errors)
        result = require_string(gate.get("result"), f"{abort_id}.result", errors)
        if result not in {"blocked", "cannot-evaluate"}:
            fail(errors, f"{abort_id}.result must be blocked or cannot-evaluate")
    missing = REQUIRED_ABORT_IDS - abort_ids
    if missing:
        fail(errors, f"missing abort gates: {sorted(missing)}")


def validate_current_decision(contract: dict[str, Any], errors: list[str]) -> None:
    decision = contract.get("currentRepositoryDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentRepositoryDecision must be an object")
        return
    if decision.get("overallAdmission") != "blocked-for-calibrated-model":
        fail(errors, "currentRepositoryDecision.overallAdmission must keep calibrated admission blocked")
    if decision.get("highestAllowedLevel") != "L3":
        fail(errors, "currentRepositoryDecision.highestAllowedLevel must be L3")
    if require_bool(decision.get("calibratedPredictionAvailable"), "calibratedPredictionAvailable", errors) is not False:
        fail(errors, "calibratedPredictionAvailable must be false")
    if require_bool(decision.get("individualUseAllowed"), "individualUseAllowed", errors) is not False:
        fail(errors, "individualUseAllowed must be false")
    if decision.get("currentC2ReviewedArtifactsAdmission") != "L1/L2-only":
        fail(errors, "currentC2ReviewedArtifactsAdmission must be L1/L2-only")
    for key in [
        "highestAllowedLevelBoundary",
        "currentC2ReviewedArtifactsBoundary",
        "nextDecisionNeeded",
    ]:
        require_string(decision.get(key), f"currentRepositoryDecision.{key}", errors)


def validate_artifact_bridge(contract: dict[str, Any], errors: list[str]) -> None:
    bridge = contract.get("artifactBridge")
    if not isinstance(bridge, dict):
        fail(errors, "artifactBridge must be an object")
        return
    expected = {
        "reviewedArtifactDefaultLevel": "L1",
        "candidateVariableMaximumWithoutData": "L2",
        "toyModelMaximumWithoutRealCohort": "L3",
        "aggregateCalibrationMinimumLevel": "L4",
        "individualSupportDefault": "L5-blocked",
    }
    for key, value in expected.items():
        if bridge.get(key) != value:
            fail(errors, f"artifactBridge.{key} must be {value}")
    statement = require_string(bridge.get("requiredStatement"), "artifactBridge.requiredStatement", errors)
    for phrase in ["not model parameters", "separate admission decision", "hazard"]:
        if phrase not in statement:
            fail(errors, f"artifactBridge.requiredStatement must contain {phrase!r}")


def validate_standards_and_work_orders(contract: dict[str, Any], errors: list[str]) -> None:
    standards = contract.get("standardsTrace")
    if not isinstance(standards, list) or len(standards) < 4:
        fail(errors, "standardsTrace must contain at least four method anchors")
    else:
        for index, item in enumerate(standards):
            if not isinstance(item, dict):
                fail(errors, f"standardsTrace[{index}] must be an object")
                continue
            require_string(item.get("id"), f"standardsTrace[{index}].id", errors)
            url = require_string(item.get("url"), f"standardsTrace[{index}].url", errors)
            if url and not url.startswith("https://"):
                fail(errors, f"standardsTrace[{index}].url must be https")
            require_string(item.get("localRole"), f"standardsTrace[{index}].localRole", errors)
            require_string(item.get("localBoundary"), f"standardsTrace[{index}].localBoundary", errors)
    work = contract.get("nextWorkOrders")
    if not isinstance(work, list) or len(work) < 3:
        fail(errors, "nextWorkOrders must contain at least three items")
        return
    for index, item in enumerate(work):
        if not isinstance(item, dict):
            fail(errors, f"nextWorkOrders[{index}] must be an object")
            continue
        if item.get("priority") != index + 1:
            fail(errors, f"nextWorkOrders[{index}].priority must be {index + 1}")
        require_string(item.get("item"), f"nextWorkOrders[{index}].item", errors)
        require_string_list(item.get("unblocks"), f"nextWorkOrders[{index}].unblocks", errors)


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
    contract = load_json(CONTRACT_PATH, errors)
    if contract:
        if contract.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if contract.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(contract.get("contractId"), "contractId", errors)
        require_string(contract.get("purpose"), "purpose", errors)
        validate_source_of_truth(contract, errors)
        validate_levels(contract, errors)
        validate_gates(contract, errors)
        validate_abort_gates(contract, errors)
        validate_current_decision(contract, errors)
        validate_artifact_bridge(contract, errors)
        validate_standards_and_work_orders(contract, errors)
    validate_index_links(errors)

    if errors:
        print("model admission contract audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("model admission contract audit ok: levels=6 gates=8 aborts=6 calibrated=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
