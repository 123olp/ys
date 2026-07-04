#!/usr/bin/env python3
"""Validate synthetic NHANES public-use LMF weighted-output implementation preflight."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
DEFAULT_POLICY = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_weighted_output_implementation_preflight_policy.json"
)
DEFAULT_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_weighted_output_implementation_preflight_test_cases.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-weighted-output-implementation-preflight-validation.json"
)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def as_set(value: Any) -> set[str]:
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value}


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


def validate_policy(policy: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if policy.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-policy.v1"
    ):
        reasons.append("policy schemaVersion mismatch")
    if policy.get("sourceId") != "nhanes-public-lmf-2017-2018":
        reasons.append("policy sourceId must be nhanes-public-lmf-2017-2018")
    if policy.get("status") != "synthetic-implementation-preflight-ready-no-real-weighted-output":
        reasons.append("policy status mismatch")

    decision = policy.get("currentDecision")
    required_false = {
        "realWeightedOutputImplemented",
        "realWeightedOutputPresent",
        "realDesignBasedIntervalsPresent",
        "publicRealOutputExportAllowed",
        "rowLevelExportAllowed",
        "identifierExportAllowed",
        "publicAiUploadAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    }
    if not isinstance(decision, dict):
        reasons.append("policy currentDecision must be an object")
    else:
        for field in sorted(required_false):
            if decision.get(field) is not False:
                reasons.append(f"policy currentDecision.{field} must be false")
        if decision.get("syntheticImplementationPreflightAllowed") is not True:
            reasons.append("policy currentDecision.syntheticImplementationPreflightAllowed must be true")

    rules = policy.get("rules")
    if not isinstance(rules, dict):
        reasons.append("policy rules must be an object")
        return reasons

    expected_values = {
        "requiredEstimatorBackend": "R survey",
        "requiredDesignFunction": "svydesign",
        "requiredDomainSubsettingFunction": "survey::subset",
        "requiredVarianceMethod": "Taylor linearization",
        "requiredWeightVariable": "WTMEC2YR",
        "requiredStrataVariable": "SDMVSTRA",
        "requiredPsuVariable": "SDMVPSU",
        "domainIndicatorTiming": "after design object creation",
    }
    for field, expected in expected_values.items():
        if rules.get(field) != expected:
            reasons.append(f"policy rules.{field} mismatch")

    expected_bools = {
        "syntheticOnlyUntilRealOutputImplementationGate": True,
        "aggregateOnly": True,
        "rowDropBeforeDesignAllowed": False,
        "rawRowPersistenceAllowed": False,
        "unweightedCountPublicOutputAllowed": False,
        "realConfidenceIntervalPublicOutputAllowed": False,
        "publicDisclosureReviewRequiredBeforeRealOutput": True,
        "effectiveSampleCiPublicationReviewRequiredBeforeRealOutput": True,
    }
    for field, expected in expected_bools.items():
        if rules.get(field) is not expected:
            reasons.append(f"policy rules.{field} must be {expected}")

    allowed = as_set(rules.get("allowedOutputTypes"))
    required_allowed = {
        "synthetic_weighted_output_implementation_preflight",
        "synthetic_estimator_pipeline_contract",
    }
    missing_allowed = sorted(required_allowed - allowed)
    if missing_allowed:
        reasons.append(f"policy missing allowed output types: {missing_allowed}")

    forbidden = as_set(rules.get("forbiddenOutputTypes"))
    for output_type in (
        "real_public_weighted_domain_rates",
        "real_public_design_based_intervals",
        "real_public_weighted_counts",
        "individual_death_date_prediction",
        "individual_risk_score",
    ):
        if output_type not in forbidden:
            reasons.append(f"policy missing forbidden output type: {output_type}")

    required_fields = as_set(rules.get("requiredReportFields"))
    for field in (
        "schemaVersion",
        "sourceId",
        "outputId",
        "outputType",
        "implementationStatus",
        "containsRealNhanesData",
        "containsRowLevelData",
        "containsIdentifiers",
        "containsRealWeightedRates",
        "containsRealDesignBasedIntervals",
        "containsUnweightedCounts",
        "publicExportRequested",
        "publicAiUploadRequested",
        "disclosureReviewStatus",
        "publicationReliabilityStatus",
        "estimatorPlan",
        "cells",
    ):
        if field not in required_fields:
            reasons.append(f"policy missing required report field: {field}")

    required_plan_fields = as_set(rules.get("requiredEstimatorPlanFields"))
    for field in (
        "estimatorBackend",
        "designFunction",
        "domainSubsettingFunction",
        "varianceMethod",
        "weightVariable",
        "strataVariable",
        "psuVariable",
        "domainIndicatorTiming",
        "rawRowsPersisted",
        "rowDropBeforeDesign",
        "publicDisclosureReviewRequired",
        "effectiveSampleCiPublicationReviewRequired",
    ):
        if field not in required_plan_fields:
            reasons.append(f"policy missing estimator plan field: {field}")

    source_trace = as_set(policy.get("sourceTrace"))
    for source_url in (
        "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
        "https://wwwn.cdc.gov/nchs/nhanes/tutorials/weighting.aspx",
        "https://wwwn.cdc.gov/nchs/nhanes/tutorials/reliabilityofestimates.aspx",
        "https://r-survey.r-forge.r-project.org/survey/html/subset.survey.design.html",
    ):
        if source_url not in source_trace:
            reasons.append(f"policy missing sourceTrace URL: {source_url}")

    return reasons


def validate_estimator_plan(output: dict[str, Any], policy: dict[str, Any]) -> list[str]:
    rules = policy.get("rules", {})
    plan = output.get("estimatorPlan")
    reasons: list[str] = []
    if not isinstance(plan, dict):
        return ["estimatorPlan must be an object"]

    required_fields = as_set(rules.get("requiredEstimatorPlanFields"))
    missing = sorted(field for field in required_fields if field not in plan)
    if missing:
        reasons.append(f"estimatorPlan missing fields: {missing}")

    expected_values = {
        "estimatorBackend": rules.get("requiredEstimatorBackend"),
        "designFunction": rules.get("requiredDesignFunction"),
        "domainSubsettingFunction": rules.get("requiredDomainSubsettingFunction"),
        "varianceMethod": rules.get("requiredVarianceMethod"),
        "weightVariable": rules.get("requiredWeightVariable"),
        "strataVariable": rules.get("requiredStrataVariable"),
        "psuVariable": rules.get("requiredPsuVariable"),
        "domainIndicatorTiming": rules.get("domainIndicatorTiming"),
    }
    for field, expected in expected_values.items():
        if plan.get(field) != expected:
            reasons.append(f"estimatorPlan.{field} must be {expected!r}")

    expected_bools = {
        "rawRowsPersisted": False,
        "rowDropBeforeDesign": False,
        "publicDisclosureReviewRequired": True,
        "effectiveSampleCiPublicationReviewRequired": True,
    }
    for field, expected in expected_bools.items():
        if plan.get(field) is not expected:
            reasons.append(f"estimatorPlan.{field} must be {expected}")

    return reasons


def validate_cell(cell: dict[str, Any], index: int, policy: dict[str, Any]) -> list[str]:
    rules = policy.get("rules", {})
    reasons: list[str] = []
    required_cell_fields = as_set(rules.get("cellFields"))
    missing = sorted(field for field in required_cell_fields if field not in cell)
    if missing:
        return [f"cell[{index}] missing fields: {missing}"]

    if cell.get("implementationDecision") not in set(rules.get("implementationDecisionVocabulary", [])):
        reasons.append(f"cell[{index}].implementationDecision is unsupported")
    for field in (
        "suppressionPolicyApplied",
        "domainDofReviewRequired",
        "effectiveSampleReviewRequired",
        "confidenceIntervalReviewRequired",
    ):
        if cell.get(field) is not True:
            reasons.append(f"cell[{index}].{field} must be true")
    return reasons


def validate_case(output: dict[str, Any], policy: dict[str, Any]) -> tuple[str, list[str]]:
    rules = policy.get("rules", {})
    allowed_output_types = as_set(rules.get("allowedOutputTypes"))
    forbidden_output_types = as_set(rules.get("forbiddenOutputTypes"))
    required_fields = as_set(rules.get("requiredReportFields"))
    prohibited_keys = as_set(rules.get("prohibitedKeys"))
    reasons: list[str] = []

    missing_fields = sorted(field for field in required_fields if field not in output)
    if missing_fields:
        reasons.append(f"missing required fields: {missing_fields}")

    if output.get("sourceId") != policy.get("sourceId"):
        reasons.append("sourceId does not match policy sourceId")
    output_type = output.get("outputType")
    if output_type not in allowed_output_types:
        reasons.append(f"outputType {output_type!r} is not allowed")
    if output_type in forbidden_output_types:
        reasons.append(f"outputType {output_type!r} is explicitly forbidden")

    required_false = {
        "containsRealNhanesData",
        "containsRowLevelData",
        "containsIdentifiers",
        "containsRealWeightedRates",
        "containsRealDesignBasedIntervals",
        "containsUnweightedCounts",
        "publicAiUploadRequested",
    }
    for field in sorted(required_false):
        if output.get(field) is not False:
            reasons.append(f"{field} must be false")
    if output.get("implementationStatus") != "synthetic-preflight-only":
        reasons.append("implementationStatus must be synthetic-preflight-only")
    if output.get("disclosureReviewStatus") != "not-real-output-preflight":
        reasons.append("disclosureReviewStatus must be not-real-output-preflight")
    if output.get("publicationReliabilityStatus") != "not-real-output-preflight":
        reasons.append("publicationReliabilityStatus must be not-real-output-preflight")

    observed_prohibited_keys = sorted(collect_keys(output) & prohibited_keys)
    if observed_prohibited_keys:
        reasons.append(f"prohibited keys present: {observed_prohibited_keys}")

    reasons.extend(validate_estimator_plan(output, policy))

    cells = output.get("cells")
    if not isinstance(cells, list):
        reasons.append("cells must be a list")
    else:
        for index, cell in enumerate(cells):
            if not isinstance(cell, dict):
                reasons.append(f"cell[{index}] must be an object")
                continue
            reasons.extend(validate_cell(cell, index, policy))

    decision = "allow-preflight-shape" if not reasons else "block-preflight-shape"
    return decision, reasons


def build_report(
    policy_path: Path,
    test_cases_path: Path,
    policy: dict[str, Any],
    test_cases: dict[str, Any],
) -> dict[str, Any]:
    policy_reasons = validate_policy(policy)
    boundary = test_cases.get("currentBoundary")
    boundary_reasons: list[str] = []
    if test_cases.get("schemaVersion") != (
        "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-test-cases.v1"
    ):
        boundary_reasons.append("test cases schemaVersion mismatch")
    if test_cases.get("sourceId") != policy.get("sourceId"):
        boundary_reasons.append("test cases sourceId must match policy")
    if not isinstance(boundary, dict):
        boundary_reasons.append("test cases currentBoundary must be an object")
    else:
        for field, expected in {
            "containsRealNhanesData": False,
            "containsSyntheticOnly": True,
            "weightedDomainOutputImplemented": False,
            "realWeightedRatesComputed": False,
            "realDesignBasedIntervalsComputed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
        }.items():
            if boundary.get(field) is not expected:
                boundary_reasons.append(f"test cases currentBoundary.{field} must be {expected}")

    case_rows: list[dict[str, Any]] = []
    cases = test_cases.get("cases")
    case_failures = 0
    allowed_count = 0
    blocked_count = 0
    if isinstance(cases, list):
        for case in cases:
            if not isinstance(case, dict):
                observed, reasons = "block-preflight-shape", ["case must be an object"]
                expected = "block-preflight-shape"
                case_id = "invalid-case"
            else:
                output = case.get("output")
                expected = case.get("expectedDecision")
                case_id = case.get("id")
                if not isinstance(output, dict):
                    observed, reasons = "block-preflight-shape", ["case output must be an object"]
                else:
                    observed, reasons = validate_case(output, policy)
            if policy_reasons:
                observed = "block-preflight-shape"
                reasons = [*reasons, *policy_reasons]
            if boundary_reasons:
                observed = "block-preflight-shape"
                reasons = [*reasons, *boundary_reasons]
            status = "PASS" if observed == expected else "FAIL"
            if status == "FAIL":
                case_failures += 1
            if observed == "allow-preflight-shape":
                allowed_count += 1
            if observed == "block-preflight-shape":
                blocked_count += 1
            case_rows.append(
                {
                    "id": case_id,
                    "expectedDecision": expected,
                    "observedDecision": observed,
                    "status": status,
                    "reasons": reasons,
                }
            )
    else:
        case_failures += 1

    case_count = len(cases) if isinstance(cases, list) else 0
    overall = (
        "PASS"
        if not policy_reasons
        and not boundary_reasons
        and case_count > 0
        and case_failures == 0
        and allowed_count > 0
        and blocked_count > 0
        else "FAIL"
    )
    return {
        "schemaVersion": "human-infra.nhanes-public-lmf-weighted-output-implementation-preflight-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "policyPath": repo_rel(policy_path),
        "policySha256": sha256_file(policy_path),
        "testCasesPath": repo_rel(test_cases_path),
        "testCasesSha256": sha256_file(test_cases_path),
        "overallStatus": overall,
        "boundary": {
            "containsRealNhanesData": False,
            "containsSyntheticOnly": True,
            "implementationPreflightOnly": True,
            "weightedDomainOutputImplemented": False,
            "realWeightedRatesComputed": False,
            "realDesignBasedIntervalsComputed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "note": "This report validates synthetic implementation preflight shape only; it does not implement or validate real NHANES weighted rates, intervals, calibration, causal inference, clinical use or individual prediction.",
        },
        "summary": {
            "caseCount": case_count,
            "pass": sum(1 for row in case_rows if row["status"] == "PASS"),
            "fail": case_failures,
            "allowedCount": allowed_count,
            "blockedCount": blocked_count,
            "policyIssueCount": len(policy_reasons),
            "boundaryIssueCount": len(boundary_reasons),
        },
        "cases": case_rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=DEFAULT_POLICY)
    parser.add_argument("--test-cases", type=Path, default=DEFAULT_TEST_CASES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    policy_path = args.policy.resolve()
    test_cases_path = args.test_cases.resolve()
    out_path = args.out.resolve()
    policy = load_json(policy_path)
    test_cases = load_json(test_cases_path)
    report = build_report(policy_path, test_cases_path, policy, test_cases)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {repo_rel(out_path)}")
    print(f"status={report['overallStatus']} cases={report['summary']}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
