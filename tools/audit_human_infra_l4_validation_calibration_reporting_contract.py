#!/usr/bin/env python3
"""审计 Human Infra L4 验证/校准报告契约。"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "docs/reference/human-infra-l4-validation-calibration-reporting-contract.json"

SCHEMA = "human-infra.l4-validation-calibration-reporting-contract.v1"
STATUS = "template-only-no-validation-report-l4-blocked"
CONTRACT_LINK = "human-infra-l4-validation-calibration-reporting-contract.json"
SCRIPT_LINK = "audit_human_infra_l4_validation_calibration_reporting_contract.py"

REQUIRED_SOURCE_KEYS = {
    "l4UnblockExecutionPlan",
    "l4EvidenceIntakeRegister",
    "l4EvidencePacketReviewPlaybook",
    "calibrationReadiness",
    "modelAdmissionContract",
    "modelAdmissionCandidateRegistry",
    "falsifierSourceCardBackfill",
}
REQUIRED_STANDARD_IDS = {
    "TRIPOD+AI",
    "TRIPOD+AI-website",
    "PROBAST+AI",
}
REQUIRED_FALSE_DECISION_KEYS = {
    "realValidationReportAttached",
    "developmentValidationDesignComplete",
    "calibrationDiagnosticsAvailable",
    "realParameterSensitivityAvailable",
    "biasApplicabilityReviewComplete",
    "tripodProbastReportingPacketComplete",
    "l4AggregateCalibratedAdmissionAllowed",
    "publicWeightedDomainOutputAllowed",
    "calibratedPredictionAvailable",
    "individualUseAllowed",
}
REQUIRED_SLOT_IDS = {
    "development-validation-design",
    "calibration-diagnostics-report",
    "real-parameter-sensitivity-analysis",
    "bias-applicability-review",
    "tripod-probast-reporting-packet",
}
REQUIRED_SECTION_IDS = {
    "study-question-and-intended-use",
    "data-source-governance-and-cohort",
    "time-zero-horizons-outcomes",
    "predictors-measurement-and-missingness",
    "model-specification-and-update-status",
    "development-validation-design",
    "performance-discrimination-and-overall-error",
    "calibration-diagnostics",
    "uncertainty-sensitivity-and-stability",
    "bias-applicability-and-subgroup-review",
    "traceability-reproducibility-and-human-review",
    "limitations-prohibited-uses-and-downstream-decision",
}
REQUIRED_DIAGNOSTIC_GROUPS = {
    "discrimination",
    "calibration",
    "overallPerformance",
    "sensitivity",
    "auditBoundaries",
}
REQUIRED_DIAGNOSTIC_PHRASES = {
    "calibration-plot-or-table-by-horizon",
    "calibration-in-the-large",
    "calibration-slope-or-equivalent",
    "observed-expected-by-risk-group-or-domain",
    "parameter-uncertainty",
    "no-individual-prediction",
    "no-calibrated-claim-until-report-packet-complete",
}
REQUIRED_ACCEPTANCE_PHRASES = {
    "all five L4WO-05 slots",
    "redacted SHA-256",
    "specific prediction horizon",
    "TRIPOD+AI reporting completeness",
    "PROBAST+AI",
    "raw rows",
    "AI-only signoff",
    "l4-still-blocked",
}
REQUIRED_PROHIBITED_CLAIMS = {
    "public-weighted-domain-output",
    "calibrated-prediction",
    "individual-prediction",
    "individual-death-date-output",
    "medical-advice",
    "intervention-ranking",
    "causal-effect-claim",
    "longevity-escape-velocity-proof",
}
REQUIRED_INDEX_LINKS = {
    "README.md": CONTRACT_LINK,
    "docs/AGENTS.md": CONTRACT_LINK,
    "docs/reference/README.md": CONTRACT_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": CONTRACT_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": CONTRACT_LINK,
    "docs/reference/human-infra-l4-unblock-execution-plan.json": CONTRACT_LINK,
    "Makefile": "l4-validation-calibration-reporting-contract-audit",
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


def validate_source_of_truth(contract: dict[str, Any], errors: list[str]) -> None:
    source = contract.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)


def validate_external_standards(contract: dict[str, Any], errors: list[str]) -> None:
    standards = require_list(contract.get("externalStandards"), "externalStandards", errors, min_len=3)
    ids: set[str] = set()
    text_blob = json.dumps(standards, ensure_ascii=False)
    for index, standard in enumerate(standards):
        if not isinstance(standard, dict):
            fail(errors, f"externalStandards[{index}] must be an object")
            continue
        standard_id = require_string(standard.get("standardId"), f"externalStandards[{index}].standardId", errors)
        ids.add(standard_id)
        url = require_string(standard.get("url"), f"externalStandards[{index}].url", errors)
        if not url.startswith("https://"):
            fail(errors, f"externalStandards[{index}].url must be https")
        require_string(standard.get("role"), f"externalStandards[{index}].role", errors)
    if ids != REQUIRED_STANDARD_IDS:
        fail(errors, "externalStandards must contain TRIPOD+AI, TRIPOD+AI-website and PROBAST+AI")
    for phrase in ["SA-TRIPOD-AI-2024", "reporting", "risk of bias", "applicability"]:
        if phrase not in text_blob:
            fail(errors, f"externalStandards must mention {phrase}")


def validate_current_decision(contract: dict[str, Any], errors: list[str]) -> None:
    decision = contract.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    if "L3" not in require_string(decision.get("highestCurrentModelLevel"), "currentDecision.highestCurrentModelLevel", errors):
        fail(errors, "currentDecision.highestCurrentModelLevel must remain L3")
    if require_bool(decision.get("reportTemplateReady"), "currentDecision.reportTemplateReady", errors) is not True:
        fail(errors, "currentDecision.reportTemplateReady must be true")
    for key in REQUIRED_FALSE_DECISION_KEYS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in ["template", "no real", "TRIPOD+AI", "PROBAST+AI", "blocked"]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase}")


def validate_work_order_binding(contract: dict[str, Any], errors: list[str]) -> None:
    binding = contract.get("workOrderBinding")
    if not isinstance(binding, dict):
        fail(errors, "workOrderBinding must be an object")
        return
    if binding.get("workOrderId") != "L4WO-05-validation-calibration-diagnostics":
        fail(errors, "workOrderBinding.workOrderId must bind L4WO-05")
    if binding.get("candidatePath") != "L4C-NHANES-PUBLIC-LMF-WEIGHTED-DOMAIN":
        fail(errors, "workOrderBinding.candidatePath must bind NHANES public LMF candidate")
    if set(require_string_list(binding.get("blocks"), "workOrderBinding.blocks", errors)) != {"L4B-06-validation-calibration"}:
        fail(errors, "workOrderBinding.blocks must only contain L4B-06-validation-calibration")
    dependencies = set(require_string_list(binding.get("dependsOn"), "workOrderBinding.dependsOn", errors, min_len=2))
    if dependencies != {"L4WO-03-nhats-real-extraction-cohort-flow", "L4WO-04-nhanes-human-disclosure-review"}:
        fail(errors, "workOrderBinding.dependsOn must bind L4WO-03 and L4WO-04")
    if set(require_string_list(binding.get("slotIds"), "workOrderBinding.slotIds", errors, min_len=5)) != REQUIRED_SLOT_IDS:
        fail(errors, "workOrderBinding.slotIds must contain exactly the five L4WO-05 slot IDs")


def validate_sections(contract: dict[str, Any], errors: list[str]) -> None:
    sections = require_list(contract.get("reportPacketSections"), "reportPacketSections", errors, min_len=12)
    ids: set[str] = set()
    for index, section in enumerate(sections):
        if not isinstance(section, dict):
            fail(errors, f"reportPacketSections[{index}] must be an object")
            continue
        section_id = require_string(section.get("sectionId"), f"reportPacketSections[{index}].sectionId", errors)
        ids.add(section_id)
        require_string(section.get("purpose"), f"reportPacketSections[{index}].purpose", errors)
        require_string_list(section.get("requiredFields"), f"reportPacketSections[{index}].requiredFields", errors, min_len=4)
        if require_bool(section.get("blocksIfMissing"), f"reportPacketSections[{index}].blocksIfMissing", errors) is not True:
            fail(errors, f"reportPacketSections[{index}].blocksIfMissing must be true")
    if ids != REQUIRED_SECTION_IDS:
        fail(errors, "reportPacketSections must contain exactly the required section IDs")


def validate_minimum_diagnostics(contract: dict[str, Any], errors: list[str]) -> None:
    diagnostics = contract.get("minimumDiagnostics")
    if not isinstance(diagnostics, dict):
        fail(errors, "minimumDiagnostics must be an object")
        return
    if set(diagnostics) != REQUIRED_DIAGNOSTIC_GROUPS:
        fail(errors, "minimumDiagnostics must contain the required diagnostic groups")
    phrases: set[str] = set()
    for key, value in diagnostics.items():
        phrases.update(require_string_list(value, f"minimumDiagnostics.{key}", errors))
    missing = REQUIRED_DIAGNOSTIC_PHRASES - phrases
    if missing:
        fail(errors, f"minimumDiagnostics missing required phrase(s): {', '.join(sorted(missing))}")


def validate_slot_mapping(contract: dict[str, Any], errors: list[str]) -> None:
    mappings = require_list(contract.get("slotMapping"), "slotMapping", errors, min_len=5)
    ids: set[str] = set()
    for index, mapping in enumerate(mappings):
        if not isinstance(mapping, dict):
            fail(errors, f"slotMapping[{index}] must be an object")
            continue
        slot_id = require_string(mapping.get("slotId"), f"slotMapping[{index}].slotId", errors)
        ids.add(slot_id)
        evidence_class = require_string(mapping.get("evidenceClass"), f"slotMapping[{index}].evidenceClass", errors)
        policy = require_string(mapping.get("repositoryPolicy"), f"slotMapping[{index}].repositoryPolicy", errors)
        if slot_id == "development-validation-design" and (evidence_class, policy) != ("redacted-artifact-hash", "study-design-summary-only"):
            fail(errors, "development-validation-design mapping has wrong class or policy")
        if slot_id in {"calibration-diagnostics-report", "real-parameter-sensitivity-analysis"} and (evidence_class, policy) != ("calibration-diagnostic-report", "reviewed-aggregate-diagnostics-only"):
            fail(errors, f"{slot_id} mapping has wrong class or policy")
        if slot_id == "bias-applicability-review" and (evidence_class, policy) != ("bias-applicability-review", "reviewed-report-summary-only"):
            fail(errors, "bias-applicability-review mapping has wrong class or policy")
        if slot_id == "tripod-probast-reporting-packet" and (evidence_class, policy) != ("bias-applicability-review", "reporting-packet-hash-only"):
            fail(errors, "tripod-probast-reporting-packet mapping has wrong class or policy")
        required_sections = set(require_string_list(mapping.get("requiredSections"), f"slotMapping[{index}].requiredSections", errors))
        if not required_sections <= REQUIRED_SECTION_IDS:
            fail(errors, f"slotMapping[{index}].requiredSections contains unknown section")
    if ids != REQUIRED_SLOT_IDS:
        fail(errors, "slotMapping must contain exactly the five L4WO-05 slot IDs")


def validate_rules_and_summary(contract: dict[str, Any], errors: list[str]) -> None:
    acceptance = " ".join(require_string_list(contract.get("acceptanceRules"), "acceptanceRules", errors, min_len=8))
    for phrase in REQUIRED_ACCEPTANCE_PHRASES:
        if phrase not in acceptance:
            fail(errors, f"acceptanceRules must mention {phrase}")

    claims = set(require_string_list(contract.get("prohibitedClaims"), "prohibitedClaims", errors, min_len=8))
    if claims != REQUIRED_PROHIBITED_CLAIMS:
        fail(errors, "prohibitedClaims must contain exactly the required blocked claims")

    summary = contract.get("reportStatusSummary")
    if not isinstance(summary, dict):
        fail(errors, "reportStatusSummary must be an object")
        return
    expected = {
        "requiredSectionCount": 12,
        "requiredSlotCount": 5,
        "completedSectionCount": 0,
        "completedSlotCount": 0,
        "reportPacketCount": 0,
        "l4ReviewOpen": False,
    }
    for key, value in expected.items():
        if summary.get(key) != value:
            fail(errors, f"reportStatusSummary.{key} must be {value!r}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} must link or mention {needle}")


def main() -> int:
    errors: list[str] = []
    contract = load_json(CONTRACT_PATH, errors, "L4 validation/calibration reporting contract")

    if contract:
        if contract.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if contract.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        require_string(contract.get("contractId"), "contractId", errors)
        if contract.get("owner") != "tradecatlabs":
            fail(errors, "owner must be tradecatlabs")
        purpose = require_string(contract.get("purpose"), "purpose", errors)
        for phrase in ["not a validation report", "not a calibrated prediction model", "not individual prediction", "not medical advice"]:
            if phrase not in purpose:
                fail(errors, f"purpose must mention {phrase}")
        validate_source_of_truth(contract, errors)
        validate_external_standards(contract, errors)
        validate_current_decision(contract, errors)
        validate_work_order_binding(contract, errors)
        validate_sections(contract, errors)
        validate_minimum_diagnostics(contract, errors)
        validate_slot_mapping(contract, errors)
        validate_rules_and_summary(contract, errors)

    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("L4 validation/calibration reporting contract audit ok: sections=12 slots=5 l4=blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
