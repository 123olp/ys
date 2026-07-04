#!/usr/bin/env python3
"""审计 Human Infra L4 验证/校准报告执行寄存器。"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTER_PATH = ROOT / "docs/reference/human-infra-l4-validation-calibration-report-execution-register.json"
CONTRACT_PATH = ROOT / "docs/reference/human-infra-l4-validation-calibration-reporting-contract.json"
SYNTHETIC_REPORT_PATH = ROOT / "web/src/data/life-path-synthetic-validation-calibration-report.json"
DEFAULT_OUT = ROOT / "web/src/data/life-path-l4-validation-calibration-report-execution-validation.json"

SCHEMA = "human-infra.l4-validation-calibration-report-execution-register.v1"
STATUS = "execution-register-ready-no-real-report-packet-l4-blocked"
CONTRACT_SCHEMA = "human-infra.l4-validation-calibration-reporting-contract.v1"
SYNTHETIC_SCHEMA = "human-infra.life-path-synthetic-validation-calibration-report.v1"
REGISTER_LINK = "human-infra-l4-validation-calibration-report-execution-register.json"
SCRIPT_LINK = "audit_human_infra_l4_validation_calibration_report_execution_register.py"

REQUIRED_SOURCE_KEYS = {
    "reportingContract",
    "syntheticDryRun",
    "l4EvidenceIntakeRegister",
    "l4EvidencePacketReviewPlaybook",
    "l4UnblockExecutionPlan",
    "modelAdmissionCandidateRegistry",
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
REQUIRED_SLOT_MAPPING = {
    "development-validation-design": ("redacted-artifact-hash", "study-design-summary-only"),
    "calibration-diagnostics-report": ("calibration-diagnostic-report", "reviewed-aggregate-diagnostics-only"),
    "real-parameter-sensitivity-analysis": (
        "calibration-diagnostic-report",
        "reviewed-aggregate-diagnostics-only",
    ),
    "bias-applicability-review": ("bias-applicability-review", "reviewed-report-summary-only"),
    "tripod-probast-reporting-packet": ("bias-applicability-review", "reporting-packet-hash-only"),
}
REQUIRED_TRUE_DECISIONS = {
    "executionRegisterValidated",
    "reportingContractValidated",
    "syntheticDryRunAvailable",
}
REQUIRED_FALSE_DECISIONS = {
    "realValidationReportPacketAttached",
    "realCalibrationDiagnosticsPacketAttached",
    "realParameterSensitivityPacketAttached",
    "biasApplicabilityReviewPacketAttached",
    "tripodProbastReportingPacketAttached",
    "allRequiredSectionsCompleted",
    "allRequiredSlotsCompleted",
    "humanReviewerSignoffPresent",
    "secondReviewerSignoffPresent",
    "l4AggregateCalibratedAdmissionAllowed",
    "publicWeightedDomainOutputAllowed",
    "calibratedPredictionAvailable",
    "individualUseAllowed",
    "medicalAdviceAllowed",
}
REQUIRED_INDEX_LINKS = {
    "README.md": REGISTER_LINK,
    "docs/AGENTS.md": REGISTER_LINK,
    "docs/reference/README.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-roadmap.md": REGISTER_LINK,
    "docs/reference/human-infra-maturity-gap-register.json": REGISTER_LINK,
    "Makefile": "l4-validation-calibration-report-execution-register-audit",
    "tools/README.md": SCRIPT_LINK,
    "tools/AGENTS.md": SCRIPT_LINK,
    "web/README.md": "life-path-l4-validation-calibration-report-execution-validation.json",
    "web/AGENTS.md": "life-path-l4-validation-calibration-report-execution-validation.json",
    "web/package.json": "export:life-path-l4-validation-calibration-report-execution-validation",
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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT))


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


def repo_path(relative_path: str, context: str, errors: list[str]) -> Path | None:
    value = require_string(relative_path, context, errors)
    if not value:
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


def validate_sources(register: dict[str, Any], errors: list[str]) -> None:
    source = register.get("sourceOfTruth")
    if not isinstance(source, dict):
        fail(errors, "sourceOfTruth must be an object")
        return
    if set(source) != REQUIRED_SOURCE_KEYS:
        fail(errors, "sourceOfTruth must contain exactly the required keys")
    for key, value in source.items():
        repo_path(value, f"sourceOfTruth.{key}", errors)
    if source.get("reportingContract") != repo_rel(CONTRACT_PATH):
        fail(errors, "sourceOfTruth.reportingContract mismatch")
    if source.get("syntheticDryRun") != repo_rel(SYNTHETIC_REPORT_PATH):
        fail(errors, "sourceOfTruth.syntheticDryRun mismatch")


def validate_upstream_contract(contract: dict[str, Any], register: dict[str, Any], errors: list[str]) -> None:
    if contract.get("schemaVersion") != CONTRACT_SCHEMA:
        fail(errors, "upstream reporting contract schemaVersion mismatch")
    if contract.get("status") != "template-only-no-validation-report-l4-blocked":
        fail(errors, "upstream reporting contract status mismatch")

    binding = register.get("workOrderBinding")
    if not isinstance(binding, dict):
        fail(errors, "workOrderBinding must be an object")
        return
    if binding.get("workOrderId") != "L4WO-05-validation-calibration-diagnostics":
        fail(errors, "workOrderBinding.workOrderId mismatch")
    if binding.get("candidatePath") != "L4C-NHANES-PUBLIC-LMF-WEIGHTED-DOMAIN":
        fail(errors, "workOrderBinding.candidatePath mismatch")
    if set(binding.get("blocks", [])) != {"L4B-06-validation-calibration"}:
        fail(errors, "workOrderBinding.blocks must contain only L4B-06-validation-calibration")
    if binding.get("requiredContractSections") != 12:
        fail(errors, "workOrderBinding.requiredContractSections must be 12")
    if binding.get("requiredL4Slots") != 5:
        fail(errors, "workOrderBinding.requiredL4Slots must be 5")

    contract_sections = contract.get("reportPacketSections")
    if not isinstance(contract_sections, list):
        fail(errors, "upstream reportPacketSections must be a list")
    else:
        section_ids = {section.get("sectionId") for section in contract_sections if isinstance(section, dict)}
        if section_ids != REQUIRED_SECTION_IDS:
            fail(errors, "upstream contract section IDs mismatch")

    contract_slots = contract.get("slotMapping")
    if not isinstance(contract_slots, list):
        fail(errors, "upstream slotMapping must be a list")
    else:
        slot_ids = {slot.get("slotId") for slot in contract_slots if isinstance(slot, dict)}
        if slot_ids != set(REQUIRED_SLOT_MAPPING):
            fail(errors, "upstream contract slot IDs mismatch")


def validate_synthetic_report(report: dict[str, Any], errors: list[str]) -> None:
    if report.get("schemaVersion") != SYNTHETIC_SCHEMA:
        fail(errors, "synthetic dry-run schemaVersion mismatch")
    if report.get("status") != "synthetic-dry-run-l4-blocked":
        fail(errors, "synthetic dry-run status must remain blocked")
    coverage = report.get("contractCoverage")
    if not isinstance(coverage, dict):
        fail(errors, "synthetic dry-run contractCoverage must be an object")
        return
    expected = {
        "requiredSectionCount": 12,
        "syntheticSectionCount": 12,
        "requiredSlotCount": 5,
        "syntheticSlotCount": 5,
        "realReportPacketCount": 0,
    }
    for key, value in expected.items():
        if coverage.get(key) != value:
            fail(errors, f"synthetic dry-run contractCoverage.{key} must be {value!r}")
    decision = report.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "synthetic dry-run currentDecision must be an object")
        return
    for key in [
        "realValidationReportAttached",
        "realCalibrationDiagnosticsAvailable",
        "realParameterSensitivityAvailable",
        "biasApplicabilityReviewComplete",
        "tripodProbastReportingPacketComplete",
        "l4AggregateCalibratedAdmissionAllowed",
        "publicWeightedDomainOutputAllowed",
        "calibratedPredictionAvailable",
        "individualUseAllowed",
    ]:
        if decision.get(key) is not False:
            fail(errors, f"synthetic dry-run currentDecision.{key} must be false")


def validate_decision(register: dict[str, Any], errors: list[str]) -> None:
    decision = register.get("currentDecision")
    if not isinstance(decision, dict):
        fail(errors, "currentDecision must be an object")
        return
    for key in REQUIRED_TRUE_DECISIONS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not True:
            fail(errors, f"currentDecision.{key} must be true")
    for key in REQUIRED_FALSE_DECISIONS:
        if require_bool(decision.get(key), f"currentDecision.{key}", errors) is not False:
            fail(errors, f"currentDecision.{key} must be false")
    if decision.get("downstreamDecision") != "l4-still-blocked":
        fail(errors, "currentDecision.downstreamDecision must be l4-still-blocked")
    reason = require_string(decision.get("reason"), "currentDecision.reason", errors)
    for phrase in [
        "no real validation/calibration report packet",
        "calibration diagnostic packet",
        "TRIPOD+AI / PROBAST+AI",
        "human reviewer signoff",
        "second reviewer signoff",
    ]:
        if phrase not in reason:
            fail(errors, f"currentDecision.reason must mention {phrase}")


def validate_sections(register: dict[str, Any], errors: list[str]) -> dict[str, int]:
    sections = require_list(register.get("sectionExecution"), "sectionExecution", errors, min_len=12)
    observed: set[str] = set()
    synthetic_count = 0
    completed_count = 0
    pending_count = 0
    for index, section in enumerate(sections):
        if not isinstance(section, dict):
            fail(errors, f"sectionExecution[{index}] must be an object")
            continue
        section_id = require_string(section.get("sectionId"), f"sectionExecution[{index}].sectionId", errors)
        observed.add(section_id)
        if section.get("contractStatus") != "defined":
            fail(errors, f"section {section_id} contractStatus must be defined")
        if section.get("executionStatus") != "pending-real-report-packet":
            fail(errors, f"section {section_id} executionStatus must be pending-real-report-packet")
        if section.get("syntheticDryRunStatus") == "filled-not-evidence":
            synthetic_count += 1
        else:
            fail(errors, f"section {section_id} syntheticDryRunStatus must be filled-not-evidence")
        if section.get("realEvidenceRef") is not None:
            fail(errors, f"section {section_id} must not carry realEvidenceRef")
        if section.get("reviewerSignoff") is not None:
            fail(errors, f"section {section_id} must not carry reviewerSignoff")
        if section.get("completedAt") is not None:
            fail(errors, f"section {section_id} must not carry completedAt")
        if section.get("blocksL4") is not True:
            fail(errors, f"section {section_id} must block L4")
        pending_count += 1
    if observed != REQUIRED_SECTION_IDS:
        fail(errors, "sectionExecution must contain exactly the required section IDs")
    return {
        "required": len(REQUIRED_SECTION_IDS),
        "synthetic": synthetic_count,
        "completed": completed_count,
        "pending": pending_count,
    }


def validate_slots(register: dict[str, Any], errors: list[str]) -> dict[str, int]:
    slots = require_list(register.get("slotExecution"), "slotExecution", errors, min_len=5)
    observed: set[str] = set()
    synthetic_count = 0
    closed_count = 0
    pending_count = 0
    for index, slot in enumerate(slots):
        if not isinstance(slot, dict):
            fail(errors, f"slotExecution[{index}] must be an object")
            continue
        slot_id = require_string(slot.get("slotId"), f"slotExecution[{index}].slotId", errors)
        observed.add(slot_id)
        expected = REQUIRED_SLOT_MAPPING.get(slot_id)
        if expected is None:
            fail(errors, f"unknown slotId: {slot_id}")
            continue
        if slot.get("contractStatus") != "defined":
            fail(errors, f"slot {slot_id} contractStatus must be defined")
        if slot.get("executionStatus") != "pending-real-report-packet":
            fail(errors, f"slot {slot_id} executionStatus must be pending-real-report-packet")
        if (slot.get("requiredEvidenceClass"), slot.get("repositoryPolicy")) != expected:
            fail(errors, f"slot {slot_id} evidence class or repository policy mismatch")
        if slot.get("evidencePacketRef") is not None:
            fail(errors, f"slot {slot_id} must not carry evidencePacketRef")
        if slot.get("firstReviewerRole") is not None:
            fail(errors, f"slot {slot_id} must not carry firstReviewerRole")
        if slot.get("secondReviewerRole") is not None:
            fail(errors, f"slot {slot_id} must not carry secondReviewerRole")
        if slot.get("closedAt") is not None:
            fail(errors, f"slot {slot_id} must not carry closedAt")
        if slot.get("blocksL4") is not True:
            fail(errors, f"slot {slot_id} must block L4")
        synthetic_count += 1
        pending_count += 1
    if observed != set(REQUIRED_SLOT_MAPPING):
        fail(errors, "slotExecution must contain exactly the required slot IDs")
    return {
        "required": len(REQUIRED_SLOT_MAPPING),
        "synthetic": synthetic_count,
        "closed": closed_count,
        "pending": pending_count,
    }


def validate_completion(register: dict[str, Any], section_summary: dict[str, int], slot_summary: dict[str, int], errors: list[str]) -> None:
    state = register.get("completionState")
    if not isinstance(state, dict):
        fail(errors, "completionState must be an object")
        return
    expected = {
        "requiredSectionCount": section_summary["required"],
        "syntheticFilledSectionCount": section_summary["synthetic"],
        "realCompletedSectionCount": section_summary["completed"],
        "pendingRealSectionCount": section_summary["pending"],
        "requiredSlotCount": slot_summary["required"],
        "syntheticFilledSlotCount": slot_summary["synthetic"],
        "realClosedSlotCount": slot_summary["closed"],
        "pendingRealSlotCount": slot_summary["pending"],
        "realReportPacketCount": 0,
        "humanReviewedPacketCount": 0,
        "secondReviewedPacketCount": 0,
        "l4AggregateCalibratedAdmissionAllowed": False,
        "publicWeightedDomainOutputAllowed": False,
        "calibratedPredictionAvailable": False,
        "individualUseAllowed": False,
    }
    for key, value in expected.items():
        if state.get(key) != value:
            fail(errors, f"completionState.{key} must be {value!r}")


def validate_state_machine(register: dict[str, Any], errors: list[str]) -> None:
    machine = register.get("stateMachine")
    if not isinstance(machine, dict):
        fail(errors, "stateMachine must be an object")
        return
    if machine.get("currentState") != "l4-still-blocked-no-real-report-packet":
        fail(errors, "stateMachine.currentState mismatch")
    forbidden = set(require_list(machine.get("forbiddenDirectTransitions"), "stateMachine.forbiddenDirectTransitions", errors, min_len=4))
    for transition in [
        "l4-review-open",
        "calibrated-prediction-available",
        "public-weighted-domain-output-allowed",
        "individual-use-allowed",
    ]:
        if transition not in forbidden:
            fail(errors, f"stateMachine.forbiddenDirectTransitions must include {transition}")
    minimum_path = " ".join(str(item) for item in require_list(machine.get("minimumL4Path"), "stateMachine.minimumL4Path", errors, min_len=6))
    for phrase in [
        "calibration-diagnostics-packet-human-reviewed",
        "real-parameter-sensitivity-packet-human-reviewed",
        "bias-applicability-review-human-reviewed",
        "tripod-probast-reporting-packet-human-reviewed",
        "second-reviewer-signoff-present",
        "model-admission-review-passes",
    ]:
        if phrase not in minimum_path:
            fail(errors, f"stateMachine.minimumL4Path must mention {phrase}")


def validate_non_proof_boundary(register: dict[str, Any], errors: list[str]) -> None:
    boundary = register.get("nonProofBoundary")
    if not isinstance(boundary, dict):
        fail(errors, "nonProofBoundary must be an object")
        return
    confirms = " ".join(str(item) for item in require_list(boundary.get("confirms"), "nonProofBoundary.confirms", errors, min_len=3))
    non_confirms = " ".join(str(item) for item in require_list(boundary.get("doesNotConfirm"), "nonProofBoundary.doesNotConfirm", errors, min_len=7))
    for phrase in ["machine-auditable", "12 report sections", "5 L4WO-05 slots", "synthetic dry-run cannot"]:
        if phrase not in confirms:
            fail(errors, f"nonProofBoundary.confirms must mention {phrase}")
    for phrase in [
        "real validation report",
        "real calibration diagnostics",
        "TRIPOD+AI / PROBAST+AI",
        "L4 aggregate calibrated model admission",
        "public weighted-domain output",
        "individual prediction",
        "medical advice",
    ]:
        if phrase not in non_confirms:
            fail(errors, f"nonProofBoundary.doesNotConfirm must mention {phrase}")


def validate_index_links(errors: list[str]) -> None:
    for relative_path, needle in REQUIRED_INDEX_LINKS.items():
        path = ROOT / relative_path
        if not path.exists():
            fail(errors, f"missing index file: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        if needle not in text:
            fail(errors, f"{relative_path} must link or mention {needle}")


def build_report(
    register: dict[str, Any],
    contract: dict[str, Any],
    synthetic: dict[str, Any],
    section_summary: dict[str, int],
    slot_summary: dict[str, int],
    out_path: Path,
) -> dict[str, Any]:
    return {
        "schemaVersion": "human-infra.l4-validation-calibration-report-execution-validation.v1",
        "generatedAt": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "PASS",
        "sourceRefs": {
            "executionRegister": {
                "path": repo_rel(REGISTER_PATH),
                "sha256": sha256_file(REGISTER_PATH),
            },
            "reportingContract": {
                "path": repo_rel(CONTRACT_PATH),
                "sha256": sha256_file(CONTRACT_PATH),
            },
            "syntheticDryRun": {
                "path": repo_rel(SYNTHETIC_REPORT_PATH),
                "sha256": sha256_file(SYNTHETIC_REPORT_PATH),
            },
        },
        "summary": {
            "registerId": register.get("registerId"),
            "contractId": contract.get("contractId"),
            "syntheticReportId": synthetic.get("reportId"),
            "requiredSectionCount": section_summary["required"],
            "syntheticFilledSectionCount": section_summary["synthetic"],
            "realCompletedSectionCount": section_summary["completed"],
            "pendingRealSectionCount": section_summary["pending"],
            "requiredSlotCount": slot_summary["required"],
            "syntheticFilledSlotCount": slot_summary["synthetic"],
            "realClosedSlotCount": slot_summary["closed"],
            "pendingRealSlotCount": slot_summary["pending"],
            "realReportPacketCount": register.get("completionState", {}).get("realReportPacketCount"),
            "humanReviewedPacketCount": register.get("completionState", {}).get("humanReviewedPacketCount"),
            "secondReviewedPacketCount": register.get("completionState", {}).get("secondReviewedPacketCount"),
            "downstreamDecision": register.get("currentDecision", {}).get("downstreamDecision"),
            "l4AggregateCalibratedAdmissionAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibratedPredictionAvailable": False,
            "individualUseAllowed": False,
        },
        "boundaries": register.get("nonProofBoundary", {}),
        "outputPath": repo_rel(out_path),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json-out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    errors: list[str] = []
    register = load_json(REGISTER_PATH, errors, "L4 validation/calibration report execution register")
    contract = load_json(CONTRACT_PATH, errors, "L4 validation/calibration reporting contract")
    synthetic = load_json(SYNTHETIC_REPORT_PATH, errors, "synthetic validation/calibration dry-run")

    section_summary = {"required": 12, "synthetic": 0, "completed": 0, "pending": 0}
    slot_summary = {"required": 5, "synthetic": 0, "closed": 0, "pending": 0}

    if register:
        if register.get("schemaVersion") != SCHEMA:
            fail(errors, f"schemaVersion must be {SCHEMA}")
        if register.get("status") != STATUS:
            fail(errors, f"status must be {STATUS}")
        if register.get("owner") != "tradecatlabs":
            fail(errors, "owner must be tradecatlabs")
        purpose = require_string(register.get("purpose"), "purpose", errors)
        for phrase in [
            "not a validation report",
            "not a calibration report",
            "not a calibrated prediction model",
            "not individual prediction",
            "not medical advice",
        ]:
            if phrase not in purpose:
                fail(errors, f"purpose must mention {phrase}")
        validate_sources(register, errors)
        if contract:
            validate_upstream_contract(contract, register, errors)
        if synthetic:
            validate_synthetic_report(synthetic, errors)
        validate_decision(register, errors)
        section_summary = validate_sections(register, errors)
        slot_summary = validate_slots(register, errors)
        validate_completion(register, section_summary, slot_summary, errors)
        validate_state_machine(register, errors)
        validate_non_proof_boundary(register, errors)

    validate_index_links(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    out_path = args.json_out
    if not out_path.is_absolute():
        out_path = (ROOT / out_path).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    report = build_report(register, contract, synthetic, section_summary, slot_summary, out_path)
    out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        "L4 validation/calibration report execution audit ok: "
        "sections=12 pending=12 slots=5 pending=5 l4=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
