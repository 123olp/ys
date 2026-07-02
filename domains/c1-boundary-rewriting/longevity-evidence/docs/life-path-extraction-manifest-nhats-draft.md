# NHATS Life-Path Extraction Manifest Draft

Last reviewed: 2026-07-02

Status: `draft / cannot-extract-yet`

This manifest is the pre-extraction contract for using the National Health and Aging Trends Study (NHATS) in a future Human Infra life-path model. It does not approve data download, extraction scripts, model fitting, calibration, validation, benchmarking, or individual prediction.

## Header

```text
manifest_id: nhats-r1-r14-effective-time-manifest-draft
source_card_id: nhats
data_card_id: nhats-r1-r14-effective-time-draft
variable_dictionary_id: nhats-life-path-variable-dictionary-draft
source_name: National Health and Aging Trends Study
review_date: 2026-07-02
reviewer: tradecatlabs
status: draft / cannot-extract-yet
access_tier: public-use first; sensitive and restricted files excluded until approved
```

## Purpose

The manifest exists to stop premature extraction. It records what must be true before NHATS can move from candidate source to governed data pipeline.

```text
candidate data source
  -> Data Card
  -> variable-family dictionary
  -> extraction manifest
  -> governed local acquisition
  -> extraction script
  -> cohort flow diagram
  -> missingness table
  -> model calibration review
```

Current decision:

```text
No NHATS data downloaded.
No extraction script authorized.
No raw data in repository.
No calibration or validation claim.
No individual death-date prediction.
```

## Official Access Facts

NHATS official pages state that all files require registration. Public data files are downloadable for registered users; sensitive and restricted files require additional application. The cross-year searchable database is provided through Colectica and requires separate registration.

The NHATS/NSOC Conditions of Use impose these model-relevant boundaries:

- No attempt to identify participants.
- No transfer of data to unregistered collaborators, staff, students, or other users.
- No upload of NHATS or NSOC data to public large language model or AI platforms.
- Use only for scientific research and aggregate statistical reporting.
- Report disclosure events and documentation/data errors.
- Cite NHATS and provide publication information where required.
- Destroy downloaded files and derived data if requested by NHATS.
- Sensitive-data magnitude and frequency tabulations with `n < 5` require suppression or additional restriction handling.

## Source Files

The first extraction attempt must use only files that can be justified by this manifest and file-specific access terms.

| Candidate file family | Candidate role | Current admission decision |
| --- | --- | --- |
| Tracker files | sample person status, residence, cohort, interview status, death/decedent boundary | Candidate, exact round-specific files pending |
| Sample Person files | function, cognition, participation, health, resources, technology and environment variables | Candidate, exact fields pending Colectica/codebook confirmation |
| Weights files / weight fields | survey weights, replicate weights, strata and cluster variables | Required before descriptive or model metrics |
| Last Month of Life files | decedent context and death-boundary information | Candidate endpoint context; no individual death timing output |
| NSOC linkage | caregiving and helper network context | Excluded until file-specific approval |
| Sensitive/restricted NHATS files | biomarker, genetics, CMS/Medicare and other restricted fields | Excluded until file-specific approval |

## Required Variable Groups

Exact field names, public/sensitive/restricted status, round coverage, missingness codes and value labels must be confirmed before extraction.

| Model group | Candidate variables / source areas | Gate before use |
| --- | --- | --- |
| Identity and join keys | `spid`, round identifier, cohort flag, interview route | Confirm official names and stable join rule |
| Design and weights | `w#anfinwgt0`, `w#varunit`, `w#varstrat`, replicate weights | Confirm round/cohort-specific weight choice and variance method |
| Endpoint boundary | `fl#spdied`, residence/decedent status, Last Month of Life route | Confirm endpoint definition and no individual death-date output |
| Functional state | self-care, mobility, household activities, medical care activities, participation | Confirm exact fields, skip patterns and directionality |
| Cognition and memory | `cg#dwrdimmrc`, `cg#dwrddlyrc`, clock drawing, orientation, proxy cognition | Confirm availability by round and proxy route |
| Support and resources | helper network, caregiving, household, insurance, economic resources | Confirm public/sensitive boundary |
| Environment and access | residence, home environment, transportation, technology use, service access | Confirm round availability |
| Effective-time proxy | `effective_time_proxy`, `functional_survival_state`, `survey_design_ready` | Pre-register formula before extraction |

## Derived Outputs

Only aggregate, study-level and model-diagnostic outputs may leave the governed workspace.

```text
alive_state
functional_survival_state
effective_time_proxy
censoring_reason
interview_route
proxy_route
residential_state
survey_design_ready
cohort_flow_counts
missingness_table
weighted_descriptive_summary
```

Forbidden outputs:

```text
individual death-date prediction
personal medical advice
personal longevity ranking
row-level records
small-cell disclosure
raw NHATS / NSOC data
unapproved redistribution
public LLM or public AI upload
```

## Extraction Rules

1. Do not write an extraction script until this manifest has exact file names, variable names, access tier, missing codes, join keys, endpoint fields, weights and allowed outputs.
2. Do not download or store NHATS raw data in this repository, `web/`, GitHub issues, public AI systems, public cloud notebooks or ungated workspaces.
3. Do not use sensitive/restricted files until NHATS approval and file-specific conditions are recorded.
4. Do not compute model metrics until the cohort flow diagram, missingness table, endpoint definition and survey design plan exist.
5. Do not display any output that can be interpreted as an individual death date, personal medical recommendation or personal longevity ranking.
6. Treat Colectica/codebook variables as the field-level truth source; do not infer exact variables from prose alone.

## Missing Codes And Quality Gates

Before extraction, the following must be filled from official codebooks or Colectica:

```text
nhats_release:
rounds:
file_names:
access_tier:
variables:
derived_variables:
weight_variables:
design_variables:
replicate_weight_variables:
missing_codes:
value_labels:
join_keys:
endpoint_fields:
interview_route_fields:
proxy_route_fields:
residential_state_fields:
privacy_boundary:
allowed_outputs:
forbidden_outputs:
```

Quality gate:

```text
If any required field above remains blank, decision = cannot-extract-yet.
```

## Abort Conditions

```text
access terms cannot be satisfied
Colectica unavailable or exact variables cannot be confirmed
public vs sensitive/restricted status cannot be resolved
required weights or design variables are unavailable
endpoint definition is ambiguous
effective_time_proxy would be chosen after seeing outcomes
missingness or censoring cannot separate death, proxy response, nonresponse and residential care
aggregate reporting and n < 5 suppression cannot be enforced
raw data would enter the repository, Web app, issue tracker, public LLM or public AI platform
outputs could be read as individual prediction, medical advice, personal ranking or re-identification
```

## Narrow First Estimand Candidate

The first governed extraction should be a narrow late-life functional-survival estimand, not a full LEV model.

```text
population:
  NHATS sample persons age 65+ within a selected cohort and round window
time_zero:
  first eligible interview round after cohort entry
outcome:
  aggregate functional-survival state at fixed follow-up horizon
predictors:
  baseline function, cognition, support, environment and survey design fields
analysis:
  survey-design-aware descriptive and model-development diagnostics
non_use:
  no individual death-date prediction, no personal medical advice, no LEV proof
```

## Source Trace

- NHATS overview: <https://www.nhats.org/nhats>
- NHATS data access: <https://www.nhats.org/data-access>
- NHATS conditions of use: <https://www.nhats.org/conditions-of-use>
- NHATS cross-year search: <https://www.nhats.org/data-access/cross-year-search>
- NHATS files: <https://www.nhats.org/data-access/nhats>
- NHATS User Guide Rounds 1-14: <https://nhats.org/sites/default/files/public-documentation/NHATSUserGuideR14_02102026.pdf>
- NHATS Sample Design FAQ / Technical Paper 55: <https://nhats.org/sites/default/files/public-documentation/NHATSTechnicalPaper55_09042025.pdf>

## Human Infra Mapping

```text
NHATS extraction manifest
  -> prevents premature data access and field inference
  -> forces exact variables, access tier, missing codes, weights and endpoint rules before extraction
  -> protects the life-path model from raw-data leakage, individual prediction and calibration overclaim
  -> allows the project to move from toy model toward governed cohort modeling without losing the subject-continuity boundary
```
