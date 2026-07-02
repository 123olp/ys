# Life-Path Data Card: NHATS

Last reviewed: 2026-07-02

This Data Card is a draft admission document for using the National Health and Aging Trends Study (NHATS) as a future life-path model source. It does not approve calibration, validation, benchmarking, data download, restricted data access, or individual prediction.

## Header

```text
data_card_id: nhats-r1-r14-effective-time-draft
source_card_id: nhats
source_name: National Health and Aging Trends Study
official_url: https://www.nhats.org/nhats
review_date: 2026-07-02
reviewer: tradecatlabs
status: draft / cannot-evaluate-yet
```

## Governance

```text
access_route: NHATS registration required for public-use data; sensitive and restricted files require additional application.
data_use_agreement: NHATS and NSOC Conditions of Use.
restricted_fields: sensitive demographics, month/year fields, detailed identifiers, Medicare/CMS linkages, NSOC sensitive files, and other files marked sensitive/restricted by NHATS.
export_rules: outputs must be aggregate scientific reporting; no public LLM upload; no transfer to unregistered collaborators; citation and publication notification required.
privacy_boundary: do not attempt participant identification; report any disclosure immediately; destroy data if requested by NHATS.
consent_boundary: use only under NHATS permitted scientific research terms and file-specific access conditions.
security_boundary: no raw NHATS or NSOC data may be placed into this repository, Web app, issue tracker, public AI system, or ungoverned workspace.
allowed_outputs: aggregate cohort-level descriptive statistics, model development diagnostics, calibration diagnostics, validation diagnostics, source-card evidence summaries.
forbidden_outputs: individual death-date prediction, personal medical advice, personal longevity ranking, re-identification, row-level disclosure, unapproved redistribution, raw data exposure.
```

Minimum rule:

```text
No individual death-date prediction.
No personal medical advice.
No personal longevity ranking.
No model calibration claim before validation diagnostics exist.
No NHATS/NSOC raw data upload to public large language models or external AI platforms.
```

## Study Design

```text
target_population: U.S. Medicare beneficiaries ages 65+ represented by NHATS sampling frames and cohort refreshes.
inclusion_criteria: sample persons in selected NHATS rounds with complete enough SP/tracker/design variables for the selected estimand.
exclusion_criteria: records without required time-zero fields, design weights, outcome fields, or governance permission for the intended use.
time_zero: candidate first eligible interview round, likely Round 1 for 2011 cohort or another clearly defined cohort entry round.
follow_up_window: annual follow-up rounds after time zero; exact horizon must be fixed before modeling.
prediction_horizons: candidate 1-year, 3-year, 5-year and longer functional-survival windows; exact horizons pending variable dictionary and endpoint feasibility.
unit_of_analysis: sample person / person-round, depending on estimand.
sampling_design: nationally representative complex survey design with weights, stratification and clustering requirements.
weights_required: yes; analyses must use NHATS round/cohort-specific weights and design variables appropriate to cross-sectional, trend, trajectory or time-to-event estimands.
```

## Outcomes

```text
primary_outcomes:
  - functional-survival state
  - self-care limitation / assistance / unmet-need trajectory
  - mobility limitation / assistance / accommodation trajectory
  - participation restriction and valued-activity loss
  - death or last-month-of-life status as endpoint boundary
secondary_outcomes:
  - cognitive status / proxy cognitive change
  - medical self-management difficulty
  - household activity difficulty
  - residence transition / residential care status
  - caregiver and helper involvement
mortality_endpoint: possible through tracker/decedent and last-month-of-life interview fields; exact death timing and access tier must be confirmed before use.
function_endpoint: strong candidate through self-care, mobility, household activities, medical care activities, performance activities and participation measures.
cognition_endpoint: candidate through sample-person cognitive assessment, proxy cognitive assessment and created cognitive variables.
health_quality_endpoint: candidate proxy through participation, wellbeing, activity limitation, pain/fatigue and quality-of-life-adjacent fields; not a direct QALY measure without additional mapping.
effective_time_proxy: candidate composite of survival, functional independence, mobility, self-care, cognition, participation and required help; composite must be pre-registered before use.
competing_risks: death, nursing-home/residential-care transition, proxy interview, missing interviews, attrition, nonresponse and restricted/sensitive file unavailability.
censoring_rules: must distinguish death, missing SP interview, nonresponse, alive-but-not-interviewed, proxy response, residential care/facility interview and file-access censoring.
endpoint_limitations: no individual death date output; no causal interpretation; no LEV validation; late-life cohort cannot represent full adult life course.
```

## Predictors

```text
baseline_demographics: age, gender, race/ethnicity, household, education and related fields subject to public/sensitive file boundary.
baseline_health_state: self-rated health, health conditions, pain, fatigue, breathing problems, sensory limitations, falls, depression/anxiety and health-care use fields.
biomarkers: limited in core public files; dried blood spot, genetics, polygenic scores and accelerometry require separate file-specific review.
functional_status: self-care, mobility, household activities, medical care activities, performance tests, accommodations and helper use.
cognition_attention: self cognitive assessment, proxy cognitive assessment, word recall, clock drawing, Cogstate availability by round and proxy route.
resource_social: household composition, children/siblings, social network, community, economic wellbeing, insurance, income/assets, helper network and caregiving linkages.
healthcare_access: regular doctor, medical visit help, transportation to care, medicine tracking, insurance/bill handling and Medicare/CMS linkage where governed.
technology_access: phone/computer/tablet/online use, telehealth, online pharmacy/insurance/health information tasks.
environmental_exposure: residence, housing, home environment, environmental modifications, community and service environment.
missing_predictors: exact variable names, public/sensitive status, wave availability, missingness codes, design weights and harmonized longitudinal field availability.
```

## Data Quality

```text
missingness_pattern: must be profiled by round, interview type, proxy status, residential status and outcome family before modeling.
measurement_error: self-report, proxy report, performance testing conditions, skip patterns and created measures require field-level assessment.
linkage_quality: Medicare/CMS, NSOC, biomarker, genetics and sensitive files require separate access and linkage review.
survey_weights: required; design variables and weights must match the selected estimand and analysis type.
representativeness: strong for U.S. Medicare beneficiaries ages 65+ under NHATS design when weights and design variables are correctly used; not representative of younger adults or non-U.S. populations.
selection_bias: survival to cohort entry, nonresponse, proxy response, attrition, residential-care sampling and access-tier restrictions must be assessed.
attrition: must separate death, nonresponse, facility status and missing interview pathways.
harmonization_required: yes; variables use round-index naming and some created measures differ by availability, round and module.
known_release_limits: as of this review, NHATS pages note temporary data-file unavailability during website updates; data access status must be rechecked before any acquisition step.
```

## Model Use

```text
model_role: candidate development source for late-life effective-time and functional-survival model; possible external validation source after another development cohort exists.
estimand: cohort-level scenario shift in functional-survival / effective-time proxy, not individual death prediction.
validation_plan: internal validation within defined cohort and external validation against another aging cohort only after variables and endpoints are harmonized.
calibration_diagnostics: calibration-in-the-large, calibration slope, Brier score, discrimination, missingness sensitivity, survey-weighted diagnostics and subgroup calibration.
sensitivity_analyses: outcome definition, time zero, proxy interviews, residential-care status, death censoring, missing data, survey weights, restricted/sensitive file exclusion and composite effective-time weights.
bias_applicability_check: age 65+ Medicare frame, race/ethnicity oversampling, Hispanic sample expansion, proxy response, residential-care inclusion, public-file restrictions and non-U.S. transportability.
minimum_reporting_artifacts: filled Data Card, variable dictionary, extraction manifest, cohort flow diagram, missingness table, endpoint definitions, design-weight plan, model card, validation report and prohibited-use statement.
```

## Decision

```text
decision: cannot-evaluate-yet
reason: NHATS is a strong candidate for late-life function and effective-time modeling, but no governed data access, variable dictionary, endpoint specification, extraction manifest, calibration, validation or sensitivity analysis exists yet.
required_next_work:
  - create a round-specific variable dictionary from NHATS documentation and codebooks
  - choose development cohort and time zero
  - define effective_time_proxy before model fitting
  - confirm public vs sensitive/restricted file requirements
  - confirm data availability after website updates
  - write extraction manifest only after registration and access approval
  - run no model until aggregate-only output and no-LLM-upload rules are operationalized
abort_conditions:
  - data access terms cannot be satisfied
  - required endpoint fields require unavailable restricted files
  - survey design cannot be represented in the model
  - effective_time_proxy cannot be defined without post-hoc outcome shopping
  - outputs would create individual prediction, medical advice, personal ranking or re-identification risk
```

## Source Trace

```text
official_docs:
  - https://www.nhats.org/nhats
  - https://www.nhats.org/data-access
  - https://www.nhats.org/conditions-of-use
  - https://www.nhats.org/nhats/methods-documentation?id=heading0
  - https://nhats.org/sites/default/files/public-documentation/NHATSUserGuideR14_02102026.pdf
  - https://nhats.org/sites/default/files/public-documentation/NHATSTechnicalPaper55_09042025.pdf
data_dictionary: pending exact cross-year searchable database / codebook review.
access_documentation: NHATS Data Access and Conditions of Use pages.
release_notes: pending round-specific file page review at time of governed acquisition.
methodology_docs: NHATS User Guide Rounds 1-14 and Sample Design FAQ / Technical Paper 55.
local_artifacts:
  - domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-source-cards.md
  - domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-variable-dictionary-nhats.md
```

## Human Infra Mapping

```text
NHATS late-life function trajectory
  -> observes mobility, self-care, cognition, participation, care help, environment and technology access
  -> supports an effective-time proxy for older adults
  -> can later stress-test whether interventions preserve action capacity rather than only survival
  -> cannot by itself prove longevity escape velocity, causal intervention benefit, or individual future lifespan
```
