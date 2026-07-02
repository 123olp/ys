# NHATS Life-Path Variable Dictionary Draft

Last reviewed: 2026-07-02

Status: `candidate-variable-dictionary-only`

This document maps NHATS documentation into Human Infra life-path model variable families. It is not an extraction manifest. Exact field availability, public/sensitive/restricted status, round coverage, missingness codes and harmonized variable names must be verified from NHATS codebooks before any data access or model fitting.

## Boundary

```text
No NHATS data downloaded.
No governed data access granted.
No extraction manifest approved.
No model calibration.
No external validation.
No individual death-date prediction.
No personal medical advice.
No personal longevity ranking.
```

The variable families below are candidate fields for a late-life effective-time model. They are intentionally grouped by model role rather than by NHATS file order, because the Human Infra model asks how a subject keeps action capacity, not merely which file contains which column.

## Minimum Model Roles

```text
design_and_identity
  -> defines sample person, round, cohort, interview route, weights and survey design
outcome_boundary
  -> defines death, last-month-of-life status, functional state and censoring
function_and_mobility
  -> measures self-care, mobility, household activity and medical self-management
cognition_and_attention
  -> measures cognitive status, memory, orientation, proxy cognition and test route
resources_and_support
  -> measures household, helpers, caregiving, insurance, economic and social support
environment_and_access
  -> measures home environment, community, transportation, technology and service access
effective_time_proxy
  -> combines survival, function, cognition, participation and help requirement
```

## Candidate Variable Families

| Model family | Candidate NHATS source area | Candidate fields / examples | Human Infra role | Current status |
| --- | --- | --- | --- | --- |
| Sample person and round | Tracker / Sample Person | `spid`, round identifier, cohort flag, interview status | Unit of analysis and longitudinal join key | Exact field names pending codebook confirmation |
| Survey weights and design | Weights / sample design | `w#anfinwgt0`, `w#varunit`, `w#varstrat` | Survey-weighted estimation and design-aware uncertainty | Candidate names from sample design FAQ; verify by round |
| Mortality / decedent boundary | Tracker / Last Month of Life | `fl#spdied`, death / deceased sample person indicator, last-month-of-life interview route | Mortality endpoint and competing-risk boundary | Candidate names from NHATS FAQ; timing detail and access tier pending |
| Residence and facility route | Tracker / residence | `r#dresid`, `r#dresidlml`, residential care or facility pathway fields | Censoring, residential transition and context state | Candidate names from user guide; verify categories |
| Proxy route | Sample person / proxy | proxy interview indicators, proxy relationship, proxy cognitive assessment route | Measurement route and missingness mechanism | Candidate family only |
| Self-care function | Self-Care Activities | eating, getting cleaned up, toileting, dressing, help, difficulty, unmet need | Effective-time outcome component and action-capacity proxy | Exact variable names pending codebook |
| Mobility | Mobility / performance | going outside, getting around inside, getting out of bed, device use, help, difficulty, duration, accommodations | Action capacity, fall-risk context and mobility-resilience proxy | Exact variable names pending codebook |
| Household activities | Household Activities | laundry, shopping for groceries, making hot meals, banking / bills, handling household tasks | Independent living and execution-cost proxy | Exact variable names pending codebook |
| Medical self-management | Medical Care Activities | doctor visits, prescription medicine, medical bills, insurance, help required | Healthcare-execution and treatment-continuity proxy | Exact variable names pending codebook |
| Participation | Participation in Activities | valued activities, restrictions due to health, transportation, importance and frequency | Subjective effective time and future-choice proxy | Exact variable names pending codebook |
| Cognitive tests | Cognitive assessment | immediate word recall `cg#dwrdimmrc`, delayed word recall `cg#dwrddlyrc`, date naming, clock drawing, executive/attention tasks where available | Cognition, memory and attention proxy | Candidate word-recall names from user guide; verify by round |
| Proxy cognition | Proxy module | memory rating, thinking/judgment, dementia-related proxy information | Cognitive status when SP test unavailable | Candidate family only |
| Physical performance | Performance activities / SPPB | walking, balance, chair stands, grip strength where available | Objective function and frailty proxy | Exact availability pending round review |
| Symptoms / energy | Health conditions and symptoms | pain, fatigue, breathing, depression/anxiety, sleep and sensory limitations where available | Health-quality and recovery-cost proxy | Candidate family only |
| Healthcare access | Medical care / insurance | regular doctor, visit access, transportation, insurance coverage, bills, medication management | Conversion channel from health state to treatment execution | Candidate family only |
| Technology access | Technology / online use | phone, computer, tablet, online health information, telehealth, online pharmacy/insurance tasks | Tool access, cognitive offloading and service access proxy | Exact round availability pending |
| Household and social network | Household / children / siblings / social network | household members, children, siblings, friends, religious/service participation | Social support and future-option-value proxy | Candidate family only |
| Helpers and caregiving | Helpers / NSOC linkage | helper count, helper tasks, caregiver relationship, NSOC linkage where approved | External support substrate and care burden proxy | Public vs NSOC access pending |
| Economic resources | Economics | income, assets, financial hardship, insurance and benefit fields | Resource resilience and access-to-care proxy | Sensitive/public status pending |
| Home environment | Home environment / modifications | stairs, accessibility, environmental modifications, assistive devices | Built environment and execution-friction proxy | Candidate family only |
| Community and transportation | Community / neighborhood / transportation | neighborhood, transportation access, leaving home and community constraints | Environmental access and participation constraint | Candidate family only |
| Biomarkers / linked files | Separate NHATS files | dried blood spots, genetics, polygenic score, accelerometry, Medicare linkage | Optional model extension for biological or utilization predictors | Not available to core draft without separate file review |

## Effective-Time Proxy Draft

The first NHATS model must pre-register a transparent proxy before touching data. A candidate structure is:

```text
effective_time_proxy_t =
  alive_t
  * function_weight_t
  * cognition_weight_t
  * participation_weight_t
  * independence_weight_t
```

Where:

```text
alive_t:
  1 if alive / interviewed or known alive at round t
  0 if deceased by endpoint definition

function_weight_t:
  derived from self-care, mobility, household and medical-care activity states

cognition_weight_t:
  derived from direct cognitive tests or proxy cognition route

participation_weight_t:
  derived from valued activities, restrictions and frequency / importance

independence_weight_t:
  derived from helper need, unmet need, accommodations and residential-care status
```

This is a model target proposal, not an approved score. It must remain separate from any clinical scale unless validated.

## Censoring And Missingness Rules To Resolve

```text
death:
  distinguish death endpoint from missing follow-up

proxy_response:
  decide whether proxy responses are included, modeled separately or treated as measurement-route indicators

residential_care:
  preserve residential-care status as a state, not a simple missingness flag

last_month_of_life:
  use only as governed endpoint/context; do not emit individual death timing

nonresponse:
  separate refusal, unavailable interview, institutional status, attrition and file-access limitation

survey_design:
  select weights and design variables before any descriptive or model metric is reported
```

## First Extraction Manifest Requirements

Before any extraction script exists, write a manifest with:

```text
nhats_release:
rounds:
file_names:
access_tier:
variables:
derived_variables:
weight_variables:
design_variables:
missing_codes:
join_keys:
endpoint_fields:
privacy_boundary:
allowed_outputs:
forbidden_outputs:
```

No extraction script should be written before this manifest exists.

## Current Decision

```text
decision: cannot-calibrate-yet
reason: variable families are mapped, but exact field names, file access tiers, missingness codes, round availability, weights, endpoint definitions and extraction manifest are not complete.
next_step: fill exact NHATS codebook variables for one narrow late-life functional-survival estimand.
```

## Source Trace

- NHATS overview: <https://www.nhats.org/nhats>
- NHATS Data Access: <https://www.nhats.org/data-access>
- NHATS Conditions of Use: <https://www.nhats.org/conditions-of-use>
- NHATS User Guide Rounds 1-14: <https://nhats.org/sites/default/files/public-documentation/NHATSUserGuideR14_02102026.pdf>
- NHATS Sample Design FAQ / Technical Paper 55: <https://nhats.org/sites/default/files/public-documentation/NHATSTechnicalPaper55_09042025.pdf>
