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
DEFAULT_SENSITIVITY = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-sensitivity-analysis.json"
)
DEFAULT_READINESS = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_calibration_readiness.json"
)
DEFAULT_DATA_SOURCES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_data_source_candidates.json"
)
DEFAULT_SOURCE_CARDS = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "docs"
    / "life-path-data-source-cards.md"
)
DEFAULT_DATA_CARD_TEMPLATE = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "docs"
    / "life-path-data-card-template.md"
)
DEFAULT_NHATS_DATA_CARD = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "docs"
    / "life-path-data-card-nhats.md"
)
DEFAULT_NHATS_VARIABLE_DICTIONARY = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "docs"
    / "life-path-variable-dictionary-nhats.md"
)
DEFAULT_NHATS_EXTRACTION_MANIFEST = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "docs"
    / "life-path-extraction-manifest-nhats-draft.md"
)
DEFAULT_NHATS_ACQUISITION_READINESS = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_acquisition_readiness.json"
)
DEFAULT_NHATS_FILE_TIER_TABLE = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_file_tier_table.json"
)
DEFAULT_NHATS_FIRST_ESTIMAND_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_first_estimand_protocol.json"
)
DEFAULT_NHATS_VARIABLE_CONFIRMATION_MATRIX = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_variable_confirmation_matrix.json"
)
DEFAULT_NHATS_COHORT_FLOW_ENDPOINT_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_cohort_flow_endpoint_protocol.json"
)
DEFAULT_NHATS_DISCLOSURE_POLICY = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_disclosure_control_policy.json"
)
DEFAULT_NHATS_DISCLOSURE_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_disclosure_control_test_cases.json"
)
DEFAULT_NHATS_DISCLOSURE_VALIDATION = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-disclosure-control-validation.json"
)
DEFAULT_NHATS_SURVEY_DESIGN_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_survey_design_protocol.json"
)
DEFAULT_NHATS_SURVEY_DESIGN_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_survey_design_test_cases.json"
)
DEFAULT_NHATS_SURVEY_DESIGN_VALIDATION = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-survey-design-validation.json"
)
DEFAULT_NHATS_MISSINGNESS_ROUTE_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_missingness_route_protocol.json"
)
DEFAULT_NHATS_MISSINGNESS_ROUTE_TEST_CASES = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_missingness_route_test_cases.json"
)
DEFAULT_NHATS_MISSINGNESS_ROUTE_VALIDATION = (
    REPO_ROOT / "web" / "src" / "data" / "life-path-nhats-missingness-route-validation.json"
)
DEFAULT_NHATS_ROUTE_FIELD_DISCOVERY_REGISTER = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_route_field_discovery_register.json"
)
DEFAULT_NHATS_ROUTE_FIELD_DISCOVERY_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-route-field-discovery-validation.json"
)
DEFAULT_NHATS_COLECTICA_VALUE_LABEL_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_colectica_value_label_review_protocol.json"
)
DEFAULT_NHATS_COLECTICA_VALUE_LABEL_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-value-label-validation.json"
)
DEFAULT_NHATS_COLECTICA_VALUE_LABEL_EXECUTION_REGISTER = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_colectica_value_label_review_execution_register.json"
)
DEFAULT_NHATS_COLECTICA_VALUE_LABEL_EXECUTION_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-value-label-review-execution-validation.json"
)
DEFAULT_NHATS_COLECTICA_ACCESS_ROUTE_PROBE_REGISTER = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_colectica_access_route_probe_register.json"
)
DEFAULT_NHATS_COLECTICA_ACCESS_ROUTE_PROBE_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-access-route-probe-validation.json"
)
DEFAULT_NHATS_COLECTICA_AUTHENTICATED_CAPTURE_TEMPLATE = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_colectica_authenticated_capture_template.json"
)
DEFAULT_NHATS_COLECTICA_AUTHENTICATED_CAPTURE_TEMPLATE_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-colectica-authenticated-capture-template-validation.json"
)
DEFAULT_NHATS_L2_VARIABLE_FAMILY_ADMISSION_REGISTER = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_l2_variable_family_admission_register.json"
)
DEFAULT_NHATS_L2_VARIABLE_FAMILY_ADMISSION_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-l2-variable-family-admission-validation.json"
)
DEFAULT_NHATS_PREOUTCOME_AGGREGATION_PROTOCOL = (
    REPO_ROOT
    / "domains"
    / "c1-boundary-rewriting"
    / "longevity-evidence"
    / "data"
    / "manual"
    / "life_path_nhats_preoutcome_aggregation_protocol.json"
)
DEFAULT_NHATS_PREOUTCOME_AGGREGATION_VALIDATION = (
    REPO_ROOT
    / "web"
    / "src"
    / "data"
    / "life-path-nhats-preoutcome-aggregation-validation.json"
)
DEFAULT_MODEL_ADMISSION_CONTRACT = (
    REPO_ROOT / "docs" / "reference" / "human-infra-model-admission-contract.json"
)
DEFAULT_MODEL_ADMISSION_CANDIDATE_REGISTRY = (
    REPO_ROOT
    / "docs"
    / "reference"
    / "human-infra-model-admission-candidate-registry.json"
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
    "publicAggregateMortalityAnchor",
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
REQUIRED_DATA_SOURCE_FIELDS = {
    "id",
    "name",
    "sourceAuthority",
    "officialUrl",
    "geography",
    "cohortType",
    "populationFrame",
    "ageFrame",
    "accessStatus",
    "governanceStatus",
    "modelRoles",
    "coverageTags",
    "outcomeSupport",
    "predictorSupport",
    "strengths",
    "limitations",
    "prohibitedClaims",
}
REQUIRED_COVERAGE_TAGS = {
    "mortality",
    "function",
    "biomarkers",
    "cognition",
    "resourceSocial",
    "externalValidation",
}
REQUIRED_DATA_CARD_TEMPLATE_SECTIONS = {
    "Header",
    "Governance",
    "Study Design",
    "Outcomes",
    "Predictors",
    "Data Quality",
    "Model Use",
    "Decision",
    "Source Trace",
}
REQUIRED_SENSITIVITY_PARAMETERS = {
    "hazardMultiplier",
    "healthQualityShiftYears",
    "capabilityMultiplier",
    "subjectiveTimeExpansion",
    "levProgressRate",
    "riskTailPenalty",
}
REQUIRED_NHATS_ACQUISITION_SOURCE_IDS = {
    "data-access",
    "cross-year-search",
    "conditions-of-use",
    "welcome-ai-notice",
    "nhats-files",
    "round-14-files",
    "round-13-files",
}
REQUIRED_NHATS_ACQUISITION_GATE_IDS = {
    "official-source-refresh",
    "registration-status",
    "file-access-tier",
    "colectica-variable-confirmation",
    "round-window",
    "survey-design-plan",
    "endpoint-definition",
    "disclosure-control",
    "ai-boundary",
    "storage-destruction-plan",
}
REQUIRED_NHATS_FILE_TIER_ROW_IDS = {
    "nhats-r13-annual-public-sas",
    "nhats-r13-annual-public-stata",
    "nhats-r14-annual-public-sas",
    "nhats-r14-annual-public-stata",
    "nhats-r13-clock-drawing-public-tiff",
    "nhats-r14-clock-drawing-public-tiff",
    "nhats-r13-sample-person-sensitive-sas",
    "nhats-r13-sample-person-sensitive-stata",
    "nhats-r14-sample-person-sensitive-sas",
    "nhats-r14-sample-person-sensitive-stata",
    "nhats-r13-other-person-sensitive-sas",
    "nhats-r13-other-person-sensitive-stata",
    "nhats-r14-other-person-sensitive-sas",
    "nhats-r14-other-person-sensitive-stata",
    "nhats-r13-seasonality-weights-sensitive-sas",
    "nhats-r13-seasonality-weights-sensitive-stata",
}
REQUIRED_NHATS_FILE_TIER_METHOD_DOC_IDS = {
    "user-guide-r1-r14",
    "sample-design-faq",
    "cross-year-search",
    "round-13-crosswalk",
    "round-14-crosswalk",
}
REQUIRED_NHATS_FIRST_ESTIMAND_PREDICTOR_IDS = {
    "design_identity",
    "baseline_function",
    "baseline_cognition_attention",
    "baseline_support_resources",
    "baseline_environment_access",
}
REQUIRED_NHATS_FIRST_ESTIMAND_GATE_IDS = {
    "registration-status",
    "canonical-file-format",
    "exact-variable-confirmation",
    "endpoint-censoring-rule",
    "survey-design-ready",
    "disclosure-control-ready",
    "governed-storage-ready",
}
REQUIRED_NHATS_VARIABLE_SOURCE_FACT_IDS = {
    "colectica-metadata-truth-source",
    "variable-naming-convention",
    "standard-missing-codes",
    "sample-design-weights",
    "conditions-of-use-ai-boundary",
}
REQUIRED_NHATS_VARIABLE_GROUP_IDS = {
    "identity_join_route",
    "survey_design",
    "endpoint_censoring",
    "baseline_function",
    "baseline_cognition_attention",
    "baseline_support_environment",
}
REQUIRED_NHATS_COHORT_FLOW_STEPS = {
    "source-and-registration",
    "canonical-files",
    "baseline-eligible-sample",
    "followup-linkage",
    "endpoint-routing",
    "survey-design-check",
    "disclosure-control",
}
REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS = {
    "colectica-confirmation",
    "round-specific-materialization",
    "cohort-flow-ready",
    "survey-design-ready",
    "missingness-map-ready",
    "ai-and-disclosure-safe",
}
REQUIRED_NHATS_COHORT_FLOW_SOURCE_FACT_IDS = {
    "colectica-required-for-routes",
    "conditions-aggregate-ai-boundary",
    "sensitive-small-cell-boundary",
    "user-guide-missing-route-boundary",
    "sample-design-weight-boundary",
    "r13-r14-file-window",
}
REQUIRED_NHATS_COHORT_FLOW_ROW_IDS = {
    "source_refresh",
    "registered_access",
    "canonical_r13_file_selection",
    "canonical_r14_file_selection",
    "r13_baseline_candidates",
    "r13_design_identity_ready",
    "r14_followup_linkage",
    "r14_endpoint_route_counts",
    "survey_design_ready",
    "disclosure_control_ready",
}
REQUIRED_NHATS_ENDPOINT_ROUTE_IDS = {
    "alive_self_interview",
    "alive_proxy_interview",
    "alive_known_not_interviewed",
    "alive_residential_or_facility_route",
    "decedent_or_death_boundary",
    "not_classifiable_missing_route",
    "excluded_sensitive_or_restricted_required",
    "suppressed_small_cell",
}
REQUIRED_NHATS_COHORT_OUTPUT_IDS = {
    "cohort_flow_counts",
    "endpoint_route_counts",
    "missingness_table",
    "survey_design_plan",
    "disclosure_control_report",
    "aggregate_functional_survival_distribution",
}
REQUIRED_NHATS_COHORT_GATE_IDS = {
    "official-source-refresh",
    "registered-access",
    "canonical-file-selection",
    "colectica-route-confirmation",
    "missingness-route-map",
    "endpoint-route-map",
    "survey-design-ready",
    "disclosure-control-ready",
    "governed-storage-ready",
}
REQUIRED_NHATS_DISCLOSURE_OUTPUT_TYPES = {
    "cohort_flow_counts",
    "endpoint_route_counts",
    "missingness_table",
    "survey_design_plan",
    "disclosure_control_report",
    "aggregate_functional_survival_distribution",
}
REQUIRED_NHATS_DISCLOSURE_CASE_IDS = {
    "synthetic-safe-aggregate",
    "synthetic-small-cell-unsuppressed",
    "synthetic-small-cell-suppressed",
    "synthetic-row-level-leak",
    "synthetic-public-ai-upload",
    "synthetic-forbidden-output-type",
}
REQUIRED_NHATS_SURVEY_DESIGN_COMPONENT_IDS = {
    "analysis_weight",
    "strata",
    "psu_or_cluster",
    "variance_method",
    "domain_subpopulation_rule",
    "missingness_and_route_rule",
    "round_linkage_rule",
    "finite_population_boundary",
}
REQUIRED_NHATS_SURVEY_DESIGN_GATE_IDS = {
    "technical-paper-confirmed",
    "colectica-design-fields-confirmed",
    "round-specific-weight-selected",
    "strata-psu-fields-confirmed",
    "variance-method-selected",
    "domain-subpopulation-rule-selected",
    "missingness-route-map-ready",
    "disclosure-validation-passed",
    "weighted-estimator-script-reviewed",
}
REQUIRED_NHATS_SURVEY_DESIGN_CASE_IDS = {
    "synthetic-complete-design-plan",
    "synthetic-missing-weight",
    "synthetic-missing-strata",
    "synthetic-missing-psu",
    "synthetic-no-variance-method",
    "synthetic-public-inference-before-disclosure",
}
REQUIRED_NHATS_MISSINGNESS_ROUTE_CLASS_IDS = {
    "alive_self_interview",
    "alive_proxy_interview",
    "alive_facility_or_residential_route",
    "alive_known_not_interviewed",
    "decedent_or_death_boundary",
    "missing_or_nonresponse",
    "not_classifiable",
    "excluded_sensitive_or_restricted_required",
    "suppressed_small_cell",
}
REQUIRED_NHATS_MISSINGNESS_ROUTE_FIELD_IDS = {
    "identity_join_key",
    "round13_baseline_eligibility",
    "round14_interview_status",
    "proxy_status",
    "facility_residential_status",
    "death_decedent_indicator",
    "nonresponse_missing_code",
    "design_weight_linkage",
    "disclosure_cell_count",
}
REQUIRED_NHATS_MISSINGNESS_ROUTE_GATE_IDS = {
    "colectica-route-fields-confirmed",
    "baseline-eligibility-rule-confirmed",
    "followup-status-fields-confirmed",
    "death-boundary-fields-confirmed",
    "proxy-facility-route-fields-confirmed",
    "missing-code-crosswalk-ready",
    "survey-design-linkage-ready",
    "disclosure-control-ready",
    "route-classifier-script-reviewed",
}
REQUIRED_NHATS_MISSINGNESS_ROUTE_CASE_IDS = {
    "synthetic-alive-self-interview-route",
    "synthetic-alive-proxy-interview-route",
    "synthetic-alive-facility-route",
    "synthetic-decedent-dominates-functional-route",
    "synthetic-missing-status-blocks-endpoint",
    "synthetic-conflicting-alive-and-decedent-flags",
    "synthetic-public-small-cell-unsuppressed",
    "synthetic-public-small-cell-suppressed",
}
REQUIRED_NHATS_ROUTE_FIELD_DISCOVERY_EVIDENCE_IDS = {
    "nhats-cross-year-search-colectica",
    "nhats-conditions-of-use-ai-and-small-cell",
    "nhats-user-guide-proxy-prefixes",
    "nhats-user-guide-weight-design",
    "nhats-user-guide-missing-negative-codes",
    "nhats-user-guide-lml-death-boundary",
    "nhats-r14-crosswalk-route-fields",
    "nhats-r13-crosswalk-route-fields",
    "nhats-r14-crosswalk-design-fields",
    "nhats-r13-crosswalk-design-fields",
}
REQUIRED_NHATS_ROUTE_FIELD_DISCOVERY_GATE_IDS = {
    "colectica-value-labels-confirmed",
    "public-use-file-access-confirmed",
    "canonical-file-format-selected",
    "sensitive-death-date-exclusion-reviewed",
    "route-value-crosswalk-reviewed",
    "negative-missing-code-map-reviewed",
    "survey-design-linkage-reviewed",
    "route-classifier-code-reviewed",
    "disclosure-output-review-ready",
}
REQUIRED_NHATS_COLECTICA_VALUE_LABEL_EVIDENCE_IDS = {
    "nhats-cross-year-search-colectica-values",
    "nhats-cross-year-search-colectica-login",
    "nhats-conditions-of-use-public-ai-and-aggregation",
}
REQUIRED_NHATS_COLECTICA_VALUE_LABEL_ARTIFACT_IDS = {
    "colectica-access-log",
    "field-level-source-trace",
    "route-value-crosswalk",
    "reviewer-signoff",
}
REQUIRED_NHATS_COLECTICA_VALUE_LABEL_GATE_IDS = {
    "colectica-login-recorded",
    "colectica-variable-pages-reviewed",
    "value-label-source-capture-hashed",
    "question-text-and-universe-reviewed",
    "route-value-crosswalk-drafted",
    "negative-missing-code-map-drafted",
    "sensitive-death-date-exclusion-confirmed",
    "second-reviewer-signoff",
    "route-classifier-promotion-review",
    "public-output-disclosure-boundary-reviewed",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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

    public_anchor = readiness.get("publicAggregateMortalityAnchor")
    public_anchor_ok = (
        isinstance(public_anchor, dict)
        and public_anchor.get("status") == "available-for-baseline-plausibility-only"
        and str(public_anchor.get("source", "")).endswith("life_path_public_mortality_anchor.json")
        and has_text(public_anchor.get("blockedUses", []), "individual")
        and has_text(public_anchor.get("blockedUses", []), "calibrated")
        and has_text(public_anchor.get("blockedUses", []), "intervention")
    )
    add_check(
        checks,
        "readiness-public-aggregate-mortality-anchor",
        status_from_bool(public_anchor_ok),
        "public mortality anchor must remain aggregate-only and calibration-blocked",
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


def audit_data_sources(data_sources: dict[str, Any], data_sources_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    schema_version = data_sources.get("schemaVersion")
    add_check(
        checks,
        "data-sources-schema-version",
        status_from_bool(schema_version == "human-infra.life-path-data-source-candidates.v1"),
        f"schemaVersion={schema_version!r}",
    )

    boundary = data_sources.get("currentBoundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("noDataDownloaded") is True
        and boundary.get("noDataAccessGranted") is True
        and boundary.get("noIndividualDataPresent") is True
        and boundary.get("noCalibrationClaim") is True
        and boundary.get("noCausalClaim") is True
    )
    add_check(
        checks,
        "data-sources-candidate-only-boundary",
        status_from_bool(boundary_ok),
        "registry must state no data download, access grant, individual data, calibration claim, or causal claim",
    )

    candidates = data_sources.get("candidates")
    candidates_ok = isinstance(candidates, list) and len(candidates) >= 8
    add_check(
        checks,
        "data-sources-candidate-count",
        status_from_bool(candidates_ok),
        f"candidate_count={len(candidates) if isinstance(candidates, list) else 'invalid'}",
    )

    candidate_ids: list[str] = []
    all_fields_ok = True
    official_urls_ok = True
    governance_ok = True
    prohibited_ok = True
    observed_tags: set[str] = set()
    if isinstance(candidates, list):
        for candidate in candidates:
            if not isinstance(candidate, dict):
                all_fields_ok = False
                continue
            candidate_id = candidate.get("id")
            if isinstance(candidate_id, str):
                candidate_ids.append(candidate_id)
            if not REQUIRED_DATA_SOURCE_FIELDS.issubset(candidate):
                all_fields_ok = False
            url = candidate.get("officialUrl")
            if not isinstance(url, str) or not url.startswith("https://"):
                official_urls_ok = False
            if not str(candidate.get("governanceStatus", "")).strip() or not str(
                candidate.get("accessStatus", "")
            ).strip():
                governance_ok = False
            if not (
                has_text(candidate.get("prohibitedClaims", []), "individual")
                and (
                    has_text(candidate.get("prohibitedClaims", []), "calibration")
                    or has_text(candidate.get("prohibitedClaims", []), "calibrated")
                    or has_text(candidate.get("prohibitedClaims", []), "causal")
                )
            ):
                prohibited_ok = False
            tags = candidate.get("coverageTags")
            if isinstance(tags, list):
                observed_tags.update(str(tag) for tag in tags)

    unique_ids = len(candidate_ids) == len(set(candidate_ids)) and len(candidate_ids) > 0
    add_check(
        checks,
        "data-sources-candidate-id-unique",
        status_from_bool(unique_ids),
        f"ids={candidate_ids}",
    )
    add_check(
        checks,
        "data-sources-required-fields",
        status_from_bool(all_fields_ok),
        f"required={sorted(REQUIRED_DATA_SOURCE_FIELDS)}",
    )
    add_check(
        checks,
        "data-sources-official-https-urls",
        status_from_bool(official_urls_ok),
        "each candidate must use an official HTTPS URL",
    )
    add_check(
        checks,
        "data-sources-access-governance",
        status_from_bool(governance_ok),
        "each candidate must state access and governance status",
    )

    missing_tags = sorted(REQUIRED_COVERAGE_TAGS - observed_tags)
    add_check(
        checks,
        "data-sources-coverage-tags",
        status_from_bool(not missing_tags),
        f"missing_tags={missing_tags}",
    )

    summary = data_sources.get("coverageSummary")
    summary_ok = isinstance(summary, dict) and all(
        isinstance(summary.get(tag), list) and summary[tag] for tag in REQUIRED_COVERAGE_TAGS
    )
    add_check(
        checks,
        "data-sources-coverage-summary",
        status_from_bool(summary_ok),
        "coverage summary must map required model needs to candidate IDs",
    )
    add_check(
        checks,
        "data-sources-prohibited-claims",
        status_from_bool(prohibited_ok),
        "each candidate must block individual prediction and calibration/causal overclaim",
    )

    next_work = data_sources.get("nextWork")
    next_work_ok = isinstance(next_work, list) and len(next_work) >= 3 and has_text(
        next_work, "Source Card"
    )
    add_check(
        checks,
        "data-sources-next-work",
        status_from_bool(next_work_ok),
        "registry must point toward Source Cards, variable dictionaries, data cards, and governed acquisition",
    )

    return {
        "path": str(data_sources_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(data_sources_path),
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_source_card_docs(
    data_sources: dict[str, Any],
    source_cards_path: Path,
    data_card_template_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    source_cards_exists = source_cards_path.exists()
    data_card_template_exists = data_card_template_path.exists()
    add_check(
        checks,
        "source-cards-doc-exists",
        status_from_bool(source_cards_exists),
        str(source_cards_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "data-card-template-exists",
        status_from_bool(data_card_template_exists),
        str(data_card_template_path.relative_to(REPO_ROOT)),
    )

    source_cards_text = load_text(source_cards_path) if source_cards_exists else ""
    data_card_template_text = load_text(data_card_template_path) if data_card_template_exists else ""
    candidates = data_sources.get("candidates")
    candidate_ids: list[str] = []
    official_urls: list[str] = []
    if isinstance(candidates, list):
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            candidate_id = candidate.get("id")
            official_url = candidate.get("officialUrl")
            if isinstance(candidate_id, str):
                candidate_ids.append(candidate_id)
            if isinstance(official_url, str):
                official_urls.append(official_url)

    missing_ids = [candidate_id for candidate_id in candidate_ids if candidate_id not in source_cards_text]
    add_check(
        checks,
        "source-cards-cover-candidate-ids",
        status_from_bool(source_cards_exists and not missing_ids),
        f"missing_ids={missing_ids}",
    )

    missing_urls = [official_url for official_url in official_urls if official_url not in source_cards_text]
    add_check(
        checks,
        "source-cards-cover-official-urls",
        status_from_bool(source_cards_exists and not missing_urls),
        f"missing_urls={missing_urls}",
    )

    source_boundary_ok = all(
        token.lower() in source_cards_text.lower()
        for token in (
            "candidate-source-card-only",
            "未下载任何真实数据",
            "未建立任何校准",
            "no individual death-date prediction",
            "no external validation",
        )
    )
    add_check(
        checks,
        "source-cards-boundary-language",
        status_from_bool(source_cards_exists and source_boundary_ok),
        "source cards must preserve candidate-only, no-data, no-calibration, no-individual-prediction, and no-validation boundaries",
    )

    missing_template_sections = [
        section
        for section in sorted(REQUIRED_DATA_CARD_TEMPLATE_SECTIONS)
        if f"## {section}" not in data_card_template_text
    ]
    add_check(
        checks,
        "data-card-template-required-sections",
        status_from_bool(data_card_template_exists and not missing_template_sections),
        f"missing_sections={missing_template_sections}",
    )

    template_boundary_ok = all(
        token.lower() in data_card_template_text.lower()
        for token in (
            "No individual death-date prediction",
            "No personal medical advice",
            "No personal longevity ranking",
            "No model calibration claim before validation diagnostics exist",
        )
    )
    add_check(
        checks,
        "data-card-template-prohibited-outputs",
        status_from_bool(data_card_template_exists and template_boundary_ok),
        "data card template must block individual death-date prediction, personal medical advice, personal longevity ranking, and premature calibration claims",
    )

    source_card_sha = sha256_file(source_cards_path) if source_cards_exists else None
    data_card_template_sha = sha256_file(data_card_template_path) if data_card_template_exists else None
    return {
        "sourceCardsPath": str(source_cards_path.relative_to(REPO_ROOT)),
        "sourceCardsSha256": source_card_sha,
        "dataCardTemplatePath": str(data_card_template_path.relative_to(REPO_ROOT)),
        "dataCardTemplateSha256": data_card_template_sha,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_data_admission_docs(
    nhats_data_card_path: Path,
    nhats_variable_dictionary_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    data_card_exists = nhats_data_card_path.exists()
    dictionary_exists = nhats_variable_dictionary_path.exists()
    add_check(
        checks,
        "nhats-data-card-exists",
        status_from_bool(data_card_exists),
        str(nhats_data_card_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-variable-dictionary-exists",
        status_from_bool(dictionary_exists),
        str(nhats_variable_dictionary_path.relative_to(REPO_ROOT)),
    )

    data_card_text = load_text(nhats_data_card_path) if data_card_exists else ""
    dictionary_text = load_text(nhats_variable_dictionary_path) if dictionary_exists else ""

    data_card_identity_ok = all(
        token in data_card_text
        for token in (
            "data_card_id: nhats-r1-r14-effective-time-draft",
            "source_card_id: nhats",
            "source_name: National Health and Aging Trends Study",
            "status: draft / cannot-evaluate-yet",
        )
    )
    add_check(
        checks,
        "nhats-data-card-identity",
        status_from_bool(data_card_exists and data_card_identity_ok),
        "NHATS Data Card must identify source_card_id, source name, draft status, and data_card_id",
    )

    data_card_boundary_ok = all(
        token.lower() in data_card_text.lower()
        for token in (
            "No individual death-date prediction",
            "No personal medical advice",
            "No personal longevity ranking",
            "No model calibration claim before validation diagnostics exist",
            "No NHATS/NSOC raw data upload",
        )
    )
    add_check(
        checks,
        "nhats-data-card-boundaries",
        status_from_bool(data_card_exists and data_card_boundary_ok),
        "NHATS Data Card must block individual prediction, medical advice, personal ranking, premature calibration, and raw-data AI upload",
    )

    data_card_sources_ok = all(
        token in data_card_text
        for token in (
            "https://www.nhats.org/nhats",
            "https://www.nhats.org/data-access",
            "https://www.nhats.org/conditions-of-use",
            "NHATSUserGuideR14_02102026.pdf",
            "NHATSTechnicalPaper55_09042025.pdf",
        )
    )
    add_check(
        checks,
        "nhats-data-card-source-trace",
        status_from_bool(data_card_exists and data_card_sources_ok),
        "NHATS Data Card must cite overview, data access, conditions of use, user guide, and sample design sources",
    )

    data_card_decision_ok = all(
        token.lower() in data_card_text.lower()
        for token in (
            "decision: cannot-evaluate-yet",
            "no governed data access",
            "effective_time_proxy",
            "abort_conditions",
        )
    )
    add_check(
        checks,
        "nhats-data-card-decision",
        status_from_bool(data_card_exists and data_card_decision_ok),
        "NHATS Data Card must keep the current decision at cannot-evaluate-yet and name effective_time_proxy plus abort conditions",
    )

    dictionary_boundary_ok = all(
        token.lower() in dictionary_text.lower()
        for token in (
            "candidate-variable-dictionary-only",
            "No NHATS data downloaded",
            "No extraction manifest approved",
            "No model calibration",
            "No individual death-date prediction",
        )
    )
    add_check(
        checks,
        "nhats-variable-dictionary-boundaries",
        status_from_bool(dictionary_exists and dictionary_boundary_ok),
        "NHATS variable dictionary must remain candidate-only and block extraction/calibration/individual-prediction claims",
    )

    dictionary_fields_ok = all(
        token in dictionary_text
        for token in (
            "w#anfinwgt0",
            "w#varunit",
            "w#varstrat",
            "fl#spdied",
            "cg#dwrdimmrc",
            "cg#dwrddlyrc",
        )
    )
    add_check(
        checks,
        "nhats-variable-dictionary-core-examples",
        status_from_bool(dictionary_exists and dictionary_fields_ok),
        "NHATS variable dictionary must include design, decedent, and cognition example fields while still marking them as candidates",
    )

    dictionary_model_roles_ok = all(
        token in dictionary_text
        for token in (
            "design_and_identity",
            "outcome_boundary",
            "function_and_mobility",
            "cognition_and_attention",
            "resources_and_support",
            "environment_and_access",
            "effective_time_proxy",
            "decision: cannot-calibrate-yet",
        )
    )
    add_check(
        checks,
        "nhats-variable-dictionary-model-roles",
        status_from_bool(dictionary_exists and dictionary_model_roles_ok),
        "NHATS variable dictionary must map variable families to Human Infra model roles and keep decision at cannot-calibrate-yet",
    )

    return {
        "dataCardPath": str(nhats_data_card_path.relative_to(REPO_ROOT)),
        "dataCardSha256": sha256_file(nhats_data_card_path) if data_card_exists else None,
        "variableDictionaryPath": str(nhats_variable_dictionary_path.relative_to(REPO_ROOT)),
        "variableDictionarySha256": sha256_file(nhats_variable_dictionary_path)
        if dictionary_exists
        else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_extraction_manifest(manifest_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    manifest_exists = manifest_path.exists()
    add_check(
        checks,
        "nhats-extraction-manifest-exists",
        status_from_bool(manifest_exists),
        str(manifest_path.relative_to(REPO_ROOT)),
    )

    manifest_text = load_text(manifest_path) if manifest_exists else ""

    identity_ok = all(
        token in manifest_text
        for token in (
            "manifest_id: nhats-r1-r14-effective-time-manifest-draft",
            "source_card_id: nhats",
            "data_card_id: nhats-r1-r14-effective-time-draft",
            "variable_dictionary_id: nhats-life-path-variable-dictionary-draft",
            "status: draft / cannot-extract-yet",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-identity",
        status_from_bool(manifest_exists and identity_ok),
        "manifest must bind NHATS source card, data card, variable dictionary, manifest ID, and cannot-extract status",
    )

    access_terms_ok = all(
        token.lower() in manifest_text.lower()
        for token in (
            "registered users",
            "sensitive and restricted files require additional application",
            "public large language model",
            "ai platforms",
            "aggregate statistical reporting",
            "n < 5",
            "Colectica",
            "separate registration",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-access-terms",
        status_from_bool(manifest_exists and access_terms_ok),
        "manifest must record registration, sensitive/restricted application, Colectica, aggregate reporting, n<5, and public AI upload boundaries",
    )

    source_refresh_ok = all(
        token.lower() in manifest_text.lower()
        for token in (
            "Observed on 2026-07-02",
            "All NHATS files require registration",
            "public-use files are for registered users",
            "Cross-year metadata search is provided through Colectica",
            "January 22, 2026",
            "April 6, 2026",
            "temporarily unavailable due to impending website updates",
            "public LLMs or AI platforms is treated as data sharing",
            "Restricted files contain fields with additional identification risk",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-official-source-refresh",
        status_from_bool(manifest_exists and source_refresh_ok),
        "manifest must record current official NHATS access, Colectica, AI-upload, temporary-file-availability and restricted-file facts",
    )

    no_data_boundary_ok = all(
        token.lower() in manifest_text.lower()
        for token in (
            "No NHATS data downloaded",
            "No extraction script authorized",
            "No raw data in repository",
            "No calibration or validation claim",
            "No individual death-date prediction",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-no-data-boundary",
        status_from_bool(manifest_exists and no_data_boundary_ok),
        "manifest must explicitly block download, extraction script, raw repository data, calibration/validation claim, and individual death-date prediction",
    )

    acquisition_gates_ok = all(
        token in manifest_text
        for token in (
            "`official-source-refresh`",
            "`registration-status`",
            "`file-access-tier`",
            "`colectica-variable-confirmation`",
            "`round-window`",
            "`survey-design-plan`",
            "`endpoint-definition`",
            "`disclosure-control`",
            "`ai-boundary`",
            "`storage-destruction-plan`",
            "If any acquisition readiness gate remains Missing or only Partial, decision = cannot-extract-yet.",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-acquisition-readiness-gates",
        status_from_bool(manifest_exists and acquisition_gates_ok),
        "manifest must expose acquisition-readiness gates before any governed NHATS extraction",
    )

    variable_groups_ok = all(
        token in manifest_text
        for token in (
            "spid",
            "w#anfinwgt0",
            "w#varunit",
            "w#varstrat",
            "fl#spdied",
            "cg#dwrdimmrc",
            "cg#dwrddlyrc",
            "effective_time_proxy",
            "functional_survival_state",
            "survey_design_ready",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-variable-groups",
        status_from_bool(manifest_exists and variable_groups_ok),
        "manifest must include identity, weight/design, endpoint, cognition, effective-time and derived-output variables",
    )

    extraction_rules_ok = all(
        token.lower() in manifest_text.lower()
        for token in (
            "do not write an extraction script",
            "do not download or store",
            "do not use sensitive/restricted files",
            "do not compute model metrics",
            "do not display any output",
            "do not infer exact variables from prose alone",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-extraction-rules",
        status_from_bool(manifest_exists and extraction_rules_ok),
        "manifest must block scripts, downloads, sensitive/restricted use, metrics, unsafe display, and prose-only variable inference",
    )

    required_slots_ok = all(
        token in manifest_text
        for token in (
            "nhats_release:",
            "rounds:",
            "file_names:",
            "access_tier:",
            "variables:",
            "derived_variables:",
            "weight_variables:",
            "design_variables:",
            "replicate_weight_variables:",
            "missing_codes:",
            "value_labels:",
            "join_keys:",
            "endpoint_fields:",
            "allowed_outputs:",
            "forbidden_outputs:",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-required-slots",
        status_from_bool(manifest_exists and required_slots_ok),
        "manifest must expose the blank slots required before governed extraction",
    )

    abort_conditions_ok = all(
        token.lower() in manifest_text.lower()
        for token in (
            "access terms cannot be satisfied",
            "colectica unavailable",
            "weights or design variables are unavailable",
            "endpoint definition is ambiguous",
            "n < 5 suppression cannot be enforced",
            "raw data would enter the repository",
            "individual prediction",
            "medical advice",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-abort-conditions",
        status_from_bool(manifest_exists and abort_conditions_ok),
        "manifest must define abort gates for access, Colectica, weights/design, endpoint ambiguity, disclosure suppression, raw-data leakage, and unsafe outputs",
    )

    source_trace_ok = all(
        token in manifest_text
        for token in (
            "https://www.nhats.org/nhats",
            "https://www.nhats.org/data-access",
            "https://www.nhats.org/conditions-of-use",
            "https://www.nhats.org/data-access/cross-year-search",
            "https://www.nhats.org/data-access/nhats",
            "NHATSUserGuideR14_02102026.pdf",
            "NHATSTechnicalPaper55_09042025.pdf",
        )
    )
    add_check(
        checks,
        "nhats-extraction-manifest-source-trace",
        status_from_bool(manifest_exists and source_trace_ok),
        "manifest must cite official NHATS overview, access, terms, cross-year search, files, user guide, and sample design sources",
    )

    return {
        "path": str(manifest_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(manifest_path) if manifest_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_acquisition_readiness(readiness_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    exists = readiness_path.exists()
    add_check(
        checks,
        "nhats-acquisition-readiness-exists",
        status_from_bool(exists),
        str(readiness_path.relative_to(REPO_ROOT)),
    )
    readiness = load_json(readiness_path) if exists else {}

    schema_ok = (
        readiness.get("schemaVersion")
        == "human-infra.life-path-nhats-acquisition-readiness.v1"
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-schema",
        status_from_bool(exists and schema_ok),
        f"schemaVersion={readiness.get('schemaVersion')!r}",
    )

    identity_ok = (
        readiness.get("sourceId") == "nhats"
        and readiness.get("dataCardId") == "nhats-r1-r14-effective-time-draft"
        and readiness.get("manifestId") == "nhats-r1-r14-effective-time-manifest-draft"
        and readiness.get("fileTierTableId") == "nhats-r13-r14-file-tier-table-draft"
        and readiness.get("status") == "cannot-extract-yet"
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-identity",
        status_from_bool(exists and identity_ok),
        "readiness contract must bind NHATS source, Data Card, manifest and cannot-extract status",
    )

    decision = readiness.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("acquisitionReady") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("rawDataAllowedInRepository") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-current-decision",
        status_from_bool(exists and decision_ok),
        "current decision must explicitly block acquisition, extraction scripts, raw repository data, calibration and individual prediction",
    )

    sources = readiness.get("officialSourceRefresh")
    observed_source_ids: set[str] = set()
    source_urls_ok = True
    source_facts_ok = True
    if isinstance(sources, list):
        for source in sources:
            if not isinstance(source, dict):
                source_facts_ok = False
                continue
            source_id = source.get("id")
            if isinstance(source_id, str):
                observed_source_ids.add(source_id)
            url = source.get("url")
            if not isinstance(url, str) or not url.startswith("https://"):
                source_urls_ok = False
            if not str(source.get("observedFact", "")).strip() or not str(
                source.get("modelConsequence", "")
            ).strip():
                source_facts_ok = False
    missing_source_ids = sorted(REQUIRED_NHATS_ACQUISITION_SOURCE_IDS - observed_source_ids)
    add_check(
        checks,
        "nhats-acquisition-readiness-source-coverage",
        status_from_bool(exists and isinstance(sources, list) and not missing_source_ids),
        f"missing_source_ids={missing_source_ids}",
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-source-urls",
        status_from_bool(exists and source_urls_ok),
        "official source refresh entries must use HTTPS URLs",
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-source-facts",
        status_from_bool(exists and source_facts_ok),
        "official source refresh entries must include observed fact and model consequence",
    )

    gates = readiness.get("gates")
    observed_gate_ids: set[str] = set()
    gate_status_ok = True
    blocking_ok = True
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gate_status_ok = False
                blocking_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            status = gate.get("status")
            if status not in {"missing", "partial", "ready"}:
                gate_status_ok = False
            if status in {"missing", "partial"} and gate.get("blocksExtraction") is not True:
                blocking_ok = False
            if not str(gate.get("requiredEvidence", "")).strip() or not str(
                gate.get("nextEvidence", "")
            ).strip():
                gate_status_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_ACQUISITION_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-acquisition-readiness-gate-coverage",
        status_from_bool(exists and isinstance(gates, list) and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-gate-status",
        status_from_bool(exists and gate_status_ok),
        "each gate must have a valid status, required evidence and next evidence",
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-blocking-gates",
        status_from_bool(exists and blocking_ok),
        "missing or partial gates must block extraction",
    )

    summary = readiness.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_ACQUISITION_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_ACQUISITION_GATE_IDS)
        and summary.get("partialGateCount", 0) + summary.get("missingGateCount", 0)
        == len(REQUIRED_NHATS_ACQUISITION_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-gate-summary",
        status_from_bool(exists and summary_ok),
        "gate summary must keep all acquisition gates blocking until ready evidence exists",
    )

    prohibited_ok = (
        has_text(readiness.get("prohibitedActions", []), "download NHATS data")
        and has_text(readiness.get("prohibitedActions", []), "extraction scripts")
        and has_text(readiness.get("prohibitedActions", []), "raw NHATS")
        and has_text(readiness.get("prohibitedActions", []), "public LLMs")
        and has_text(readiness.get("prohibitedActions", []), "individual death-date")
        and has_text(readiness.get("prohibitedActions", []), "calibration")
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-prohibited-actions",
        status_from_bool(exists and prohibited_ok),
        "readiness contract must prohibit premature download, scripts, raw data, public AI upload, individual death-date prediction and calibration claims",
    )

    next_work_ok = (
        isinstance(readiness.get("nextWork"), list)
        and has_text(readiness["nextWork"], "file-tier table")
        and has_text(readiness["nextWork"], "Cross-Year Search")
        and has_text(readiness["nextWork"], "disclosure-control")
    )
    add_check(
        checks,
        "nhats-acquisition-readiness-next-work",
        status_from_bool(exists and next_work_ok),
        "next work must point to file-tier, Cross-Year Search variable confirmation and disclosure control",
    )

    return {
        "path": str(readiness_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(readiness_path) if exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_file_tier_table(table_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    exists = table_path.exists()
    add_check(
        checks,
        "nhats-file-tier-table-exists",
        status_from_bool(exists),
        str(table_path.relative_to(REPO_ROOT)),
    )
    table = load_json(table_path) if exists else {}

    schema_ok = table.get("schemaVersion") == "human-infra.life-path-nhats-file-tier-table.v1"
    add_check(
        checks,
        "nhats-file-tier-table-schema",
        status_from_bool(exists and schema_ok),
        f"schemaVersion={table.get('schemaVersion')!r}",
    )

    identity_ok = (
        table.get("sourceId") == "nhats"
        and table.get("tableId") == "nhats-r13-r14-file-tier-table-draft"
        and table.get("dataCardId") == "nhats-r1-r14-effective-time-draft"
        and table.get("manifestId") == "nhats-r1-r14-effective-time-manifest-draft"
        and table.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and table.get("status") == "candidate-file-tier-table-only"
    )
    add_check(
        checks,
        "nhats-file-tier-table-identity",
        status_from_bool(exists and identity_ok),
        "file-tier table must bind NHATS source, Data Card, manifest, acquisition readiness and candidate-only status",
    )

    decision = table.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("fileTierTableReady") is False
        and decision.get("downloadAllowed") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("rawDataAllowedInRepository") is False
        and decision.get("publicAiUploadAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-file-tier-table-current-decision",
        status_from_bool(exists and decision_ok),
        "file-tier table must still block download, scripts, repository storage, public AI upload, calibration and individual prediction",
    )

    round_window = table.get("roundWindowCandidate")
    round_window_ok = (
        isinstance(round_window, dict)
        and round_window.get("baselineRound") == 13
        and round_window.get("followupRound") == 14
        and round_window.get("decision") == "candidate-only"
        and round_window.get("extractionAllowed") is False
    )
    add_check(
        checks,
        "nhats-file-tier-table-round-window",
        status_from_bool(exists and round_window_ok),
        "round-window candidate must remain R13/R14 candidate-only and extraction-blocked",
    )

    rows = table.get("fileRows")
    observed_row_ids: set[str] = set()
    row_shape_ok = True
    source_paths_ok = True
    row_boundary_ok = True
    candidate_core_rows = 0
    public_rows = 0
    sensitive_rows = 0
    if isinstance(rows, list):
        for row in rows:
            if not isinstance(row, dict):
                row_shape_ok = False
                row_boundary_ok = False
                continue
            row_id = row.get("id")
            if isinstance(row_id, str):
                observed_row_ids.add(row_id)
            required_keys = {
                "round",
                "fileFamily",
                "format",
                "accessTier",
                "officialPageUrl",
                "officialFilePath",
                "downloadStateOnOfficialPage",
                "publicIndicatorOnOfficialPage",
                "candidateUse",
                "whyItMatters",
                "blocksRemaining",
                "downloadAllowedNow",
                "extractionAllowedNow",
                "repoStorageAllowed",
                "publicAiUploadAllowed",
            }
            if any(key not in row for key in required_keys):
                row_shape_ok = False
            if not str(row.get("officialPageUrl", "")).startswith("https://"):
                source_paths_ok = False
            if not str(row.get("officialFilePath", "")).startswith("/system/files/"):
                source_paths_ok = False
            if not isinstance(row.get("blocksRemaining"), list) or not row["blocksRemaining"]:
                row_boundary_ok = False
            if (
                row.get("downloadAllowedNow") is not False
                or row.get("extractionAllowedNow") is not False
                or row.get("repoStorageAllowed") is not False
                or row.get("publicAiUploadAllowed") is not False
            ):
                row_boundary_ok = False
            if row.get("candidateUse") == "candidate-core":
                candidate_core_rows += 1
            if row.get("accessTier") == "public-use-registration-required":
                public_rows += 1
            if row.get("accessTier") == "sensitive-application-required":
                sensitive_rows += 1
    missing_rows = sorted(REQUIRED_NHATS_FILE_TIER_ROW_IDS - observed_row_ids)
    add_check(
        checks,
        "nhats-file-tier-table-row-coverage",
        status_from_bool(exists and isinstance(rows, list) and not missing_rows),
        f"missing_row_ids={missing_rows}",
    )
    add_check(
        checks,
        "nhats-file-tier-table-row-shape",
        status_from_bool(exists and row_shape_ok),
        "each file row must expose file family, format, access tier, official path, planned use and blocking fields",
    )
    add_check(
        checks,
        "nhats-file-tier-table-source-paths",
        status_from_bool(exists and source_paths_ok),
        "file rows must point to official HTTPS pages and official /system/files paths",
    )
    add_check(
        checks,
        "nhats-file-tier-table-row-boundaries",
        status_from_bool(exists and row_boundary_ok),
        "every row must keep download, extraction, repository storage and public AI upload blocked",
    )

    tier_summary = table.get("tierSummary")
    tier_summary_ok = (
        isinstance(tier_summary, dict)
        and tier_summary.get("fileRowCount") == len(REQUIRED_NHATS_FILE_TIER_ROW_IDS)
        and tier_summary.get("candidateCoreRows") == candidate_core_rows == 4
        and tier_summary.get("publicUseRegistrationRequiredRows") == public_rows == 6
        and tier_summary.get("sensitiveApplicationRequiredRows") == sensitive_rows == 10
        and tier_summary.get("downloadAllowedRows") == 0
        and tier_summary.get("extractionAllowedRows") == 0
        and tier_summary.get("repoStorageAllowedRows") == 0
        and tier_summary.get("publicAiUploadAllowedRows") == 0
    )
    add_check(
        checks,
        "nhats-file-tier-table-tier-summary",
        status_from_bool(exists and tier_summary_ok),
        "tier summary must match row counts and keep all download/extraction/storage/AI rows blocked",
    )

    method_docs = table.get("methodDocumentRequirements")
    observed_doc_ids: set[str] = set()
    method_docs_ok = True
    if isinstance(method_docs, list):
        for doc in method_docs:
            if not isinstance(doc, dict):
                method_docs_ok = False
                continue
            doc_id = doc.get("id")
            if isinstance(doc_id, str):
                observed_doc_ids.add(doc_id)
            if not str(doc.get("url", "")).startswith("https://"):
                method_docs_ok = False
            if not str(doc.get("requiredFor", "")).strip() or not str(doc.get("status", "")).strip():
                method_docs_ok = False
    missing_doc_ids = sorted(REQUIRED_NHATS_FILE_TIER_METHOD_DOC_IDS - observed_doc_ids)
    add_check(
        checks,
        "nhats-file-tier-table-method-docs",
        status_from_bool(exists and isinstance(method_docs, list) and method_docs_ok and not missing_doc_ids),
        f"missing_method_doc_ids={missing_doc_ids}",
    )

    prohibited_ok = (
        has_text(table.get("prohibitedActions", []), "download NHATS files")
        and has_text(table.get("prohibitedActions", []), "Colectica")
        and has_text(table.get("prohibitedActions", []), "sensitive files")
        and has_text(table.get("prohibitedActions", []), "raw NHATS")
        and has_text(table.get("prohibitedActions", []), "public LLMs")
        and has_text(table.get("prohibitedActions", []), "individual death-date")
    )
    add_check(
        checks,
        "nhats-file-tier-table-prohibited-actions",
        status_from_bool(exists and prohibited_ok),
        "file-tier table must prohibit premature download, prose-only variables, sensitive-file use, raw storage, public AI upload and individual prediction",
    )

    next_work_ok = (
        isinstance(table.get("nextWork"), list)
        and has_text(table["nextWork"], "canonical public-use annual file format")
        and has_text(table["nextWork"], "Colectica")
        and has_text(table["nextWork"], "weights")
        and has_text(table["nextWork"], "endpoint")
        and has_text(table["nextWork"], "disclosure-control")
    )
    add_check(
        checks,
        "nhats-file-tier-table-next-work",
        status_from_bool(exists and next_work_ok),
        "next work must point to canonical format, Colectica variables, weights, endpoint and disclosure-control work",
    )

    source_trace = table.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "methods-documentation")
        and has_text(source_trace, "conditions-of-use")
    )
    add_check(
        checks,
        "nhats-file-tier-table-source-trace",
        status_from_bool(exists and source_trace_ok),
        "source trace must include R13/R14 files, Cross-Year Search, methods documentation and Conditions of Use",
    )

    return {
        "path": str(table_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(table_path) if exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_first_estimand_protocol(protocol_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    exists = protocol_path.exists()
    add_check(
        checks,
        "nhats-first-estimand-protocol-exists",
        status_from_bool(exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    protocol = load_json(protocol_path) if exists else {}

    schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-first-estimand-protocol.v1"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-schema",
        status_from_bool(exists and schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId") == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and protocol.get("dataCardId") == "nhats-r1-r14-effective-time-draft"
        and protocol.get("manifestId") == "nhats-r1-r14-effective-time-manifest-draft"
        and protocol.get("variableDictionaryId") == "nhats-life-path-variable-dictionary-draft"
        and protocol.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and protocol.get("fileTierTableId") == "nhats-r13-r14-file-tier-table-draft"
        and protocol.get("status") == "protocol-only-cannot-run-yet"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-identity",
        status_from_bool(exists and identity_ok),
        "protocol must bind NHATS source, Data Card, manifest, variable dictionary, acquisition readiness and file-tier table",
    )

    decision = protocol.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("estimandRunnable") is False
        and decision.get("downloadAllowed") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("variableSelectionAfterOutcomeAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("externalValidationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-current-decision",
        status_from_bool(exists and decision_ok),
        "protocol must block running, download, extraction scripts, post-outcome variable selection, calibration, validation and individual prediction",
    )

    estimand = protocol.get("estimand")
    estimand_ok = (
        isinstance(estimand, dict)
        and estimand.get("id") == "E-NHATS-R13R14-FS-01"
        and "functional-survival" in str(estimand.get("label", "")).lower()
        and "cohort-level" in str(estimand.get("estimandType", "")).lower()
        and has_text(estimand.get("notAnEstimandFor", []), "individual death-date")
        and has_text(estimand.get("notAnEstimandFor", []), "causal effect")
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-estimand-boundary",
        status_from_bool(exists and estimand_ok),
        "estimand must be cohort-level functional-survival and must not claim individual, causal, clinical or LEV proof use",
    )

    target = protocol.get("targetPopulation")
    target_ok = (
        isinstance(target, dict)
        and target.get("baselineRound") == 13
        and target.get("followupRound") == 14
        and "65+" in str(target.get("ageFrame", ""))
        and has_text(target.get("inclusionCriteria", []), "R13 public-use annual")
        and has_text(target.get("exclusionCriteria", []), "sensitive or restricted")
        and target.get("status") == "candidate-only-unverified"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-target-population",
        status_from_bool(exists and target_ok),
        "target population must bind R13/R14, age 65+, public-use first pass and sensitive/restricted exclusion",
    )

    time_zero = protocol.get("timeZero")
    time_zero_ok = (
        isinstance(time_zero, dict)
        and "R13" in str(time_zero.get("indexRule", ""))
        and "R14" in str(time_zero.get("followupEnd", ""))
        and time_zero.get("outcomePeekingBlocked") is True
        and time_zero.get("status") == "pre-registered-draft"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-time-zero",
        status_from_bool(exists and time_zero_ok),
        "time zero must freeze R13 predictors, end at R14 follow-up and block outcome peeking",
    )

    outcome = protocol.get("outcomeDefinition")
    outcome_ok = (
        isinstance(outcome, dict)
        and outcome.get("primaryOutcome") == "functional_survival_state_r14"
        and has_text(outcome.get("components", []), "alive_or_decedent_boundary")
        and has_text(outcome.get("components", []), "functional_state")
        and has_text(outcome.get("candidateScale", []), "decedent")
        and "individual death date" in str(outcome.get("forbiddenOutcome", "")).lower()
        and outcome.get("status") == "definition-draft-no-field-names-yet"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-outcome-definition",
        status_from_bool(exists and outcome_ok),
        "outcome must define aggregate functional-survival state and forbid individual death-date output",
    )

    predictor_families = protocol.get("predictorFamilies")
    observed_predictor_ids: set[str] = set()
    predictors_ok = True
    if isinstance(predictor_families, list):
        for family in predictor_families:
            if not isinstance(family, dict):
                predictors_ok = False
                continue
            family_id = family.get("id")
            if isinstance(family_id, str):
                observed_predictor_ids.add(family_id)
            if family.get("status") != "exact-fields-pending":
                predictors_ok = False
            if not str(family.get("role", "")).strip() or not str(family.get("sourceFamily", "")).strip():
                predictors_ok = False
    missing_predictor_ids = sorted(
        REQUIRED_NHATS_FIRST_ESTIMAND_PREDICTOR_IDS - observed_predictor_ids
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-predictor-families",
        status_from_bool(exists and isinstance(predictor_families, list) and predictors_ok and not missing_predictor_ids),
        f"missing_predictor_ids={missing_predictor_ids}",
    )

    censoring = protocol.get("censoringAndMissingness")
    censoring_ok = (
        isinstance(censoring, dict)
        and has_text(censoring.get("mustDistinguish", []), "death")
        and has_text(censoring.get("mustDistinguish", []), "proxy interview")
        and has_text(censoring.get("mustDistinguish", []), "residential care")
        and has_text(censoring.get("mustDistinguish", []), "nonresponse")
        and "before any model metric" in str(censoring.get("rule", "")).lower()
        and censoring.get("status") == "rules-draft-no-field-names-yet"
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-censoring-missingness",
        status_from_bool(exists and censoring_ok),
        "censoring rules must distinguish death, proxy, residential care, nonresponse and not-classifiable states before metrics",
    )

    survey_design = protocol.get("surveyDesignPlan")
    survey_design_ok = (
        isinstance(survey_design, dict)
        and has_text(survey_design.get("requiredBeforeMetrics", []), "analysis weight")
        and has_text(survey_design.get("requiredBeforeMetrics", []), "strata")
        and has_text(survey_design.get("requiredBeforeMetrics", []), "cluster")
        and has_text(survey_design.get("requiredBeforeMetrics", []), "variance")
        and survey_design.get("currentStatus") == "not-ready"
        and "blocked" in str(survey_design.get("blockedUntil", "")).lower()
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-survey-design",
        status_from_bool(exists and survey_design_ok),
        "survey design must require weights, strata, cluster/PSU and variance method before metrics",
    )

    analysis_plan = protocol.get("analysisPlan")
    analysis_plan_ok = (
        isinstance(analysis_plan, dict)
        and has_text(analysis_plan.get("allowedFirstOutputs", []), "cohort_flow_counts")
        and has_text(analysis_plan.get("allowedFirstOutputs", []), "missingness_table")
        and has_text(analysis_plan.get("prohibitedFirstOutputs", []), "row-level")
        and has_text(analysis_plan.get("prohibitedFirstOutputs", []), "individual death-date")
        and has_text(analysis_plan.get("prohibitedFirstOutputs", []), "small-cell")
        and "descriptive-predictive protocol" in str(analysis_plan.get("modelClassBoundary", "")).lower()
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-analysis-boundary",
        status_from_bool(exists and analysis_plan_ok),
        "analysis plan must allow only aggregate diagnostics and prohibit row-level, small-cell, individual and validation/calibration outputs",
    )

    gates = protocol.get("readinessGates")
    observed_gate_ids: set[str] = set()
    gates_ok = True
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksRun") is not True:
                gates_ok = False
            if not str(gate.get("requiredEvidence", "")).strip():
                gates_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_FIRST_ESTIMAND_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-first-estimand-protocol-readiness-gates",
        status_from_bool(exists and isinstance(gates, list) and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    summary = protocol.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_FIRST_ESTIMAND_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_NHATS_FIRST_ESTIMAND_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_FIRST_ESTIMAND_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-gate-summary",
        status_from_bool(exists and summary_ok),
        "gate summary must keep every estimand gate blocking until ready evidence exists",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "methods-documentation")
        and has_text(source_trace, "conditions-of-use")
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-source-trace",
        status_from_bool(exists and source_trace_ok),
        "source trace must include R13/R14 files, Cross-Year Search, methods documentation and Conditions of Use",
    )

    next_work_ok = (
        isinstance(protocol.get("nextWork"), list)
        and has_text(protocol["nextWork"], "canonical R13/R14")
        and has_text(protocol["nextWork"], "Colectica")
        and has_text(protocol["nextWork"], "cohort-flow")
        and has_text(protocol["nextWork"], "disclosure-control")
    )
    add_check(
        checks,
        "nhats-first-estimand-protocol-next-work",
        status_from_bool(exists and next_work_ok),
        "next work must point to canonical files, Colectica/codebooks, cohort flow and disclosure control",
    )

    return {
        "path": str(protocol_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(protocol_path) if exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_variable_confirmation_matrix(matrix_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    exists = matrix_path.exists()
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-exists",
        status_from_bool(exists),
        str(matrix_path.relative_to(REPO_ROOT)),
    )
    matrix = load_json(matrix_path) if exists else {}

    schema_ok = (
        matrix.get("schemaVersion")
        == "human-infra.life-path-nhats-variable-confirmation-matrix.v1"
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-schema",
        status_from_bool(exists and schema_ok),
        f"schemaVersion={matrix.get('schemaVersion')!r}",
    )

    identity_ok = (
        matrix.get("sourceId") == "nhats"
        and matrix.get("matrixId") == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and matrix.get("protocolId") == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and matrix.get("manifestId") == "nhats-r1-r14-effective-time-manifest-draft"
        and matrix.get("variableDictionaryId") == "nhats-life-path-variable-dictionary-draft"
        and matrix.get("status") == "candidate-variable-confirmation-only-cannot-extract"
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-identity",
        status_from_bool(exists and identity_ok),
        "matrix must bind NHATS source, first estimand protocol, manifest and variable dictionary",
    )

    decision = matrix.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("exactVariablesReady") is False
        and decision.get("cohortFlowReady") is False
        and decision.get("endpointRoutingReady") is False
        and decision.get("surveyDesignReady") is False
        and decision.get("missingCodesReady") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("downloadAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-current-decision",
        status_from_bool(exists and decision_ok),
        "matrix must block exact-variable readiness, cohort flow, endpoint routing, survey design, download, extraction, calibration and individual prediction",
    )

    facts = matrix.get("officialSourceFacts")
    observed_fact_ids: set[str] = set()
    facts_ok = isinstance(facts, list) and len(facts) >= len(REQUIRED_NHATS_VARIABLE_SOURCE_FACT_IDS)
    if isinstance(facts, list):
        for fact in facts:
            if not isinstance(fact, dict):
                facts_ok = False
                continue
            fact_id = fact.get("id")
            if isinstance(fact_id, str):
                observed_fact_ids.add(fact_id)
            if not str(fact.get("fact", "")).strip() or not str(
                fact.get("modelConsequence", "")
            ).strip():
                facts_ok = False
            url = fact.get("sourceUrl")
            if not isinstance(url, str) or not url.startswith("https://"):
                facts_ok = False
    missing_fact_ids = sorted(REQUIRED_NHATS_VARIABLE_SOURCE_FACT_IDS - observed_fact_ids)
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-source-facts",
        status_from_bool(exists and facts_ok and not missing_fact_ids),
        f"missing_fact_ids={missing_fact_ids}",
    )

    round_rules = matrix.get("roundInstantiationRules")
    examples = round_rules.get("examples") if isinstance(round_rules, dict) else None
    round_rules_ok = (
        isinstance(round_rules, dict)
        and round_rules.get("baselineRound") == 13
        and round_rules.get("followupRound") == 14
        and round_rules.get("roundPlaceholder") == "#"
        and isinstance(examples, list)
        and len(examples) >= 6
        and has_text(examples, "w13anfinwgt0")
        and has_text(examples, "w14anfinwgt0")
        and has_text(examples, "fl14spdied")
        and has_text(examples, "cg13dwrdimmrc")
        and has_text(examples, "candidate-pattern-only")
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-round-rules",
        status_from_bool(exists and round_rules_ok),
        "round instantiation must bind R13/R14, # placeholder, candidate R13/R14 examples and candidate-pattern-only status",
    )

    groups = matrix.get("candidateVariableGroups")
    observed_group_ids: set[str] = set()
    groups_ok = isinstance(groups, list) and len(groups) >= len(REQUIRED_NHATS_VARIABLE_GROUP_IDS)
    if isinstance(groups, list):
        for group in groups:
            if not isinstance(group, dict):
                groups_ok = False
                continue
            group_id = group.get("id")
            if isinstance(group_id, str):
                observed_group_ids.add(group_id)
            if not str(group.get("modelRole", "")).strip():
                groups_ok = False
            if not isinstance(group.get("candidateFields"), list) or not isinstance(
                group.get("requiredEvidenceBeforeUse"), list
            ):
                groups_ok = False
            if group.get("currentStatus") not in {
                "candidate-only",
                "candidate-pattern-only",
                "family-only",
            }:
                groups_ok = False
    missing_group_ids = sorted(REQUIRED_NHATS_VARIABLE_GROUP_IDS - observed_group_ids)
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-variable-groups",
        status_from_bool(exists and groups_ok and not missing_group_ids),
        f"missing_group_ids={missing_group_ids}",
    )

    cohort_flow = matrix.get("cohortFlowTemplate")
    observed_steps: set[str] = set()
    cohort_flow_ok = isinstance(cohort_flow, list) and len(cohort_flow) >= len(
        REQUIRED_NHATS_COHORT_FLOW_STEPS
    )
    if isinstance(cohort_flow, list):
        for step in cohort_flow:
            if not isinstance(step, dict):
                cohort_flow_ok = False
                continue
            step_id = step.get("step")
            if isinstance(step_id, str):
                observed_steps.add(step_id)
            if step.get("currentStatus") != "missing":
                cohort_flow_ok = False
            if not str(step.get("requiredEvidence", "")).strip() or not str(
                step.get("output", "")
            ).strip():
                cohort_flow_ok = False
    missing_steps = sorted(REQUIRED_NHATS_COHORT_FLOW_STEPS - observed_steps)
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-cohort-flow",
        status_from_bool(exists and cohort_flow_ok and not missing_steps),
        f"missing_steps={missing_steps}",
    )

    gates = matrix.get("readinessGates")
    observed_gate_ids: set[str] = set()
    gates_ok = isinstance(gates, list) and len(gates) >= len(REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS)
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksExtraction") is not True:
                gates_ok = False
            if not str(gate.get("requiredEvidence", "")).strip():
                gates_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-readiness-gates",
        status_from_bool(exists and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    summary = matrix.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_VARIABLE_MATRIX_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-gate-summary",
        status_from_bool(exists and summary_ok),
        "gate summary must keep every variable-confirmation gate missing and blocking",
    )

    prohibited = matrix.get("prohibitedActions")
    prohibited_ok = (
        isinstance(prohibited, list)
        and has_text(prohibited, "download")
        and has_text(prohibited, "extraction script")
        and has_text(prohibited, "pattern-resolved names")
        and has_text(prohibited, "after seeing R14 outcomes")
        and has_text(prohibited, "public AI")
        and has_text(prohibited, "individual death")
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-prohibited-actions",
        status_from_bool(exists and prohibited_ok),
        "matrix must prohibit download, extraction scripts, unconfirmed pattern names, outcome-peeking, public AI upload and individual outputs",
    )

    next_work_ok = (
        isinstance(matrix.get("nextWork"), list)
        and has_text(matrix["nextWork"], "Colectica")
        and has_text(matrix["nextWork"], "cohort-flow")
        and has_text(matrix["nextWork"], "survey-design")
        and has_text(matrix["nextWork"], "disclosure-control")
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-next-work",
        status_from_bool(exists and next_work_ok),
        "next work must point to Colectica, cohort flow, survey design and disclosure control",
    )

    source_trace = matrix.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
    )
    add_check(
        checks,
        "nhats-variable-confirmation-matrix-source-trace",
        status_from_bool(exists and source_trace_ok),
        "source trace must include Cross-Year Search, User Guide, Technical Paper 55, Conditions of Use and R13/R14 file pages",
    )

    return {
        "path": str(matrix_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(matrix_path) if exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_cohort_flow_endpoint_protocol(protocol_path: Path) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    exists = protocol_path.exists()
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-exists",
        status_from_bool(exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    protocol = load_json(protocol_path) if exists else {}

    schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-cohort-flow-endpoint-protocol.v1"
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-schema",
        status_from_bool(exists and schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId") == "nhats-r13-r14-cohort-flow-endpoint-protocol-draft"
        and protocol.get("estimandProtocolId")
        == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and protocol.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and protocol.get("manifestId") == "nhats-r1-r14-effective-time-manifest-draft"
        and protocol.get("fileTierTableId") == "nhats-r13-r14-file-tier-table-draft"
        and protocol.get("status") == "protocol-only-cannot-extract"
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-identity",
        status_from_bool(exists and identity_ok),
        "protocol must bind NHATS source, first estimand, variable matrix, manifest, file-tier table and cannot-extract status",
    )

    decision = protocol.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("cohortFlowRunnable") is False
        and decision.get("endpointRoutingRunnable") is False
        and decision.get("downloadAllowed") is False
        and decision.get("extractionScriptAllowed") is False
        and decision.get("weightedMetricsAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-current-decision",
        status_from_bool(exists and decision_ok),
        "current decision must block cohort flow, endpoint routing, download, extraction scripts, weighted metrics, public export, calibration and individual prediction",
    )

    facts = protocol.get("officialSourceFacts")
    observed_fact_ids: set[str] = set()
    facts_ok = isinstance(facts, list) and len(facts) >= len(
        REQUIRED_NHATS_COHORT_FLOW_SOURCE_FACT_IDS
    )
    source_urls_ok = True
    if isinstance(facts, list):
        for fact in facts:
            if not isinstance(fact, dict):
                facts_ok = False
                continue
            fact_id = fact.get("id")
            if isinstance(fact_id, str):
                observed_fact_ids.add(fact_id)
            url = fact.get("sourceUrl")
            if not isinstance(url, str) or not url.startswith("https://"):
                source_urls_ok = False
            if not str(fact.get("fact", "")).strip() or not str(
                fact.get("modelConsequence", "")
            ).strip():
                facts_ok = False
    missing_fact_ids = sorted(REQUIRED_NHATS_COHORT_FLOW_SOURCE_FACT_IDS - observed_fact_ids)
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-source-facts",
        status_from_bool(exists and facts_ok and source_urls_ok and not missing_fact_ids),
        f"missing_fact_ids={missing_fact_ids}",
    )

    rows = protocol.get("cohortFlowRows")
    observed_row_ids: set[str] = set()
    rows_ok = isinstance(rows, list) and len(rows) >= len(REQUIRED_NHATS_COHORT_FLOW_ROW_IDS)
    if isinstance(rows, list):
        for row in rows:
            if not isinstance(row, dict):
                rows_ok = False
                continue
            row_id = row.get("id")
            if isinstance(row_id, str):
                observed_row_ids.add(row_id)
            if row.get("status") != "missing" or row.get("blocksRun") is not True:
                rows_ok = False
            if not str(row.get("requiredEvidence", "")).strip() or not str(
                row.get("outputArtifact", "")
            ).strip():
                rows_ok = False
    missing_row_ids = sorted(REQUIRED_NHATS_COHORT_FLOW_ROW_IDS - observed_row_ids)
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-flow-rows",
        status_from_bool(exists and rows_ok and not missing_row_ids),
        f"missing_row_ids={missing_row_ids}",
    )

    routes = protocol.get("endpointRouteClasses")
    observed_route_ids: set[str] = set()
    routes_ok = isinstance(routes, list) and len(routes) >= len(REQUIRED_NHATS_ENDPOINT_ROUTE_IDS)
    if isinstance(routes, list):
        for route in routes:
            if not isinstance(route, dict):
                routes_ok = False
                continue
            route_id = route.get("id")
            if isinstance(route_id, str):
                observed_route_ids.add(route_id)
            if route.get("currentStatus") != "unconfirmed":
                routes_ok = False
            if not str(route.get("meaning", "")).strip() or not str(
                route.get("requiredEvidence", "")
            ).strip():
                routes_ok = False
    missing_route_ids = sorted(REQUIRED_NHATS_ENDPOINT_ROUTE_IDS - observed_route_ids)
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-route-classes",
        status_from_bool(exists and routes_ok and not missing_route_ids),
        f"missing_route_ids={missing_route_ids}",
    )

    outputs = protocol.get("analysisOutputContracts")
    observed_output_ids: set[str] = set()
    outputs_ok = isinstance(outputs, list) and len(outputs) >= len(REQUIRED_NHATS_COHORT_OUTPUT_IDS)
    if isinstance(outputs, list):
        for output in outputs:
            if not isinstance(output, dict):
                outputs_ok = False
                continue
            output_id = output.get("id")
            if isinstance(output_id, str):
                observed_output_ids.add(output_id)
            if output.get("rowLevelAllowed") is not False:
                outputs_ok = False
            if output.get("requiresDisclosureReview") is not True:
                outputs_ok = False
            if not str(output.get("meaning", "")).strip():
                outputs_ok = False
    missing_output_ids = sorted(REQUIRED_NHATS_COHORT_OUTPUT_IDS - observed_output_ids)
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-output-contracts",
        status_from_bool(exists and outputs_ok and not missing_output_ids),
        f"missing_output_ids={missing_output_ids}",
    )

    disclosure = protocol.get("disclosureControl")
    disclosure_ok = (
        isinstance(disclosure, dict)
        and disclosure.get("smallCellThreshold") == 5
        and has_text(disclosure.get("smallCellRule", ""), "Counts below 5")
        and disclosure.get("publicAiUploadAllowed") is False
        and disclosure.get("rowLevelExportAllowed") is False
        and disclosure.get("aggregateOnly") is True
        and disclosure.get("status") == "not-ready"
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-disclosure-control",
        status_from_bool(exists and disclosure_ok),
        "disclosure control must enforce n<5 suppression, aggregate-only export, no row-level export and no public AI upload",
    )

    gates = protocol.get("readinessGates")
    observed_gate_ids: set[str] = set()
    gates_ok = isinstance(gates, list) and len(gates) >= len(REQUIRED_NHATS_COHORT_GATE_IDS)
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksRun") is not True:
                gates_ok = False
            if not str(gate.get("requiredEvidence", "")).strip():
                gates_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_COHORT_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-readiness-gates",
        status_from_bool(exists and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    summary = protocol.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_COHORT_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_NHATS_COHORT_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_COHORT_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-gate-summary",
        status_from_bool(exists and summary_ok),
        "gate summary must keep every cohort-flow and endpoint-routing gate missing and blocking",
    )

    prohibited = protocol.get("prohibitedActions")
    prohibited_ok = (
        isinstance(prohibited, list)
        and has_text(prohibited, "download")
        and has_text(prohibited, "extraction scripts")
        and has_text(prohibited, "candidate field names")
        and has_text(prohibited, "row-level")
        and has_text(prohibited, "individual death-date")
        and has_text(prohibited, "public AI")
        and has_text(prohibited, "small-cell")
        and has_text(prohibited, "calibration")
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-prohibited-actions",
        status_from_bool(exists and prohibited_ok),
        "protocol must prohibit download, scripts, candidate-name routing, row-level export, individual death-date prediction, public AI upload, small-cell export and calibration claims",
    )

    next_work_ok = (
        isinstance(protocol.get("nextWork"), list)
        and has_text(protocol["nextWork"], "Colectica")
        and has_text(protocol["nextWork"], "canonical public annual")
        and has_text(protocol["nextWork"], "cohort-flow")
        and has_text(protocol["nextWork"], "missingness")
        and has_text(protocol["nextWork"], "disclosure-control")
        and has_text(protocol["nextWork"], "survey-design")
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-next-work",
        status_from_bool(exists and next_work_ok),
        "next work must point to Colectica route fields, canonical files, cohort-flow table, missingness map, disclosure control and survey design",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
    )
    add_check(
        checks,
        "nhats-cohort-flow-endpoint-protocol-source-trace",
        status_from_bool(exists and source_trace_ok),
        "source trace must include Cross-Year Search, Conditions, User Guide, Technical Paper 55 and R13/R14 file pages",
    )

    return {
        "path": str(protocol_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(protocol_path) if exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_disclosure_control(
    policy_path: Path,
    test_cases_path: Path,
    validation_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    policy_exists = policy_path.exists()
    test_cases_exists = test_cases_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-disclosure-policy-exists",
        status_from_bool(policy_exists),
        str(policy_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-disclosure-test-cases-exist",
        status_from_bool(test_cases_exists),
        str(test_cases_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-disclosure-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    policy = load_json(policy_path) if policy_exists else {}
    test_cases = load_json(test_cases_path) if test_cases_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    policy_schema_ok = (
        policy.get("schemaVersion")
        == "human-infra.life-path-nhats-disclosure-control-policy.v1"
    )
    add_check(
        checks,
        "nhats-disclosure-policy-schema",
        status_from_bool(policy_exists and policy_schema_ok),
        f"schemaVersion={policy.get('schemaVersion')!r}",
    )

    policy_identity_ok = (
        policy.get("sourceId") == "nhats"
        and policy.get("policyId") == "nhats-r13-r14-disclosure-control-policy-draft"
        and policy.get("cohortFlowEndpointProtocolId")
        == "nhats-r13-r14-cohort-flow-endpoint-protocol-draft"
        and policy.get("estimandProtocolId")
        == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and policy.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and policy.get("status") == "policy-draft-validator-required"
    )
    add_check(
        checks,
        "nhats-disclosure-policy-identity",
        status_from_bool(policy_exists and policy_identity_ok),
        "policy must bind NHATS source, cohort-flow protocol, first estimand, variable matrix and draft status",
    )

    decision = policy.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("publicExportAllowed") is False
        and decision.get("rowLevelExportAllowed") is False
        and decision.get("publicAiUploadAllowed") is False
        and decision.get("smallCellExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-disclosure-policy-current-decision",
        status_from_bool(policy_exists and decision_ok),
        "policy must block public export, row-level export, public AI upload, small-cell export, calibration and individual prediction",
    )

    rules = policy.get("rules")
    allowed_output_types = set(rules.get("allowedOutputTypes", [])) if isinstance(rules, dict) else set()
    forbidden_output_types = set(rules.get("forbiddenOutputTypes", [])) if isinstance(rules, dict) else set()
    rules_ok = (
        isinstance(rules, dict)
        and rules.get("aggregateOnly") is True
        and rules.get("smallCellThreshold") == 5
        and REQUIRED_NHATS_DISCLOSURE_OUTPUT_TYPES.issubset(allowed_output_types)
        and {"row_level_records", "individual_death_date_prediction", "calibration_claim"}.issubset(
            forbidden_output_types
        )
        and has_text(rules.get("publicAiUploadRule", ""), "public LLM")
        and has_text(rules.get("rowLevelRule", ""), "Row-level")
    )
    add_check(
        checks,
        "nhats-disclosure-policy-rules",
        status_from_bool(policy_exists and rules_ok),
        "policy rules must require aggregate-only output, n<5 suppression, allowed aggregate outputs, forbidden unsafe outputs, row-level block and public-AI block",
    )

    source_trace = policy.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
    )
    add_check(
        checks,
        "nhats-disclosure-policy-source-trace",
        status_from_bool(policy_exists and source_trace_ok),
        "policy source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55",
    )

    cases_schema_ok = (
        test_cases.get("schemaVersion")
        == "human-infra.life-path-nhats-disclosure-control-test-cases.v1"
        and test_cases.get("sourceId") == "nhats"
        and test_cases.get("policyId") == "nhats-r13-r14-disclosure-control-policy-draft"
        and test_cases.get("status") == "synthetic-only-no-real-nhats-data"
    )
    add_check(
        checks,
        "nhats-disclosure-test-cases-schema",
        status_from_bool(test_cases_exists and cases_schema_ok),
        "test cases must bind NHATS source and synthetic-only policy status",
    )

    boundary = test_cases.get("currentBoundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("containsRealNhatsData") is False
        and boundary.get("containsSyntheticOnly") is True
        and boundary.get("publicExportProofOnly") is True
        and boundary.get("calibrationAllowed") is False
        and boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-disclosure-test-cases-boundary",
        status_from_bool(test_cases_exists and boundary_ok),
        "test cases must be synthetic-only and prohibit calibration plus individual prediction",
    )

    cases = test_cases.get("cases")
    observed_case_ids: set[str] = set()
    expected_mix_ok = False
    if isinstance(cases, list):
        expected_decisions = {
            str(case.get("expectedDecision"))
            for case in cases
            if isinstance(case, dict)
        }
        expected_mix_ok = {"allow-export", "block-export"}.issubset(expected_decisions)
        for case in cases:
            if isinstance(case, dict) and isinstance(case.get("id"), str):
                observed_case_ids.add(case["id"])
    missing_case_ids = sorted(REQUIRED_NHATS_DISCLOSURE_CASE_IDS - observed_case_ids)
    add_check(
        checks,
        "nhats-disclosure-test-case-coverage",
        status_from_bool(test_cases_exists and isinstance(cases, list) and not missing_case_ids),
        f"missing_case_ids={missing_case_ids}",
    )
    add_check(
        checks,
        "nhats-disclosure-test-case-decision-mix",
        status_from_bool(test_cases_exists and expected_mix_ok),
        "synthetic cases must include both allowed and blocked examples",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-disclosure-control-validation.v1"
    )
    add_check(
        checks,
        "nhats-disclosure-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_paths_ok = (
        validation.get("policyPath") == str(policy_path.relative_to(REPO_ROOT))
        and validation.get("policySha256") == sha256_file(policy_path)
        and validation.get("testCasesPath") == str(test_cases_path.relative_to(REPO_ROOT))
        and validation.get("testCasesSha256") == sha256_file(test_cases_path)
    )
    add_check(
        checks,
        "nhats-disclosure-validation-source-hashes",
        status_from_bool(validation_exists and validation_paths_ok),
        "validation report must point back to current policy and test-case hashes",
    )

    summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(summary, dict)
        and summary.get("caseCount", 0) >= len(REQUIRED_NHATS_DISCLOSURE_CASE_IDS)
        and summary.get("fail") == 0
        and summary.get("allowedCount", 0) > 0
        and summary.get("blockedCount", 0) > 0
        and summary.get("policyIssueCount") == 0
        and summary.get("boundaryIssueCount") == 0
    )
    add_check(
        checks,
        "nhats-disclosure-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "validation report must pass every synthetic case and include both allowed and blocked outputs",
    )

    validation_cases = validation.get("cases")
    validation_cases_ok = isinstance(validation_cases, list)
    validation_case_ids: set[str] = set()
    if isinstance(validation_cases, list):
        for case in validation_cases:
            if not isinstance(case, dict):
                validation_cases_ok = False
                continue
            case_id = case.get("id")
            if isinstance(case_id, str):
                validation_case_ids.add(case_id)
            if case.get("status") != "PASS":
                validation_cases_ok = False
            if case.get("observedDecision") != case.get("expectedDecision"):
                validation_cases_ok = False
    missing_validation_case_ids = sorted(
        REQUIRED_NHATS_DISCLOSURE_CASE_IDS - validation_case_ids
    )
    add_check(
        checks,
        "nhats-disclosure-validation-case-results",
        status_from_bool(validation_exists and validation_cases_ok and not missing_validation_case_ids),
        f"missing_validation_case_ids={missing_validation_case_ids}",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        isinstance(validation_boundary, dict)
        and validation_boundary.get("containsRealNhatsData") is False
        and validation_boundary.get("containsSyntheticOnly") is True
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-disclosure-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries",
    )

    return {
        "policyPath": str(policy_path.relative_to(REPO_ROOT)),
        "policySha256": sha256_file(policy_path) if policy_exists else None,
        "testCasesPath": str(test_cases_path.relative_to(REPO_ROOT)),
        "testCasesSha256": sha256_file(test_cases_path) if test_cases_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_survey_design(
    protocol_path: Path,
    test_cases_path: Path,
    validation_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    protocol_exists = protocol_path.exists()
    test_cases_exists = test_cases_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-survey-design-protocol-exists",
        status_from_bool(protocol_exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-survey-design-test-cases-exist",
        status_from_bool(test_cases_exists),
        str(test_cases_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-survey-design-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    protocol = load_json(protocol_path) if protocol_exists else {}
    test_cases = load_json(test_cases_path) if test_cases_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    protocol_schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-survey-design-protocol.v1"
    )
    add_check(
        checks,
        "nhats-survey-design-protocol-schema",
        status_from_bool(protocol_exists and protocol_schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    protocol_identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId") == "nhats-r13-r14-survey-design-protocol-draft"
        and protocol.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and protocol.get("fileTierTableId") == "nhats-r13-r14-file-tier-table-draft"
        and protocol.get("estimandProtocolId")
        == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and protocol.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and protocol.get("cohortFlowEndpointProtocolId")
        == "nhats-r13-r14-cohort-flow-endpoint-protocol-draft"
        and protocol.get("disclosureControlPolicyId")
        == "nhats-r13-r14-disclosure-control-policy-draft"
        and protocol.get("status") == "protocol-only-cannot-weight-yet"
    )
    add_check(
        checks,
        "nhats-survey-design-protocol-identity",
        status_from_bool(protocol_exists and protocol_identity_ok),
        "survey-design protocol must bind NHATS source, upstream readiness/file/estimand/variable/cohort/disclosure contracts and cannot-weight status",
    )

    decision = protocol.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("surveyDesignReady") is False
        and decision.get("weightedCountsAllowed") is False
        and decision.get("weightedCurvesAllowed") is False
        and decision.get("varianceEstimationAllowed") is False
        and decision.get("populationInferenceAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-survey-design-current-decision",
        status_from_bool(protocol_exists and decision_ok),
        "survey-design protocol must block weighted counts, weighted curves, variance estimation, population inference, public export, calibration and individual prediction",
    )

    components = protocol.get("requiredDesignComponents")
    observed_component_ids: set[str] = set()
    components_ok = True
    if isinstance(components, list):
        for component in components:
            if not isinstance(component, dict):
                components_ok = False
                continue
            component_id = component.get("id")
            if isinstance(component_id, str):
                observed_component_ids.add(component_id)
            if component.get("status") != "missing" or component.get("blocksWeightedEstimate") is not True:
                components_ok = False
            if not str(component.get("minimumEvidence", "")).strip():
                components_ok = False
    missing_components = sorted(
        REQUIRED_NHATS_SURVEY_DESIGN_COMPONENT_IDS - observed_component_ids
    )
    add_check(
        checks,
        "nhats-survey-design-component-coverage",
        status_from_bool(protocol_exists and isinstance(components, list) and components_ok and not missing_components),
        f"missing_component_ids={missing_components}",
    )

    candidate_fields = protocol.get("candidateFieldFamilies")
    candidate_fields_ok = (
        isinstance(candidate_fields, list)
        and has_text(candidate_fields, "w#anfinwgt0")
        and has_text(candidate_fields, "w#varunit")
        and has_text(candidate_fields, "w#varstrat")
    )
    if isinstance(candidate_fields, list):
        for candidate in candidate_fields:
            if not isinstance(candidate, dict) or candidate.get("status") != "candidate-pattern-only":
                candidate_fields_ok = False
    add_check(
        checks,
        "nhats-survey-design-candidate-fields",
        status_from_bool(protocol_exists and candidate_fields_ok),
        "candidate field families must include weight, variance-unit and stratum patterns while staying candidate-pattern-only",
    )

    gates = protocol.get("readinessGates")
    observed_gate_ids: set[str] = set()
    gates_ok = True
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksWeightedEstimate") is not True:
                gates_ok = False
            if not str(gate.get("requiredEvidence", "")).strip():
                gates_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_SURVEY_DESIGN_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-survey-design-readiness-gates",
        status_from_bool(protocol_exists and isinstance(gates, list) and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    summary = protocol.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_SURVEY_DESIGN_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_NHATS_SURVEY_DESIGN_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_SURVEY_DESIGN_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-survey-design-gate-summary",
        status_from_bool(protocol_exists and summary_ok),
        "gate summary must keep every survey-design gate missing and blocking",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
    )
    add_check(
        checks,
        "nhats-survey-design-source-trace",
        status_from_bool(protocol_exists and source_trace_ok),
        "survey-design protocol source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55",
    )

    prohibited_ok = (
        has_text(protocol.get("prohibitedActions", []), "weighted NHATS counts")
        and has_text(protocol.get("prohibitedActions", []), "weighted curves")
        and has_text(protocol.get("prohibitedActions", []), "population-inference")
        and has_text(protocol.get("prohibitedActions", []), "candidate field patterns")
        and has_text(protocol.get("prohibitedActions", []), "individual death dates")
    )
    add_check(
        checks,
        "nhats-survey-design-prohibited-actions",
        status_from_bool(protocol_exists and prohibited_ok),
        "survey-design protocol must prohibit premature weighted estimates, population inference, candidate-field overuse and individual outputs",
    )

    cases_schema_ok = (
        test_cases.get("schemaVersion")
        == "human-infra.life-path-nhats-survey-design-test-cases.v1"
        and test_cases.get("sourceId") == "nhats"
        and test_cases.get("protocolId") == "nhats-r13-r14-survey-design-protocol-draft"
        and test_cases.get("status") == "synthetic-only-no-real-nhats-data"
    )
    add_check(
        checks,
        "nhats-survey-design-test-cases-schema",
        status_from_bool(test_cases_exists and cases_schema_ok),
        "survey-design test cases must bind NHATS source and synthetic-only protocol status",
    )

    boundary = test_cases.get("currentBoundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("containsRealNhatsData") is False
        and boundary.get("containsSyntheticOnly") is True
        and boundary.get("surveyDesignProofOnly") is True
        and boundary.get("calibrationAllowed") is False
        and boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-survey-design-test-cases-boundary",
        status_from_bool(test_cases_exists and boundary_ok),
        "survey-design test cases must be synthetic-only and prohibit calibration plus individual prediction",
    )

    cases = test_cases.get("cases")
    observed_case_ids: set[str] = set()
    expected_mix_ok = False
    if isinstance(cases, list):
        expected_decisions = {
            str(case.get("expectedDecision"))
            for case in cases
            if isinstance(case, dict)
        }
        expected_mix_ok = {
            "allow-weighted-diagnostics",
            "block-weighted-estimate",
        }.issubset(expected_decisions)
        for case in cases:
            if isinstance(case, dict) and isinstance(case.get("id"), str):
                observed_case_ids.add(case["id"])
    missing_case_ids = sorted(REQUIRED_NHATS_SURVEY_DESIGN_CASE_IDS - observed_case_ids)
    add_check(
        checks,
        "nhats-survey-design-test-case-coverage",
        status_from_bool(test_cases_exists and isinstance(cases, list) and not missing_case_ids),
        f"missing_case_ids={missing_case_ids}",
    )
    add_check(
        checks,
        "nhats-survey-design-test-case-decision-mix",
        status_from_bool(test_cases_exists and expected_mix_ok),
        "synthetic survey-design cases must include both allowed diagnostics and blocked estimate examples",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-survey-design-validation.v1"
    )
    add_check(
        checks,
        "nhats-survey-design-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_paths_ok = (
        validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
        and validation.get("testCasesPath") == str(test_cases_path.relative_to(REPO_ROOT))
        and validation.get("testCasesSha256") == sha256_file(test_cases_path)
    )
    add_check(
        checks,
        "nhats-survey-design-validation-source-hashes",
        status_from_bool(validation_exists and validation_paths_ok),
        "survey-design validation report must point back to current protocol and test-case hashes",
    )

    validation_summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation_summary, dict)
        and validation_summary.get("caseCount", 0) >= len(REQUIRED_NHATS_SURVEY_DESIGN_CASE_IDS)
        and validation_summary.get("fail") == 0
        and validation_summary.get("allowedCount", 0) > 0
        and validation_summary.get("blockedCount", 0) > 0
        and validation_summary.get("protocolIssueCount") == 0
        and validation_summary.get("boundaryIssueCount") == 0
    )
    add_check(
        checks,
        "nhats-survey-design-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "survey-design validation report must pass every synthetic case and include both allowed and blocked results",
    )

    validation_cases = validation.get("cases")
    validation_cases_ok = isinstance(validation_cases, list)
    validation_case_ids: set[str] = set()
    if isinstance(validation_cases, list):
        for case in validation_cases:
            if not isinstance(case, dict):
                validation_cases_ok = False
                continue
            case_id = case.get("id")
            if isinstance(case_id, str):
                validation_case_ids.add(case_id)
            if case.get("status") != "PASS":
                validation_cases_ok = False
            if case.get("observedDecision") != case.get("expectedDecision"):
                validation_cases_ok = False
    missing_validation_case_ids = sorted(
        REQUIRED_NHATS_SURVEY_DESIGN_CASE_IDS - validation_case_ids
    )
    add_check(
        checks,
        "nhats-survey-design-validation-case-results",
        status_from_bool(validation_exists and validation_cases_ok and not missing_validation_case_ids),
        f"missing_validation_case_ids={missing_validation_case_ids}",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        isinstance(validation_boundary, dict)
        and validation_boundary.get("containsRealNhatsData") is False
        and validation_boundary.get("containsSyntheticOnly") is True
        and validation_boundary.get("surveyDesignProofOnly") is True
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-survey-design-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "survey-design validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries",
    )

    return {
        "protocolPath": str(protocol_path.relative_to(REPO_ROOT)),
        "protocolSha256": sha256_file(protocol_path) if protocol_exists else None,
        "testCasesPath": str(test_cases_path.relative_to(REPO_ROOT)),
        "testCasesSha256": sha256_file(test_cases_path) if test_cases_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_missingness_route(
    protocol_path: Path,
    test_cases_path: Path,
    validation_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    protocol_exists = protocol_path.exists()
    test_cases_exists = test_cases_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-missingness-route-protocol-exists",
        status_from_bool(protocol_exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-missingness-route-test-cases-exist",
        status_from_bool(test_cases_exists),
        str(test_cases_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    protocol = load_json(protocol_path) if protocol_exists else {}
    test_cases = load_json(test_cases_path) if test_cases_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    protocol_schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-missingness-route-protocol.v1"
    )
    add_check(
        checks,
        "nhats-missingness-route-protocol-schema",
        status_from_bool(protocol_exists and protocol_schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    protocol_identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and protocol.get("acquisitionReadinessId") == "nhats-acquisition-readiness-2026-07-02"
        and protocol.get("fileTierTableId") == "nhats-r13-r14-file-tier-table-draft"
        and protocol.get("estimandProtocolId")
        == "nhats-r13-r14-functional-survival-estimand-protocol-draft"
        and protocol.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and protocol.get("cohortFlowEndpointProtocolId")
        == "nhats-r13-r14-cohort-flow-endpoint-protocol-draft"
        and protocol.get("disclosureControlPolicyId")
        == "nhats-r13-r14-disclosure-control-policy-draft"
        and protocol.get("surveyDesignProtocolId")
        == "nhats-r13-r14-survey-design-protocol-draft"
        and protocol.get("status") == "protocol-only-cannot-route-yet"
    )
    add_check(
        checks,
        "nhats-missingness-route-protocol-identity",
        status_from_bool(protocol_exists and protocol_identity_ok),
        "missingness-route protocol must bind NHATS source, upstream readiness/file/estimand/variable/cohort/disclosure/survey contracts and cannot-route status",
    )

    decision = protocol.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("routeMapReady") is False
        and decision.get("endpointClassificationAllowed") is False
        and decision.get("missingnessRateAllowed") is False
        and decision.get("weightedRouteCountsAllowed") is False
        and decision.get("functionalSurvivalCurveAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-missingness-route-current-decision",
        status_from_bool(protocol_exists and decision_ok),
        "missingness-route protocol must block endpoint classification, missingness rates, weighted route counts, functional-survival curves, public export, calibration and individual prediction",
    )

    route_classes = protocol.get("requiredRouteClasses")
    observed_route_class_ids: set[str] = set()
    route_classes_ok = True
    if isinstance(route_classes, list):
        for route_class in route_classes:
            if not isinstance(route_class, dict):
                route_classes_ok = False
                continue
            route_class_id = route_class.get("id")
            if isinstance(route_class_id, str):
                observed_route_class_ids.add(route_class_id)
            if (
                route_class.get("status") != "unconfirmed"
                or route_class.get("blocksEndpointClassification") is not True
            ):
                route_classes_ok = False
            if not str(route_class.get("minimumEvidence", "")).strip():
                route_classes_ok = False
    missing_route_classes = sorted(
        REQUIRED_NHATS_MISSINGNESS_ROUTE_CLASS_IDS - observed_route_class_ids
    )
    add_check(
        checks,
        "nhats-missingness-route-class-coverage",
        status_from_bool(protocol_exists and isinstance(route_classes, list) and route_classes_ok and not missing_route_classes),
        f"missing_route_class_ids={missing_route_classes}",
    )

    route_fields = protocol.get("requiredRouteFields")
    observed_route_field_ids: set[str] = set()
    route_fields_ok = True
    if isinstance(route_fields, list):
        for route_field in route_fields:
            if not isinstance(route_field, dict):
                route_fields_ok = False
                continue
            route_field_id = route_field.get("id")
            if isinstance(route_field_id, str):
                observed_route_field_ids.add(route_field_id)
            if (
                route_field.get("status") != "missing"
                or route_field.get("blocksEndpointClassification") is not True
            ):
                route_fields_ok = False
            if not str(route_field.get("minimumEvidence", "")).strip():
                route_fields_ok = False
    missing_route_fields = sorted(
        REQUIRED_NHATS_MISSINGNESS_ROUTE_FIELD_IDS - observed_route_field_ids
    )
    add_check(
        checks,
        "nhats-missingness-route-field-coverage",
        status_from_bool(protocol_exists and isinstance(route_fields, list) and route_fields_ok and not missing_route_fields),
        f"missing_route_field_ids={missing_route_fields}",
    )

    candidate_fields = protocol.get("candidateFieldFamilies")
    candidate_fields_ok = (
        isinstance(candidate_fields, list)
        and has_text(candidate_fields, "sample-person identifier")
        and has_text(candidate_fields, "interview-status")
        and has_text(candidate_fields, "proxy")
        and has_text(candidate_fields, "residential")
        and has_text(candidate_fields, "death")
        and has_text(candidate_fields, "negative-value missing-code")
    )
    if isinstance(candidate_fields, list):
        for candidate in candidate_fields:
            if not isinstance(candidate, dict) or candidate.get("status") != "candidate-pattern-only":
                candidate_fields_ok = False
    add_check(
        checks,
        "nhats-missingness-route-candidate-fields",
        status_from_bool(protocol_exists and candidate_fields_ok),
        "candidate field families must cover identity, interview status, proxy, residential, death and missing codes while staying candidate-pattern-only",
    )

    dominance_rules = protocol.get("dominanceRules")
    dominance_rules_ok = (
        isinstance(dominance_rules, list)
        and has_text(dominance_rules, "death-boundary-dominates-functional-state")
        and has_text(dominance_rules, "missingness-is-not-outcome")
        and has_text(dominance_rules, "proxy-and-facility-stay-separate")
        and has_text(dominance_rules, "not-classifiable-keeps-denominator")
        and has_text(dominance_rules, "small-cell-suppression-before-public-export")
    )
    add_check(
        checks,
        "nhats-missingness-route-dominance-rules",
        status_from_bool(protocol_exists and dominance_rules_ok),
        "dominance rules must register death dominance, missingness blocking, proxy/facility separation, denominator handling and small-cell suppression",
    )

    gates = protocol.get("readinessGates")
    observed_gate_ids: set[str] = set()
    gates_ok = True
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksEndpointClassification") is not True:
                gates_ok = False
            if not str(gate.get("requiredEvidence", "")).strip():
                gates_ok = False
    missing_gate_ids = sorted(REQUIRED_NHATS_MISSINGNESS_ROUTE_GATE_IDS - observed_gate_ids)
    add_check(
        checks,
        "nhats-missingness-route-readiness-gates",
        status_from_bool(protocol_exists and isinstance(gates, list) and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    summary = protocol.get("gateSummary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("requiredGateCount") == len(REQUIRED_NHATS_MISSINGNESS_ROUTE_GATE_IDS)
        and summary.get("readyGateCount") == 0
        and summary.get("missingGateCount") == len(REQUIRED_NHATS_MISSINGNESS_ROUTE_GATE_IDS)
        and summary.get("blockingGateCount") == len(REQUIRED_NHATS_MISSINGNESS_ROUTE_GATE_IDS)
    )
    add_check(
        checks,
        "nhats-missingness-route-gate-summary",
        status_from_bool(protocol_exists and summary_ok),
        "gate summary must keep every missingness-route gate missing and blocking",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "nhats/13")
        and has_text(source_trace, "nhats/14")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSTechnicalPaper55")
    )
    add_check(
        checks,
        "nhats-missingness-route-source-trace",
        status_from_bool(protocol_exists and source_trace_ok),
        "missingness-route protocol source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55",
    )

    prohibited_ok = (
        has_text(protocol.get("prohibitedActions", []), "exact route fields")
        and has_text(protocol.get("prohibitedActions", []), "missingness")
        and has_text(protocol.get("prohibitedActions", []), "weighted route counts")
        and has_text(protocol.get("prohibitedActions", []), "public AI")
        and has_text(protocol.get("prohibitedActions", []), "individual death dates")
    )
    add_check(
        checks,
        "nhats-missingness-route-prohibited-actions",
        status_from_bool(protocol_exists and prohibited_ok),
        "missingness-route protocol must prohibit premature routing, missingness-as-outcome, weighted route counts, public AI upload and individual death-date outputs",
    )

    cases_schema_ok = (
        test_cases.get("schemaVersion")
        == "human-infra.life-path-nhats-missingness-route-test-cases.v1"
        and test_cases.get("sourceId") == "nhats"
        and test_cases.get("protocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and test_cases.get("status") == "synthetic-only-no-real-nhats-data"
    )
    add_check(
        checks,
        "nhats-missingness-route-test-cases-schema",
        status_from_bool(test_cases_exists and cases_schema_ok),
        "missingness-route test cases must bind NHATS source and synthetic-only protocol status",
    )

    boundary = test_cases.get("currentBoundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("containsRealNhatsData") is False
        and boundary.get("containsSyntheticOnly") is True
        and boundary.get("routeMapProofOnly") is True
        and boundary.get("calibrationAllowed") is False
        and boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-missingness-route-test-cases-boundary",
        status_from_bool(test_cases_exists and boundary_ok),
        "missingness-route test cases must be synthetic-only and prohibit calibration plus individual prediction",
    )

    cases = test_cases.get("cases")
    observed_case_ids: set[str] = set()
    expected_mix_ok = False
    if isinstance(cases, list):
        expected_decisions = {
            str(case.get("expectedDecision"))
            for case in cases
            if isinstance(case, dict)
        }
        expected_mix_ok = {
            "allow-route-classification",
            "block-route-classification",
        }.issubset(expected_decisions)
        for case in cases:
            if isinstance(case, dict) and isinstance(case.get("id"), str):
                observed_case_ids.add(case["id"])
    missing_case_ids = sorted(REQUIRED_NHATS_MISSINGNESS_ROUTE_CASE_IDS - observed_case_ids)
    add_check(
        checks,
        "nhats-missingness-route-test-case-coverage",
        status_from_bool(test_cases_exists and isinstance(cases, list) and not missing_case_ids),
        f"missing_case_ids={missing_case_ids}",
    )
    add_check(
        checks,
        "nhats-missingness-route-test-case-decision-mix",
        status_from_bool(test_cases_exists and expected_mix_ok),
        "synthetic missingness-route cases must include both allowed route classifications and blocked endpoint examples",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-missingness-route-validation.v1"
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_paths_ok = (
        validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
        and validation.get("testCasesPath") == str(test_cases_path.relative_to(REPO_ROOT))
        and validation.get("testCasesSha256") == sha256_file(test_cases_path)
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-source-hashes",
        status_from_bool(validation_exists and validation_paths_ok),
        "missingness-route validation report must point back to current protocol and test-case hashes",
    )

    validation_summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation_summary, dict)
        and validation_summary.get("caseCount", 0)
        >= len(REQUIRED_NHATS_MISSINGNESS_ROUTE_CASE_IDS)
        and validation_summary.get("fail") == 0
        and validation_summary.get("allowedCount", 0) > 0
        and validation_summary.get("blockedCount", 0) > 0
        and validation_summary.get("protocolIssueCount") == 0
        and validation_summary.get("boundaryIssueCount") == 0
        and validation_summary.get("routeCoverageOk") is True
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "missingness-route validation report must pass every synthetic case, include allow/block results and cover route classes",
    )

    validation_cases = validation.get("cases")
    validation_cases_ok = isinstance(validation_cases, list)
    validation_case_ids: set[str] = set()
    validation_route_classes: set[str] = set()
    if isinstance(validation_cases, list):
        for case in validation_cases:
            if not isinstance(case, dict):
                validation_cases_ok = False
                continue
            case_id = case.get("id")
            if isinstance(case_id, str):
                validation_case_ids.add(case_id)
            route_class = case.get("observedRouteClass")
            if isinstance(route_class, str):
                validation_route_classes.add(route_class)
            if case.get("status") != "PASS":
                validation_cases_ok = False
            if case.get("observedDecision") != case.get("expectedDecision"):
                validation_cases_ok = False
    missing_validation_case_ids = sorted(
        REQUIRED_NHATS_MISSINGNESS_ROUTE_CASE_IDS - validation_case_ids
    )
    route_validation_ok = {
        "alive_self_interview",
        "alive_proxy_interview",
        "alive_facility_or_residential_route",
        "decedent_or_death_boundary",
        "missing_or_nonresponse",
        "not_classifiable",
        "suppressed_small_cell",
    }.issubset(validation_route_classes)
    add_check(
        checks,
        "nhats-missingness-route-validation-case-results",
        status_from_bool(validation_exists and validation_cases_ok and not missing_validation_case_ids),
        f"missing_validation_case_ids={missing_validation_case_ids}",
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-route-coverage",
        status_from_bool(validation_exists and route_validation_ok),
        f"observed_route_classes={sorted(validation_route_classes)}",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        isinstance(validation_boundary, dict)
        and validation_boundary.get("containsRealNhatsData") is False
        and validation_boundary.get("containsSyntheticOnly") is True
        and validation_boundary.get("routeMapProofOnly") is True
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-missingness-route-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "missingness-route validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries",
    )

    return {
        "protocolPath": str(protocol_path.relative_to(REPO_ROOT)),
        "protocolSha256": sha256_file(protocol_path) if protocol_exists else None,
        "testCasesPath": str(test_cases_path.relative_to(REPO_ROOT)),
        "testCasesSha256": sha256_file(test_cases_path) if test_cases_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_route_field_discovery(
    register_path: Path,
    validation_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    register_exists = register_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-route-field-discovery-register-exists",
        status_from_bool(register_exists),
        str(register_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-route-field-discovery-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    register = load_json(register_path) if register_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    schema_ok = (
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-route-field-discovery-register.v1"
    )
    add_check(
        checks,
        "nhats-route-field-discovery-schema",
        status_from_bool(register_exists and schema_ok),
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("registerId")
        == "nhats-r13-r14-route-field-discovery-register-draft"
        and register.get("routeProtocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and register.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and register.get("status") == "crosswalk-confirmed-colectica-pending-cannot-route"
    )
    add_check(
        checks,
        "nhats-route-field-discovery-identity",
        status_from_bool(register_exists and identity_ok),
        "register must bind NHATS, route protocol, variable confirmation matrix and cannot-route status",
    )

    decision = register.get("fieldDiscoveryDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("routeFieldsDiscoveredFromOfficialCrosswalk") is True
        and decision.get("colecticaValueLabelsConfirmed") is False
        and decision.get("publicUseDataDownloaded") is False
        and decision.get("routeClassifierAllowed") is False
        and decision.get("endpointClassificationAllowed") is False
        and decision.get("weightedRouteCountsAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-route-field-discovery-current-decision",
        status_from_bool(register_exists and decision_ok),
        "crosswalk field discovery may be true, but Colectica, data download, classifier, endpoint, weighted counts, public export, calibration and individual prediction must remain false",
    )

    evidence = register.get("sourceEvidence")
    observed_evidence_ids: set[str] = set()
    evidence_ok = isinstance(evidence, list)
    if isinstance(evidence, list):
        for row in evidence:
            if not isinstance(row, dict):
                evidence_ok = False
                continue
            evidence_id = row.get("id")
            if isinstance(evidence_id, str):
                observed_evidence_ids.add(evidence_id)
            if not (
                isinstance(row.get("url"), str)
                and row["url"].startswith("https://")
                and isinstance(row.get("supports"), list)
                and isinstance(row.get("doesNotSupport"), list)
            ):
                evidence_ok = False
    missing_evidence_ids = sorted(
        REQUIRED_NHATS_ROUTE_FIELD_DISCOVERY_EVIDENCE_IDS - observed_evidence_ids
    )
    add_check(
        checks,
        "nhats-route-field-discovery-source-evidence",
        status_from_bool(register_exists and evidence_ok and not missing_evidence_ids),
        f"missing_evidence_ids={missing_evidence_ids}",
    )

    families = register.get("routeFieldFamilies")
    observed_field_ids: set[str] = set()
    families_ok = isinstance(families, list)
    if isinstance(families, list):
        for family in families:
            if not isinstance(family, dict):
                families_ok = False
                continue
            field_id = family.get("requiredRouteFieldId")
            if isinstance(field_id, str):
                observed_field_ids.add(field_id)
            if (
                family.get("classificationReadiness") is not False
                or not str(family.get("status", "")).strip()
                or not isinstance(family.get("candidateVariables"), dict)
                or not isinstance(family.get("evidenceIds"), list)
                or not isinstance(family.get("remainingChecks"), list)
            ):
                families_ok = False
    missing_field_ids = sorted(
        REQUIRED_NHATS_MISSINGNESS_ROUTE_FIELD_IDS - observed_field_ids
    )
    add_check(
        checks,
        "nhats-route-field-discovery-field-families",
        status_from_bool(register_exists and families_ok and not missing_field_ids),
        f"missing_field_ids={missing_field_ids}",
    )

    death_family: dict[str, Any] = {}
    if isinstance(families, list):
        death_family = next(
            (
                family
                for family in families
                if isinstance(family, dict)
                and family.get("requiredRouteFieldId") == "death_decedent_indicator"
            ),
            {},
        )
    sensitive_excluded: set[str] = set()
    if isinstance(death_family, dict):
        sensitive = death_family.get("sensitiveExcludedVariables")
        if isinstance(sensitive, dict):
            for values in sensitive.values():
                if isinstance(values, list):
                    sensitive_excluded.update(str(value) for value in values)
    sensitive_ok = {
        "dm13mthdied",
        "dm13yrdied",
        "dm14mthdied",
        "dm14yrdied",
    }.issubset(sensitive_excluded)
    add_check(
        checks,
        "nhats-route-field-discovery-sensitive-death-exclusion",
        status_from_bool(
            register_exists
            and sensitive_ok
            and has_text(register.get("prohibitedActions", []), "individual death dates")
        ),
        f"sensitive_excluded={sorted(sensitive_excluded)}",
    )

    gates = register.get("blockingGates")
    observed_gate_ids: set[str] = set()
    gates_ok = isinstance(gates, list)
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksRouteClassification") is not True:
                gates_ok = False
    missing_gate_ids = sorted(
        REQUIRED_NHATS_ROUTE_FIELD_DISCOVERY_GATE_IDS - observed_gate_ids
    )
    add_check(
        checks,
        "nhats-route-field-discovery-blocking-gates",
        status_from_bool(register_exists and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    prohibited = register.get("prohibitedActions", [])
    prohibited_ok = (
        has_text(prohibited, "classify real NHATS records")
        and has_text(prohibited, "weighted route counts")
        and has_text(prohibited, "public AI")
        and has_text(prohibited, "individual death dates")
        and has_text(prohibited, "Colectica value-label confirmation")
    )
    add_check(
        checks,
        "nhats-route-field-discovery-prohibited-actions",
        status_from_bool(register_exists and prohibited_ok),
        "register must block real routing, weighted counts, public AI upload, individual death dates and crosswalk-as-Colectica substitution",
    )

    source_trace = register.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSR13Instrument-VariableCrosswalk")
        and has_text(source_trace, "NHATSR14Instrument-VariableCrosswalk")
    )
    add_check(
        checks,
        "nhats-route-field-discovery-source-trace",
        status_from_bool(register_exists and source_trace_ok),
        "sourceTrace must include official Colectica, conditions, User Guide and R13/R14 crosswalk URLs",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-route-field-discovery-validation.v1"
    )
    add_check(
        checks,
        "nhats-route-field-discovery-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )
    validation_source_ok = (
        validation.get("registerPath") == str(register_path.relative_to(REPO_ROOT))
        and validation.get("registerSha256") == sha256_file(register_path)
    )
    add_check(
        checks,
        "nhats-route-field-discovery-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "route-field discovery validation must point back to current register hash",
    )
    validation_summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation_summary, dict)
        and validation_summary.get("fail") == 0
    )
    add_check(
        checks,
        "nhats-route-field-discovery-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "route-field discovery validation must pass with zero failed checks",
    )
    boundary_ok = (
        has_text(validation.get("boundary"), "Colectica value labels")
        and has_text(validation.get("boundary"), "weighted route counts")
        and has_text(validation.get("boundary"), "individual prediction")
    )
    add_check(
        checks,
        "nhats-route-field-discovery-validation-boundary",
        status_from_bool(validation_exists and boundary_ok),
        "validation boundary must keep Colectica, weighted count and individual prediction gates blocked",
    )

    return {
        "registerPath": str(register_path.relative_to(REPO_ROOT)),
        "registerSha256": sha256_file(register_path) if register_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_colectica_value_label_review(
    protocol_path: Path,
    validation_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    protocol_exists = protocol_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-colectica-value-label-protocol-exists",
        status_from_bool(protocol_exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-colectica-value-label-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    protocol = load_json(protocol_path) if protocol_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-review-protocol.v1"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-protocol-schema",
        status_from_bool(protocol_exists and schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    identity_ok = (
        protocol.get("sourceId") == "nhats"
        and protocol.get("protocolId")
        == "nhats-r13-r14-colectica-value-label-review-protocol-draft"
        and protocol.get("routeFieldDiscoveryRegisterId")
        == "nhats-r13-r14-route-field-discovery-register-draft"
        and protocol.get("missingnessRouteProtocolId")
        == "nhats-r13-r14-missingness-route-protocol-draft"
        and protocol.get("variableConfirmationMatrixId")
        == "nhats-r13-r14-variable-confirmation-matrix-draft"
        and protocol.get("status") == "protocol-only-value-labels-not-reviewed"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-protocol-identity",
        status_from_bool(protocol_exists and identity_ok),
        "protocol must bind NHATS, route-field discovery, missingness route, variable matrix and value-labels-not-reviewed status",
    )

    decision = protocol.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("colecticaReviewProtocolReady") is True
        and decision.get("colecticaLoginCompleted") is False
        and decision.get("valueLabelsConfirmed") is False
        and decision.get("questionTextConfirmed") is False
        and decision.get("universeSkipLogicConfirmed") is False
        and decision.get("routeValueCrosswalkReady") is False
        and decision.get("negativeMissingCodeMapReady") is False
        and decision.get("routeClassifierAllowed") is False
        and decision.get("endpointClassificationAllowed") is False
        and decision.get("weightedRouteCountsAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-value-label-decision-boundary",
        status_from_bool(protocol_exists and decision_ok),
        "only protocol readiness may be true; Colectica login, labels, question text, route crosswalk, classifier, endpoint, weighted counts, export, calibration and individual prediction must remain false",
    )

    evidence = protocol.get("sourceEvidence")
    observed_evidence_ids: set[str] = set()
    evidence_ok = isinstance(evidence, list)
    if isinstance(evidence, list):
        for row in evidence:
            if not isinstance(row, dict):
                evidence_ok = False
                continue
            evidence_id = row.get("id")
            if isinstance(evidence_id, str):
                observed_evidence_ids.add(evidence_id)
            if not (
                isinstance(row.get("url"), str)
                and row["url"].startswith("https://")
                and isinstance(row.get("supports"), list)
                and isinstance(row.get("doesNotSupport"), list)
            ):
                evidence_ok = False
    missing_evidence_ids = sorted(
        REQUIRED_NHATS_COLECTICA_VALUE_LABEL_EVIDENCE_IDS - observed_evidence_ids
    )
    add_check(
        checks,
        "nhats-colectica-value-label-source-evidence",
        status_from_bool(protocol_exists and evidence_ok and not missing_evidence_ids),
        f"missing_evidence_ids={missing_evidence_ids}",
    )

    artifacts = protocol.get("reviewArtifactRequirements")
    observed_artifact_ids: set[str] = set()
    artifacts_ok = isinstance(artifacts, list)
    if isinstance(artifacts, list):
        for artifact in artifacts:
            if not isinstance(artifact, dict):
                artifacts_ok = False
                continue
            artifact_id = artifact.get("id")
            if isinstance(artifact_id, str):
                observed_artifact_ids.add(artifact_id)
            if (
                artifact.get("status") != "missing"
                or artifact.get("blocksPromotion") is not True
                or not isinstance(artifact.get("requiredFields"), list)
                or len(artifact.get("requiredFields", [])) < 4
            ):
                artifacts_ok = False
    missing_artifact_ids = sorted(
        REQUIRED_NHATS_COLECTICA_VALUE_LABEL_ARTIFACT_IDS - observed_artifact_ids
    )
    add_check(
        checks,
        "nhats-colectica-value-label-review-artifacts",
        status_from_bool(protocol_exists and artifacts_ok and not missing_artifact_ids),
        f"missing_artifact_ids={missing_artifact_ids}",
    )

    units = protocol.get("routeFieldReviewUnits")
    observed_unit_ids: set[str] = set()
    units_ok = isinstance(units, list)
    if isinstance(units, list):
        for unit in units:
            if not isinstance(unit, dict):
                units_ok = False
                continue
            unit_id = unit.get("requiredRouteFieldId")
            if isinstance(unit_id, str):
                observed_unit_ids.add(unit_id)
            if (
                unit.get("promotionAllowed") is not False
                or unit.get("status")
                not in {
                    "pending-colectica-review",
                    "computed-output-gate-pending-review",
                }
                or not isinstance(unit.get("candidateVariables"), list)
                or not unit.get("candidateVariables")
                or not isinstance(unit.get("mustConfirm"), list)
                or len(unit.get("mustConfirm", [])) < 3
            ):
                units_ok = False
    missing_unit_ids = sorted(REQUIRED_NHATS_MISSINGNESS_ROUTE_FIELD_IDS - observed_unit_ids)
    add_check(
        checks,
        "nhats-colectica-value-label-review-units",
        status_from_bool(protocol_exists and units_ok and not missing_unit_ids),
        f"missing_unit_ids={missing_unit_ids}",
    )

    death_unit: dict[str, Any] = {}
    if isinstance(units, list):
        death_unit = next(
            (
                unit
                for unit in units
                if isinstance(unit, dict)
                and unit.get("requiredRouteFieldId") == "death_decedent_indicator"
            ),
            {},
        )
    sensitive_excluded = set()
    if isinstance(death_unit, dict) and isinstance(
        death_unit.get("sensitiveExcludedVariables"), list
    ):
        sensitive_excluded.update(
            str(value) for value in death_unit["sensitiveExcludedVariables"]
        )
    sensitive_ok = {
        "dm13mthdied",
        "dm13yrdied",
        "dm14mthdied",
        "dm14yrdied",
    }.issubset(sensitive_excluded)
    add_check(
        checks,
        "nhats-colectica-value-label-sensitive-death-exclusion",
        status_from_bool(
            protocol_exists
            and sensitive_ok
            and has_text(protocol.get("prohibitedActions", []), "individual death dates")
        ),
        f"sensitive_excluded={sorted(sensitive_excluded)}",
    )

    gates = protocol.get("blockingGates")
    observed_gate_ids: set[str] = set()
    gates_ok = isinstance(gates, list)
    if isinstance(gates, list):
        for gate in gates:
            if not isinstance(gate, dict):
                gates_ok = False
                continue
            gate_id = gate.get("id")
            if isinstance(gate_id, str):
                observed_gate_ids.add(gate_id)
            if gate.get("status") != "missing" or gate.get("blocksValueLabelPromotion") is not True:
                gates_ok = False
    missing_gate_ids = sorted(
        REQUIRED_NHATS_COLECTICA_VALUE_LABEL_GATE_IDS - observed_gate_ids
    )
    add_check(
        checks,
        "nhats-colectica-value-label-blocking-gates",
        status_from_bool(protocol_exists and gates_ok and not missing_gate_ids),
        f"missing_gate_ids={missing_gate_ids}",
    )

    prohibited = protocol.get("prohibitedActions", [])
    prohibited_ok = (
        has_text(prohibited, "unreviewed Colectica value-label tables")
        and has_text(prohibited, "crosswalk variable names")
        and has_text(prohibited, "real NHATS route classifier")
        and has_text(prohibited, "weighted route counts")
        and has_text(prohibited, "public AI")
    )
    add_check(
        checks,
        "nhats-colectica-value-label-prohibited-actions",
        status_from_bool(protocol_exists and prohibited_ok),
        "protocol must block unreviewed value-label tables, crosswalk-as-values, route classifier, weighted counts and public AI upload",
    )

    value_label_key_hits = sorted(
        collect_keys(protocol)
        & {
            "confirmedValueLabels",
            "valueLabelMap",
            "routeValueMap",
            "colecticaValueLabelTable",
            "rawValueLabels",
        }
    )
    add_check(
        checks,
        "nhats-colectica-value-label-no-confirmed-map",
        status_from_bool(protocol_exists and not value_label_key_hits),
        f"prohibited_keys={value_label_key_hits}",
    )

    source_trace = protocol.get("sourceTrace")
    source_trace_ok = (
        isinstance(source_trace, list)
        and all(isinstance(url, str) and url.startswith("https://") for url in source_trace)
        and has_text(source_trace, "cross-year-search")
        and has_text(source_trace, "conditions-of-use")
        and has_text(source_trace, "NHATSUserGuideR14")
        and has_text(source_trace, "NHATSR13Instrument-VariableCrosswalk")
        and has_text(source_trace, "NHATSR14Instrument-VariableCrosswalk")
    )
    add_check(
        checks,
        "nhats-colectica-value-label-source-trace",
        status_from_bool(protocol_exists and source_trace_ok),
        "sourceTrace must include official Colectica, conditions, User Guide and R13/R14 crosswalk URLs",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-validation.v1"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )
    validation_source_ok = (
        validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
    )
    add_check(
        checks,
        "nhats-colectica-value-label-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "Colectica value-label validation must point back to current protocol hash",
    )
    validation_summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation_summary, dict)
        and validation_summary.get("fail") == 0
    )
    add_check(
        checks,
        "nhats-colectica-value-label-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "Colectica value-label validation must pass with zero failed checks",
    )
    boundary_ok = (
        has_text(validation.get("boundary"), "value labels")
        and has_text(validation.get("boundary"), "route-value crosswalk")
        and has_text(validation.get("boundary"), "individual prediction")
    )
    add_check(
        checks,
        "nhats-colectica-value-label-validation-boundary",
        status_from_bool(validation_exists and boundary_ok),
        "validation boundary must keep value labels, route-value crosswalk and individual prediction blocked",
    )

    return {
        "protocolPath": str(protocol_path.relative_to(REPO_ROOT)),
        "protocolSha256": sha256_file(protocol_path) if protocol_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_colectica_value_label_review_execution(
    execution_register_path: Path,
    execution_validation_path: Path,
    protocol_path: Path,
    route_field_register_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    register_exists = execution_register_path.exists()
    validation_exists = execution_validation_path.exists()
    add_check(
        checks,
        "nhats-colectica-value-label-execution-register-exists",
        status_from_bool(register_exists),
        str(execution_register_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-validation-exists",
        status_from_bool(validation_exists),
        str(execution_validation_path.relative_to(REPO_ROOT)),
    )

    register = load_json(execution_register_path) if register_exists else {}
    validation = load_json(execution_validation_path) if validation_exists else {}

    schema_ok = (
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-review-execution-register.v1"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-schema",
        status_from_bool(register_exists and schema_ok),
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    identity_ok = (
        register.get("sourceId") == "nhats"
        and register.get("protocolId")
        == "nhats-r13-r14-colectica-value-label-review-protocol-draft"
        and register.get("routeFieldDiscoveryRegisterId")
        == "nhats-r13-r14-route-field-discovery-register-draft"
        and register.get("status")
        == "partial-executed-official-source-trace-ready-colectica-login-required"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-identity",
        status_from_bool(register_exists and identity_ok),
        "execution register must bind NHATS, current protocol, current route-field register and login-required partial execution status",
    )

    decision = register.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("fieldLevelSourceTracePrepared") is True
        and decision.get("negativeMissingCodeFamilyMapped") is True
        and decision.get("colecticaLoginCompleted") is False
        and decision.get("colecticaVariablePagesCaptured") is False
        and decision.get("valueLabelsConfirmed") is False
        and decision.get("questionTextConfirmed") is False
        and decision.get("universeSkipLogicConfirmed") is False
        and decision.get("routeValueCrosswalkReady") is False
        and decision.get("variableSpecificMissingCodeMapReady") is False
        and decision.get("secondReviewerSignoff") is False
        and decision.get("routeClassifierAllowed") is False
        and decision.get("weightedRouteCountsAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-boundary",
        status_from_bool(register_exists and decision_ok),
        "field trace and standard negative-code family may be prepared, but login, labels, crosswalk, signoff, classifier, weighted counts, export, calibration and individual prediction must remain blocked",
    )

    value_label_key_hits = sorted(
        collect_keys(register)
        & {
            "confirmedValueLabels",
            "valueLabelMap",
            "routeValueMap",
            "colecticaValueLabelTable",
            "rawValueLabels",
        }
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-no-confirmed-map",
        status_from_bool(register_exists and not value_label_key_hits),
        f"prohibited_keys={value_label_key_hits}",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-value-label-review-execution-validation.v1"
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_source_ok = (
        validation.get("executionRegisterPath")
        == str(execution_register_path.relative_to(REPO_ROOT))
        and validation.get("executionRegisterSha256") == sha256_file(execution_register_path)
        and validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
        and validation.get("routeFieldDiscoveryRegisterPath")
        == str(route_field_register_path.relative_to(REPO_ROOT))
        and validation.get("routeFieldDiscoveryRegisterSha256")
        == sha256_file(route_field_register_path)
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "execution validation must point back to current register, protocol and route-field register hashes",
    )

    validation_summary = validation.get("summary")
    validation_summary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation_summary, dict)
        and validation_summary.get("fail") == 0
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-validation-summary",
        status_from_bool(validation_exists and validation_summary_ok),
        "Colectica execution validation must pass with zero failed checks",
    )

    boundary = validation.get("boundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and boundary.get("fieldLevelSourceTracePrepared") is True
        and boundary.get("standardNegativeCodeFamilyOnly") is True
        and boundary.get("containsConfirmedValueLabels") is False
        and boundary.get("containsRouteValueMap") is False
        and boundary.get("routeClassifierAllowed") is False
        and boundary.get("weightedRouteCountsAllowed") is False
        and boundary.get("publicExportAllowed") is False
        and boundary.get("calibrationAllowed") is False
        and boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-value-label-execution-validation-boundary",
        status_from_bool(validation_exists and boundary_ok),
        "execution validation boundary must preserve field-trace-only status and block labels, route maps, classifier, export, calibration and individual prediction",
    )

    return {
        "registerPath": str(execution_register_path.relative_to(REPO_ROOT)),
        "registerSha256": sha256_file(execution_register_path) if register_exists else None,
        "validationPath": str(execution_validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(execution_validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_colectica_access_route_probe(
    probe_register_path: Path,
    probe_validation_path: Path,
    execution_register_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    register_exists = probe_register_path.exists()
    validation_exists = probe_validation_path.exists()
    add_check(
        checks,
        "nhats-colectica-access-route-probe-register-exists",
        status_from_bool(register_exists),
        str(probe_register_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-validation-exists",
        status_from_bool(validation_exists),
        str(probe_validation_path.relative_to(REPO_ROOT)),
    )

    register = load_json(probe_register_path) if register_exists else {}
    validation = load_json(probe_validation_path) if validation_exists else {}

    schema_ok = (
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-access-route-probe-register.v1"
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-schema",
        status_from_bool(register_exists and schema_ok),
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    decision = register.get("currentDecision")
    decision_ok = (
        isinstance(decision, dict)
        and decision.get("officialAccessRouteProbed") is True
        and decision.get("technicalGuideCaptured") is True
        and decision.get("anonymousPortalProbeCompleted") is True
        and decision.get("colecticaAccountCreated") is False
        and decision.get("colecticaLoginCompleted") is False
        and decision.get("colecticaVariablePagesCaptured") is False
        and decision.get("valueLabelsConfirmed") is False
        and decision.get("questionTextConfirmed") is False
        and decision.get("universeSkipLogicConfirmed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-boundary",
        status_from_bool(register_exists and decision_ok),
        "access route may be probed, but account, login, variable pages, labels, export, calibration and individual prediction must remain blocked",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-access-route-probe-validation.v1"
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_source_ok = (
        validation.get("probeRegisterPath") == str(probe_register_path.relative_to(REPO_ROOT))
        and validation.get("probeRegisterSha256") == sha256_file(probe_register_path)
        and validation.get("executionRegisterPath")
        == str(execution_register_path.relative_to(REPO_ROOT))
        and validation.get("executionRegisterSha256") == sha256_file(execution_register_path)
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "access-route validation must point back to current probe register and execution register hashes",
    )

    boundary = validation.get("boundary")
    boundary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation.get("summary"), dict)
        and validation["summary"].get("fail") == 0
        and isinstance(boundary, dict)
        and boundary.get("officialAccessRouteProbed") is True
        and boundary.get("technicalGuideCaptured") is True
        and boundary.get("anonymousPortalProbeCompleted") is True
        and boundary.get("colecticaAccountCreated") is False
        and boundary.get("colecticaLoginCompleted") is False
        and boundary.get("colecticaVariablePagesCaptured") is False
        and boundary.get("valueLabelsConfirmed") is False
        and boundary.get("publicExportAllowed") is False
        and boundary.get("calibrationAllowed") is False
        and boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-access-route-probe-validation-boundary",
        status_from_bool(validation_exists and boundary_ok),
        "validation must prove only public access-route probing while keeping authenticated capture and model admission blocked",
    )

    return {
        "registerPath": str(probe_register_path.relative_to(REPO_ROOT)),
        "registerSha256": sha256_file(probe_register_path) if register_exists else None,
        "validationPath": str(probe_validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(probe_validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_colectica_authenticated_capture_template(
    template_path: Path,
    validation_path: Path,
    access_route_probe_path: Path,
    execution_register_path: Path,
    protocol_path: Path,
    route_field_register_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    template_exists = template_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-exists",
        status_from_bool(template_exists),
        str(template_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    template = load_json(template_path) if template_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    schema_ok = (
        template.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-authenticated-capture-template.v1"
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-schema",
        status_from_bool(template_exists and schema_ok),
        f"schemaVersion={template.get('schemaVersion')!r}",
    )

    decision = template.get("currentDecision")
    boundary_ok = (
        isinstance(decision, dict)
        and decision.get("templateReady") is True
        and decision.get("controlledColecticaAccountStatusRecorded") is False
        and decision.get("colecticaLoginCompleted") is False
        and decision.get("authenticatedVariablePagesCaptured") is False
        and decision.get("sourceCaptureHashesRecorded") is False
        and decision.get("valueLabelsConfirmed") is False
        and decision.get("questionTextConfirmed") is False
        and decision.get("universeSkipLogicConfirmed") is False
        and decision.get("routeClassifierAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-boundary",
        status_from_bool(template_exists and boundary_ok),
        "template may be ready, but account status, login, captures, labels, classifier, export, calibration and individual prediction must remain blocked",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-colectica-authenticated-capture-template-validation.v1"
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_source_ok = (
        validation.get("templatePath") == str(template_path.relative_to(REPO_ROOT))
        and validation.get("templateSha256") == sha256_file(template_path)
        and validation.get("accessRouteProbeRegisterPath")
        == str(access_route_probe_path.relative_to(REPO_ROOT))
        and validation.get("accessRouteProbeRegisterSha256")
        == sha256_file(access_route_probe_path)
        and validation.get("executionRegisterPath")
        == str(execution_register_path.relative_to(REPO_ROOT))
        and validation.get("executionRegisterSha256") == sha256_file(execution_register_path)
        and validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
        and validation.get("routeFieldDiscoveryRegisterPath")
        == str(route_field_register_path.relative_to(REPO_ROOT))
        and validation.get("routeFieldDiscoveryRegisterSha256")
        == sha256_file(route_field_register_path)
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "capture-template validation must point back to current template, access-route probe, execution register, protocol and route-field register hashes",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation.get("summary"), dict)
        and validation["summary"].get("fail") == 0
        and isinstance(validation_boundary, dict)
        and validation_boundary.get("templateReady") is True
        and validation_boundary.get("controlledColecticaAccountStatusRecorded") is False
        and validation_boundary.get("colecticaLoginCompleted") is False
        and validation_boundary.get("authenticatedVariablePagesCaptured") is False
        and validation_boundary.get("sourceCaptureHashesRecorded") is False
        and validation_boundary.get("valueLabelsConfirmed") is False
        and validation_boundary.get("questionTextConfirmed") is False
        and validation_boundary.get("universeSkipLogicConfirmed") is False
        and validation_boundary.get("routeClassifierAllowed") is False
        and validation_boundary.get("publicExportAllowed") is False
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-colectica-authenticated-capture-template-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "validation must prove only template readiness while keeping authenticated capture and model admission blocked",
    )

    return {
        "templatePath": str(template_path.relative_to(REPO_ROOT)),
        "templateSha256": sha256_file(template_path) if template_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_l2_variable_family_admission(
    register_path: Path,
    validation_path: Path,
    first_estimand_path: Path,
    variable_confirmation_matrix_path: Path,
    model_admission_contract_path: Path,
    model_admission_candidate_registry_path: Path,
    authenticated_capture_template_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    register_exists = register_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-l2-variable-family-admission-register-exists",
        status_from_bool(register_exists),
        str(register_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    register = load_json(register_path) if register_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    schema_ok = (
        register.get("schemaVersion")
        == "human-infra.life-path-nhats-l2-variable-family-admission.v1"
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-schema",
        status_from_bool(register_exists and schema_ok),
        f"schemaVersion={register.get('schemaVersion')!r}",
    )

    decision = register.get("currentDecision")
    boundary_ok = (
        isinstance(decision, dict)
        and decision.get("narrowEstimandSelected") is True
        and decision.get("l2CandidateFamiliesMapped") is True
        and decision.get("exactVariablesConfirmed") is False
        and decision.get("colecticaValueLabelsConfirmed") is False
        and decision.get("colecticaAuthenticatedCapturesComplete") is False
        and decision.get("governedDataAccessReady") is False
        and decision.get("realExtractionAllowed") is False
        and decision.get("l4AdmissionAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-boundary",
        status_from_bool(register_exists and boundary_ok),
        "L2 candidate family mapping may be ready, but exact variables, data access, extraction, L4, calibration and individual prediction must remain blocked",
    )

    summary = register.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("candidateFamilyMappings") == 6
        and summary.get("l2CandidateFamilies") == 6
        and summary.get("l4Admissions") == 0
        and summary.get("l5Admissions") == 0
        and summary.get("calibratedPredictionAvailable") is False
        and summary.get("individualUseAllowed") is False
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-summary",
        status_from_bool(register_exists and summary_ok),
        "summary must preserve six L2 families and zero L4/L5 admissions",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-l2-variable-family-admission-validation.v1"
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_source_ok = (
        validation.get("registerPath") == str(register_path.relative_to(REPO_ROOT))
        and validation.get("registerSha256") == sha256_file(register_path)
        and validation.get("firstEstimandProtocolPath")
        == str(first_estimand_path.relative_to(REPO_ROOT))
        and validation.get("firstEstimandProtocolSha256") == sha256_file(first_estimand_path)
        and validation.get("variableConfirmationMatrixPath")
        == str(variable_confirmation_matrix_path.relative_to(REPO_ROOT))
        and validation.get("variableConfirmationMatrixSha256")
        == sha256_file(variable_confirmation_matrix_path)
        and validation.get("modelAdmissionContractPath")
        == str(model_admission_contract_path.relative_to(REPO_ROOT))
        and validation.get("modelAdmissionContractSha256")
        == sha256_file(model_admission_contract_path)
        and validation.get("modelAdmissionCandidateRegistryPath")
        == str(model_admission_candidate_registry_path.relative_to(REPO_ROOT))
        and validation.get("modelAdmissionCandidateRegistrySha256")
        == sha256_file(model_admission_candidate_registry_path)
        and validation.get("authenticatedCaptureTemplatePath")
        == str(authenticated_capture_template_path.relative_to(REPO_ROOT))
        and validation.get("authenticatedCaptureTemplateSha256")
        == sha256_file(authenticated_capture_template_path)
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "L2 family validation must point back to current estimand, variable matrix, model-admission contract, candidate registry and capture template hashes",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation.get("summary"), dict)
        and validation["summary"].get("fail") == 0
        and validation.get("candidateFamilyCount") == 6
        and validation.get("l4Admissions") == 0
        and validation.get("l5Admissions") == 0
        and isinstance(validation_boundary, dict)
        and validation_boundary.get("narrowEstimandSelected") is True
        and validation_boundary.get("l2CandidateFamiliesMapped") is True
        and validation_boundary.get("exactVariablesConfirmed") is False
        and validation_boundary.get("l4AdmissionAllowed") is False
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-l2-variable-family-admission-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "validation must prove only L2 family mapping while keeping L4, calibration and individual prediction blocked",
    )

    return {
        "registerPath": str(register_path.relative_to(REPO_ROOT)),
        "registerSha256": sha256_file(register_path) if register_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_nhats_preoutcome_aggregation_protocol(
    protocol_path: Path,
    validation_path: Path,
    first_estimand_path: Path,
    l2_variable_family_admission_register_path: Path,
    variable_confirmation_matrix_path: Path,
    cohort_flow_endpoint_protocol_path: Path,
    survey_design_protocol_path: Path,
    disclosure_control_policy_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    protocol_exists = protocol_path.exists()
    validation_exists = validation_path.exists()
    add_check(
        checks,
        "nhats-preoutcome-aggregation-protocol-exists",
        status_from_bool(protocol_exists),
        str(protocol_path.relative_to(REPO_ROOT)),
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-validation-exists",
        status_from_bool(validation_exists),
        str(validation_path.relative_to(REPO_ROOT)),
    )

    protocol = load_json(protocol_path) if protocol_exists else {}
    validation = load_json(validation_path) if validation_exists else {}

    schema_ok = (
        protocol.get("schemaVersion")
        == "human-infra.life-path-nhats-preoutcome-aggregation-protocol.v1"
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-schema",
        status_from_bool(protocol_exists and schema_ok),
        f"schemaVersion={protocol.get('schemaVersion')!r}",
    )

    decision = protocol.get("currentDecision")
    boundary_ok = (
        isinstance(decision, dict)
        and decision.get("preOutcomeAggregationRulesFrozen") is True
        and decision.get("syntheticRuleValidationAllowed") is True
        and decision.get("containsRealNhatsData") is False
        and decision.get("exactVariablesConfirmed") is False
        and decision.get("realAggregationAllowed") is False
        and decision.get("weightedAggregationAllowed") is False
        and decision.get("publicExportAllowed") is False
        and decision.get("l4AdmissionAllowed") is False
        and decision.get("calibrationAllowed") is False
        and decision.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-boundary",
        status_from_bool(protocol_exists and boundary_ok),
        "pre-outcome rules may be frozen, but real aggregation, weighted estimates, public export, L4, calibration and individual prediction must remain blocked",
    )

    summary = protocol.get("summary")
    summary_ok = (
        isinstance(summary, dict)
        and summary.get("aggregationRuleCount") == 8
        and summary.get("syntheticTestCaseCount") == 7
        and summary.get("preOutcomeRulesFrozen") is True
        and summary.get("realAggregationAllowed") is False
        and summary.get("weightedAggregationAllowed") is False
        and summary.get("l4Admissions") == 0
        and summary.get("calibrationAllowed") is False
        and summary.get("individualUseAllowed") is False
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-summary",
        status_from_bool(protocol_exists and summary_ok),
        "summary must freeze eight rules and keep real, weighted, L4, calibration and individual uses blocked",
    )

    validation_schema_ok = (
        validation.get("schemaVersion")
        == "human-infra.life-path-nhats-preoutcome-aggregation-validation.v1"
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-validation-schema",
        status_from_bool(validation_exists and validation_schema_ok),
        f"schemaVersion={validation.get('schemaVersion')!r}",
    )

    validation_source_ok = (
        validation.get("protocolPath") == str(protocol_path.relative_to(REPO_ROOT))
        and validation.get("protocolSha256") == sha256_file(protocol_path)
        and validation.get("firstEstimandProtocolPath")
        == str(first_estimand_path.relative_to(REPO_ROOT))
        and validation.get("firstEstimandProtocolSha256") == sha256_file(first_estimand_path)
        and validation.get("l2VariableFamilyAdmissionRegisterPath")
        == str(l2_variable_family_admission_register_path.relative_to(REPO_ROOT))
        and validation.get("l2VariableFamilyAdmissionRegisterSha256")
        == sha256_file(l2_variable_family_admission_register_path)
        and validation.get("variableConfirmationMatrixPath")
        == str(variable_confirmation_matrix_path.relative_to(REPO_ROOT))
        and validation.get("variableConfirmationMatrixSha256")
        == sha256_file(variable_confirmation_matrix_path)
        and validation.get("cohortFlowEndpointProtocolPath")
        == str(cohort_flow_endpoint_protocol_path.relative_to(REPO_ROOT))
        and validation.get("cohortFlowEndpointProtocolSha256")
        == sha256_file(cohort_flow_endpoint_protocol_path)
        and validation.get("surveyDesignProtocolPath")
        == str(survey_design_protocol_path.relative_to(REPO_ROOT))
        and validation.get("surveyDesignProtocolSha256")
        == sha256_file(survey_design_protocol_path)
        and validation.get("disclosureControlPolicyPath")
        == str(disclosure_control_policy_path.relative_to(REPO_ROOT))
        and validation.get("disclosureControlPolicySha256")
        == sha256_file(disclosure_control_policy_path)
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-validation-source-hash",
        status_from_bool(validation_exists and validation_source_ok),
        "pre-outcome aggregation validation must point back to current upstream protocol hashes",
    )

    validation_boundary = validation.get("boundary")
    validation_boundary_ok = (
        validation.get("overallStatus") == "PASS"
        and isinstance(validation.get("summary"), dict)
        and validation["summary"].get("fail") == 0
        and validation.get("aggregationRuleCount") == 8
        and isinstance(validation.get("syntheticCaseRows"), list)
        and len(validation["syntheticCaseRows"]) == 7
        and all(row.get("status") == "PASS" for row in validation["syntheticCaseRows"])
        and isinstance(validation_boundary, dict)
        and validation_boundary.get("preOutcomeAggregationRulesFrozen") is True
        and validation_boundary.get("syntheticRuleValidationAllowed") is True
        and validation_boundary.get("realAggregationAllowed") is False
        and validation_boundary.get("weightedAggregationAllowed") is False
        and validation_boundary.get("l4AdmissionAllowed") is False
        and validation_boundary.get("calibrationAllowed") is False
        and validation_boundary.get("individualPredictionAllowed") is False
    )
    add_check(
        checks,
        "nhats-preoutcome-aggregation-validation-boundary",
        status_from_bool(validation_exists and validation_boundary_ok),
        "validation must prove only pre-outcome L2 rule freezing while keeping real aggregation, L4, calibration and individual prediction blocked",
    )

    return {
        "protocolPath": str(protocol_path.relative_to(REPO_ROOT)),
        "protocolSha256": sha256_file(protocol_path) if protocol_exists else None,
        "validationPath": str(validation_path.relative_to(REPO_ROOT)),
        "validationSha256": sha256_file(validation_path) if validation_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_sensitivity_analysis(
    sensitivity_path: Path,
    model_data: dict[str, Any],
    model_path: Path,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    sensitivity_exists = sensitivity_path.exists()
    add_check(
        checks,
        "sensitivity-analysis-exists",
        status_from_bool(sensitivity_exists),
        str(sensitivity_path.relative_to(REPO_ROOT)),
    )

    sensitivity = load_json(sensitivity_path) if sensitivity_exists else {}
    schema_version = sensitivity.get("schemaVersion")
    add_check(
        checks,
        "sensitivity-schema-version",
        status_from_bool(schema_version == "human-infra.life-path-sensitivity.v1"),
        f"schemaVersion={schema_version!r}",
    )

    source_model = sensitivity.get("sourceModel")
    source_model_ok = (
        isinstance(source_model, dict)
        and source_model.get("path") == str(model_path.relative_to(REPO_ROOT))
        and source_model.get("sha256") == sha256_file(model_path)
    )
    add_check(
        checks,
        "sensitivity-source-model-hash",
        status_from_bool(sensitivity_exists and source_model_ok),
        "sensitivity output must point back to the generated model path and sha256",
    )

    boundary = sensitivity.get("analysisBoundary")
    boundary_ok = (
        isinstance(boundary, dict)
        and has_text(boundary, "Synthetic toy model")
        and has_text(boundary, "no real cohort")
        and has_text(boundary, "no real cohort, calibration, validation")
        and has_text(boundary, "individual death-date prediction")
        and has_text(boundary, "medical advice")
        and has_text(boundary, "empirically estimated")
    )
    add_check(
        checks,
        "sensitivity-boundary-language",
        status_from_bool(sensitivity_exists and boundary_ok),
        "sensitivity analysis must preserve synthetic/no-real-cohort/no-calibration/no-individual-use boundaries",
    )

    plan = sensitivity.get("perturbationPlan")
    observed_parameters: set[str] = set()
    plan_bounds_ok = True
    if isinstance(plan, list):
        for row in plan:
            if not isinstance(row, dict):
                plan_bounds_ok = False
                continue
            parameter = row.get("parameter")
            if isinstance(parameter, str):
                observed_parameters.add(parameter)
            if row.get("mode") not in {"relative", "absolute"}:
                plan_bounds_ok = False
            if not all(isinstance(row.get(key), (int, float)) for key in ("low", "high")):
                plan_bounds_ok = False
    missing_parameters = sorted(REQUIRED_SENSITIVITY_PARAMETERS - observed_parameters)
    add_check(
        checks,
        "sensitivity-parameter-coverage",
        status_from_bool(isinstance(plan, list) and not missing_parameters and plan_bounds_ok),
        f"missing_parameters={missing_parameters}",
    )

    scenarios = model_data.get("scenarios")
    scenario_ids: list[str] = []
    if isinstance(scenarios, list):
        scenario_ids = [
            scenario["id"]
            for scenario in scenarios
            if isinstance(scenario, dict) and isinstance(scenario.get("id"), str)
        ]
    expected_count = len(scenario_ids) * len(REQUIRED_SENSITIVITY_PARAMETERS) * 2
    results = sensitivity.get("results")
    result_count_ok = isinstance(results, list) and len(results) == expected_count
    add_check(
        checks,
        "sensitivity-result-count",
        status_from_bool(result_count_ok),
        f"expected={expected_count}, actual={len(results) if isinstance(results, list) else 'invalid'}",
    )

    result_shape_ok = True
    result_ranges_ok = True
    observed_directions: set[str] = set()
    observed_result_parameters: set[str] = set()
    observed_result_scenarios: set[str] = set()
    if isinstance(results, list):
        for row in results:
            if not isinstance(row, dict):
                result_shape_ok = False
                continue
            observed_directions.add(str(row.get("direction")))
            parameter = row.get("parameter")
            scenario_id = row.get("scenarioId")
            if isinstance(parameter, str):
                observed_result_parameters.add(parameter)
            if isinstance(scenario_id, str):
                observed_result_scenarios.add(scenario_id)
            if not {
                "scenarioId",
                "variantId",
                "parameter",
                "direction",
                "nominalValue",
                "variantValue",
                "metrics",
                "delta",
            }.issubset(row):
                result_shape_ok = False
            metrics = row.get("metrics")
            if not isinstance(metrics, dict):
                result_ranges_ok = False
                continue
            for key in ("survivalAt80", "survivalAt100", "optionValue"):
                value = metrics.get(key)
                if not isinstance(value, (int, float)) or not 0 <= float(value) <= 1:
                    result_ranges_ok = False
            for key in (
                "expectedLifeAgeProxy",
                "expectedEffectiveTimeYears",
                "expectedEffectiveTimeGainYears",
                "healthspanAgeProxy",
                "levRatio",
                "riskTailPenalty",
            ):
                value = metrics.get(key)
                if not isinstance(value, (int, float)):
                    result_ranges_ok = False

    expected_scenario_set = set(str(item) for item in scenario_ids)
    result_coverage_ok = (
        observed_directions == {"low", "high"}
        and observed_result_parameters == REQUIRED_SENSITIVITY_PARAMETERS
        and observed_result_scenarios == expected_scenario_set
    )
    add_check(
        checks,
        "sensitivity-result-shape",
        status_from_bool(result_shape_ok and result_coverage_ok),
        f"directions={sorted(observed_directions)}, scenarios={sorted(observed_result_scenarios)}",
    )
    add_check(
        checks,
        "sensitivity-result-ranges",
        status_from_bool(result_ranges_ok),
        "sensitivity result metrics must keep survival/option probabilities in [0, 1] and numeric summary fields present",
    )

    stability = sensitivity.get("stabilitySummary")
    stability_ok = isinstance(stability, list) and len(stability) == len(expected_scenario_set)
    if isinstance(stability, list):
        for row in stability:
            if not isinstance(row, dict):
                stability_ok = False
                continue
            if not {
                "scenarioId",
                "nominalOpenBoundary",
                "openBoundaryStable",
                "effectiveTimeRange",
                "lifeAgeRange",
                "mostSensitiveParameter",
            }.issubset(row):
                stability_ok = False
            if row.get("mostSensitiveParameter") not in REQUIRED_SENSITIVITY_PARAMETERS:
                stability_ok = False
            for range_key in ("effectiveTimeRange", "lifeAgeRange"):
                range_value = row.get(range_key)
                if not isinstance(range_value, dict) or not all(
                    isinstance(range_value.get(key), (int, float))
                    for key in ("min", "max", "width")
                ):
                    stability_ok = False
    add_check(
        checks,
        "sensitivity-stability-summary",
        status_from_bool(stability_ok),
        "stability summary must cover every scenario, boundary stability, ranges, and most-sensitive parameter",
    )

    sanity = sensitivity.get("sanityChecks")
    sanity_ok = (
        isinstance(sanity, dict)
        and sanity.get("resultCount") == expected_count
        and sanity.get("scenarioCount") == len(expected_scenario_set)
        and sanity.get("parameterCount") == len(REQUIRED_SENSITIVITY_PARAMETERS)
        and sanity.get("deathDateSuppressed") is True
        and sanity.get("individualPredictionSuppressed") is True
    )
    add_check(
        checks,
        "sensitivity-sanity-checks",
        status_from_bool(sanity_ok),
        "sensitivity sanity checks must bind expected result count and suppress death-date / individual prediction",
    )

    key_set = collect_keys(sensitivity)
    prohibited_keys = sorted(key_set & PROHIBITED_FIELD_NAMES)
    add_check(
        checks,
        "sensitivity-no-individual-death-date-fields",
        status_from_bool(not prohibited_keys),
        f"prohibited_keys={prohibited_keys}",
    )

    return {
        "path": str(sensitivity_path.relative_to(REPO_ROOT)),
        "sha256": sha256_file(sensitivity_path) if sensitivity_exists else None,
        "status": "PASS" if summarize_checks(checks)["fail"] == 0 else "FAIL",
        "checks": checks,
        "summary": summarize_checks(checks),
    }


def audit_model(
    data: dict[str, Any],
    model_path: Path,
    sensitivity_path: Path,
    readiness_path: Path,
    data_sources_path: Path,
    source_cards_path: Path,
    data_card_template_path: Path,
    nhats_data_card_path: Path,
    nhats_variable_dictionary_path: Path,
    nhats_extraction_manifest_path: Path,
    nhats_acquisition_readiness_path: Path,
    nhats_file_tier_table_path: Path,
    nhats_first_estimand_protocol_path: Path,
    nhats_variable_confirmation_matrix_path: Path,
    nhats_cohort_flow_endpoint_protocol_path: Path,
    nhats_disclosure_policy_path: Path,
    nhats_disclosure_test_cases_path: Path,
    nhats_disclosure_validation_path: Path,
    nhats_survey_design_protocol_path: Path,
    nhats_survey_design_test_cases_path: Path,
    nhats_survey_design_validation_path: Path,
    nhats_missingness_route_protocol_path: Path,
    nhats_missingness_route_test_cases_path: Path,
    nhats_missingness_route_validation_path: Path,
    nhats_route_field_discovery_register_path: Path,
    nhats_route_field_discovery_validation_path: Path,
    nhats_colectica_value_label_protocol_path: Path,
    nhats_colectica_value_label_validation_path: Path,
    nhats_colectica_value_label_execution_register_path: Path,
    nhats_colectica_value_label_execution_validation_path: Path,
    nhats_colectica_access_route_probe_register_path: Path,
    nhats_colectica_access_route_probe_validation_path: Path,
    nhats_colectica_authenticated_capture_template_path: Path,
    nhats_colectica_authenticated_capture_template_validation_path: Path,
    nhats_l2_variable_family_admission_register_path: Path,
    nhats_l2_variable_family_admission_validation_path: Path,
    nhats_preoutcome_aggregation_protocol_path: Path,
    nhats_preoutcome_aggregation_validation_path: Path,
) -> dict[str, Any]:
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
    data_sources = load_json(data_sources_path)
    data_sources_audit = audit_data_sources(data_sources, data_sources_path)
    source_card_docs_audit = audit_source_card_docs(
        data_sources,
        source_cards_path,
        data_card_template_path,
    )
    nhats_docs_audit = audit_nhats_data_admission_docs(
        nhats_data_card_path,
        nhats_variable_dictionary_path,
    )
    nhats_extraction_manifest_audit = audit_nhats_extraction_manifest(
        nhats_extraction_manifest_path,
    )
    nhats_acquisition_readiness_audit = audit_nhats_acquisition_readiness(
        nhats_acquisition_readiness_path,
    )
    nhats_file_tier_table_audit = audit_nhats_file_tier_table(
        nhats_file_tier_table_path,
    )
    nhats_first_estimand_protocol_audit = audit_nhats_first_estimand_protocol(
        nhats_first_estimand_protocol_path,
    )
    nhats_variable_confirmation_matrix_audit = audit_nhats_variable_confirmation_matrix(
        nhats_variable_confirmation_matrix_path,
    )
    nhats_cohort_flow_endpoint_protocol_audit = (
        audit_nhats_cohort_flow_endpoint_protocol(
            nhats_cohort_flow_endpoint_protocol_path,
        )
    )
    nhats_disclosure_control_audit = audit_nhats_disclosure_control(
        nhats_disclosure_policy_path,
        nhats_disclosure_test_cases_path,
        nhats_disclosure_validation_path,
    )
    nhats_survey_design_audit = audit_nhats_survey_design(
        nhats_survey_design_protocol_path,
        nhats_survey_design_test_cases_path,
        nhats_survey_design_validation_path,
    )
    nhats_missingness_route_audit = audit_nhats_missingness_route(
        nhats_missingness_route_protocol_path,
        nhats_missingness_route_test_cases_path,
        nhats_missingness_route_validation_path,
    )
    nhats_route_field_discovery_audit = audit_nhats_route_field_discovery(
        nhats_route_field_discovery_register_path,
        nhats_route_field_discovery_validation_path,
    )
    nhats_colectica_value_label_audit = audit_nhats_colectica_value_label_review(
        nhats_colectica_value_label_protocol_path,
        nhats_colectica_value_label_validation_path,
    )
    nhats_colectica_value_label_execution_audit = (
        audit_nhats_colectica_value_label_review_execution(
            nhats_colectica_value_label_execution_register_path,
            nhats_colectica_value_label_execution_validation_path,
            nhats_colectica_value_label_protocol_path,
            nhats_route_field_discovery_register_path,
        )
    )
    nhats_colectica_access_route_probe_audit = audit_nhats_colectica_access_route_probe(
        nhats_colectica_access_route_probe_register_path,
        nhats_colectica_access_route_probe_validation_path,
        nhats_colectica_value_label_execution_register_path,
    )
    nhats_colectica_authenticated_capture_template_audit = (
        audit_nhats_colectica_authenticated_capture_template(
            nhats_colectica_authenticated_capture_template_path,
            nhats_colectica_authenticated_capture_template_validation_path,
            nhats_colectica_access_route_probe_register_path,
            nhats_colectica_value_label_execution_register_path,
            nhats_colectica_value_label_protocol_path,
            nhats_route_field_discovery_register_path,
        )
    )
    nhats_l2_variable_family_admission_audit = audit_nhats_l2_variable_family_admission(
        nhats_l2_variable_family_admission_register_path,
        nhats_l2_variable_family_admission_validation_path,
        nhats_first_estimand_protocol_path,
        nhats_variable_confirmation_matrix_path,
        DEFAULT_MODEL_ADMISSION_CONTRACT,
        DEFAULT_MODEL_ADMISSION_CANDIDATE_REGISTRY,
        nhats_colectica_authenticated_capture_template_path,
    )
    nhats_preoutcome_aggregation_audit = audit_nhats_preoutcome_aggregation_protocol(
        nhats_preoutcome_aggregation_protocol_path,
        nhats_preoutcome_aggregation_validation_path,
        nhats_first_estimand_protocol_path,
        nhats_l2_variable_family_admission_register_path,
        nhats_variable_confirmation_matrix_path,
        nhats_cohort_flow_endpoint_protocol_path,
        nhats_survey_design_protocol_path,
        nhats_disclosure_policy_path,
    )
    sensitivity_audit = audit_sensitivity_analysis(sensitivity_path, data, model_path)
    checks.extend(readiness_audit["checks"])
    checks.extend(data_sources_audit["checks"])
    checks.extend(source_card_docs_audit["checks"])
    checks.extend(nhats_docs_audit["checks"])
    checks.extend(nhats_extraction_manifest_audit["checks"])
    checks.extend(nhats_acquisition_readiness_audit["checks"])
    checks.extend(nhats_file_tier_table_audit["checks"])
    checks.extend(nhats_first_estimand_protocol_audit["checks"])
    checks.extend(nhats_variable_confirmation_matrix_audit["checks"])
    checks.extend(nhats_cohort_flow_endpoint_protocol_audit["checks"])
    checks.extend(nhats_disclosure_control_audit["checks"])
    checks.extend(nhats_survey_design_audit["checks"])
    checks.extend(nhats_missingness_route_audit["checks"])
    checks.extend(nhats_route_field_discovery_audit["checks"])
    checks.extend(nhats_colectica_value_label_audit["checks"])
    checks.extend(nhats_colectica_value_label_execution_audit["checks"])
    checks.extend(nhats_colectica_access_route_probe_audit["checks"])
    checks.extend(nhats_colectica_authenticated_capture_template_audit["checks"])
    checks.extend(nhats_l2_variable_family_admission_audit["checks"])
    checks.extend(nhats_preoutcome_aggregation_audit["checks"])
    checks.extend(sensitivity_audit["checks"])
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
        "dataSourceCandidates": data_sources_audit,
        "sourceCardDocs": source_card_docs_audit,
        "nhatsDataAdmission": nhats_docs_audit,
        "nhatsExtractionManifest": nhats_extraction_manifest_audit,
        "nhatsAcquisitionReadiness": nhats_acquisition_readiness_audit,
        "nhatsFileTierTable": nhats_file_tier_table_audit,
        "nhatsFirstEstimandProtocol": nhats_first_estimand_protocol_audit,
        "nhatsVariableConfirmationMatrix": nhats_variable_confirmation_matrix_audit,
        "nhatsCohortFlowEndpointProtocol": nhats_cohort_flow_endpoint_protocol_audit,
        "nhatsDisclosureControl": nhats_disclosure_control_audit,
        "nhatsSurveyDesign": nhats_survey_design_audit,
        "nhatsMissingnessRoute": nhats_missingness_route_audit,
        "nhatsRouteFieldDiscovery": nhats_route_field_discovery_audit,
        "nhatsColecticaValueLabelReview": nhats_colectica_value_label_audit,
        "nhatsColecticaValueLabelReviewExecution": nhats_colectica_value_label_execution_audit,
        "nhatsColecticaAccessRouteProbe": nhats_colectica_access_route_probe_audit,
        "nhatsColecticaAuthenticatedCaptureTemplate": nhats_colectica_authenticated_capture_template_audit,
        "nhatsL2VariableFamilyAdmission": nhats_l2_variable_family_admission_audit,
        "nhatsPreoutcomeAggregation": nhats_preoutcome_aggregation_audit,
        "sensitivityAnalysis": sensitivity_audit,
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
            "## Data Source Candidates",
            "",
            f"- Registry path: `{audit['dataSourceCandidates']['path']}`",
            f"- Registry SHA-256: `{audit['dataSourceCandidates']['sha256']}`",
            f"- Registry status: `{audit['dataSourceCandidates']['status']}`",
            "- Boundary: candidate sources are mapped, but no data has been downloaded, accessed, fitted, calibrated, or validated.",
            "",
            "## Source Card Docs",
            "",
            f"- Source Cards path: `{audit['sourceCardDocs']['sourceCardsPath']}`",
            f"- Source Cards SHA-256: `{audit['sourceCardDocs']['sourceCardsSha256']}`",
            f"- Data Card template path: `{audit['sourceCardDocs']['dataCardTemplatePath']}`",
            f"- Data Card template SHA-256: `{audit['sourceCardDocs']['dataCardTemplateSha256']}`",
            f"- Source Card docs status: `{audit['sourceCardDocs']['status']}`",
            "- Boundary: source cards and the data-card template only prove data-governance readiness scaffolding; they do not prove data access, field availability, calibration, or validation.",
            "",
            "## NHATS Data Admission",
            "",
            f"- NHATS Data Card path: `{audit['nhatsDataAdmission']['dataCardPath']}`",
            f"- NHATS Data Card SHA-256: `{audit['nhatsDataAdmission']['dataCardSha256']}`",
            f"- NHATS variable dictionary path: `{audit['nhatsDataAdmission']['variableDictionaryPath']}`",
            f"- NHATS variable dictionary SHA-256: `{audit['nhatsDataAdmission']['variableDictionarySha256']}`",
            f"- NHATS data admission status: `{audit['nhatsDataAdmission']['status']}`",
            "- Boundary: NHATS is only a draft admission candidate for late-life effective-time modeling; no data access, extraction, calibration, validation, or individual prediction is claimed.",
            "",
            "## NHATS Extraction Manifest",
            "",
            f"- Manifest path: `{audit['nhatsExtractionManifest']['path']}`",
            f"- Manifest SHA-256: `{audit['nhatsExtractionManifest']['sha256']}`",
            f"- Manifest status: `{audit['nhatsExtractionManifest']['status']}`",
            "- Boundary: the manifest is a pre-extraction gate; it blocks scripts, downloads, field inference, calibration, validation, raw-data exposure and unsafe individual outputs until official file-level requirements are complete.",
            "",
            "## NHATS Acquisition Readiness",
            "",
            f"- Acquisition readiness path: `{audit['nhatsAcquisitionReadiness']['path']}`",
            f"- Acquisition readiness SHA-256: `{audit['nhatsAcquisitionReadiness']['sha256']}`",
            f"- Acquisition readiness status: `{audit['nhatsAcquisitionReadiness']['status']}`",
            "- Boundary: the structured readiness contract keeps NHATS at cannot-extract-yet until registration, file-tier, Colectica variables, endpoint, survey design, disclosure control, AI boundary and storage/destruction gates are ready.",
            "",
            "## NHATS File Tier Table",
            "",
            f"- File-tier table path: `{audit['nhatsFileTierTable']['path']}`",
            f"- File-tier table SHA-256: `{audit['nhatsFileTierTable']['sha256']}`",
            f"- File-tier table status: `{audit['nhatsFileTierTable']['status']}`",
            "- Boundary: the file-tier table maps official R13/R14 public and sensitive file families, but it still blocks download, extraction, repository storage, public AI upload, calibration and individual prediction.",
            "",
            "## NHATS First Estimand Protocol",
            "",
            f"- First estimand protocol path: `{audit['nhatsFirstEstimandProtocol']['path']}`",
            f"- First estimand protocol SHA-256: `{audit['nhatsFirstEstimandProtocol']['sha256']}`",
            f"- First estimand protocol status: `{audit['nhatsFirstEstimandProtocol']['status']}`",
            "- Boundary: the first estimand protocol pre-registers the R13/R14 aggregate functional-survival question, time-zero, outcome, censoring, survey-design and output boundaries, but it still blocks data download, extraction, calibration, validation and individual prediction.",
            "",
            "## NHATS Variable Confirmation Matrix",
            "",
            f"- Variable confirmation matrix path: `{audit['nhatsVariableConfirmationMatrix']['path']}`",
            f"- Variable confirmation matrix SHA-256: `{audit['nhatsVariableConfirmationMatrix']['sha256']}`",
            f"- Variable confirmation matrix status: `{audit['nhatsVariableConfirmationMatrix']['status']}`",
            "- Boundary: the variable confirmation matrix records official source facts, candidate field patterns, variable groups and cohort-flow gates, but it still blocks data download, extraction scripts, unconfirmed pattern-derived variables, calibration and individual prediction.",
            "",
            "## NHATS Cohort Flow Endpoint Protocol",
            "",
            f"- Cohort-flow endpoint protocol path: `{audit['nhatsCohortFlowEndpointProtocol']['path']}`",
            f"- Cohort-flow endpoint protocol SHA-256: `{audit['nhatsCohortFlowEndpointProtocol']['sha256']}`",
            f"- Cohort-flow endpoint protocol status: `{audit['nhatsCohortFlowEndpointProtocol']['status']}`",
            "- Boundary: the cohort-flow endpoint protocol pre-registers route classes, aggregate output contracts, disclosure control and blocking gates, but it still blocks download, extraction, endpoint routing, public export, calibration and individual prediction.",
            "",
            "## NHATS Disclosure Control Validation",
            "",
            f"- Disclosure policy path: `{audit['nhatsDisclosureControl']['policyPath']}`",
            f"- Disclosure policy SHA-256: `{audit['nhatsDisclosureControl']['policySha256']}`",
            f"- Disclosure test cases path: `{audit['nhatsDisclosureControl']['testCasesPath']}`",
            f"- Disclosure test cases SHA-256: `{audit['nhatsDisclosureControl']['testCasesSha256']}`",
            f"- Disclosure validation path: `{audit['nhatsDisclosureControl']['validationPath']}`",
            f"- Disclosure validation SHA-256: `{audit['nhatsDisclosureControl']['validationSha256']}`",
            f"- Disclosure validation status: `{audit['nhatsDisclosureControl']['status']}`",
            "- Boundary: disclosure-control validation proves only that synthetic output envelopes obey aggregate-only, n<5 suppression, row-level blocking, public-AI blocking and forbidden-output rules; it does not authorize real NHATS extraction, public export, calibration, validation or individual prediction.",
            "",
            "## NHATS Survey Design Validation",
            "",
            f"- Survey-design protocol path: `{audit['nhatsSurveyDesign']['protocolPath']}`",
            f"- Survey-design protocol SHA-256: `{audit['nhatsSurveyDesign']['protocolSha256']}`",
            f"- Survey-design test cases path: `{audit['nhatsSurveyDesign']['testCasesPath']}`",
            f"- Survey-design test cases SHA-256: `{audit['nhatsSurveyDesign']['testCasesSha256']}`",
            f"- Survey-design validation path: `{audit['nhatsSurveyDesign']['validationPath']}`",
            f"- Survey-design validation SHA-256: `{audit['nhatsSurveyDesign']['validationSha256']}`",
            f"- Survey-design validation status: `{audit['nhatsSurveyDesign']['status']}`",
            "- Boundary: survey-design validation proves only that synthetic design-plan envelopes enforce weights, strata, PSU/variance-unit, variance-method, route-map and disclosure prerequisites; it does not authorize real NHATS weighted estimates, population inference, calibration, validation or individual prediction.",
            "",
            "## NHATS Missingness Route Validation",
            "",
            f"- Missingness-route protocol path: `{audit['nhatsMissingnessRoute']['protocolPath']}`",
            f"- Missingness-route protocol SHA-256: `{audit['nhatsMissingnessRoute']['protocolSha256']}`",
            f"- Missingness-route test cases path: `{audit['nhatsMissingnessRoute']['testCasesPath']}`",
            f"- Missingness-route test cases SHA-256: `{audit['nhatsMissingnessRoute']['testCasesSha256']}`",
            f"- Missingness-route validation path: `{audit['nhatsMissingnessRoute']['validationPath']}`",
            f"- Missingness-route validation SHA-256: `{audit['nhatsMissingnessRoute']['validationSha256']}`",
            f"- Missingness-route validation status: `{audit['nhatsMissingnessRoute']['status']}`",
            "- Boundary: missingness-route validation proves only that synthetic route envelopes separate death, self interview, proxy interview, facility route, missingness, conflicts and small-cell suppression; it does not authorize real NHATS route classification, weighted route counts, calibration, validation or individual prediction.",
            "",
            "## NHATS Route Field Discovery",
            "",
            f"- Route-field discovery register path: `{audit['nhatsRouteFieldDiscovery']['registerPath']}`",
            f"- Route-field discovery register SHA-256: `{audit['nhatsRouteFieldDiscovery']['registerSha256']}`",
            f"- Route-field discovery validation path: `{audit['nhatsRouteFieldDiscovery']['validationPath']}`",
            f"- Route-field discovery validation SHA-256: `{audit['nhatsRouteFieldDiscovery']['validationSha256']}`",
            f"- Route-field discovery validation status: `{audit['nhatsRouteFieldDiscovery']['status']}`",
            "- Boundary: route-field discovery records official R13/R14 crosswalk candidates, but it does not replace Colectica value-label confirmation, governed file access, classifier review, disclosure review, weighted route counts, calibration, validation or individual prediction.",
            "",
            "## NHATS Colectica Value-Label Review",
            "",
            f"- Colectica value-label protocol path: `{audit['nhatsColecticaValueLabelReview']['protocolPath']}`",
            f"- Colectica value-label protocol SHA-256: `{audit['nhatsColecticaValueLabelReview']['protocolSha256']}`",
            f"- Colectica value-label validation path: `{audit['nhatsColecticaValueLabelReview']['validationPath']}`",
            f"- Colectica value-label validation SHA-256: `{audit['nhatsColecticaValueLabelReview']['validationSha256']}`",
            f"- Colectica value-label validation status: `{audit['nhatsColecticaValueLabelReview']['status']}`",
            "- Boundary: Colectica value-label review protocol defines the next evidence gate, but it does not contain confirmed value-label maps, question text, skip logic, route-value crosswalks, classifier promotion, weighted route counts, public export, calibration, validation or individual prediction.",
            "",
            "## NHATS Colectica Value-Label Review Execution",
            "",
            f"- Colectica execution register path: `{audit['nhatsColecticaValueLabelReviewExecution']['registerPath']}`",
            f"- Colectica execution register SHA-256: `{audit['nhatsColecticaValueLabelReviewExecution']['registerSha256']}`",
            f"- Colectica execution validation path: `{audit['nhatsColecticaValueLabelReviewExecution']['validationPath']}`",
            f"- Colectica execution validation SHA-256: `{audit['nhatsColecticaValueLabelReviewExecution']['validationSha256']}`",
            f"- Colectica execution validation status: `{audit['nhatsColecticaValueLabelReviewExecution']['status']}`",
            "- Boundary: Colectica execution now records official source trace, field-level source-trace skeleton and standard negative-code family only; it still blocks login-derived value labels, question text, universe/skip logic, route-value maps, classifier promotion, weighted route counts, public export, calibration, validation and individual prediction.",
            "",
            "## NHATS Colectica Access-Route Probe",
            "",
            f"- Colectica access-route probe register path: `{audit['nhatsColecticaAccessRouteProbe']['registerPath']}`",
            f"- Colectica access-route probe register SHA-256: `{audit['nhatsColecticaAccessRouteProbe']['registerSha256']}`",
            f"- Colectica access-route probe validation path: `{audit['nhatsColecticaAccessRouteProbe']['validationPath']}`",
            f"- Colectica access-route probe validation SHA-256: `{audit['nhatsColecticaAccessRouteProbe']['validationSha256']}`",
            f"- Colectica access-route probe validation status: `{audit['nhatsColecticaAccessRouteProbe']['status']}`",
            "- Boundary: access-route probing verifies the public entry point, anonymous login boundary and technical-guide workflow only; it still blocks account status, authenticated variable page capture, value labels, question text, exports, calibration and individual prediction.",
            "",
            "## NHATS Colectica Authenticated Capture Template",
            "",
            f"- Colectica authenticated capture template path: `{audit['nhatsColecticaAuthenticatedCaptureTemplate']['templatePath']}`",
            f"- Colectica authenticated capture template SHA-256: `{audit['nhatsColecticaAuthenticatedCaptureTemplate']['templateSha256']}`",
            f"- Colectica authenticated capture template validation path: `{audit['nhatsColecticaAuthenticatedCaptureTemplate']['validationPath']}`",
            f"- Colectica authenticated capture template validation SHA-256: `{audit['nhatsColecticaAuthenticatedCaptureTemplate']['validationSha256']}`",
            f"- Colectica authenticated capture template validation status: `{audit['nhatsColecticaAuthenticatedCaptureTemplate']['status']}`",
            "- Boundary: authenticated capture template validation proves only that the next capture evidence slots are complete; it still blocks account status, login, authenticated variable pages, value labels, question text, universe/skip logic, route classifiers, public export, calibration and individual prediction.",
            "",
            "## NHATS L2 Variable Family Admission",
            "",
            f"- L2 variable-family admission register path: `{audit['nhatsL2VariableFamilyAdmission']['registerPath']}`",
            f"- L2 variable-family admission register SHA-256: `{audit['nhatsL2VariableFamilyAdmission']['registerSha256']}`",
            f"- L2 variable-family admission validation path: `{audit['nhatsL2VariableFamilyAdmission']['validationPath']}`",
            f"- L2 variable-family admission validation SHA-256: `{audit['nhatsL2VariableFamilyAdmission']['validationSha256']}`",
            f"- L2 variable-family admission validation status: `{audit['nhatsL2VariableFamilyAdmission']['status']}`",
            "- Boundary: L2 variable-family admission validation proves only that the narrow estimand is mapped to six candidate families; it still blocks exact variables, governed data access, extraction, L4 admission, calibration and individual prediction.",
            "",
            "## NHATS Pre-Outcome Aggregation",
            "",
            f"- Pre-outcome aggregation protocol path: `{audit['nhatsPreoutcomeAggregation']['protocolPath']}`",
            f"- Pre-outcome aggregation protocol SHA-256: `{audit['nhatsPreoutcomeAggregation']['protocolSha256']}`",
            f"- Pre-outcome aggregation validation path: `{audit['nhatsPreoutcomeAggregation']['validationPath']}`",
            f"- Pre-outcome aggregation validation SHA-256: `{audit['nhatsPreoutcomeAggregation']['validationSha256']}`",
            f"- Pre-outcome aggregation validation status: `{audit['nhatsPreoutcomeAggregation']['status']}`",
            "- Boundary: pre-outcome aggregation validation proves only that L2 aggregation rules are frozen before outcome inspection; it still blocks real aggregation, weighted estimates, public export, L4 admission, calibration and individual prediction.",
            "",
            "## Sensitivity Analysis",
            "",
            f"- Sensitivity path: `{audit['sensitivityAnalysis']['path']}`",
            f"- Sensitivity SHA-256: `{audit['sensitivityAnalysis']['sha256']}`",
            f"- Sensitivity status: `{audit['sensitivityAnalysis']['status']}`",
            "- Boundary: sensitivity analysis is synthetic one-factor-at-a-time stress testing; it does not prove empirical parameter values, causal effects, calibrated prediction, or individual usefulness.",
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
    parser.add_argument("--sensitivity", type=Path, default=DEFAULT_SENSITIVITY)
    parser.add_argument("--readiness", type=Path, default=DEFAULT_READINESS)
    parser.add_argument("--data-sources", type=Path, default=DEFAULT_DATA_SOURCES)
    parser.add_argument("--source-cards", type=Path, default=DEFAULT_SOURCE_CARDS)
    parser.add_argument("--data-card-template", type=Path, default=DEFAULT_DATA_CARD_TEMPLATE)
    parser.add_argument("--nhats-data-card", type=Path, default=DEFAULT_NHATS_DATA_CARD)
    parser.add_argument(
        "--nhats-variable-dictionary",
        type=Path,
        default=DEFAULT_NHATS_VARIABLE_DICTIONARY,
    )
    parser.add_argument(
        "--nhats-extraction-manifest",
        type=Path,
        default=DEFAULT_NHATS_EXTRACTION_MANIFEST,
    )
    parser.add_argument(
        "--nhats-acquisition-readiness",
        type=Path,
        default=DEFAULT_NHATS_ACQUISITION_READINESS,
    )
    parser.add_argument(
        "--nhats-file-tier-table",
        type=Path,
        default=DEFAULT_NHATS_FILE_TIER_TABLE,
    )
    parser.add_argument(
        "--nhats-first-estimand-protocol",
        type=Path,
        default=DEFAULT_NHATS_FIRST_ESTIMAND_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-variable-confirmation-matrix",
        type=Path,
        default=DEFAULT_NHATS_VARIABLE_CONFIRMATION_MATRIX,
    )
    parser.add_argument(
        "--nhats-cohort-flow-endpoint-protocol",
        type=Path,
        default=DEFAULT_NHATS_COHORT_FLOW_ENDPOINT_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-disclosure-policy",
        type=Path,
        default=DEFAULT_NHATS_DISCLOSURE_POLICY,
    )
    parser.add_argument(
        "--nhats-disclosure-test-cases",
        type=Path,
        default=DEFAULT_NHATS_DISCLOSURE_TEST_CASES,
    )
    parser.add_argument(
        "--nhats-disclosure-validation",
        type=Path,
        default=DEFAULT_NHATS_DISCLOSURE_VALIDATION,
    )
    parser.add_argument(
        "--nhats-survey-design-protocol",
        type=Path,
        default=DEFAULT_NHATS_SURVEY_DESIGN_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-survey-design-test-cases",
        type=Path,
        default=DEFAULT_NHATS_SURVEY_DESIGN_TEST_CASES,
    )
    parser.add_argument(
        "--nhats-survey-design-validation",
        type=Path,
        default=DEFAULT_NHATS_SURVEY_DESIGN_VALIDATION,
    )
    parser.add_argument(
        "--nhats-missingness-route-protocol",
        type=Path,
        default=DEFAULT_NHATS_MISSINGNESS_ROUTE_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-missingness-route-test-cases",
        type=Path,
        default=DEFAULT_NHATS_MISSINGNESS_ROUTE_TEST_CASES,
    )
    parser.add_argument(
        "--nhats-missingness-route-validation",
        type=Path,
        default=DEFAULT_NHATS_MISSINGNESS_ROUTE_VALIDATION,
    )
    parser.add_argument(
        "--nhats-route-field-discovery-register",
        type=Path,
        default=DEFAULT_NHATS_ROUTE_FIELD_DISCOVERY_REGISTER,
    )
    parser.add_argument(
        "--nhats-route-field-discovery-validation",
        type=Path,
        default=DEFAULT_NHATS_ROUTE_FIELD_DISCOVERY_VALIDATION,
    )
    parser.add_argument(
        "--nhats-colectica-value-label-protocol",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_VALUE_LABEL_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-colectica-value-label-validation",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_VALUE_LABEL_VALIDATION,
    )
    parser.add_argument(
        "--nhats-colectica-value-label-execution-register",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_VALUE_LABEL_EXECUTION_REGISTER,
    )
    parser.add_argument(
        "--nhats-colectica-value-label-execution-validation",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_VALUE_LABEL_EXECUTION_VALIDATION,
    )
    parser.add_argument(
        "--nhats-colectica-access-route-probe-register",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_ACCESS_ROUTE_PROBE_REGISTER,
    )
    parser.add_argument(
        "--nhats-colectica-access-route-probe-validation",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_ACCESS_ROUTE_PROBE_VALIDATION,
    )
    parser.add_argument(
        "--nhats-colectica-authenticated-capture-template",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_AUTHENTICATED_CAPTURE_TEMPLATE,
    )
    parser.add_argument(
        "--nhats-colectica-authenticated-capture-template-validation",
        type=Path,
        default=DEFAULT_NHATS_COLECTICA_AUTHENTICATED_CAPTURE_TEMPLATE_VALIDATION,
    )
    parser.add_argument(
        "--nhats-l2-variable-family-admission-register",
        type=Path,
        default=DEFAULT_NHATS_L2_VARIABLE_FAMILY_ADMISSION_REGISTER,
    )
    parser.add_argument(
        "--nhats-l2-variable-family-admission-validation",
        type=Path,
        default=DEFAULT_NHATS_L2_VARIABLE_FAMILY_ADMISSION_VALIDATION,
    )
    parser.add_argument(
        "--nhats-preoutcome-aggregation-protocol",
        type=Path,
        default=DEFAULT_NHATS_PREOUTCOME_AGGREGATION_PROTOCOL,
    )
    parser.add_argument(
        "--nhats-preoutcome-aggregation-validation",
        type=Path,
        default=DEFAULT_NHATS_PREOUTCOME_AGGREGATION_VALIDATION,
    )
    parser.add_argument("--json-out", type=Path, default=DEFAULT_JSON_OUT)
    parser.add_argument("--md-out", type=Path, default=DEFAULT_MD_OUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    model_path = args.model.resolve()
    sensitivity_path = args.sensitivity.resolve()
    readiness_path = args.readiness.resolve()
    data_sources_path = args.data_sources.resolve()
    source_cards_path = args.source_cards.resolve()
    data_card_template_path = args.data_card_template.resolve()
    nhats_data_card_path = args.nhats_data_card.resolve()
    nhats_variable_dictionary_path = args.nhats_variable_dictionary.resolve()
    nhats_extraction_manifest_path = args.nhats_extraction_manifest.resolve()
    nhats_acquisition_readiness_path = args.nhats_acquisition_readiness.resolve()
    nhats_file_tier_table_path = args.nhats_file_tier_table.resolve()
    nhats_first_estimand_protocol_path = args.nhats_first_estimand_protocol.resolve()
    nhats_variable_confirmation_matrix_path = (
        args.nhats_variable_confirmation_matrix.resolve()
    )
    nhats_cohort_flow_endpoint_protocol_path = (
        args.nhats_cohort_flow_endpoint_protocol.resolve()
    )
    nhats_disclosure_policy_path = args.nhats_disclosure_policy.resolve()
    nhats_disclosure_test_cases_path = args.nhats_disclosure_test_cases.resolve()
    nhats_disclosure_validation_path = args.nhats_disclosure_validation.resolve()
    nhats_survey_design_protocol_path = args.nhats_survey_design_protocol.resolve()
    nhats_survey_design_test_cases_path = args.nhats_survey_design_test_cases.resolve()
    nhats_survey_design_validation_path = args.nhats_survey_design_validation.resolve()
    nhats_missingness_route_protocol_path = (
        args.nhats_missingness_route_protocol.resolve()
    )
    nhats_missingness_route_test_cases_path = (
        args.nhats_missingness_route_test_cases.resolve()
    )
    nhats_missingness_route_validation_path = (
        args.nhats_missingness_route_validation.resolve()
    )
    nhats_route_field_discovery_register_path = (
        args.nhats_route_field_discovery_register.resolve()
    )
    nhats_route_field_discovery_validation_path = (
        args.nhats_route_field_discovery_validation.resolve()
    )
    nhats_colectica_value_label_protocol_path = (
        args.nhats_colectica_value_label_protocol.resolve()
    )
    nhats_colectica_value_label_validation_path = (
        args.nhats_colectica_value_label_validation.resolve()
    )
    nhats_colectica_value_label_execution_register_path = (
        args.nhats_colectica_value_label_execution_register.resolve()
    )
    nhats_colectica_value_label_execution_validation_path = (
        args.nhats_colectica_value_label_execution_validation.resolve()
    )
    nhats_colectica_access_route_probe_register_path = (
        args.nhats_colectica_access_route_probe_register.resolve()
    )
    nhats_colectica_access_route_probe_validation_path = (
        args.nhats_colectica_access_route_probe_validation.resolve()
    )
    nhats_colectica_authenticated_capture_template_path = (
        args.nhats_colectica_authenticated_capture_template.resolve()
    )
    nhats_colectica_authenticated_capture_template_validation_path = (
        args.nhats_colectica_authenticated_capture_template_validation.resolve()
    )
    nhats_l2_variable_family_admission_register_path = (
        args.nhats_l2_variable_family_admission_register.resolve()
    )
    nhats_l2_variable_family_admission_validation_path = (
        args.nhats_l2_variable_family_admission_validation.resolve()
    )
    nhats_preoutcome_aggregation_protocol_path = (
        args.nhats_preoutcome_aggregation_protocol.resolve()
    )
    nhats_preoutcome_aggregation_validation_path = (
        args.nhats_preoutcome_aggregation_validation.resolve()
    )
    audit = audit_model(
        load_json(model_path),
        model_path,
        sensitivity_path,
        readiness_path,
        data_sources_path,
        source_cards_path,
        data_card_template_path,
        nhats_data_card_path,
        nhats_variable_dictionary_path,
        nhats_extraction_manifest_path,
        nhats_acquisition_readiness_path,
        nhats_file_tier_table_path,
        nhats_first_estimand_protocol_path,
        nhats_variable_confirmation_matrix_path,
        nhats_cohort_flow_endpoint_protocol_path,
        nhats_disclosure_policy_path,
        nhats_disclosure_test_cases_path,
        nhats_disclosure_validation_path,
        nhats_survey_design_protocol_path,
        nhats_survey_design_test_cases_path,
        nhats_survey_design_validation_path,
        nhats_missingness_route_protocol_path,
        nhats_missingness_route_test_cases_path,
        nhats_missingness_route_validation_path,
        nhats_route_field_discovery_register_path,
        nhats_route_field_discovery_validation_path,
        nhats_colectica_value_label_protocol_path,
        nhats_colectica_value_label_validation_path,
        nhats_colectica_value_label_execution_register_path,
        nhats_colectica_value_label_execution_validation_path,
        nhats_colectica_access_route_probe_register_path,
        nhats_colectica_access_route_probe_validation_path,
        nhats_colectica_authenticated_capture_template_path,
        nhats_colectica_authenticated_capture_template_validation_path,
        nhats_l2_variable_family_admission_register_path,
        nhats_l2_variable_family_admission_validation_path,
        nhats_preoutcome_aggregation_protocol_path,
        nhats_preoutcome_aggregation_validation_path,
    )
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
