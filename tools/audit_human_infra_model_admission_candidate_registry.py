#!/usr/bin/env python3
"""审计 Human Infra 模型准入候选注册表。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs/reference/human-infra-model-admission-candidate-registry.json"
CONTRACT_PATH = ROOT / "docs/reference/human-infra-model-admission-contract.json"

SCHEMA = "human-infra.model-admission-candidate-registry.v1"
STATUS = "active-model-admission-candidate-registry-calibrated-blocked"
REGISTER_LINK = "human-infra-model-admission-candidate-registry.json"
SCRIPT_LINK = "audit_human_infra_model_admission_candidate_registry.py"

REQUIRED_BLOCKED_USES = {
    "calibrated-prediction",
    "individual-advice",
    "individual-death-date-output",
    "intervention-ranking",
    "clinical-validity-claim",
}
REQUIRED_ABORTS = {
    "ABORT-1-no-source-identity",
    "ABORT-2-biomarker-to-lifespan-leap",
    "ABORT-3-animal-to-human-effect-leap",
    "ABORT-4-no-comparator-or-time-zero",
    "ABORT-5-individual-output",
    "ABORT-6-raw-data-exposure",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "model-admission-candidate-registry-audit",
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


def require_int(value: Any, context: str, errors: list[str]) -> int | None:
    if not isinstance(value, int):
        fail(errors, f"{context} must be integer")
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


def reviewed_register_paths_from_contract(errors: list[str]) -> list[str]:
    contract = load_json(CONTRACT_PATH, errors, "model admission contract")
    source = contract.get("sourceOfTruth") if contract else None
    if not isinstance(source, dict):
        fail(errors, "contract.sourceOfTruth must be an object")
        return []
    paths = source.get("reviewedArtifactRegisters")
    if not isinstance(paths, list) or len(paths) < 7:
        fail(errors, "contract.sourceOfTruth.reviewedArtifactRegisters must list reviewed artifact registers")
        return []
    result: list[str] = []
    for index, item in enumerate(paths):
        if not isinstance(item, str) or not item.strip():
            fail(errors, f"contract reviewedArtifactRegisters[{index}] must be string")
            continue
        repo_path(item, f"contract reviewedArtifactRegisters[{index}]", errors)
        result.append(item)
    return result


def validate_source_of_truth(registry: dict[str, Any], contract_paths: list[str], errors: list[str]) -> None:
    source = registry.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    for key in [
        "modelAdmissionContract",
        "maturityGapRegister",
        "maturityRoadmap",
        "predictionModelContract",
        "predictionModelGovernance",
        "toyModelOutput",
        "toyModelAudit",
        "publicMortalityAnchor",
        "firstEstimandProtocol",
        "variableConfirmationMatrix",
    ]:
        repo_path(source.get(key), f"sourceOfTruth.{key}", errors)
    if source.get("modelAdmissionContract") != str(CONTRACT_PATH.relative_to(ROOT)):
        fail(errors, "sourceOfTruth.modelAdmissionContract must point to the contract")
    reviewed = source.get("reviewedArtifactRegisters")
    if reviewed != contract_paths:
        fail(errors, "sourceOfTruth.reviewedArtifactRegisters must match the model-admission contract")


def register_counts(path: str, errors: list[str]) -> tuple[str, int, int, list[dict[str, Any]]]:
    target = repo_path(path, f"source register {path}", errors)
    if target is None:
        return "", 0, 0, []
    data = load_json(target, errors, f"source register {path}")
    status = str(data.get("status", ""))
    artifacts = data.get("reviewedArtifacts", [])
    blocked = data.get("blockedRows", [])
    if not isinstance(artifacts, list):
        fail(errors, f"{path}.reviewedArtifacts must be a list")
        artifacts = []
    if not isinstance(blocked, list):
        fail(errors, f"{path}.blockedRows must be a list when present")
        blocked = []
    return status, len(artifacts), len(blocked), [a for a in artifacts if isinstance(a, dict)]


def validate_decisions(registry: dict[str, Any], contract_paths: list[str], errors: list[str]) -> tuple[int, int]:
    decisions = registry.get("reviewedArtifactAdmissionDecisions")
    if not isinstance(decisions, list):
        fail(errors, "reviewedArtifactAdmissionDecisions must be a list")
        return 0, 0
    if len(decisions) != len(contract_paths):
        fail(errors, "reviewedArtifactAdmissionDecisions must cover every reviewed register from the contract")

    seen: set[str] = set()
    total_artifacts = 0
    total_blocked = 0
    for index, decision in enumerate(decisions):
        if not isinstance(decision, dict):
            fail(errors, f"reviewedArtifactAdmissionDecisions[{index}] must be an object")
            continue
        decision_id = require_string(decision.get("decisionId"), f"decision[{index}].decisionId", errors)
        if decision_id in seen:
            fail(errors, f"duplicate decisionId: {decision_id}")
        seen.add(decision_id)

        source_path = require_string(decision.get("sourceRegisterPath"), f"{decision_id}.sourceRegisterPath", errors)
        if source_path not in contract_paths:
            fail(errors, f"{decision_id}.sourceRegisterPath is not in contract reviewed registers")
        status, artifact_count, blocked_count, artifacts = register_counts(source_path, errors)
        must_contain = require_string(
            decision.get("sourceRegisterStatusMustContain"),
            f"{decision_id}.sourceRegisterStatusMustContain",
            errors,
        )
        if must_contain and must_contain not in status:
            fail(errors, f"{decision_id}.source register status must contain {must_contain!r}")
        if require_int(decision.get("reviewedArtifactCount"), f"{decision_id}.reviewedArtifactCount", errors) != artifact_count:
            fail(errors, f"{decision_id}.reviewedArtifactCount does not match source register")
        if require_int(decision.get("blockedRowCount"), f"{decision_id}.blockedRowCount", errors) != blocked_count:
            fail(errors, f"{decision_id}.blockedRowCount does not match source register")
        total_artifacts += artifact_count
        total_blocked += blocked_count

        if decision.get("currentAdmissionLevel") != "L1/L2-only":
            fail(errors, f"{decision_id}.currentAdmissionLevel must be L1/L2-only")
        if decision.get("maxLevelWithoutAdditionalGates") != "L2":
            fail(errors, f"{decision_id}.maxLevelWithoutAdditionalGates must be L2")
        blocked_levels = set(require_string_list(decision.get("blockedLevels"), f"{decision_id}.blockedLevels", errors))
        for level in ["L3", "L4", "L5"]:
            if not any(item.startswith(level) for item in blocked_levels):
                fail(errors, f"{decision_id}.blockedLevels must include {level}")
        blocked_uses = set(require_string_list(decision.get("blockedUses"), f"{decision_id}.blockedUses", errors))
        missing = REQUIRED_BLOCKED_USES - blocked_uses
        if missing:
            fail(errors, f"{decision_id}.blockedUses missing {sorted(missing)}")
        for gate_name in ["requiredBeforeL3", "requiredBeforeL4", "requiredBeforeL5"]:
            require_string_list(decision.get(gate_name), f"{decision_id}.{gate_name}", errors, min_len=3)
        for artifact in artifacts[:10]:
            model_decision = str(artifact.get("modelAdmissionDecision", ""))
            if "blocked" not in model_decision:
                fail(errors, f"{decision_id} source artifact has non-blocked modelAdmissionDecision")
            artifact_blocked = set(artifact.get("blockedUses", []))
            if "individual-death-date-output" not in artifact_blocked:
                fail(errors, f"{decision_id} source artifact missing individual-death-date-output block")
    return total_artifacts, total_blocked


def validate_aggregate(
    registry: dict[str, Any],
    register_count: int,
    total_artifacts: int,
    total_blocked: int,
    errors: list[str],
) -> None:
    aggregate = registry.get("aggregateDecision")
    if not isinstance(aggregate, dict):
        fail(errors, "aggregateDecision must be an object")
        return
    expected = {
        "reviewedArtifactRegisters": register_count,
        "reviewedArtifactsCovered": total_artifacts,
        "blockedRowsPreserved": total_blocked,
        "l4AggregateCalibratedAdmissions": 0,
        "l5IndividualAdmissions": 0,
    }
    for key, value in expected.items():
        if aggregate.get(key) != value:
            fail(errors, f"aggregateDecision.{key} must be {value}")
    if aggregate.get("highestReviewedArtifactLevel") != "L2":
        fail(errors, "aggregateDecision.highestReviewedArtifactLevel must be L2")
    if aggregate.get("highestCurrentModelLevel") != "L3":
        fail(errors, "aggregateDecision.highestCurrentModelLevel must be L3")
    if require_bool(aggregate.get("calibratedPredictionAvailable"), "aggregateDecision.calibratedPredictionAvailable", errors) is not False:
        fail(errors, "aggregateDecision.calibratedPredictionAvailable must be false")
    if require_bool(aggregate.get("individualUseAllowed"), "aggregateDecision.individualUseAllowed", errors) is not False:
        fail(errors, "aggregateDecision.individualUseAllowed must be false")
    decision = require_string(aggregate.get("decision"), "aggregateDecision.decision", errors)
    for phrase in ["L1/L2", "L4", "L5", "blocked"]:
        if phrase not in decision:
            fail(errors, f"aggregateDecision.decision must contain {phrase!r}")


def validate_l3_and_l4(registry: dict[str, Any], errors: list[str]) -> None:
    l3 = registry.get("existingL3Decisions")
    if not isinstance(l3, list) or len(l3) != 2:
        fail(errors, "existingL3Decisions must contain exactly two decisions")
    else:
        for index, item in enumerate(l3):
            if not isinstance(item, dict):
                fail(errors, f"existingL3Decisions[{index}] must be an object")
                continue
            repo_path(item.get("sourcePath"), f"existingL3Decisions[{index}].sourcePath", errors)
            if "auditPath" in item:
                repo_path(item.get("auditPath"), f"existingL3Decisions[{index}].auditPath", errors)
            if "L3" not in require_string(item.get("currentAdmissionLevel"), f"existingL3Decisions[{index}].currentAdmissionLevel", errors):
                fail(errors, f"existingL3Decisions[{index}] must be L3-level")
            if require_bool(item.get("calibrated"), f"existingL3Decisions[{index}].calibrated", errors) is not False:
                fail(errors, f"existingL3Decisions[{index}].calibrated must be false")
            blocked = set(require_string_list(item.get("blockedUses"), f"existingL3Decisions[{index}].blockedUses", errors))
            if "individual prediction" not in blocked:
                fail(errors, f"existingL3Decisions[{index}] must block individual prediction")

    blocked_l4 = registry.get("blockedL4Candidates")
    if not isinstance(blocked_l4, list) or len(blocked_l4) < 2:
        fail(errors, "blockedL4Candidates must contain at least two blocked candidates")
        return
    for index, item in enumerate(blocked_l4):
        if not isinstance(item, dict):
            fail(errors, f"blockedL4Candidates[{index}] must be an object")
            continue
        repo_path(item.get("sourcePath"), f"blockedL4Candidates[{index}].sourcePath", errors)
        gates = set(require_string_list(item.get("blockedAt"), f"blockedL4Candidates[{index}].blockedAt", errors, min_len=2))
        if not gates & {"MAC-G4-data-access", "MAC-G5-variable-confirmation", "MAC-G7-validation-calibration"}:
            fail(errors, f"blockedL4Candidates[{index}] must block on data/variable/validation gates")
        require_string(item.get("reason"), f"blockedL4Candidates[{index}].reason", errors)


def validate_abort_and_work_orders(registry: dict[str, Any], errors: list[str]) -> None:
    aborts = set(require_string_list(registry.get("hardAbortInheritance"), "hardAbortInheritance", errors, min_len=6))
    if aborts != REQUIRED_ABORTS:
        fail(errors, "hardAbortInheritance must exactly inherit contract abort gates")
    work = registry.get("nextWorkOrders")
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
    registry = load_json(REGISTRY_PATH, errors, "model admission candidate registry")
    contract_paths = reviewed_register_paths_from_contract(errors)
    if registry:
        if registry.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if registry.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(registry.get("registryId"), "registryId", errors)
        require_string(registry.get("purpose"), "purpose", errors)
        validate_source_of_truth(registry, contract_paths, errors)
        total_artifacts, total_blocked = validate_decisions(registry, contract_paths, errors)
        validate_aggregate(registry, len(contract_paths), total_artifacts, total_blocked, errors)
        validate_l3_and_l4(registry, errors)
        validate_abort_and_work_orders(registry, errors)
    validate_index_links(errors)

    if errors:
        print("model admission candidate registry audit failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    aggregate = registry.get("aggregateDecision", {})
    print(
        "model admission candidate registry audit ok: "
        f"registers={aggregate.get('reviewedArtifactRegisters')} "
        f"artifacts={aggregate.get('reviewedArtifactsCovered')} "
        f"blocked_rows={aggregate.get('blockedRowsPreserved')} l4=0 l5=0"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
