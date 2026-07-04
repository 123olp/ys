#!/usr/bin/env python3
"""Validate synthetic NHANES public-use LMF publication reliability criteria."""

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
    / "life_path_nhanes_public_lmf_effective_sample_ci_publication_policy.json"
)
DEFAULT_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhanes_public_lmf_effective_sample_ci_publication_test_cases.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhanes-public-lmf-effective-sample-ci-publication-validation.json"
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
        "human-infra.nhanes-public-lmf-effective-sample-ci-publication-policy.v1"
    ):
        reasons.append("policy schemaVersion mismatch")
    if policy.get("sourceId") != "nhanes-public-lmf-2017-2018":
        reasons.append("policy sourceId must be nhanes-public-lmf-2017-2018")
    if policy.get("status") != "synthetic-publication-criteria-policy-ready-no-real-output":
        reasons.append("policy status mismatch")

    decision = policy.get("currentDecision")
    required_false = {
        "realWeightedOutputPresent",
        "realConfidenceIntervalsPresent",
        "publicRealOutputExportAllowed",
        "calibrationAllowed",
        "individualPredictionAllowed",
    }
    if not isinstance(decision, dict):
        reasons.append("policy currentDecision must be an object")
    else:
        for field in sorted(required_false):
            if decision.get(field) is not False:
                reasons.append(f"policy currentDecision.{field} must be false")
        if decision.get("syntheticPublicationCriteriaValidationAllowed") is not True:
            reasons.append(
                "policy currentDecision.syntheticPublicationCriteriaValidationAllowed must be true"
            )

    rules = policy.get("rules")
    if not isinstance(rules, dict):
        reasons.append("policy rules must be an object")
        return reasons
    if rules.get("syntheticOnlyUntilRealOutputImplementationGate") is not True:
        reasons.append("policy must stay synthetic-only until real output implementation gate")
    if rules.get("aggregateOnly") is not True:
        reasons.append("policy rules.aggregateOnly must be true")
    if rules.get("minimumSyntheticDenominatorClass") != "threshold-met":
        reasons.append("policy minimumSyntheticDenominatorClass mismatch")
    if rules.get("minimumSyntheticEffectiveSampleSizeClass") != "threshold-met":
        reasons.append("policy minimumSyntheticEffectiveSampleSizeClass mismatch")
    if rules.get("minimumDomainDof") != 8:
        reasons.append("policy minimumDomainDof must be 8")
    if rules.get("confidenceIntervalWidthRequired") is not True:
        reasons.append("policy must require confidence interval width review")
    if rules.get("relativeStandardErrorReviewRequired") is not True:
        reasons.append("policy must require relative standard error review")

    allowed = as_set(rules.get("allowedOutputTypes"))
    required_allowed = {
        "synthetic_effective_sample_ci_publication_review",
        "synthetic_reliability_standards_report",
    }
    missing_allowed = sorted(required_allowed - allowed)
    if missing_allowed:
        reasons.append(f"policy missing allowed output types: {missing_allowed}")

    forbidden = as_set(rules.get("forbiddenOutputTypes"))
    for output_type in (
        "real_public_weighted_domain_rates",
        "real_public_design_based_intervals",
        "individual_death_date_prediction",
    ):
        if output_type not in forbidden:
            reasons.append(f"policy missing forbidden output type: {output_type}")

    required_fields = as_set(rules.get("requiredReportFields"))
    for field in (
        "schemaVersion",
        "sourceId",
        "outputId",
        "outputType",
        "containsRealNhanesData",
        "containsRowLevelData",
        "containsIdentifiers",
        "containsRealConfidenceIntervals",
        "publicExportRequested",
        "publicAiUploadRequested",
        "publicationReviewStatus",
        "cells",
    ):
        if field not in required_fields:
            reasons.append(f"policy missing required report field: {field}")

    required_cell_fields = as_set(rules.get("cellFields"))
    for field in (
        "id",
        "suppressed",
        "syntheticDenominatorClass",
        "syntheticEffectiveSampleSizeClass",
        "relativeStandardErrorClass",
        "confidenceIntervalWidthClass",
        "domainDof",
        "publicationDecision",
    ):
        if field not in required_cell_fields:
            reasons.append(f"policy missing required cell field: {field}")

    source_trace = as_set(policy.get("sourceTrace"))
    for source_url in (
        "https://wwwn.cdc.gov/nchs/nhanes/tutorials/reliabilityofestimates.aspx",
        "https://wwwn.cdc.gov/nchs/nhanes/tutorials/varianceestimation.aspx",
        "https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf",
        "https://www.cdc.gov/nchs/data/series/sr_02/sr02-200.pdf",
    ):
        if source_url not in source_trace:
            reasons.append(f"policy missing sourceTrace URL: {source_url}")
    return reasons


def validate_cell(cell: dict[str, Any], index: int, output: dict[str, Any], policy: dict[str, Any]) -> list[str]:
    rules = policy.get("rules", {})
    reasons: list[str] = []
    required_cell_fields = as_set(rules.get("cellFields"))
    missing_cell_fields = sorted(field for field in required_cell_fields if field not in cell)
    if missing_cell_fields:
        return [f"cell[{index}] missing fields: {missing_cell_fields}"]

    allowed_class_values = rules.get("allowedClassValues", {})
    for field, allowed_values in allowed_class_values.items():
        if isinstance(allowed_values, list) and cell.get(field) not in set(allowed_values):
            reasons.append(f"cell[{index}].{field} has unsupported value {cell.get(field)!r}")

    publication_decisions = set(rules.get("publicationDecisionVocabulary", []))
    if cell.get("publicationDecision") not in publication_decisions:
        reasons.append(f"cell[{index}].publicationDecision is unsupported")

    domain_dof = cell.get("domainDof")
    if not isinstance(domain_dof, int) or domain_dof < 0:
        reasons.append(f"cell[{index}].domainDof must be a non-negative integer")
        return reasons

    public_export = output.get("publicExportRequested") is True
    suppressed = cell.get("suppressed") is True
    if public_export and not suppressed:
        if cell.get("syntheticDenominatorClass") != rules.get("minimumSyntheticDenominatorClass"):
            reasons.append(f"cell[{index}] synthetic denominator class is not publication-ready")
        if cell.get("syntheticEffectiveSampleSizeClass") != rules.get(
            "minimumSyntheticEffectiveSampleSizeClass"
        ):
            reasons.append(f"cell[{index}] synthetic effective sample size class is not publication-ready")
        if cell.get("relativeStandardErrorClass") in {"unacceptable", "not-computed-real"}:
            reasons.append(f"cell[{index}] relative standard error class blocks publication")
        if cell.get("confidenceIntervalWidthClass") in {
            "unacceptable",
            "computed-real-public",
            "not-computed-real",
        }:
            reasons.append(f"cell[{index}] confidence interval width class blocks publication")
        if domain_dof < int(rules.get("minimumDomainDof", 8)):
            reasons.append(f"cell[{index}] domainDof is below publication review threshold")
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

    if output.get("containsRealNhanesData") is not False:
        reasons.append("containsRealNhanesData must be false")
    if output.get("containsRowLevelData") is not False:
        reasons.append("containsRowLevelData must be false")
    if output.get("containsIdentifiers") is not False:
        reasons.append("containsIdentifiers must be false")
    if output.get("containsRealConfidenceIntervals") is not False:
        reasons.append("containsRealConfidenceIntervals must be false")
    if output.get("publicAiUploadRequested") is not False:
        reasons.append("publicAiUploadRequested must be false")
    if output.get("publicationReviewStatus") != "synthetic-publication-criteria-only":
        reasons.append("publicationReviewStatus must be synthetic-publication-criteria-only")

    observed_prohibited_keys = sorted(collect_keys(output) & prohibited_keys)
    if observed_prohibited_keys:
        reasons.append(f"prohibited keys present: {observed_prohibited_keys}")

    cells = output.get("cells")
    if not isinstance(cells, list):
        reasons.append("cells must be a list")
    else:
        for index, cell in enumerate(cells):
            if not isinstance(cell, dict):
                reasons.append(f"cell[{index}] must be an object")
                continue
            reasons.extend(validate_cell(cell, index, output, policy))

    decision = "allow-publication-shape" if not reasons else "block-publication-shape"
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
        "human-infra.nhanes-public-lmf-effective-sample-ci-publication-test-cases.v1"
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
            "realConfidenceIntervalsComputed": False,
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
                observed, reasons = "block-publication-shape", ["case must be an object"]
                expected = "block-publication-shape"
                case_id = "invalid-case"
            else:
                output = case.get("output")
                expected = case.get("expectedDecision")
                case_id = case.get("id")
                if not isinstance(output, dict):
                    observed, reasons = "block-publication-shape", ["case output must be an object"]
                else:
                    observed, reasons = validate_case(output, policy)
            if policy_reasons:
                observed = "block-publication-shape"
                reasons = [*reasons, *policy_reasons]
            if boundary_reasons:
                observed = "block-publication-shape"
                reasons = [*reasons, *boundary_reasons]
            status = "PASS" if observed == expected else "FAIL"
            if status == "FAIL":
                case_failures += 1
            if observed == "allow-publication-shape":
                allowed_count += 1
            if observed == "block-publication-shape":
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
        "schemaVersion": "human-infra.nhanes-public-lmf-effective-sample-ci-publication-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "policyPath": repo_rel(policy_path),
        "policySha256": sha256_file(policy_path),
        "testCasesPath": repo_rel(test_cases_path),
        "testCasesSha256": sha256_file(test_cases_path),
        "overallStatus": overall,
        "boundary": {
            "containsRealNhanesData": False,
            "containsSyntheticOnly": True,
            "publicationCriteriaProofOnly": True,
            "weightedDomainOutputImplemented": False,
            "realConfidenceIntervalsComputed": False,
            "publicWeightedDomainOutputAllowed": False,
            "calibrationAllowed": False,
            "individualPredictionAllowed": False,
            "note": "This report validates synthetic NHANES publication reliability criteria only; it does not validate real weighted rates, intervals, calibration, causal inference, clinical use or individual prediction.",
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
