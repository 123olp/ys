#!/usr/bin/env python3
"""Export synthetic sensitivity analysis for the Human Infra life-path toy model."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_life_path_toy_model import (
    REPO_ROOT,
    build_scenario_output,
    integrate_curve,
    load_json,
    make_age_grid,
    require_number,
    sha256_file,
    validate_config,
)


DEFAULT_INPUT = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_toy_model_scenarios.json"
)
DEFAULT_MODEL = REPO_ROOT / "web" / "src" / "data" / "life-path-toy-model.json"
DEFAULT_OUTPUT = REPO_ROOT / "web" / "src" / "data" / "life-path-sensitivity-analysis.json"


PERTURBATION_PLAN = [
    {
        "parameter": "hazardMultiplier",
        "label": "死亡风险倍率",
        "mode": "relative",
        "low": 0.9,
        "high": 1.1,
        "floor": 0.05,
        "ceiling": 2.0,
    },
    {
        "parameter": "healthQualityShiftYears",
        "label": "健康质量位移年数",
        "mode": "absolute",
        "low": -2.0,
        "high": 2.0,
        "floor": -20.0,
        "ceiling": 60.0,
    },
    {
        "parameter": "capabilityMultiplier",
        "label": "能力倍率",
        "mode": "relative",
        "low": 0.95,
        "high": 1.05,
        "floor": 0.2,
        "ceiling": 3.0,
    },
    {
        "parameter": "subjectiveTimeExpansion",
        "label": "主观时间扩展",
        "mode": "absolute",
        "low": -0.05,
        "high": 0.05,
        "floor": 0.0,
        "ceiling": 2.0,
    },
    {
        "parameter": "levProgressRate",
        "label": "LEV 进度率",
        "mode": "absolute",
        "low": -0.08,
        "high": 0.08,
        "floor": 0.0,
        "ceiling": 2.0,
    },
    {
        "parameter": "riskTailPenalty",
        "label": "尾部风险扣减",
        "mode": "absolute",
        "low": -0.03,
        "high": 0.03,
        "floor": 0.0,
        "ceiling": 1.0,
    },
]


def clamp(value: float, floor: float, ceiling: float) -> float:
    return max(floor, min(ceiling, value))


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def baseline_references(config: dict[str, Any]) -> tuple[float, float]:
    baseline_scenario = next(
        (row for row in config["scenarios"] if row["id"] == "baseline"),
        config["scenarios"][0],
    )
    integrated = integrate_curve(
        make_age_grid(config["population"]),
        config["baselineHazard"],
        config["healthQuality"],
        baseline_scenario,
        config["population"],
    )
    return (
        float(integrated["expectedEffectiveTimeYears"]),
        float(integrated["expectedLifeAgeProxy"]),
    )


def perturb_value(original: float, rule: dict[str, Any], direction: str) -> float:
    delta = require_number(rule, direction)
    if rule["mode"] == "relative":
        value = original * delta
    else:
        value = original + delta
    return clamp(value, float(rule["floor"]), float(rule["ceiling"]))


def variant_label(rule: dict[str, Any], direction: str) -> str:
    sign = "下调" if direction == "low" else "上调"
    return f"{rule['label']}{sign}"


def build_nominal_map(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    baseline_effective, baseline_life_age = baseline_references(config)
    return {
        scenario["id"]: build_scenario_output(
            scenario,
            config,
            baseline_effective,
            baseline_life_age,
        )
        for scenario in config["scenarios"]
    }


def build_variant(
    config: dict[str, Any],
    scenario: dict[str, Any],
    rule: dict[str, Any],
    direction: str,
    baseline_effective: float,
    baseline_life_age: float,
) -> dict[str, Any]:
    variant_scenario = copy.deepcopy(scenario)
    parameter = str(rule["parameter"])
    original = require_number(variant_scenario, parameter)
    adjusted = perturb_value(original, rule, direction)
    variant_scenario[parameter] = adjusted
    variant_scenario["id"] = f"{scenario['id']}::{parameter}::{direction}"
    variant_scenario["label"] = f"{scenario['label']} / {variant_label(rule, direction)}"
    variant_scenario["description"] = (
        f"Synthetic sensitivity variant. {parameter} changed from {original:.6g} to {adjusted:.6g}."
    )
    output = build_scenario_output(
        variant_scenario,
        config,
        baseline_effective,
        baseline_life_age,
    )
    metrics = output["metrics"]
    return {
        "scenarioId": scenario["id"],
        "scenarioLabel": scenario["label"],
        "variantId": variant_scenario["id"],
        "parameter": parameter,
        "parameterLabel": rule["label"],
        "direction": direction,
        "mode": rule["mode"],
        "nominalValue": round(original, 6),
        "variantValue": round(adjusted, 6),
        "metrics": {
            "expectedLifeAgeProxy": metrics["expectedLifeAgeProxy"],
            "expectedEffectiveTimeYears": metrics["expectedEffectiveTimeYears"],
            "expectedEffectiveTimeGainYears": metrics["expectedEffectiveTimeGainYears"],
            "healthspanAgeProxy": metrics["healthspanAgeProxy"],
            "survivalAt80": metrics["survivalAt80"],
            "survivalAt100": metrics["survivalAt100"],
            "levRatio": metrics["levRatio"],
            "optionValue": metrics["optionValue"],
            "riskTailPenalty": metrics["riskTailPenalty"],
            "thresholdStatus": metrics["thresholdStatus"],
            "openBoundary": metrics["openBoundary"],
        },
    }


def delta(value: float, nominal: float) -> float:
    return round(value - nominal, 6)


def attach_deltas(
    rows: list[dict[str, Any]],
    nominal_map: dict[str, dict[str, Any]],
) -> None:
    for row in rows:
        nominal_metrics = nominal_map[row["scenarioId"]]["metrics"]
        metrics = row["metrics"]
        row["delta"] = {
            "expectedLifeAgeProxy": delta(
                float(metrics["expectedLifeAgeProxy"]),
                float(nominal_metrics["expectedLifeAgeProxy"]),
            ),
            "expectedEffectiveTimeYears": delta(
                float(metrics["expectedEffectiveTimeYears"]),
                float(nominal_metrics["expectedEffectiveTimeYears"]),
            ),
            "expectedEffectiveTimeGainYears": delta(
                float(metrics["expectedEffectiveTimeGainYears"]),
                float(nominal_metrics["expectedEffectiveTimeGainYears"]),
            ),
            "healthspanAgeProxy": delta(
                float(metrics["healthspanAgeProxy"]),
                float(nominal_metrics["healthspanAgeProxy"]),
            ),
            "survivalAt100": delta(
                float(metrics["survivalAt100"]),
                float(nominal_metrics["survivalAt100"]),
            ),
            "levRatio": delta(
                float(metrics["levRatio"]),
                float(nominal_metrics["levRatio"]),
            ),
            "optionValue": delta(
                float(metrics["optionValue"]),
                float(nominal_metrics["optionValue"]),
            ),
        }


def summarize_stability(
    rows: list[dict[str, Any]],
    nominal_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    scenario_ids = sorted({row["scenarioId"] for row in rows})
    for scenario_id in scenario_ids:
        scenario_rows = [row for row in rows if row["scenarioId"] == scenario_id]
        nominal_metrics = nominal_map[scenario_id]["metrics"]
        effective_values = [
            float(row["metrics"]["expectedEffectiveTimeYears"]) for row in scenario_rows
        ]
        life_values = [float(row["metrics"]["expectedLifeAgeProxy"]) for row in scenario_rows]
        threshold_values = {bool(row["metrics"]["openBoundary"]) for row in scenario_rows}
        threshold_values.add(bool(nominal_metrics["openBoundary"]))
        most_sensitive = max(
            scenario_rows,
            key=lambda row: abs(float(row["delta"]["expectedEffectiveTimeYears"])),
        )
        summaries.append(
            {
                "scenarioId": scenario_id,
                "scenarioLabel": nominal_map[scenario_id]["label"],
                "nominalOpenBoundary": bool(nominal_metrics["openBoundary"]),
                "openBoundaryStable": len(threshold_values) == 1,
                "effectiveTimeRange": {
                    "min": round(min(effective_values), 3),
                    "max": round(max(effective_values), 3),
                    "width": round(max(effective_values) - min(effective_values), 3),
                },
                "lifeAgeRange": {
                    "min": round(min(life_values), 3),
                    "max": round(max(life_values), 3),
                    "width": round(max(life_values) - min(life_values), 3),
                },
                "mostSensitiveParameter": most_sensitive["parameter"],
                "mostSensitiveDirection": most_sensitive["direction"],
                "maxEffectiveTimeDelta": round(
                    abs(float(most_sensitive["delta"]["expectedEffectiveTimeYears"])),
                    6,
                ),
            }
        )
    return summaries


def build_sensitivity_output(config: dict[str, Any], input_path: Path, model_path: Path) -> dict[str, Any]:
    validate_config(config)
    baseline_effective, baseline_life_age = baseline_references(config)
    nominal_map = build_nominal_map(config)
    rows: list[dict[str, Any]] = []
    for scenario in config["scenarios"]:
        for rule in PERTURBATION_PLAN:
            for direction in ("low", "high"):
                rows.append(
                    build_variant(
                        config,
                        scenario,
                        rule,
                        direction,
                        baseline_effective,
                        baseline_life_age,
                    )
                )
    attach_deltas(rows, nominal_map)
    return {
        "schemaVersion": "human-infra.life-path-sensitivity.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": {
            "path": str(input_path.relative_to(REPO_ROOT)),
            "sha256": sha256_file(input_path),
        },
        "sourceModel": {
            "path": str(model_path.relative_to(REPO_ROOT)),
            "sha256": sha256_file(model_path) if model_path.exists() else None,
        },
        "analysisBoundary": {
            "modelClass": "synthetic one-factor-at-a-time sensitivity analysis",
            "evidenceBoundary": "Synthetic toy model only; no real cohort, calibration, validation, causal effect, or individual prediction is claimed.",
            "nonUses": [
                "individual death-date prediction",
                "medical advice",
                "treatment selection",
                "claims that any parameter value is empirically estimated",
                "claims that scenario ordering is stable outside this synthetic toy model",
            ],
            "upgradeGate": "A calibrated sensitivity report requires governed cohort extraction, exact endpoint definitions, missingness tables, calibration diagnostics, external validation, and prespecified perturbation ranges.",
        },
        "perturbationPlan": PERTURBATION_PLAN,
        "nominalScenarioHashes": {
            scenario_id: sha256_json(nominal)
            for scenario_id, nominal in sorted(nominal_map.items())
        },
        "results": rows,
        "stabilitySummary": summarize_stability(rows, nominal_map),
        "sanityChecks": {
            "resultCount": len(rows),
            "scenarioCount": len(config["scenarios"]),
            "parameterCount": len(PERTURBATION_PLAN),
            "directions": ["low", "high"],
            "deathDateSuppressed": True,
            "individualPredictionSuppressed": True,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    model_path = args.model.resolve()
    output_path = args.out.resolve()
    output = build_sensitivity_output(load_json(input_path), input_path, model_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {output_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
