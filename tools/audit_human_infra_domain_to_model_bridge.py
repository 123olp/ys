#!/usr/bin/env python3
"""审计 Human Infra 研究域到模型候选变量的桥接契约。"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs/reference/human-infra-domain-to-model-bridge-contract.json"
REGISTER_PATH = ROOT / "docs/reference/human-infra-domain-to-model-bridge-register.json"
DEFAULT_JSON_OUT = ROOT / "web/src/data/human-infra-domain-to-model-bridge-validation.json"

CONTRACT_SCHEMA = "human-infra.domain-to-model-bridge-contract.v1"
REGISTER_SCHEMA = "human-infra.domain-to-model-bridge-register.v1"
VALIDATION_SCHEMA = "human-infra.domain-to-model-bridge-validation.v1"
CONTRACT_STATUS = "active-domain-to-model-bridge-q2-current-q4-q5-blocked"
REGISTER_STATUS = "active-representative-domain-bridge-q2-only"

REQUIRED_BRIDGE_LEVELS = ["B0", "B1", "B2", "B3", "B4", "B5"]
EXPECTED_LEVEL_MAP = {
    "B0": ("L0", "Q0"),
    "B1": ("L1", "Q1"),
    "B2": ("L2", "Q2"),
    "B3": ("L3", "Q3"),
    "B4": ("L4", "Q4"),
    "B5": ("L5", "Q5"),
}
REQUIRED_TIERS = {"C1", "C2", "C3", "C4", "C5", "C6"}
REQUIRED_MODEL_LOCATIONS = {
    "state-variable",
    "state-transition",
    "hazard-function",
    "observation-process",
    "time-accounting",
    "action-policy",
    "access-adoption-probability",
    "option-value",
    "governance-boundary",
    "uncertainty-channel",
}
ALLOWED_MODEL_LOCATIONS = REQUIRED_MODEL_LOCATIONS | {"action-or-intervention"}
REQUIRED_CONTRACT_SOURCE_KEYS = {
    "domainClassification",
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "quantitativeCapabilityLadder",
    "maturityGapRegister",
    "lifePathPredictionModelContract",
    "lifePathPredictionModelGovernance",
    "domainClaimEvidenceMatrix",
    "domainSourceCardFieldExtraction",
}
REQUIRED_REGISTER_SOURCE_KEYS = {
    "bridgeContract",
    "domainClassification",
    "modelAdmissionContract",
    "quantitativeCapabilityLadder",
    "lifePathPredictionModelContract",
    "maturityRoadmap",
}
REQUIRED_REGISTER_FIELDS = {
    "bridgeId",
    "domainId",
    "domainPath",
    "tier",
    "tierName",
    "bridgeLevel",
    "mappedAdmissionLevel",
    "mappedQuantitativeCapability",
    "subjectContinuityFunction",
    "modelLocation",
    "variableFamily",
    "candidateModelRole",
    "mechanismStatement",
    "measurementProxy",
    "populationOrSetting",
    "endpointOrOutcomeFamily",
    "causalStatus",
    "evidenceAnchor",
    "uncertaintyChannel",
    "downgradeTrigger",
    "prohibitedUse",
    "nextEvidenceNeeded",
    "currentDecision",
}
REQUIRED_ABORT_IDS = {
    "DMB-ABORT-1-no-domain-path",
    "DMB-ABORT-2-no-model-location",
    "DMB-ABORT-3-narrative-to-coefficient-leap",
    "DMB-ABORT-4-association-to-intervention-effect-leap",
    "DMB-ABORT-5-individual-output",
    "DMB-ABORT-6-raw-or-sensitive-data",
}
REQUIRED_INDEX_LINKS = {
    "README.md": "human-infra-domain-to-model-bridge-contract.json",
    "docs/AGENTS.md": "human-infra-domain-to-model-bridge-contract.json",
    "docs/reference/README.md": "human-infra-domain-to-model-bridge-contract.json",
    "docs/reference/human-infra-maturity-roadmap.md": "human-infra-domain-to-model-bridge-contract.json",
    "docs/reference/human-infra-maturity-gap-register.json": "human-infra-domain-to-model-bridge-contract.json",
    "Makefile": "domain-to-model-bridge-audit",
    "tools/README.md": "audit_human_infra_domain_to_model_bridge.py",
    "tools/AGENTS.md": "audit_human_infra_domain_to_model_bridge.py",
    "web/README.md": "human-infra-domain-to-model-bridge-validation.json",
    "web/AGENTS.md": "human-infra-domain-to-model-bridge-validation.json",
}


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str], label: str) -> dict[str, Any]:
    if not path.exists():
        fail(errors, f"missing {label}: {path.relative_to(ROOT)}")
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(errors, f"invalid {label} JSON: {exc}")
        return {}
    if not isinstance(data, dict):
        fail(errors, f"{label} must be a JSON object")
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
        fail(errors, f"{context} must be a local repository path")
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


def load_classification(path: Path, errors: list[str]) -> dict[str, dict[str, str]]:
    if not path.exists():
        fail(errors, f"missing classification table: {path.relative_to(ROOT)}")
        return {}
    rows: dict[str, dict[str, str]] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        required = {"domain", "tier", "tier_name", "physical_path"}
        if not reader.fieldnames or not required <= set(reader.fieldnames):
            fail(errors, "classification.tsv must contain domain, tier, tier_name and physical_path columns")
            return {}
        for row in reader:
            domain = row.get("domain", "").strip()
            if domain:
                rows[domain] = {key: (row.get(key) or "").strip() for key in row}
    return rows


def validate_source_map(data: dict[str, Any], required_keys: set[str], context: str, errors: list[str]) -> None:
    source = data.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, f"{context}.sourceOfTruth must be an object")
        return
    if set(source) != required_keys:
        fail(errors, f"{context}.sourceOfTruth must contain exactly {sorted(required_keys)}")
    for key, value in source.items():
        repo_path(value, f"{context}.sourceOfTruth.{key}", errors)


def validate_contract(contract: dict[str, Any], errors: list[str]) -> set[str]:
    if contract.get("schemaVersion") != CONTRACT_SCHEMA:
        fail(errors, "contract.schemaVersion mismatch")
    if contract.get("status") != CONTRACT_STATUS:
        fail(errors, "contract.status mismatch")
    validate_source_map(contract, REQUIRED_CONTRACT_SOURCE_KEYS, "contract", errors)

    decision = contract.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "contract.currentDecision must be an object")
    else:
        expected_false = [
            "aggregateCalibratedUseAllowed",
            "individualUseAllowed",
            "coefficientOutputAllowed",
            "causalEffectOutputAllowed",
            "interventionRankingAllowed",
            "medicalAdviceAllowed",
            "individualDeathDateOutputAllowed",
        ]
        if decision.get("highestCurrentBridgeLevel") != "B2-model-candidate-variable":
            fail(errors, "currentDecision.highestCurrentBridgeLevel must remain B2")
        if decision.get("mappedAdmissionLevel") != "L2":
            fail(errors, "currentDecision.mappedAdmissionLevel must remain L2")
        if decision.get("mappedQuantitativeCapability") != "Q2":
            fail(errors, "currentDecision.mappedQuantitativeCapability must remain Q2")
        if require_bool(decision.get("candidateVariablesAllowed"), "currentDecision.candidateVariablesAllowed", errors) is not True:
            fail(errors, "candidateVariablesAllowed must be true")
        for key in expected_false:
            if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
                fail(errors, f"currentDecision.{key} must be false")

    levels = contract.get("bridgeLevels")
    if not isinstance(levels, list):
        fail(errors, "contract.bridgeLevels must be a list")
    else:
        actual = [item.get("bridgeLevel") for item in levels if isinstance(item, dict)]
        if actual != REQUIRED_BRIDGE_LEVELS:
            fail(errors, f"contract.bridgeLevels must be ordered {REQUIRED_BRIDGE_LEVELS}, got {actual}")
        for item in levels:
            if not isinstance(item, dict):
                fail(errors, "contract.bridgeLevels[] must contain objects")
                continue
            level = require_string(item.get("bridgeLevel"), "bridgeLevels[].bridgeLevel", errors)
            expected_admission, expected_q = EXPECTED_LEVEL_MAP.get(level, ("", ""))
            if item.get("mappedAdmissionLevel") != expected_admission:
                fail(errors, f"{level}.mappedAdmissionLevel must be {expected_admission}")
            if item.get("mappedQuantitativeCapability") != expected_q:
                fail(errors, f"{level}.mappedQuantitativeCapability must be {expected_q}")
            require_string(item.get("allowedUse"), f"{level}.allowedUse", errors)
            require_string_list(item.get("blockedUse"), f"{level}.blockedUse", errors, min_len=3)
            require_string_list(item.get("minimumEvidence"), f"{level}.minimumEvidence", errors, min_len=3)

    locations = contract.get("modelLocations")
    contract_locations: set[str] = set()
    if not isinstance(locations, list):
        fail(errors, "contract.modelLocations must be a list")
    else:
        for item in locations:
            if not isinstance(item, dict):
                fail(errors, "contract.modelLocations[] must contain objects")
                continue
            location = require_string(item.get("modelLocation"), "modelLocations[].modelLocation", errors)
            require_string(item.get("meaning"), f"modelLocations[{location}].meaning", errors)
            contract_locations.add(location)
        if not REQUIRED_MODEL_LOCATIONS <= contract_locations:
            fail(errors, f"contract.modelLocations missing {sorted(REQUIRED_MODEL_LOCATIONS - contract_locations)}")

    fields = set(require_string_list(contract.get("requiredRegisterFields"), "contract.requiredRegisterFields", errors, min_len=len(REQUIRED_REGISTER_FIELDS)))
    if not REQUIRED_REGISTER_FIELDS <= fields:
        fail(errors, f"contract.requiredRegisterFields missing {sorted(REQUIRED_REGISTER_FIELDS - fields)}")

    aborts = contract.get("hardAbortGates")
    if not isinstance(aborts, list):
        fail(errors, "contract.hardAbortGates must be a list")
    else:
        abort_ids = {item.get("abortId") for item in aborts if isinstance(item, dict)}
        missing = REQUIRED_ABORT_IDS - abort_ids
        if missing:
            fail(errors, f"contract.hardAbortGates missing {sorted(missing)}")

    representative = contract.get("minimumRepresentativeRegister")
    if not isinstance(representative, dict):
        fail(errors, "contract.minimumRepresentativeRegister must be an object")
    else:
        if representative.get("requiredRows", 0) < 12:
            fail(errors, "minimumRepresentativeRegister.requiredRows must be at least 12")
        if set(representative.get("requiredTiers", [])) != REQUIRED_TIERS:
            fail(errors, "minimumRepresentativeRegister.requiredTiers must cover C1-C6")
        if not REQUIRED_MODEL_LOCATIONS <= set(representative.get("requiredModelLocations", [])):
            fail(errors, "minimumRepresentativeRegister.requiredModelLocations must cover core model locations")
        if representative.get("maximumCurrentBridgeLevel") != "B2":
            fail(errors, "minimumRepresentativeRegister.maximumCurrentBridgeLevel must be B2")
        if representative.get("maximumCurrentAdmissionLevel") != "L2":
            fail(errors, "minimumRepresentativeRegister.maximumCurrentAdmissionLevel must be L2")
        if representative.get("maximumCurrentQuantitativeCapability") != "Q2":
            fail(errors, "minimumRepresentativeRegister.maximumCurrentQuantitativeCapability must be Q2")

    non_goals = " ".join(require_string_list(contract.get("nonGoals"), "contract.nonGoals", errors, min_len=4))
    for phrase in ["does not estimate", "does not validate", "does not open", "does not support"]:
        if phrase not in non_goals:
            fail(errors, f"contract.nonGoals must include phrase {phrase!r}")
    return contract_locations


def validate_register(
    register: dict[str, Any],
    contract_locations: set[str],
    classification: dict[str, dict[str, str]],
    errors: list[str],
) -> tuple[int, set[str], set[str]]:
    if register.get("schemaVersion") != REGISTER_SCHEMA:
        fail(errors, "register.schemaVersion mismatch")
    if register.get("status") != REGISTER_STATUS:
        fail(errors, "register.status mismatch")
    validate_source_map(register, REQUIRED_REGISTER_SOURCE_KEYS, "register", errors)

    decision = register.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "register.currentDecision must be an object")
    else:
        if decision.get("highestCurrentBridgeLevel") != "B2-model-candidate-variable":
            fail(errors, "register.currentDecision.highestCurrentBridgeLevel must remain B2")
        if decision.get("mappedAdmissionLevel") != "L2":
            fail(errors, "register.currentDecision.mappedAdmissionLevel must remain L2")
        if decision.get("mappedQuantitativeCapability") != "Q2":
            fail(errors, "register.currentDecision.mappedQuantitativeCapability must remain Q2")
        for key in [
            "syntheticScenarioInputsOpened",
            "aggregateCalibratedInputsOpened",
            "individualUseOpened",
        ]:
            if require_bool(decision.get(key), f"register.currentDecision.{key}", errors) is not False:
                fail(errors, f"register.currentDecision.{key} must be false")

    rows = register.get("bridgeRows")
    if not isinstance(rows, list):
        fail(errors, "register.bridgeRows must be a list")
        return 0, set(), set()
    if len(rows) < 12:
        fail(errors, "register.bridgeRows must contain at least 12 rows")

    ids: set[str] = set()
    tiers: set[str] = set()
    locations: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"register.bridgeRows[{index}] must be an object")
            continue
        missing = REQUIRED_REGISTER_FIELDS - set(row)
        if missing:
            fail(errors, f"bridgeRows[{index}] missing fields {sorted(missing)}")
        bridge_id = require_string(row.get("bridgeId"), f"bridgeRows[{index}].bridgeId", errors)
        if bridge_id in ids:
            fail(errors, f"duplicate bridgeId: {bridge_id}")
        ids.add(bridge_id)

        domain_id = require_string(row.get("domainId"), f"{bridge_id}.domainId", errors)
        domain_path = require_string(row.get("domainPath"), f"{bridge_id}.domainPath", errors)
        repo_path(domain_path, f"{bridge_id}.domainPath", errors)
        evidence_anchor = require_string(row.get("evidenceAnchor"), f"{bridge_id}.evidenceAnchor", errors)
        repo_path(evidence_anchor, f"{bridge_id}.evidenceAnchor", errors)

        tier = require_string(row.get("tier"), f"{bridge_id}.tier", errors)
        tiers.add(tier)
        classification_row = classification.get(domain_id)
        if not classification_row:
            fail(errors, f"{bridge_id}.domainId not found in classification.tsv: {domain_id}")
        else:
            if classification_row.get("tier") != tier:
                fail(errors, f"{bridge_id}.tier does not match classification.tsv")
            if classification_row.get("physical_path") != domain_path:
                fail(errors, f"{bridge_id}.domainPath does not match classification.tsv")

        if row.get("bridgeLevel") != "B2":
            fail(errors, f"{bridge_id}.bridgeLevel must remain B2")
        if row.get("mappedAdmissionLevel") != "L2":
            fail(errors, f"{bridge_id}.mappedAdmissionLevel must remain L2")
        if row.get("mappedQuantitativeCapability") != "Q2":
            fail(errors, f"{bridge_id}.mappedQuantitativeCapability must remain Q2")
        if row.get("currentDecision") != "candidate-only":
            fail(errors, f"{bridge_id}.currentDecision must be candidate-only")

        location = require_string(row.get("modelLocation"), f"{bridge_id}.modelLocation", errors)
        locations.add(location)
        if location not in contract_locations or location not in ALLOWED_MODEL_LOCATIONS:
            fail(errors, f"{bridge_id}.modelLocation is not allowed: {location}")

        for field in [
            "subjectContinuityFunction",
            "variableFamily",
            "candidateModelRole",
            "mechanismStatement",
            "measurementProxy",
            "populationOrSetting",
            "endpointOrOutcomeFamily",
            "causalStatus",
            "uncertaintyChannel",
            "downgradeTrigger",
            "prohibitedUse",
            "nextEvidenceNeeded",
        ]:
            require_string(row.get(field), f"{bridge_id}.{field}", errors)
        prohibited = str(row.get("prohibitedUse", ""))
        if "No " not in prohibited and "no " not in prohibited:
            fail(errors, f"{bridge_id}.prohibitedUse must explicitly block unsafe use")

    if not REQUIRED_TIERS <= tiers:
        fail(errors, f"register tier coverage missing {sorted(REQUIRED_TIERS - tiers)}")
    if not REQUIRED_MODEL_LOCATIONS <= locations:
        fail(errors, f"register model-location coverage missing {sorted(REQUIRED_MODEL_LOCATIONS - locations)}")

    boundary = register.get("aggregateBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "register.aggregateBoundary must be an object")
    else:
        expected_true = ["rowsAreRepresentative", "allRowsCandidateOnly"]
        for key in expected_true:
            if require_bool(boundary.get(key), f"aggregateBoundary.{key}", errors) is not True:
                fail(errors, f"aggregateBoundary.{key} must be true")
        expected_false = [
            "coefficientsAvailable",
            "causalEffectsAvailable",
            "calibratedPredictionAvailable",
            "individualUseAllowed",
            "medicalAdviceAllowed",
            "individualDeathDateOutputAllowed",
        ]
        for key in expected_false:
            if require_bool(boundary.get(key), f"aggregateBoundary.{key}", errors) is not False:
                fail(errors, f"aggregateBoundary.{key} must be false")
        if boundary.get("allRowsMaxBridgeLevel") != "B2":
            fail(errors, "aggregateBoundary.allRowsMaxBridgeLevel must be B2")
        if boundary.get("allRowsMaxAdmissionLevel") != "L2":
            fail(errors, "aggregateBoundary.allRowsMaxAdmissionLevel must be L2")
        if boundary.get("allRowsMaxQuantitativeCapability") != "Q2":
            fail(errors, "aggregateBoundary.allRowsMaxQuantitativeCapability must be Q2")

    return len(rows), tiers, locations


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        target = ROOT / relative_path
        if not target.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = target.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} must mention {needle}")


def build_validation(contract_path: Path, register_path: Path) -> dict[str, Any]:
    errors: list[str] = []
    contract = load_json(contract_path, errors, "bridge contract")
    register = load_json(register_path, errors, "bridge register")
    classification_path = ROOT / "domains/_possibility-space-control/classification.tsv"
    classification = load_classification(classification_path, errors)

    contract_locations = validate_contract(contract, errors)
    row_count, tiers, locations = validate_register(register, contract_locations, classification, errors)
    validate_index_links(errors)

    status = "pass-q2-only-q4-q5-blocked" if not errors else "fail"
    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "status": status,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "contractPath": str(contract_path.relative_to(ROOT)),
        "contractSha256": sha256_file(contract_path) if contract_path.exists() else None,
        "registerPath": str(register_path.relative_to(ROOT)),
        "registerSha256": sha256_file(register_path) if register_path.exists() else None,
        "rowCount": row_count,
        "tierCoverage": sorted(tiers),
        "modelLocationCoverage": sorted(locations),
        "highestCurrentBridgeLevel": "B2-model-candidate-variable",
        "mappedAdmissionLevel": "L2",
        "mappedQuantitativeCapability": "Q2",
        "candidateVariablesAllowed": status != "fail",
        "aggregateCalibratedUseAllowed": False,
        "individualUseAllowed": False,
        "coefficientOutputAllowed": False,
        "causalEffectOutputAllowed": False,
        "interventionRankingAllowed": False,
        "medicalAdviceAllowed": False,
        "individualDeathDateOutputAllowed": False,
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, default=CONTRACT_PATH)
    parser.add_argument("--register", type=Path, default=REGISTER_PATH)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    validation = build_validation(args.contract.resolve(), args.register.resolve())
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if validation["status"] != "pass-q2-only-q4-q5-blocked":
        print("domain-to-model bridge audit failed:", file=sys.stderr)
        for error in validation["errors"]:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "domain-to-model bridge audit ok: "
        f"rows={validation['rowCount']} tiers={','.join(validation['tierCoverage'])} "
        f"locations={len(validation['modelLocationCoverage'])} admission=L2 q=Q2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
