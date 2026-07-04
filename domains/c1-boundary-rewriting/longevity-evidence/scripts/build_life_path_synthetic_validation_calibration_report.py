#!/usr/bin/env python3
"""Build and audit a synthetic validation/calibration report dry-run.

This script binds the existing life-path toy model, sensitivity output and
L4 reporting contract into one machine-readable report packet. It is a dry-run
only: it must never be interpreted as real validation, real calibration, public
release permission, clinical advice or an individual prediction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MODEL = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model.json"
DEFAULT_SENSITIVITY = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-sensitivity-analysis.json"
)
DEFAULT_CONTRACT = (
    REPO_ROOT
    / "docs"
    / "reference"
    / "human-infra-l4-validation-calibration-reporting-contract.json"
)
DEFAULT_JSON_OUT = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-synthetic-validation-calibration-report.json"
)
DEFAULT_MD_OUT = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-synthetic-validation-calibration-report.md"
)

PROHIBITED_KEY_NAMES = {
    "deathDate",
    "death_date",
    "individualDeathDate",
    "individual_death_date",
    "predictedDeathDate",
    "predicted_death_date",
}
REPORT_ID = "life-path-synthetic-validation-calibration-report-2026-07-04"
REPORT_GENERATED_AT = "2026-07-04T00:00:00+00:00"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def source_ref(path: Path) -> dict[str, str]:
    return {"path": rel(path), "sha256": sha256_file(path)}


def require_dict(value: Any, name: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be an object")
    return value


def require_list(value: Any, name: str) -> list[Any]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be an array")
    return value


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, nested in value.items():
            keys.add(str(key))
            keys.update(collect_keys(nested))
    elif isinstance(value, list):
        for item in value:
            keys.update(collect_keys(item))
    return keys


def scenario_summary(model: dict[str, Any]) -> dict[str, Any]:
    scenarios = require_list(model.get("scenarios"), "model.scenarios")
    open_boundary = [
        scenario["id"]
        for scenario in scenarios
        if require_dict(scenario.get("metrics"), "scenario.metrics").get("openBoundary") is True
    ]
    curve_points = sum(len(require_list(scenario.get("curve"), "scenario.curve")) for scenario in scenarios)
    return {
        "scenarioCount": len(scenarios),
        "curvePointCount": curve_points,
        "openBoundaryScenarioIds": open_boundary,
        "modelClass": require_dict(model.get("modelCard"), "model.modelCard").get("modelClass"),
        "modelEvidenceBoundary": require_dict(model.get("modelCard"), "model.modelCard").get(
            "evidenceBoundary"
        ),
    }


def sensitivity_summary(sensitivity: dict[str, Any]) -> dict[str, Any]:
    results = require_list(sensitivity.get("results"), "sensitivity.results")
    stability = require_list(sensitivity.get("stabilitySummary"), "sensitivity.stabilitySummary")
    max_width = 0.0
    most_unstable: str | None = None
    for row in stability:
        item = require_dict(row, "stabilitySummary row")
        width = float(require_dict(item.get("effectiveTimeRange"), "effectiveTimeRange").get("width", 0))
        if width >= max_width:
            max_width = width
            most_unstable = str(item.get("scenarioId"))
    return {
        "resultCount": len(results),
        "stabilitySummaryCount": len(stability),
        "mostVariableSyntheticScenarioId": most_unstable,
        "maxSyntheticEffectiveTimeRangeWidth": round(max_width, 6),
        "analysisBoundary": sensitivity.get("analysisBoundary"),
    }


def field_status(required_fields: list[Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for field in required_fields:
        rows.append(
            {
                "field": str(field),
                "dryRunFilled": True,
                "realEvidenceAttached": False,
                "l4ClosureAllowed": False,
                "valueClass": "synthetic-placeholder-or-derived-toy-summary",
            }
        )
    return rows


def build_sections(contract: dict[str, Any], model: dict[str, Any], sensitivity: dict[str, Any]) -> list[dict[str, Any]]:
    model_summary = scenario_summary(model)
    sens_summary = sensitivity_summary(sensitivity)
    sections: list[dict[str, Any]] = []
    for raw_section in require_list(contract.get("reportPacketSections"), "contract.reportPacketSections"):
        section = require_dict(raw_section, "reportPacketSections row")
        section_id = str(section.get("sectionId"))
        required_fields = require_list(section.get("requiredFields"), f"{section_id}.requiredFields")
        sections.append(
            {
                "sectionId": section_id,
                "contractPurpose": section.get("purpose"),
                "dryRunStatus": "synthetic-filled-not-evidence",
                "blocksIfRealPacketMissing": bool(section.get("blocksIfMissing")),
                "requiredFieldStatus": field_status(required_fields),
                "syntheticEvidence": {
                    "toyModelScenarioSummary": model_summary,
                    "sensitivitySummary": sens_summary,
                },
                "realEvidenceAttached": False,
                "l4ClosureAllowed": False,
                "sectionDecision": "usable-as-report-shape-demo-only",
            }
        )
    return sections


def build_slot_outcomes(contract: dict[str, Any], sections: list[dict[str, Any]]) -> list[dict[str, Any]]:
    section_ids = {section["sectionId"] for section in sections}
    outcomes: list[dict[str, Any]] = []
    for raw_slot in require_list(contract.get("slotMapping"), "contract.slotMapping"):
        slot = require_dict(raw_slot, "slotMapping row")
        required_sections = [str(item) for item in require_list(slot.get("requiredSections"), "requiredSections")]
        missing_sections = sorted(set(required_sections) - section_ids)
        outcomes.append(
            {
                "slotId": slot.get("slotId"),
                "evidenceClass": slot.get("evidenceClass"),
                "repositoryPolicy": slot.get("repositoryPolicy"),
                "requiredSections": required_sections,
                "missingSections": missing_sections,
                "dryRunExercised": not missing_sections,
                "realEvidenceAttached": False,
                "slotCloseAllowed": False,
                "reason": "Synthetic report dry-run exercises the slot shape but cannot close any L4 slot.",
            }
        )
    return outcomes


def build_report(
    model: dict[str, Any],
    sensitivity: dict[str, Any],
    contract: dict[str, Any],
    model_path: Path,
    sensitivity_path: Path,
    contract_path: Path,
) -> dict[str, Any]:
    sections = build_sections(contract, model, sensitivity)
    slot_outcomes = build_slot_outcomes(contract, sections)
    return {
        "schemaVersion": "human-infra.life-path-synthetic-validation-calibration-report.v1",
        "reportId": REPORT_ID,
        "status": "synthetic-dry-run-l4-blocked",
        "generatedAt": REPORT_GENERATED_AT,
        "owner": "tradecatlabs",
        "sourceRefs": {
            "toyModel": source_ref(model_path),
            "sensitivityAnalysis": source_ref(sensitivity_path),
            "l4ReportingContract": source_ref(contract_path),
        },
        "currentDecision": {
            "syntheticReportGenerated": True,
            "contractSectionsExercised": True,
            "contractSlotsExercised": True,
            "realValidationReportAttached": False,
            "realCalibrationDiagnosticsAvailable": False,
            "realParameterSensitivityAvailable": False,
            "biasApplicabilityReviewComplete": False,
            "tripodProbastReportingPacketComplete": False,
            "l4AggregateCalibratedAdmissionAllowed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibratedPredictionAvailable": False,
            "individualUseAllowed": False,
            "reason": "The report is generated only from synthetic toy and synthetic sensitivity artifacts. It demonstrates report shape and blocking behavior, not real validation or calibration.",
        },
        "reportBoundary": {
            "modelClass": "synthetic validation/calibration report dry-run",
            "allowedUse": "machine-readable L4 report-shape rehearsal and web explanation",
            "evidenceBoundary": "No real cohort, no observed outcomes, no calibration target, no validation cohort, no individual records and no public weighted-domain release are present.",
            "nonUses": [
                "real validation report",
                "real calibration report",
                "clinical prediction model",
                "medical advice",
                "treatment selection",
                "insurance or eligibility decision",
                "individual death-date prediction",
                "claim that any technology achieves longevity escape velocity",
            ],
        },
        "contractCoverage": {
            "contractId": contract.get("contractId"),
            "requiredSectionCount": len(require_list(contract.get("reportPacketSections"), "reportPacketSections")),
            "syntheticSectionCount": len(sections),
            "requiredSlotCount": len(require_list(contract.get("slotMapping"), "slotMapping")),
            "syntheticSlotCount": len(slot_outcomes),
            "syntheticReportPacketCount": 1,
            "realReportPacketCount": 0,
        },
        "modelSummary": scenario_summary(model),
        "sensitivitySummary": sensitivity_summary(sensitivity),
        "sections": sections,
        "slotOutcomes": slot_outcomes,
        "minimumDiagnosticStatus": {
            "discrimination": "synthetic-toy-output-only",
            "calibration": "blocked-no-observed-outcomes",
            "overallPerformance": "synthetic-toy-output-only",
            "sensitivity": "synthetic-one-factor-at-a-time-only",
            "biasApplicability": "blocked-no-real-population-review",
        },
        "prohibitedClaims": contract.get("prohibitedClaims", []),
        "auditSummary": {
            "deathDateSuppressed": True,
            "individualPredictionSuppressed": True,
            "rawRowsAbsent": True,
            "l4StillBlocked": True,
        },
    }


def validate_report(report: dict[str, Any], contract: dict[str, Any]) -> None:
    if report.get("schemaVersion") != "human-infra.life-path-synthetic-validation-calibration-report.v1":
        raise ValueError("unexpected report schemaVersion")
    if report.get("status") != "synthetic-dry-run-l4-blocked":
        raise ValueError("report status must keep L4 blocked")

    decision = require_dict(report.get("currentDecision"), "currentDecision")
    for key in (
        "realValidationReportAttached",
        "realCalibrationDiagnosticsAvailable",
        "realParameterSensitivityAvailable",
        "biasApplicabilityReviewComplete",
        "tripodProbastReportingPacketComplete",
        "l4AggregateCalibratedAdmissionAllowed",
        "publicWeightedDomainOutputAllowed",
        "calibratedPredictionAvailable",
        "individualUseAllowed",
    ):
        if decision.get(key) is not False:
            raise ValueError(f"currentDecision.{key} must be false")

    section_ids = [section["sectionId"] for section in require_list(report.get("sections"), "sections")]
    contract_section_ids = [
        str(section["sectionId"])
        for section in require_list(contract.get("reportPacketSections"), "contract.reportPacketSections")
    ]
    if section_ids != contract_section_ids:
        raise ValueError("report sections must exactly follow the contract section order")

    slot_ids = [slot["slotId"] for slot in require_list(report.get("slotOutcomes"), "slotOutcomes")]
    contract_slot_ids = [
        str(slot["slotId"])
        for slot in require_list(contract.get("slotMapping"), "contract.slotMapping")
    ]
    if slot_ids != contract_slot_ids:
        raise ValueError("slot outcomes must exactly follow the contract slot order")
    for slot in require_list(report.get("slotOutcomes"), "slotOutcomes"):
        slot_obj = require_dict(slot, "slot outcome")
        if slot_obj.get("slotCloseAllowed") is not False:
            raise ValueError(f"{slot_obj.get('slotId')} must not close")
        if slot_obj.get("realEvidenceAttached") is not False:
            raise ValueError(f"{slot_obj.get('slotId')} must not attach real evidence")

    coverage = require_dict(report.get("contractCoverage"), "contractCoverage")
    if coverage.get("realReportPacketCount") != 0:
        raise ValueError("realReportPacketCount must stay 0")
    if coverage.get("syntheticReportPacketCount") != 1:
        raise ValueError("syntheticReportPacketCount must be 1")

    prohibited_keys = PROHIBITED_KEY_NAMES & collect_keys(report)
    if prohibited_keys:
        raise ValueError(f"prohibited field names present: {sorted(prohibited_keys)}")

    audit = require_dict(report.get("auditSummary"), "auditSummary")
    if audit.get("l4StillBlocked") is not True:
        raise ValueError("auditSummary.l4StillBlocked must be true")


def write_markdown(report: dict[str, Any], out_path: Path) -> None:
    coverage = require_dict(report.get("contractCoverage"), "contractCoverage")
    decision = require_dict(report.get("currentDecision"), "currentDecision")
    lines = [
        "# Life-Path Synthetic Validation/Calibration Report Dry-Run",
        "",
        f"- Status: `{report['status']}`",
        f"- Synthetic sections: {coverage['syntheticSectionCount']} / {coverage['requiredSectionCount']}",
        f"- Synthetic slots: {coverage['syntheticSlotCount']} / {coverage['requiredSlotCount']}",
        f"- Real report packets: {coverage['realReportPacketCount']}",
        f"- L4 admission allowed: `{decision['l4AggregateCalibratedAdmissionAllowed']}`",
        f"- Individual use allowed: `{decision['individualUseAllowed']}`",
        "",
        "This artifact only exercises the reporting shape required by the L4 contract. It is not a real validation report, not a calibration report, and not a prediction model.",
        "",
        "## Slot Outcomes",
        "",
        "| Slot | Dry-run exercised | Slot close allowed |",
        "| --- | --- | --- |",
    ]
    for slot in require_list(report.get("slotOutcomes"), "slotOutcomes"):
        slot_obj = require_dict(slot, "slot outcome")
        lines.append(
            f"| `{slot_obj['slotId']}` | `{slot_obj['dryRunExercised']}` | `{slot_obj['slotCloseAllowed']}` |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            str(require_dict(report.get("reportBoundary"), "reportBoundary")["evidenceBoundary"]),
            "",
        ]
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--sensitivity", type=Path, default=DEFAULT_SENSITIVITY)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    model_path = args.model.resolve()
    sensitivity_path = args.sensitivity.resolve()
    contract_path = args.contract.resolve()
    json_out = args.json_out.resolve()
    md_out = args.md_out.resolve()

    model = load_json(model_path)
    sensitivity = load_json(sensitivity_path)
    contract = load_json(contract_path)
    report = build_report(model, sensitivity, contract, model_path, sensitivity_path, contract_path)
    validate_report(report, contract)

    json_out.parent.mkdir(parents=True, exist_ok=True)
    with json_out.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    write_markdown(report, md_out)
    print(
        "life-path synthetic validation/calibration report dry-run ok: "
        f"sections={report['contractCoverage']['syntheticSectionCount']} "
        f"slots={report['contractCoverage']['syntheticSlotCount']} "
        "l4=blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
