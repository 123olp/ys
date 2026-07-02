#!/usr/bin/env python3
"""Validate the NHATS pre-outcome aggregation protocol."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
MANUAL_DIR = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
)
DEFAULT_PROTOCOL = MANUAL_DIR / "life_path_nhats_preoutcome_aggregation_protocol.json"
DEFAULT_FIRST_ESTIMAND_PROTOCOL = (
    MANUAL_DIR / "life_path_nhats_first_estimand_protocol.json"
)
DEFAULT_L2_ADMISSION_REGISTER = (
    MANUAL_DIR / "life_path_nhats_l2_variable_family_admission_register.json"
)
DEFAULT_VARIABLE_CONFIRMATION_MATRIX = (
    MANUAL_DIR / "life_path_nhats_variable_confirmation_matrix.json"
)
DEFAULT_COHORT_FLOW_ENDPOINT_PROTOCOL = (
    MANUAL_DIR / "life_path_nhats_cohort_flow_endpoint_protocol.json"
)
DEFAULT_SURVEY_DESIGN_PROTOCOL = MANUAL_DIR / "life_path_nhats_survey_design_protocol.json"
DEFAULT_DISCLOSURE_CONTROL_POLICY = (
    MANUAL_DIR / "life_path_nhats_disclosure_control_policy.json"
)
DEFAULT_OUT = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-preoutcome-aggregation-validation.json"
)

REQUIRED_RULE_IDS = {
    "AGG-01-freeze-time-zero",
    "AGG-02-freeze-denominator",
    "AGG-03-separate-route-classes",
    "AGG-04-separate-negative-codes",
    "AGG-05-l2-family-only",
    "AGG-06-unweighted-diagnostics-only",
    "AGG-07-disclosure-first",
    "AGG-08-no-calibration-or-individual-use",
}
REQUIRED_TEST_CASES = {
    "SYN-AGG-ALLOW-001-rule-freeze-only",
    "SYN-AGG-BLOCK-002-post-outcome-selection",
    "SYN-AGG-BLOCK-003-row-level-output",
    "SYN-AGG-BLOCK-004-small-cell-unsuppressed",
    "SYN-AGG-BLOCK-005-weighted-before-design",
    "SYN-AGG-BLOCK-006-calibration-or-individual-use",
    "SYN-AGG-BLOCK-007-real-aggregation-before-gates",
}
REQUIRED_FALSE_DECISIONS = {
    "containsRealNhatsData",
    "exactVariablesConfirmed",
    "colecticaValueLabelsConfirmed",
    "governedDataAccessReady",
    "realAggregationAllowed",
    "routeClassificationAllowed",
    "weightedAggregationAllowed",
    "publicExportAllowed",
    "l4AdmissionAllowed",
    "calibrationAllowed",
    "individualPredictionAllowed",
}
REQUIRED_TRUE_DECISIONS = {
    "preOutcomeAggregationRulesFrozen",
    "syntheticRuleValidationAllowed",
}
PROHIBITED_KEYS = {
    "rowLevelData",
    "rawNhatsData",
    "deathDate",
    "individualDeathDate",
    "predictedDeathDate",
    "hazardRatio",
    "coefficient",
    "calibratedRisk",
}


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


def repo_rel(path: Path) -> str:
    return str(path.resolve().relative_to(REPO_ROOT))


def collect_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(collect_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(collect_keys(child))
    return keys


def row_ids(rows: Any, key: str) -> set[str]:
    if not isinstance(rows, list):
        return set()
    return {
        str(row[key])
        for row in rows
        if isinstance(row, dict) and isinstance(row.get(key), str)
    }


def add_check(checks: list[dict[str, Any]], check_id: str, passed: bool, detail: str) -> None:
    checks.append({"id": check_id, "status": "PASS" if passed else "FAIL", "detail": detail})


def summarize(checks: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "pass": sum(1 for check in checks if check["status"] == "PASS"),
        "fail": sum(1 for check in checks if check["status"] == "FAIL"),
    }


def validate_case(case: dict[str, Any]) -> tuple[str, list[str]]:
    reasons: list[str] = []
    if case.get("containsRealNhatsData") is not False:
        reasons.append("containsRealNhatsData must be false")
    if case.get("containsRowLevelData") is not False:
        reasons.append("containsRowLevelData must be false")
    if case.get("preOutcomeOnly") is not True:
        reasons.append("preOutcomeOnly must be true")
    if case.get("postOutcomeVariableSelectionRequested") is not False:
        reasons.append("postOutcomeVariableSelectionRequested must be false")
    if case.get("realAggregationRequested") is not False:
        reasons.append("realAggregationRequested must be false until G3-G7 pass")
    if case.get("weightedEstimateRequested") is not False:
        reasons.append("weightedEstimateRequested must be false until survey-design gates pass")
    if case.get("calibrationRequested") is not False:
        reasons.append("calibrationRequested must be false")
    if case.get("individualPredictionRequested") is not False:
        reasons.append("individualPredictionRequested must be false")
    if case.get("allAggregationRulesReferenced") is not True:
        reasons.append("allAggregationRulesReferenced must be true")

    cells = case.get("disclosureCells", [])
    if not isinstance(cells, list):
        reasons.append("disclosureCells must be a list")
    else:
        for index, cell in enumerate(cells):
            if not isinstance(cell, dict):
                reasons.append(f"disclosureCells[{index}] must be an object")
                continue
            count = cell.get("count")
            if not isinstance(count, int) or count < 0:
                reasons.append(f"disclosureCells[{index}].count must be a non-negative integer")
                continue
            if (
                case.get("publicExportRequested") is True
                and count < 5
                and cell.get("suppressed") is not True
            ):
                reasons.append(f"disclosureCells[{index}] count below 5 is not suppressed")

    decision = "allow-l2-rule-freeze" if not reasons else "block-real-aggregation"
    return decision, reasons


def validate_protocol(
    protocol: dict[str, Any],
    first_estimand: dict[str, Any],
    l2_register: dict[str, Any],
    matrix: dict[str, Any],
    cohort_flow: dict[str, Any],
    survey_design: dict[str, Any],
    disclosure_policy: dict[str, Any],
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    add_check(
        checks,
        "schema-version",
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-preoutcome-aggregation-protocol.v1",
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )
    add_check(
        checks,
        "protocol-identity",
        protocol.get("sourceId") == "nhats"
        and protocol.get("status")
        == "protocol-only-preoutcome-rules-frozen-l4-blocked"
        and protocol.get("targetEstimand", {}).get("id")
        == first_estimand.get("estimand", {}).get("id")
        and protocol.get("targetEstimand", {}).get("admissionLevel")
        == "L2-preoutcome-aggregation-rules-only",
        "protocol must bind NHATS first estimand and stay L2-only",
    )

    upstream = protocol.get("upstreamBindings")
    required_upstream = {
        "firstEstimandProtocolPath",
        "l2VariableFamilyAdmissionRegisterPath",
        "variableConfirmationMatrixPath",
        "cohortFlowEndpointProtocolPath",
        "surveyDesignProtocolPath",
        "disclosureControlPolicyPath",
    }
    add_check(
        checks,
        "upstream-bindings-present",
        isinstance(upstream, dict) and required_upstream.issubset(set(upstream)),
        f"missing={sorted(required_upstream - set(upstream or {}))}",
    )

    decision = protocol.get("currentDecision")
    decision_ok = isinstance(decision, dict)
    if decision_ok:
        for field in REQUIRED_TRUE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is True
        for field in REQUIRED_FALSE_DECISIONS:
            decision_ok = decision_ok and decision.get(field) is False
    add_check(
        checks,
        "current-decision-boundary",
        decision_ok,
        "pre-outcome rules may be frozen, while real data, weighted aggregation, L4, calibration and individual prediction remain false",
    )

    l2_decision = l2_register.get("currentDecision")
    upstream_boundaries_ok = (
        isinstance(l2_decision, dict)
        and l2_decision.get("l2CandidateFamiliesMapped") is True
        and l2_decision.get("l4AdmissionAllowed") is False
        and matrix.get("currentDecision", {}).get("exactVariablesReady") is False
        and cohort_flow.get("currentDecision", {}).get("endpointRoutingRunnable") is False
        and survey_design.get("currentDecision", {}).get("weightedCountsAllowed") is False
        and disclosure_policy.get("currentDecision", {}).get("publicExportAllowed") is False
    )
    add_check(
        checks,
        "upstream-boundaries-inherited",
        upstream_boundaries_ok,
        "protocol must inherit L2-only variable mapping, unconfirmed variables, blocked endpoint routing, blocked weighted counts and blocked public export",
    )

    rule_ids = row_ids(protocol.get("aggregationRules"), "ruleId")
    add_check(
        checks,
        "aggregation-rules-complete",
        rule_ids == REQUIRED_RULE_IDS,
        f"missing={sorted(REQUIRED_RULE_IDS - rule_ids)} extra={sorted(rule_ids - REQUIRED_RULE_IDS)}",
    )
    rule_boundaries_ok = True
    for rule in protocol.get("aggregationRules", []):
        if not isinstance(rule, dict):
            rule_boundaries_ok = False
            continue
        if not isinstance(rule.get("blocksIfViolated"), list) or not rule["blocksIfViolated"]:
            rule_boundaries_ok = False
    add_check(
        checks,
        "aggregation-rules-have-blockers",
        rule_boundaries_ok,
        "every aggregation rule must include explicit blocking conditions",
    )

    required_before = protocol.get("requiredBeforeRealAggregation")
    required_before_ok = isinstance(required_before, list) and len(required_before) >= 8
    add_check(
        checks,
        "required-before-real-aggregation",
        required_before_ok,
        "protocol must enumerate gated evidence required before real aggregation",
    )

    case_ids = row_ids(protocol.get("syntheticTestCases"), "caseId")
    add_check(
        checks,
        "synthetic-test-cases-complete",
        case_ids == REQUIRED_TEST_CASES,
        f"missing={sorted(REQUIRED_TEST_CASES - case_ids)} extra={sorted(case_ids - REQUIRED_TEST_CASES)}",
    )

    case_rows: list[dict[str, Any]] = []
    for case in protocol.get("syntheticTestCases", []):
        if not isinstance(case, dict):
            case_rows.append(
                {
                    "caseId": "<invalid>",
                    "expectedDecision": "<invalid>",
                    "observedDecision": "block-real-aggregation",
                    "reasons": ["case must be an object"],
                    "status": "FAIL",
                }
            )
            continue
        observed, reasons = validate_case(case)
        expected = case.get("expectedDecision")
        case_rows.append(
            {
                "caseId": case.get("caseId"),
                "expectedDecision": expected,
                "observedDecision": observed,
                "reasons": reasons,
                "status": "PASS" if observed == expected else "FAIL",
            }
        )
    add_check(
        checks,
        "synthetic-case-decisions",
        all(row["status"] == "PASS" for row in case_rows),
        "synthetic cases must allow only L2 rule-freeze and block unsafe aggregation attempts",
    )

    summary = protocol.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("aggregationRuleCount") == len(REQUIRED_RULE_IDS)
        and summary.get("syntheticTestCaseCount") == len(REQUIRED_TEST_CASES)
        and summary.get("preOutcomeRulesFrozen") is True
        and summary.get("realAggregationAllowed") is False
        and summary.get("weightedAggregationAllowed") is False
        and summary.get("l4Admissions") == 0
        and summary.get("calibrationAllowed") is False
        and summary.get("individualUseAllowed") is False
    )
    add_check(
        checks,
        "summary-boundary",
        summary_ok,
        "summary must freeze L2 rules while preserving zero real, weighted, L4, calibration and individual use",
    )

    prohibited_keys_seen = sorted(collect_keys(protocol) & PROHIBITED_KEYS)
    add_check(
        checks,
        "prohibited-keys-absent",
        not prohibited_keys_seen,
        f"prohibitedKeysPresent={prohibited_keys_seen}",
    )

    validate_protocol.case_rows = case_rows  # type: ignore[attr-defined]
    return checks


def build_report(
    protocol_path: Path,
    first_estimand_path: Path,
    l2_register_path: Path,
    matrix_path: Path,
    cohort_flow_path: Path,
    survey_design_path: Path,
    disclosure_policy_path: Path,
) -> dict[str, Any]:
    protocol = load_json(protocol_path)
    first_estimand = load_json(first_estimand_path)
    l2_register = load_json(l2_register_path)
    matrix = load_json(matrix_path)
    cohort_flow = load_json(cohort_flow_path)
    survey_design = load_json(survey_design_path)
    disclosure_policy = load_json(disclosure_policy_path)
    checks = validate_protocol(
        protocol,
        first_estimand,
        l2_register,
        matrix,
        cohort_flow,
        survey_design,
        disclosure_policy,
    )
    case_rows = getattr(validate_protocol, "case_rows", [])
    summary = summarize(checks)
    return {
        "schemaVersion": "human-infra.life-path-nhats-preoutcome-aggregation-validation.v1",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "protocolPath": repo_rel(protocol_path),
        "protocolSha256": sha256_file(protocol_path),
        "firstEstimandProtocolPath": repo_rel(first_estimand_path),
        "firstEstimandProtocolSha256": sha256_file(first_estimand_path),
        "l2VariableFamilyAdmissionRegisterPath": repo_rel(l2_register_path),
        "l2VariableFamilyAdmissionRegisterSha256": sha256_file(l2_register_path),
        "variableConfirmationMatrixPath": repo_rel(matrix_path),
        "variableConfirmationMatrixSha256": sha256_file(matrix_path),
        "cohortFlowEndpointProtocolPath": repo_rel(cohort_flow_path),
        "cohortFlowEndpointProtocolSha256": sha256_file(cohort_flow_path),
        "surveyDesignProtocolPath": repo_rel(survey_design_path),
        "surveyDesignProtocolSha256": sha256_file(survey_design_path),
        "disclosureControlPolicyPath": repo_rel(disclosure_policy_path),
        "disclosureControlPolicySha256": sha256_file(disclosure_policy_path),
        "overallStatus": "PASS" if summary["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summary,
        "aggregationRuleCount": len(protocol.get("aggregationRules", [])),
        "syntheticCaseRows": case_rows,
        "boundary": {
            "preOutcomeAggregationRulesFrozen": protocol.get("currentDecision", {}).get(
                "preOutcomeAggregationRulesFrozen"
            ),
            "syntheticRuleValidationAllowed": protocol.get("currentDecision", {}).get(
                "syntheticRuleValidationAllowed"
            ),
            "realAggregationAllowed": protocol.get("currentDecision", {}).get(
                "realAggregationAllowed"
            ),
            "weightedAggregationAllowed": protocol.get("currentDecision", {}).get(
                "weightedAggregationAllowed"
            ),
            "l4AdmissionAllowed": protocol.get("currentDecision", {}).get(
                "l4AdmissionAllowed"
            ),
            "calibrationAllowed": protocol.get("currentDecision", {}).get(
                "calibrationAllowed"
            ),
            "individualPredictionAllowed": protocol.get("currentDecision", {}).get(
                "individualPredictionAllowed"
            ),
        },
        "note": "This validation proves only that pre-outcome L2 aggregation rules are frozen and unsafe synthetic envelopes are blocked. It does not validate real NHATS extraction, route classification, weighted estimates, calibration, public export or individual prediction.",
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate NHATS pre-outcome aggregation protocol."
    )
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument(
        "--first-estimand-protocol",
        type=Path,
        default=DEFAULT_FIRST_ESTIMAND_PROTOCOL,
    )
    parser.add_argument(
        "--l2-variable-family-admission-register",
        type=Path,
        default=DEFAULT_L2_ADMISSION_REGISTER,
    )
    parser.add_argument(
        "--variable-confirmation-matrix",
        type=Path,
        default=DEFAULT_VARIABLE_CONFIRMATION_MATRIX,
    )
    parser.add_argument(
        "--cohort-flow-endpoint-protocol",
        type=Path,
        default=DEFAULT_COHORT_FLOW_ENDPOINT_PROTOCOL,
    )
    parser.add_argument(
        "--survey-design-protocol",
        type=Path,
        default=DEFAULT_SURVEY_DESIGN_PROTOCOL,
    )
    parser.add_argument(
        "--disclosure-control-policy",
        type=Path,
        default=DEFAULT_DISCLOSURE_CONTROL_POLICY,
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        args.protocol.resolve(),
        args.first_estimand_protocol.resolve(),
        args.l2_variable_family_admission_register.resolve(),
        args.variable_confirmation_matrix.resolve(),
        args.cohort_flow_endpoint_protocol.resolve(),
        args.survey_design_protocol.resolve(),
        args.disclosure_control_policy.resolve(),
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {repo_rel(args.out.resolve())}")
    print(f"status={report['overallStatus']} checks={report['summary']}")
    return 0 if report["overallStatus"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
