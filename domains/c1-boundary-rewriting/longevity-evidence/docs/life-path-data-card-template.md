# Life-Path Data Card Template

Last reviewed: 2026-07-02

This template must be filled before any candidate source is used to calibrate, validate, benchmark, or display a real life-path model result. It is intentionally stricter than the current toy model because real cohorts introduce privacy, representativeness, measurement, endpoint and governance risks.

## Header

```text
data_card_id:
source_card_id:
source_name:
official_url:
review_date:
reviewer:
status: draft / access-planned / access-approved / extracted / analysis-ready / rejected
```

## Governance

```text
access_route:
data_use_agreement:
restricted_fields:
export_rules:
privacy_boundary:
consent_boundary:
security_boundary:
allowed_outputs:
forbidden_outputs:
```

Minimum rule:

```text
No individual death-date prediction.
No personal medical advice.
No personal longevity ranking.
No model calibration claim before validation diagnostics exist.
```

## Study Design

```text
target_population:
inclusion_criteria:
exclusion_criteria:
time_zero:
follow_up_window:
prediction_horizons:
unit_of_analysis:
sampling_design:
weights_required:
```

## Outcomes

```text
primary_outcomes:
secondary_outcomes:
mortality_endpoint:
function_endpoint:
cognition_endpoint:
health_quality_endpoint:
effective_time_proxy:
competing_risks:
censoring_rules:
endpoint_limitations:
```

## Predictors

```text
baseline_demographics:
baseline_health_state:
biomarkers:
functional_status:
cognition_attention:
resource_social:
healthcare_access:
technology_access:
environmental_exposure:
missing_predictors:
```

## Data Quality

```text
missingness_pattern:
measurement_error:
linkage_quality:
survey_weights:
representativeness:
selection_bias:
attrition:
harmonization_required:
known_release_limits:
```

## Model Use

```text
model_role: development / internal-validation / external-validation / transportability / endpoint-reference / rejected
estimand:
validation_plan:
calibration_diagnostics:
sensitivity_analyses:
bias_applicability_check:
minimum_reporting_artifacts:
```

## Decision

```text
decision: use / do-not-use / cannot-evaluate-yet
reason:
required_next_work:
abort_conditions:
```

## Source Trace

```text
official_docs:
data_dictionary:
access_documentation:
release_notes:
methodology_docs:
local_artifacts:
```
