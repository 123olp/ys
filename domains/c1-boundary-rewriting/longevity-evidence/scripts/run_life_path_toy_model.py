#!/usr/bin/env python3
"""Export a synthetic life-path toy model for the Human Infra web page."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_INPUT = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_toy_model_scenarios.json"
)
DEFAULT_OUTPUT = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model.json"


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


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def require_number(row: dict[str, Any], key: str) -> float:
    value = row.get(key)
    if not isinstance(value, (int, float)):
        raise ValueError(f"{key} must be numeric")
    return float(value)


def validate_config(config: dict[str, Any]) -> None:
    population = config.get("population")
    baseline = config.get("baselineHazard")
    quality = config.get("healthQuality")
    scenarios = config.get("scenarios")
    if not isinstance(population, dict):
        raise ValueError("population must be an object")
    if not isinstance(baseline, dict):
        raise ValueError("baselineHazard must be an object")
    if not isinstance(quality, dict):
        raise ValueError("healthQuality must be an object")
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("scenarios must be a non-empty array")

    start_age = require_number(population, "startAge")
    end_age = require_number(population, "endAge")
    step_years = require_number(population, "stepYears")
    if start_age >= end_age:
        raise ValueError("population.startAge must be lower than population.endAge")
    if step_years <= 0:
        raise ValueError("population.stepYears must be positive")

    seen_ids: set[str] = set()
    for scenario in scenarios:
        if not isinstance(scenario, dict):
            raise ValueError("each scenario must be an object")
        scenario_id = scenario.get("id")
        if not isinstance(scenario_id, str) or not scenario_id:
            raise ValueError("each scenario must have a non-empty id")
        if scenario_id in seen_ids:
            raise ValueError(f"duplicate scenario id: {scenario_id}")
        seen_ids.add(scenario_id)
        controls = scenario.get("controlValues")
        if not isinstance(controls, dict):
            raise ValueError(f"{scenario_id}.controlValues must be an object")
        for key in ("ai", "biomedical", "interfaceLevel", "waiting", "governance"):
            value = controls.get(key)
            if not isinstance(value, (int, float)) or not 0 <= float(value) <= 1:
                raise ValueError(f"{scenario_id}.controlValues.{key} must be within [0, 1]")
        for key in (
            "hazardMultiplier",
            "healthQualityShiftYears",
            "capabilityMultiplier",
            "subjectiveTimeExpansion",
            "levProgressRate",
            "riskTailPenalty",
        ):
            require_number(scenario, key)


def make_age_grid(population: dict[str, Any]) -> list[float]:
    start_age = require_number(population, "startAge")
    end_age = require_number(population, "endAge")
    step_years = require_number(population, "stepYears")
    ages: list[float] = []
    current = start_age
    while current <= end_age + 1e-9:
        ages.append(round(current, 6))
        current += step_years
    return ages


def gompertz_hazard(age: float, baseline: dict[str, Any]) -> float:
    base_hazard = require_number(baseline, "baseHazard")
    slope = require_number(baseline, "gompertzSlope")
    reference_age = require_number(baseline, "referenceAge")
    return base_hazard * math.exp(slope * (age - reference_age))


def health_quality(age: float, quality: dict[str, Any], shift_years: float) -> float:
    decline_start = require_number(quality, "declineStartAge") + shift_years
    decline_rate = require_number(quality, "declineRatePerYear")
    minimum = require_number(quality, "minimumQuality")
    return clamp(1.0 - max(0.0, age - decline_start) * decline_rate, minimum, 1.0)


def scenario_hazard(age: float, baseline: dict[str, Any], scenario: dict[str, Any]) -> float:
    hazard_multiplier = require_number(scenario, "hazardMultiplier")
    lev_rate = require_number(scenario, "levProgressRate")
    hazard = gompertz_hazard(age, baseline) * hazard_multiplier
    if lev_rate >= 1.0:
        boundary_relief = clamp((age - 70.0) * 0.012 * (lev_rate - 1.0), 0.0, 0.35)
        hazard *= 1.0 - boundary_relief
    return max(hazard, 0.0)


def integrate_curve(
    ages: list[float],
    baseline: dict[str, Any],
    quality: dict[str, Any],
    scenario: dict[str, Any],
    population: dict[str, Any],
) -> dict[str, Any]:
    step_years = require_number(population, "stepYears")
    threshold = require_number(population, "healthQualityThreshold")
    start_age = require_number(population, "startAge")
    scenario_survival = 1.0
    baseline_survival = 1.0
    remaining_years = 0.0
    effective_years = 0.0
    healthspan_years = 0.0
    curve: list[dict[str, float]] = []
    shift_years = require_number(scenario, "healthQualityShiftYears")
    capability_multiplier = require_number(scenario, "capabilityMultiplier")
    subjective_expansion = require_number(scenario, "subjectiveTimeExpansion")
    effective_multiplier = capability_multiplier * (1.0 + subjective_expansion)

    for index, age in enumerate(ages):
        quality_score = health_quality(age, quality, shift_years)
        curve.append(
            {
                "age": age,
                "baselineSurvival": round(baseline_survival, 6),
                "scenarioSurvival": round(scenario_survival, 6),
                "healthQuality": round(quality_score, 6),
                "effectiveDensity": round(
                    scenario_survival * quality_score * effective_multiplier, 6
                ),
            }
        )
        if index == len(ages) - 1:
            break
        remaining_years += scenario_survival * step_years
        effective_years += scenario_survival * quality_score * effective_multiplier * step_years
        if quality_score >= threshold:
            healthspan_years += scenario_survival * step_years
        scenario_survival *= math.exp(-scenario_hazard(age, baseline, scenario) * step_years)
        baseline_survival *= math.exp(-gompertz_hazard(age, baseline) * step_years)

    return {
        "curve": curve,
        "expectedLifeAgeProxy": round(start_age + remaining_years, 3),
        "expectedEffectiveTimeYears": round(effective_years, 3),
        "healthspanAgeProxy": round(start_age + healthspan_years, 3),
        "survivalAt80": survival_at(curve, 80, "scenarioSurvival"),
        "survivalAt100": survival_at(curve, 100, "scenarioSurvival"),
    }


def survival_at(curve: list[dict[str, float]], age: int, key: str) -> float:
    closest = min(curve, key=lambda row: abs(row["age"] - age))
    return round(float(closest[key]), 6)


def build_scenario_output(
    scenario: dict[str, Any],
    config: dict[str, Any],
    baseline_effective: float,
    baseline_life_age: float,
) -> dict[str, Any]:
    population = config["population"]
    baseline = config["baselineHazard"]
    quality = config["healthQuality"]
    ages = make_age_grid(population)
    integrated = integrate_curve(ages, baseline, quality, scenario, population)
    controls = scenario["controlValues"]
    risk_reduction = clamp(1.0 - require_number(scenario, "hazardMultiplier"), 0.0, 0.95)
    capability_gain = max(0.0, require_number(scenario, "capabilityMultiplier") - 1.0)
    lev_ratio = require_number(scenario, "levProgressRate")
    risk_tail_penalty = require_number(scenario, "riskTailPenalty")
    effective_gain = integrated["expectedEffectiveTimeYears"] - baseline_effective
    option_value = clamp(
        0.2
        + controls["ai"] * 0.2
        + controls["biomedical"] * 0.22
        + controls["governance"] * 0.18
        + risk_reduction * 0.22
        - risk_tail_penalty,
        0.0,
        1.0,
    )
    threshold_status = "越过阈值 / 开放边界" if lev_ratio >= 1.0 else "低于阈值 / 有限边界"

    def percent(value: float) -> int:
        return round(clamp(value, 0.0, 100.0))

    return {
        "id": scenario["id"],
        "label": scenario["label"],
        "description": scenario["description"],
        "evidenceGrade": scenario["evidenceGrade"],
        "controlValues": controls,
        "metrics": {
            "riskReduction": round(risk_reduction, 6),
            "capabilityGain": round(capability_gain, 6),
            "subjectiveCompression": round(
                require_number(scenario, "subjectiveTimeExpansion"), 6
            ),
            "levRatio": round(lev_ratio, 6),
            "distributionShiftYears": round(
                integrated["expectedLifeAgeProxy"] - baseline_life_age,
                6,
            ),
            "expectedLifeAgeProxy": integrated["expectedLifeAgeProxy"],
            "expectedEffectiveTimeYears": integrated["expectedEffectiveTimeYears"],
            "expectedEffectiveTimeGainYears": round(effective_gain, 3),
            "healthspanAgeProxy": integrated["healthspanAgeProxy"],
            "survivalAt80": integrated["survivalAt80"],
            "survivalAt100": integrated["survivalAt100"],
            "optionValue": round(option_value, 6),
            "riskTailPenalty": round(risk_tail_penalty, 6),
            "thresholdStatus": threshold_status,
            "openBoundary": lev_ratio >= 1.0,
            "resourceBudget": {
                "attention": percent((controls["ai"] * 0.42 + controls["governance"] * 0.18) * 100),
                "time": percent((effective_gain / 45.0 + controls["waiting"] * 0.25) * 100),
                "recovery": percent((controls["biomedical"] * 0.5 + controls["governance"] * 0.2) * 100),
                "option": percent(option_value * 100),
            },
        },
        "curve": integrated["curve"],
    }


def build_output(config: dict[str, Any], source_path: Path) -> dict[str, Any]:
    validate_config(config)
    scenarios = config["scenarios"]
    baseline_scenario = next((row for row in scenarios if row["id"] == "baseline"), scenarios[0])
    baseline_integrated = integrate_curve(
        make_age_grid(config["population"]),
        config["baselineHazard"],
        config["healthQuality"],
        baseline_scenario,
        config["population"],
    )
    baseline_effective = baseline_integrated["expectedEffectiveTimeYears"]
    baseline_life_age = baseline_integrated["expectedLifeAgeProxy"]
    scenario_outputs = [
        build_scenario_output(scenario, config, baseline_effective, baseline_life_age)
        for scenario in scenarios
    ]
    sanity = run_sanity_checks(scenario_outputs)
    return {
        "schemaVersion": "human-infra.life-path-toy-results.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": str(source_path.relative_to(REPO_ROOT)),
            "sha256": sha256_file(source_path),
        },
        "modelCard": {
            "modelName": "Human Infra Synthetic Life-Path Toy Model",
            "modelClass": "synthetic cohort toy model",
            "purpose": "Demonstrate the quantitative contract from intervention variables to hazard, survival, effective time, and option value.",
            "nonUses": [
                "individual death-date prediction",
                "medical advice",
                "treatment selection",
                "insurance or eligibility decisions",
                "claims that any intervention already achieves longevity escape velocity"
            ],
            "evidenceBoundary": "All scenarios are synthetic. Values are illustrative until calibrated with real cohorts, target-trial emulation, external validation, and bias assessment.",
            "upgradeGate": "A calibrated version requires target population, time zero, outcomes, censoring, covariates, data quality audit, validation plan, and model reporting aligned with TRIPOD+AI / PROBAST-style review."
        },
        "population": config["population"],
        "baselineHazard": config["baselineHazard"],
        "healthQuality": config["healthQuality"],
        "scenarios": scenario_outputs,
        "sanityChecks": sanity,
    }


def run_sanity_checks(scenarios: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [scenario["id"] for scenario in scenarios]
    monotonic = True
    probabilities_valid = True
    for scenario in scenarios:
        last = 1.0
        for point in scenario["curve"]:
            value = float(point["scenarioSurvival"])
            baseline = float(point["baselineSurvival"])
            if value > last + 1e-9:
                monotonic = False
            if not 0 <= value <= 1 or not 0 <= baseline <= 1:
                probabilities_valid = False
            last = value
    return {
        "uniqueScenarioIds": len(ids) == len(set(ids)),
        "monotonicScenarioSurvival": monotonic,
        "probabilitiesWithinUnitInterval": probabilities_valid,
        "deathDateSuppressed": True,
        "individualPredictionSuppressed": True,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config_path = args.input.resolve()
    output_path = args.out.resolve()
    config = load_json(config_path)
    output = build_output(config, config_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {output_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
