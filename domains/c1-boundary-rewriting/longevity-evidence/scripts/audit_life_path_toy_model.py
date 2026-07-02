#!/usr/bin/env python3
"""Audit the generated Human Infra life-path toy model output."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_MODEL = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model.json"
DEFAULT_JSON_OUT = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model-audit.json"
DEFAULT_MD_OUT = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model-audit.md"
DEFAULT_READINESS = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_calibration_readiness.json"
)
REQUIRED_MODEL_CARD_FIELDS = {
    "modelName",
    "modelClass",
    "purpose",
    "nonUses",
    "evidenceBoundary",
    "upgradeGate",
}
REQUIRED_METRICS = {
    "riskReduction",
    "capabilityGain",
    "subjectiveCompression",
    "levRatio",
    "distributionShiftYears",
    "expectedLifeAgeProxy",
    "expectedEffectiveTimeYears",
    "expectedEffectiveTimeGainYears",
    "healthspanAgeProxy",
    "survivalAt80",
    "survivalAt100",
    "optionValue",
    "riskTailPenalty",
    "thresholdStatus",
    "openBoundary",
    "resourceBudget",
}
PROHIBITED_FIELD_NAMES = {
    "deathDate",
    "death_date",
    "individualDeathDate",
    "individual_death_date",
    "predictedDeathDate",
    "predicted_death_date",
}
REQUIRED_READINESS_SECTIONS = {
    "targetPopulation",
    "timeZero",
    "predictionHorizons",
    "outcomes",
    "estimands",
    "candidatePredictors",
    "dataRequirements",
    "censoringAndCompetingRisks",
    "validationPlan",
    "calibrationPlan",
    "sensitivityAnalysisPlan",
    "biasAndApplicabilityPlan",
    "reportingPlan",
    "prohibitedUses",
    "upgradeGate",
}
REQUIRED_STANDARD_TOKENS = ("TRIPOD", "PROBAST", "ISPOR", "MRC", "OHDSI")


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


def add_check(checks: list[dict[str, Any]], check_id: str, status: str, detail: str) -> None:
    checks.append({"id": check_id, "status": status, "detail": detail})


def status_from_bool(condition: bool) -> str:
    return "PASS" if condition else "FAIL"


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


def summarize_checks(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "warn": sum(1 for check in checks if check["status"] == "WARN"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def has_text(value: Any, needle: str) -> bool:
    return needle.lower() in json.dumps(value, ensure_ascii=False).lower()


def audit_readiness(readiness: dict[str, Any], readiness_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    schema_version = readiness.get("schemaVersion")
    add_check(
        checks,
        "readiness-schema-version",
        status_from_bool(schema_version == "human-infra.life-path-calibration-readiness.v1"),
        f"schemaVersion={schema_version!r}",
    )

    current_boundary = readiness.get("currentBoundary")
    boundary_ok = (
        isinstance(current_boundary, dict)
        and current_boundary.get("realCohortAvailable") is False
        and current_boundary.get("calibratedPredictionAvailable") is False
        and current_boundary.get("externalValidationAvailable") is False
        and current_boundary.get("individualUseAllowed") is False
    )
    add_check(
        checks,
        "readiness-honest-current-boundary",
        status_from_bool(boundary_ok),
        "readiness contract must explicitly say real cohort, calibration, external validation, and individual use are unavailable",
    )

    standards = readiness.get("standards")
    standards_text = json.dumps(standards, ensure_ascii=False) if isinstance(standards, list) else ""
    missing_standards = [
        token for token in REQUIRED_STANDARD_TOKENS if token.lower() not in standards_text.lower()
    ]
    add_check(
        checks,
        "readiness-method-anchors",
        status_from_bool(isinstance(standards, list) and not missing_standards),
        f"missing_standards={missing_standards}",
    )

    missing_sections = sorted(REQUIRED_READINESS_SECTIONS - set(readiness))
    add_check(
        checks,
        "readiness-required-sections",
        status_from_bool(not missing_sections),
        f"missing_sections={missing_sections}",
    )

    population = readiness.get("targetPopulation")
    population_ok = isinstance(population, dict) and {
        "definition",
        "minimumFields",
        "currentPlaceholder",
    }.issubset(population)
    add_check(
        checks,
        "readiness-target-population",
        status_from_bool(population_ok),
        "target population must define minimum real-cohort fields and current placeholder",
    )

    time_zero = readiness.get("timeZero")
    time_zero_ok = isinstance(time_zero, dict) and {
        "definition",
        "minimumFields",
        "currentPlaceholder",
    }.issubset(time_zero)
    add_check(
        checks,
        "readiness-time-zero",
        status_from_bool(time_zero_ok),
        "time zero must define index-date rule fields before calibration",
    )

    outcomes = readiness.get("outcomes")
    outcomes_ok = (
        isinstance(outcomes, dict)
        and isinstance(outcomes.get("primary"), list)
        and len(outcomes["primary"]) >= 3
        and "death" in str(outcomes.get("forbiddenOutcome", "")).lower()
    )
    add_check(
        checks,
        "readiness-outcome-boundary",
        status_from_bool(outcomes_ok),
        "outcomes must include primary cohort outcomes and forbid individual death-date output",
    )

    estimands = readiness.get("estimands")
    estimands_ok = (
        isinstance(estimands, dict)
        and isinstance(estimands.get("minimumEstimands"), list)
        and len(estimands["minimumEstimands"]) >= 3
    )
    add_check(
        checks,
        "readiness-estimands",
        status_from_bool(estimands_ok),
        "estimands must define scenario-level questions before calibration",
    )

    data_requirements = readiness.get("dataRequirements")
    data_ok = (
        isinstance(data_requirements, dict)
        and data_requirements.get("status") == "missing-real-cohort"
        and has_text(data_requirements, "No real cohort")
    )
    add_check(
        checks,
        "readiness-data-missing-boundary",
        status_from_bool(data_ok),
        "data requirements must state that real cohort and endpoint follow-up are missing",
    )

    validation_plan = readiness.get("validationPlan")
    validation_ok = (
        isinstance(validation_plan, dict)
        and isinstance(validation_plan.get("internalValidation"), list)
        and isinstance(validation_plan.get("externalValidation"), list)
        and validation_plan.get("status") == "not-started"
    )
    add_check(
        checks,
        "readiness-validation-plan",
        status_from_bool(validation_ok),
        "validation plan must include internal/external validation fields and not-started status",
    )

    calibration_plan = readiness.get("calibrationPlan")
    calibration_ok = (
        isinstance(calibration_plan, dict)
        and isinstance(calibration_plan.get("calibrationDiagnostics"), list)
        and calibration_plan.get("status") == "not-started"
    )
    add_check(
        checks,
        "readiness-calibration-plan",
        status_from_bool(calibration_ok),
        "calibration plan must include diagnostics and not-started status",
    )

    sensitivity_ok = isinstance(readiness.get("sensitivityAnalysisPlan"), dict) and isinstance(
        readiness["sensitivityAnalysisPlan"].get("requiredAnalyses"), list
    )
    add_check(
        checks,
        "readiness-sensitivity-plan",
        status_from_bool(sensitivity_ok),
        "sensitivity analysis plan must define required analyses",
    )

    bias_ok = isinstance(readiness.get("biasAndApplicabilityPlan"), dict) and isinstance(
        readiness["biasAndApplicabilityPlan"].get("riskDomains"), list
    )
    add_check(
        checks,
        "readiness-bias-applicability-plan",
        status_from_bool(bias_ok),
        "bias and applicability plan must define risk domains",
    )

    reporting_ok = isinstance(readiness.get("reportingPlan"), dict) and isinstance(
        readiness["reportingPlan"].get("requiredArtifacts"), list
    )
    add_check(
        checks,
        "readiness-reporting-plan",
        status_from_bool(reporting_ok),
        "reporting plan must define required artifacts beyond Web visualization",
    )

    prohibited_uses = readiness.get("prohibitedUses")
    prohibited_ok = (
        isinstance(prohibited_uses, list)
        and has_text(prohibited_uses, "individual")
        and has_text(prohibited_uses, "death-date")
        and has_text(prohibited_uses, "medical advice")
    )
    add_check(
        checks,
        "readiness-prohibited-uses",
        status_from_bool(prohibited_ok),
        "prohibited uses must block individual death-date prediction and medical advice",
    )

    upgrade_gate = readiness.get("upgradeGate")
    gate_ok = (
        isinstance(upgrade_gate, dict)
        and upgrade_gate.get("currentDecision") == "cannot-calibrate-yet"
        and isinstance(upgrade_gate.get("minimumRequirements"), list)
    )
    add_check(
        checks,
        "readiness-upgrade-gate",
        status_from_bool(gate_ok),
        "upgrade gate must keep the current decision at cannot-calibrate-yet",
    )

    return {
        "path": str(readiness_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(readiness_path),
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_model(data: dict[str, Any], model_path: Path, readiness_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    schema_version = data.get("schemaVersion")
    add_check(
        checks,
        "schema-version",
        status_from_bool(schema_version == "human-infra.life-path-toy-results.v1"),
        f"schemaVersion={schema_version!r}",
    )

    source = data.get("source")
    source_ok = isinstance(source, dict) and isinstance(source.get("path"), str)
    source_hash_ok = False
    if source_ok:
        source_path = (REPO_ROOT / source["path"]).resolve()
        if source_path.exists():
            source_hash_ok = sha256_file(source_path) == source.get("sha256")
    add_check(
        checks,
        "source-hash",
        status_from_bool(source_hash_ok),
        "source path and sha256 must point back to the scenario input",
    )

    model_card = data.get("modelCard")
    model_card_ok = isinstance(model_card, dict) and REQUIRED_MODEL_CARD_FIELDS.issubset(model_card)
    add_check(
        checks,
        "model-card-required-fields",
        status_from_bool(model_card_ok),
        f"required={sorted(REQUIRED_MODEL_CARD_FIELDS)}",
    )
    non_uses = model_card.get("nonUses") if isinstance(model_card, dict) else None
    non_use_ok = isinstance(non_uses, list) and any("death" in str(item).lower() for item in non_uses)
    add_check(
        checks,
        "prohibited-use-boundary",
        status_from_bool(non_use_ok),
        "model card must explicitly prohibit death-date or individual prediction use",
    )
    evidence_ok = isinstance(model_card, dict) and "synthetic" in str(
        model_card.get("evidenceBoundary", "")
    ).lower()
    add_check(
        checks,
        "synthetic-evidence-boundary",
        status_from_bool(evidence_ok),
        "model card must state the synthetic evidence boundary",
    )

    scenarios = data.get("scenarios")
    scenario_list_ok = isinstance(scenarios, list) and len(scenarios) >= 4
    add_check(
        checks,
        "scenario-count",
        status_from_bool(scenario_list_ok),
        f"scenario_count={len(scenarios) if isinstance(scenarios, list) else 'invalid'}",
    )

    scenario_ids = [scenario.get("id") for scenario in scenarios if isinstance(scenario, dict)] if isinstance(scenarios, list) else []
    unique_ids = len(scenario_ids) == len(set(scenario_ids)) and all(isinstance(item, str) for item in scenario_ids)
    add_check(checks, "scenario-id-unique", status_from_bool(unique_ids), f"ids={scenario_ids}")
    add_check(
        checks,
        "baseline-scenario-present",
        status_from_bool("baseline" in scenario_ids),
        "baseline scenario must be present for comparison",
    )

    metrics_ok = True
    curve_ok = True
    probability_ok = True
    resource_budget_ok = True
    open_boundary_ok = True
    for scenario in scenarios if isinstance(scenarios, list) else []:
        if not isinstance(scenario, dict):
            metrics_ok = False
            continue
        metrics = scenario.get("metrics")
        if not isinstance(metrics, dict) or not REQUIRED_METRICS.issubset(metrics):
            metrics_ok = False
            continue
        budget = metrics.get("resourceBudget")
        if not isinstance(budget, dict) or not all(
            isinstance(value, (int, float)) and 0 <= float(value) <= 100
            for value in budget.values()
        ):
            resource_budget_ok = False
        if metrics.get("levRatio", 0) >= 1:
            if metrics.get("openBoundary") is not True or "开放边界" not in str(metrics.get("thresholdStatus", "")):
                open_boundary_ok = False
        curve = scenario.get("curve")
        if not isinstance(curve, list) or len(curve) < 2:
            curve_ok = False
            continue
        previous = 1.0
        for point in curve:
            if not isinstance(point, dict):
                curve_ok = False
                continue
            survival = point.get("scenarioSurvival")
            baseline = point.get("baselineSurvival")
            health_quality = point.get("healthQuality")
            if not all(isinstance(item, (int, float)) for item in (survival, baseline, health_quality)):
                probability_ok = False
                continue
            if not (0 <= survival <= 1 and 0 <= baseline <= 1 and 0 <= health_quality <= 1):
                probability_ok = False
            if survival > previous + 1e-9:
                curve_ok = False
            previous = float(survival)

    add_check(checks, "metrics-required-fields", status_from_bool(metrics_ok), "each scenario must expose required metrics")
    add_check(checks, "survival-curve-monotonic", status_from_bool(curve_ok), "scenario survival curves must be monotonic non-increasing")
    add_check(checks, "probability-ranges", status_from_bool(probability_ok), "survival and health-quality values must remain in [0, 1]")
    add_check(checks, "resource-budget-ranges", status_from_bool(resource_budget_ok), "resource budget percentages must remain in [0, 100]")
    add_check(checks, "lev-open-boundary-contract", status_from_bool(open_boundary_ok), "LEV >= 1 must be reported as open boundary")

    key_set = collect_keys(data)
    prohibited_keys = sorted(key_set & PROHIBITED_FIELD_NAMES)
    add_check(
        checks,
        "no-individual-death-date-fields",
        status_from_bool(not prohibited_keys),
        f"prohibited_keys={prohibited_keys}",
    )

    standard_alignment = [
        {
            "standard": "TRIPOD+AI",
            "localGate": "model card + schema + transparent scenario output + calibration readiness fields",
            "status": "PARTIAL",
            "boundary": "toy model only; no development, calibration, or validation cohort",
        },
        {
            "standard": "PROBAST / PROBAST+AI",
            "localGate": "bias/applicability plan and prohibited-use boundary",
            "status": "PARTIAL",
            "boundary": "formal risk-of-bias assessment requires real study design and data",
        },
        {
            "standard": "ISPOR modeling good practices",
            "localGate": "versioned inputs, executable model, generated outputs, audit artifact, planned sensitivity fields",
            "status": "PARTIAL",
            "boundary": "no decision model, calibration, cost model, or executed sensitivity analysis yet",
        },
        {
            "standard": "MRC complex interventions framework",
            "localGate": "mechanism chain and context boundary in maturity roadmap",
            "status": "PARTIAL",
            "boundary": "stakeholder process and implementation evaluation are not started",
        },
        {
            "standard": "OHDSI Patient-Level Prediction",
            "localGate": "target population, time zero, outcome, predictor, time-at-risk and validation placeholders",
            "status": "PARTIAL",
            "boundary": "no OHDSI dataset, package execution, or patient-level prediction study is claimed",
        },
    ]
    readiness_audit = audit_readiness(load_json(readiness_path), readiness_path)
    checks.extend(readiness_audit["checks"])
    failed = [check for check in checks if check["status"] == "FAIL"]
    overall = "PASS" if not failed else "FAIL"
    return {
        "schemaVersion": "human-infra.life-path-toy-audit.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "modelPath": str(model_path.relative_to(REPO_ROOT)),
        "modelSha256": sha256_file(model_path),
        "overallStatus": overall,
        "checks": checks,
        "summary": summarize_checks(checks),
        "standardAlignment": standard_alignment,
        "calibrationReadiness": readiness_audit,
    }


def render_markdown(audit: dict[str, Any]) -> str:
    lines = [
        "# Life-Path Toy Model Audit",
        "",
        f"- Overall status: `{audit['overallStatus']}`",
        f"- Model path: `{audit['modelPath']}`",
        f"- Model SHA-256: `{audit['modelSha256']}`",
        f"- Generated at: `{audit['generatedAt']}`",
        "",
        "## Checks",
        "",
        "| Check | Status | Detail |",
        "| --- | --- | --- |",
    ]
    for check in audit["checks"]:
        detail = str(check["detail"]).replace("|", "\\|")
        lines.append(f"| `{check['id']}` | `{check['status']}` | {detail} |")
    lines.extend(
        [
            "",
            "## Calibration Readiness",
            "",
            f"- Readiness path: `{audit['calibrationReadiness']['path']}`",
            f"- Readiness SHA-256: `{audit['calibrationReadiness']['sha256']}`",
            f"- Readiness status: `{audit['calibrationReadiness']['status']}`",
            "- Boundary: readiness fields are present, but no real cohort, calibration, external validation, or individual use is available.",
            "",
            "## Standard Alignment",
            "",
            "| Standard | Local gate | Status | Boundary |",
            "| --- | --- | --- | --- |",
        ]
    )
    for row in audit["standardAlignment"]:
        lines.append(
            f"| {row['standard']} | {row['localGate']} | `{row['status']}` | {row['boundary']} |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This audit proves only that the synthetic toy model output satisfies the local reporting and sanity contract. It does not prove clinical validity, predictive validity, causal validity, or individual usefulness.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--readiness", type=Path, default=DEFAULT_READINESS)
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    model_path = args.model.resolve()
    readiness_path = args.readiness.resolve()
    audit = audit_model(load_json(model_path), model_path, readiness_path)
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    with args.json_out.open("w", encoding="utf-8") as handle:
        json.dump(audit, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    with args.md_out.open("w", encoding="utf-8") as handle:
        handle.write(render_markdown(audit))
    print(f"wrote {args.json_out.resolve().relative_to(REPO_ROOT)}")
    print(f"wrote {args.md_out.resolve().relative_to(REPO_ROOT)}")
    return 0 if audit["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
