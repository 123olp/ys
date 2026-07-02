# Life-Path Data Source Cards

Last reviewed: 2026-07-02

本文保存生命路径模型进入真实校准前的数据源 Source Cards。它的任务不是证明任何模型已经可用，而是把每个候选队列放入同一个审查格式：它可能支持什么变量、不能支持什么结论、接入前还缺哪些治理和变量工作。

## 使用边界

- 当前状态是 `candidate-source-card-only`。
- 未下载任何真实数据。
- 未获得任何受限数据访问。
- 未建立任何校准、外部验证、因果推断或个体预测能力。
- 所有条目只能作为后续 Data Card、变量字典、访问申请和模型开发计划的入口。

## Source Card Format

```text
id:
source:
official_url:
type:
candidate_role:
supports:
does_not_support:
minimum_before_use:
maps_to_model_need:
next_check:
```

## Cards

### SRC-DATA-HRS

- id: `hrs`
- source: Health and Retirement Study
- official_url: <https://hrs.isr.umich.edu/>
- type: aging longitudinal panel
- candidate_role: development candidate for late-life function, cognition, resources, social support and mortality-linked aging trajectories.
- supports: resource/social variables, functional status, cognition, health and retirement context, and aging-panel model design.
- does_not_support: no individual death-date prediction; no calibrated Human Infra model; no causal intervention effect by itself.
- minimum_before_use: confirm release, variables, mortality linkage availability, restricted-use requirements, weights, missingness, wave structure and survey design.
- maps_to_model_need: `function`, `cognition`, `resourceSocial`, `mortality`, `externalValidation`
- next_check: produce a Data Card from HRS documentation and determine whether HRS should be the first development dataset or an external comparison source.

### SRC-DATA-NCHS-LMF

- id: `nchs-linked-mortality-nhanes-nhis`
- source: NCHS Linked Mortality Files for NHANES and NHIS
- official_url: <https://www.cdc.gov/nchs/linked-data/mortality-files/index.html>
- type: survey-to-mortality linkage
- candidate_role: mortality endpoint and biomarker-to-mortality boundary candidate.
- supports: survey-to-National Death Index linkage, mortality follow-up boundary, NHANES biomarker association checks, and NHIS population survey mortality checks.
- does_not_support: no individual prediction; no LEV scenario validation; no automatic causal interpretation of biomarker associations.
- minimum_before_use: choose NHANES or NHIS first, select public-use vs restricted-use path, define mortality outcome, censoring, survey weights, variable availability and privacy perturbation limits.
- maps_to_model_need: `mortality`, `biomarkers`, `resourceSocial`, `externalValidation`
- next_check: use NCHS documentation to write endpoint and censoring fields for the first mortality Data Card.

### SRC-DATA-UK-BIOBANK

- id: `uk-biobank`
- source: UK Biobank
- official_url: <https://www.ukbiobank.ac.uk/>
- type: prospective biomedical cohort
- candidate_role: high-dimensional biomarker, genetics, imaging and health-record validation candidate.
- supports: high-dimensional predictors, biomarker stress tests, genetic and phenotypic model inputs, UK external validation boundary.
- does_not_support: no local data use without approval; no calibrated Human Infra model; no individual longevity decision.
- minimum_before_use: confirm project approval path, cloud platform requirements, participant selection bias, outcome definitions, linkage completeness, de-identification rules and export restrictions.
- maps_to_model_need: `mortality`, `biomarkers`, `genomics`, `imaging`, `externalValidation`
- next_check: create a UK Biobank Data Card only after access route and exact field IDs are chosen.

### SRC-DATA-ALL-OF-US

- id: `all-of-us`
- source: NIH All of Us Research Program
- official_url: <https://allofus.nih.gov/>
- type: governed precision-medicine research program
- candidate_role: diversity, EHR, genomics, survey and transportability candidate.
- supports: EHR-linked events, genomic and survey predictors, equity and transportability stress tests, U.S. diversity context.
- does_not_support: no proof of model fairness by itself; no local data extraction here; no individual prediction or calibrated Human Infra model.
- minimum_before_use: confirm Researcher Workbench access, data tier, allowed outputs, EHR endpoint completeness, genomic availability, survey variables and participant privacy rules.
- maps_to_model_need: `biomarkers`, `genomics`, `ehr`, `resourceSocial`, `externalValidation`
- next_check: write a governed-workbench Data Card that separates data access, analysis workspace and allowed export.

### SRC-DATA-NHATS

- id: `nhats`
- source: National Health and Aging Trends Study
- official_url: <https://www.nhats.org/nhats>
- type: annual aging-function panel
- candidate_role: function-weighted survival, disability trajectory and late-life effective-time validation candidate.
- supports: nationally representative Medicare 65+ late-life function, disability process, caregiving context and annual trajectory thinking.
- does_not_support: no younger-adult trajectory coverage; no biomedical deep-phenotyping claim; no individual-level decision or calibrated Human Infra model.
- minimum_before_use: confirm wave availability, death/last-month-of-life variables, Medicare linkage rules, disability measures, sampling weights and caregiver linkage.
- maps_to_model_need: `function`, `cognition`, `caregiving`, `resourceSocial`, `externalValidation`
- next_check: prioritize NHATS for the first effective-time outcome Data Card.

### SRC-DATA-ELSA

- id: `elsa`
- source: English Longitudinal Study of Ageing
- official_url: <https://www.elsa-project.ac.uk/>
- type: longitudinal aging panel
- candidate_role: cross-system aging panel comparison and resource/social predictor validation candidate.
- supports: England 50+ aging trajectories, social and economic circumstances, health and wellbeing comparison outside the United States.
- does_not_support: no global transportability proof; no individual prediction validation; no calibrated Human Infra model.
- minimum_before_use: confirm data release, UK Data Service conditions, wave structure, mortality/health linkage availability, weights, socioeconomic fields and comparability with HRS/SHARE.
- maps_to_model_need: `mortality`, `function`, `cognition`, `resourceSocial`, `externalValidation`
- next_check: use ELSA as a cross-national validation candidate after HRS/NHATS field mapping is stable.

### SRC-DATA-SHARE

- id: `share`
- source: Survey of Health, Ageing and Retirement in Europe
- official_url: <https://share-eric.eu/>
- type: cross-national aging panel
- candidate_role: cross-national transportability, policy-context and resource/social comparison candidate.
- supports: multi-country 50+ health, cognition, employment, social networks, economics and partial biomarker comparison.
- does_not_support: no guarantee that one model transports across all countries; no commercial scoring; no individual longevity prediction or calibrated Human Infra model.
- minimum_before_use: confirm non-commercial access terms, country/wave selection, harmonized variables, missingness, mortality endpoints, biomarker availability and policy-context coding.
- maps_to_model_need: `function`, `cognition`, `biomarkers`, `resourceSocial`, `externalValidation`
- next_check: create a transportability Data Card after defining the baseline development cohort.

### SRC-DATA-FRAMINGHAM

- id: `framingham-heart-study`
- source: Framingham Heart Study
- official_url: <https://www.framinghamheartstudy.org/>
- type: multi-generation cardiovascular cohort
- candidate_role: classical risk-modeling reference, cardiovascular endpoint and biomarker-risk history candidate.
- supports: cardiovascular risk-factor logic, long-run cohort tradition, disease event modeling and methodological comparison.
- does_not_support: no broad effective-immortality validation; no all-mechanism aging coverage; no individual death-date prediction or calibrated Human Infra model.
- minimum_before_use: confirm data access path, cohort generation, consent and repository constraints, endpoint definitions, covariate history and demographic transportability.
- maps_to_model_need: `mortality`, `biomarkers`, `cardiovascular`, `genomics`, `externalValidation`
- next_check: use as a cardiovascular model sanity reference, not as the main Human Infra life-path cohort.

## Cross-Source Selection Logic

The first real calibration attempt must not start by asking which source is most prestigious. It must ask which source can satisfy the model contract:

```text
target population
  -> time zero
  -> outcome definition
  -> censoring rule
  -> predictor availability
  -> missingness and measurement error
  -> internal validation
  -> external validation
  -> prohibited use boundary
```

Minimum recommended sequence:

1. Choose one development source for a narrow cohort-level question.
2. Write a Data Card before any data access or modeling.
3. Use a second source for external validation or transportability stress testing.
4. Keep outputs cohort-level and scenario-level.
5. Do not emit individual death-date, medical advice, or personal longevity ranking.

## Current Decision

No source is approved for model calibration yet. The correct current status is:

```text
candidate sources registered
  -> Source Cards drafted
  -> Data Card template required
  -> variable dictionaries missing
  -> no governed data acquisition
  -> no calibration
  -> no external validation
```
