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

## Official Source Refresh

Observed on 2026-07-02 from official NHATS pages:

| Official source | Current fact captured for this manifest | Human Infra consequence |
| --- | --- | --- |
| Data Access | All NHATS files require registration. Public-use files are for registered users; sensitive and restricted files require additional application. | No acquisition, extraction or field table may be marked ready without registration status and file-specific access tier. |
| Cross-Year Search | Cross-year metadata search is provided through Colectica and requires separate registration; metadata includes item numbers, variable names, labels, values, value labels and question text. | Exact variables must come from Colectica/codebooks, not prose inference. |
| Conditions of Use | January 22, 2026 added a condition prohibiting NHATS/NSOC uploads to public LLMs or AI platforms; April 6, 2026 edited the public-use sharing rule. | No NHATS/NSOC raw data, row-level derivatives or small-cell tables may enter public AI systems, this repository, public issues or ungated notebooks. |
| Welcome / AI notice | Uploading NHATS/NSOC data to public LLMs or AI platforms is treated as data sharing and is not allowed. | AI assistance may only use public documentation, synthetic examples or aggregate non-disclosive outputs. |
| NHATS Files | NHATS file pages state data files are temporarily unavailable due to impending website updates; round pages still expose file families and approval boundaries. | Acquisition readiness must be rechecked immediately before any registration, download or script work. |
| Sensitive & Restricted Files | Restricted files contain fields with additional identification risk and are limited to qualifying researchers meeting additional requirements. | Biomarkers, genetics, CMS/Medicare linkage, sensitive demographics and restricted geography remain excluded until approval is documented. |

## Acquisition Readiness Gates

The manifest may move from `draft / cannot-extract-yet` to `acquisition-ready` only when all gates below are filled from official NHATS sources and reviewed locally.

| Gate | Required evidence before acquisition | Current status |
| --- | --- | --- |
| `official-source-refresh` | Date-stamped review of Data Access, Conditions of Use, Cross-Year Search, Files and Sensitive/Restricted file pages. | Ready for public-source freshness only; still not enough for registration, download, extraction or calibration. |
| `registration-status` | Registered NHATS account identity, permitted user boundary and no-sharing obligations recorded outside the public repository. | Missing. |
| `file-access-tier` | For each planned file: public-use, sensitive or restricted tier; approval status; allowed local storage path. | Missing. |
| `colectica-variable-confirmation` | Exact variable names, labels, value labels, missing codes and question text confirmed from Colectica or official codebooks. | Missing. |
| `round-window` | Selected rounds, file versions, release dates and cohort refresh handling fixed before extraction. | Missing. |
| `survey-design-plan` | Weight, strata, cluster and replicate-weight strategy matched to estimand. | Missing. |
| `endpoint-definition` | Death, functional-survival, proxy interview, residential-care and censoring rules fixed before data access. | Missing. |
| `disclosure-control` | `n < 5` suppression, aggregate-only export and no row-level output checks implemented. | Missing. |
| `ai-boundary` | Written rule that public AI tools may see only public docs, synthetic examples or aggregate non-disclosive outputs. | Partial; boundary written, not operationalized. |
| `storage-destruction-plan` | Governed local storage, access log, derived-data boundary and destruction-on-request process defined. | Missing. |

Quality gate:

```text
If any acquisition readiness gate remains Missing or only Partial, decision = cannot-extract-yet.
```

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
