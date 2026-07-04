#!/usr/bin/env python3
"""审计 Human Infra 定量模型能力分层契约。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LADDER_PATH = ROOT / "docs/reference/human-infra-quantitative-capability-ladder.json"
DEFAULT_JSON_OUT = ROOT / "web/src/data/human-infra-quantitative-capability-ladder-validation.json"

SCHEMA = "human-infra.quantitative-capability-ladder.v1"
STATUS = "active-quantitative-capability-ladder-q3-current-q4-q5-blocked"
VALIDATION_SCHEMA = "human-infra.quantitative-capability-ladder-validation.v1"
REGISTER_LINK = "human-infra-quantitative-capability-ladder.json"
SCRIPT_LINK = "audit_human_infra_quantitative_capability_ladder.py"

REQUIRED_Q_LEVELS = ["Q0", "Q1", "Q2", "Q3", "Q4", "Q5"]
EXPECTED_LEVEL_MAP = {
    "Q0": "L0",
    "Q1": "L1",
    "Q2": "L2",
    "Q3": "L3",
    "Q4": "L4",
    "Q5": "L5",
}
REQUIRED_SOURCE_KEYS = {
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "l4ModelReadinessBlockerMatrix",
    "l4EvidenceIntakeRegister",
    "l4EvidencePacketReviewPlaybook",
    "l4ValidationCalibrationReportingContract",
    "researchStandardsSourceAnchorRegister",
    "toyModelOutput",
    "toyModelSensitivity",
    "syntheticValidationCalibrationReport",
    "syntheticL4EvidencePacketDryRun",
    "nhanesWeightedDomainOutputReadiness",
    "nhatsL4ReadinessRunway",
}
REQUIRED_OUTPUT_FAMILIES = {
    "narrative-concept-map",
    "reviewed-source-card",
    "candidate-variable-or-endpoint",
    "synthetic-curve-or-score",
    "synthetic-validation-calibration-report-shape",
    "synthetic-l4-evidence-packet-dry-run",
    "real-public-weighted-domain-output",
    "aggregate-calibrated-survival-model",
    "individual-prediction",
    "individual-death-date-output",
    "medical-advice-or-treatment-selection",
    "intervention-ranking-for-users",
}
FORBIDDEN_OUTPUT_FAMILIES = {
    "individual-prediction",
    "individual-death-date-output",
    "medical-advice-or-treatment-selection",
    "intervention-ranking-for-users",
}
REQUIRED_HARD_BOUNDARIES = {
    "No individual death-date output.",
    "No individual medical advice.",
    "No intervention ranking for users.",
    "Q5 is out of current repository scope and blocked by default.",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "docs/reference/human-infra-model-admission-contract.json": REGISTER_LINK,
    "docs/reference/human-infra-model-admission-candidate-registry.json": REGISTER_LINK,
    "Makefile": "quantitative-capability-ladder-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
    "web/README.md": "human-infra-quantitative-capability-ladder-validation.json",
    "web/AGENTS.md": "human-infra-quantitative-capability-ladder-validation.json",
    "web/package.json": "export:quantitative-capability-ladder-validation",
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


def validate_source_of_truth(ladder: dict[str, Any], errors: list[str]) -> None:
    source = ladder.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_current_decision(ladder: dict[str, Any], errors: list[str]) -> None:
    decision = ladder.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if decision.get("highestCurrentQuantitativeCapability") != "Q3-synthetic-life-path-model":
        fail(errors, "currentDecision.highestCurrentQuantitativeCapability must remain Q3")
    if decision.get("mappedModelAdmissionLevel") != "L3":
        fail(errors, "currentDecision.mappedModelAdmissionLevel must remain L3")
    for key in [
        "q3SyntheticCurvesAllowed",
        "q3SyntheticSensitivityAllowed",
        "q3SyntheticReportShapeAllowed",
    ]:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not True:
            fail(errors, f"currentDecision.{key} must be true")
    for key in [
        "q4AggregateCalibratedResearchModelAllowed",
        "q4PublicWeightedDomainOutputAllowed",
        "q4CalibratedPredictionAllowed",
        "q5IndividualDecisionSupportAllowed",
        "individualDeathDateOutputAllowed",
        "medicalAdviceAllowed",
        "interventionRankingAllowed",
    ]:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in ["synthetic", "real validation/calibration", "individual-use"]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase!r}")


def validate_capability_levels(ladder: dict[str, Any], errors: list[str]) -> None:
    levels = ladder.get("capabilityLevels")
    if not isinstance(levels, list):
        fail(errors, "capabilityLevels must be a list")
        return
    actual = [item.get("qLevel") for item in levels if isinstance(item, dict)]
    if actual != REQUIRED_Q_LEVELS:
        fail(errors, f"capabilityLevels must be ordered {REQUIRED_Q_LEVELS}, got {actual}")
    for item in levels:
        if not isinstance(item, dict):
            fail(errors, "capabilityLevels[] must contain objects")
            continue
        q_level = require_string(item.get("qLevel"), "capabilityLevels[].qLevel", errors)
        require_string(item.get("name"), f"{q_level}.name", errors)
        if item.get("mappedAdmissionLevel") != EXPECTED_LEVEL_MAP.get(q_level):
            fail(errors, f"{q_level}.mappedAdmissionLevel must be {EXPECTED_LEVEL_MAP.get(q_level)}")
        require_string_list(item.get("allowedOutputs"), f"{q_level}.allowedOutputs", errors, min_len=0)
        blocked = set(require_string_list(item.get("blockedOutputs"), f"{q_level}.blockedOutputs", errors, min_len=3))
        require_string_list(item.get("requiredEvidence"), f"{q_level}.requiredEvidence", errors, min_len=3)
        require_string(item.get("currentState"), f"{q_level}.currentState", errors)
        if q_level == "Q3" and not {"individual death date", "medical advice", "intervention ranking"} <= blocked:
            fail(errors, "Q3.blockedOutputs must include death date, medical advice and intervention ranking")
        if q_level == "Q4" and "unreviewed public weighted output" not in blocked:
            fail(errors, "Q4.blockedOutputs must include unreviewed public weighted output")
        if q_level == "Q5" and item.get("allowedOutputs") != []:
            fail(errors, "Q5.allowedOutputs must remain empty")
        if q_level == "Q5" and item.get("currentState") != "blocked-by-default":
            fail(errors, "Q5.currentState must be blocked-by-default")


def validate_output_matrix(ladder: dict[str, Any], errors: list[str]) -> None:
    rows = ladder.get("outputFamilyMatrix")
    if not isinstance(rows, list):
        fail(errors, "outputFamilyMatrix must be a list")
        return
    seen: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            fail(errors, f"outputFamilyMatrix[{index}] must be an object")
            continue
        family = require_string(row.get("outputFamily"), f"outputFamilyMatrix[{index}].outputFamily", errors)
        if family in seen:
            fail(errors, f"duplicate outputFamily: {family}")
        seen.add(family)
        min_level = require_string(row.get("minimumLevel"), f"{family}.minimumLevel", errors)
        if min_level not in {*REQUIRED_Q_LEVELS, "never"}:
            fail(errors, f"{family}.minimumLevel must be Q0-Q5 or never")
        current = require_bool(row.get("currentAllowed"), f"{family}.currentAllowed", errors)
        public = require_bool(row.get("publicWebAllowed"), f"{family}.publicWebAllowed", errors)
        require_string(row.get("boundary"), f"{family}.boundary", errors)
        if family in FORBIDDEN_OUTPUT_FAMILIES:
            if current is not False or public is not False:
                fail(errors, f"{family} must be blocked for current and public web use")
        if min_level == "Q4" and (current is not False or public is not False):
            fail(errors, f"{family} requires Q4 and must remain blocked")
    missing = REQUIRED_OUTPUT_FAMILIES - seen
    if missing:
        fail(errors, f"outputFamilyMatrix missing output families: {sorted(missing)}")


def validate_promotion_rules(ladder: dict[str, Any], errors: list[str]) -> None:
    rules = ladder.get("promotionRules")
    if not isinstance(rules, list) or len(rules) != 2:
        fail(errors, "promotionRules must contain exactly two rules")
        return
    expected = {("Q3", "Q4"), ("Q4", "Q5")}
    actual: set[tuple[str, str]] = set()
    for rule in rules:
        if not isinstance(rule, dict):
            fail(errors, "promotionRules[] must contain objects")
            continue
        source = require_string(rule.get("from"), "promotionRules[].from", errors)
        target = require_string(rule.get("to"), "promotionRules[].to", errors)
        actual.add((source, target))
        require_string_list(rule.get("requires"), f"{source}->{target}.requires", errors, min_len=5)
        decision = require_string(rule.get("currentDecision"), f"{source}->{target}.currentDecision", errors)
        if "blocked" not in decision:
            fail(errors, f"{source}->{target}.currentDecision must remain blocked")
    if actual != expected:
        fail(errors, f"promotionRules must be {sorted(expected)}, got {sorted(actual)}")


def validate_boundaries(ladder: dict[str, Any], errors: list[str]) -> None:
    boundaries = set(require_string_list(ladder.get("hardBoundaries"), "hardBoundaries", errors, min_len=6))
    missing = REQUIRED_HARD_BOUNDARIES - boundaries
    if missing:
        fail(errors, f"hardBoundaries missing required boundaries: {sorted(missing)}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} missing reference to {needle}")


def build_validation(ladder: dict[str, Any]) -> dict[str, Any]:
    levels = ladder.get("capabilityLevels", [])
    matrix = ladder.get("outputFamilyMatrix", [])
    return {
        "schemaVersion": VALIDATION_SCHEMA,
        "status": "pass-q3-current-q4-q5-blocked",
        "source": str(LADDER_PATH.relative_to(ROOT)),
        "qLevelCount": len(levels) if isinstance(levels, list) else 0,
        "outputFamilyCount": len(matrix) if isinstance(matrix, list) else 0,
        "highestCurrentQuantitativeCapability": ladder["currentDecision"]["highestCurrentQuantitativeCapability"],
        "mappedModelAdmissionLevel": ladder["currentDecision"]["mappedModelAdmissionLevel"],
        "q4AggregateCalibratedResearchModelAllowed": False,
        "q5IndividualDecisionSupportAllowed": False,
        "individualDeathDateOutputAllowed": False,
        "medicalAdviceAllowed": False,
        "interventionRankingAllowed": False,
        "publicWebBoundary": "Only Q0-Q3 bounded, synthetic or non-calibrated outputs may be consumed by public Web surfaces.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    args = parser.parse_args()

    errors: list[str] = []
    ladder = load_json(LADDER_PATH, errors, "quantitative capability ladder")
    if ladder:
        if ladder.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if ladder.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        validate_source_of_truth(ladder, errors)
        validate_current_decision(ladder, errors)
        validate_capability_levels(ladder, errors)
        validate_output_matrix(ladder, errors)
        validate_promotion_rules(ladder, errors)
        validate_boundaries(ladder, errors)
    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"quantitative capability ladder audit failed: {error}", file=sys.stderr)
        return 1

    validation = build_validation(ladder)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "quantitative capability ladder audit ok: "
        f"levels={validation['qLevelCount']} "
        f"outputs={validation['outputFamilyCount']} "
        "highest=Q3 q4=blocked q5=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
