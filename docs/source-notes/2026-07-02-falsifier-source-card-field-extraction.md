# Falsifier Source Card Field Extraction v0.1

This pack promotes the first 10 high-leverage anchors from
[`human-infra-falsifier-source-card-backfill.json`](../reference/human-infra-falsifier-source-card-backfill.json)
into field-level Source Cards.

It follows the [`Source Card System`](../reference/source-card-system.md): each source must say what it supports, where it fits in Human Infra, what model position it can occupy, and what it cannot support.

## Scope

| Item | Status |
| --- | --- |
| Selected source anchors | 10 |
| Backfill anchors remaining | 11 |
| Main purpose | Move from source links to field-level source use |
| Allowed use | Research traceability, model-position mapping, falsifier and downgrade checks |
| Prohibited use | Individual prediction, clinical advice, intervention ranking, proof of effective immortality |

## Extraction Table

| Source ID | Human Infra use | Model position | Boundary |
| --- | --- | --- | --- |
| `SA-HALLMARKS-AGING-2023` | Aging mechanism scaffold for C2 source-maintenance domains | State-variable families and mechanism vocabulary | Does not prove any intervention extends lifespan |
| `SA-GRIMAGE-2019` | Biological-age clock observation and mortality-risk association | Observation process and risk-association proxy | Biomarker change is not endpoint or causal proof |
| `SA-YAMANAKA-IPS-2006` | Defined-factor cell identity reprogramming origin | Cell-state transition proof of principle | iPS induction is not whole-body rejuvenation |
| `SA-PARTIAL-REPROGRAMMING-2016` | Preclinical partial reprogramming route hypothesis | Candidate transition under safety gates | Animal/preclinical signals are not human longevity evidence |
| `SA-HALLMARKS-CANCER-2022` | Cancer-risk negative channel for repair and reprogramming routes | Tumor-risk mechanism and safety falsifier | Cancer taxonomy is not screening or treatment benefit |
| `SA-KAPLAN-MEIER-1958` | Aggregate survival-curve and censoring-aware visualization method | Survival function and time-to-event accounting | Aggregate curves are not individual death-date predictions |
| `SA-COX-1972` | Hazard-function and covariate-risk model language | Hazard model and risk-function discipline | Hazard association is not causal intervention proof |
| `SA-TARGET-TRIAL-2022` | Intervention-versus-association boundary | Causal estimand and action-policy gate | Target-trial language does not remove data limitations |
| `SA-TRIPOD-AI-2024` | Prediction model reporting and validation boundary | Model-card, validation and calibration reporting | Reporting guidance does not validate the current toy model |
| `SA-CAPABILITY-APPROACH` | Normative support for capability, function and future choice | Value objective and option-value framing | Normative support is not empirical effectiveness |

## Cards

### `SA-HALLMARKS-AGING-2023`

- Source: *Hallmarks of aging: An expanding universe*, 2023, `https://pubmed.ncbi.nlm.nih.gov/36599349/`
- Use: high-level aging-mechanism scaffold for biological source-maintenance domains.
- Domains: `longevity-evidence`, `cellular-reprogramming`, `mitochondrial-bioenergetics`, `proteostasis-autophagy`, `cellular-senescence-clearance`, `stem-cell-reserve-renewal`.
- Model position: candidate state-variable families, mechanism hypotheses, observation targets.
- Falsifier use: if one hallmark or biomarker is presented as sufficient for effective immortality, downgrade to a narrow candidate mechanism.
- Boundary: does not prove any individual intervention extends lifespan or healthspan.

### `SA-GRIMAGE-2019`

- Source: *DNA methylation GrimAge strongly predicts lifespan and healthspan*, 2019, `https://pmc.ncbi.nlm.nih.gov/articles/PMC6366976/`
- Use: biological-age clock observation and risk-association anchor.
- Domains: `biological-age-clocks-biomarker-validation`, `longevity-evidence`.
- Model position: observation proxy and risk marker; not a causal transition.
- Falsifier use: if a lower clock age is treated as sufficient evidence of extended effective life, downgrade the claim.
- Boundary: changing a biomarker is not the same as changing mortality, function or future option value.

### `SA-YAMANAKA-IPS-2006`

- Source: *Induction of pluripotent stem cells from mouse embryonic and adult fibroblast cultures by defined factors*, 2006, `https://pubmed.ncbi.nlm.nih.gov/16904174/`
- Use: origin anchor for defined-factor cell-state reprogramming.
- Domains: `cellular-reprogramming`, `regenerative-medicine`, `stem-cell-reserve-renewal`.
- Model position: cell identity and differentiation state transition.
- Falsifier use: if a claim jumps from iPS induction to human rejuvenation, require partial-reprogramming, cancer and clinical safety evidence.
- Boundary: does not support whole-body rejuvenation, clinical anti-aging use or subject-continuity preservation.

### `SA-PARTIAL-REPROGRAMMING-2016`

- Source: *In Vivo Amelioration of Age-Associated Hallmarks by Partial Reprogramming*, 2016, `https://pmc.ncbi.nlm.nih.gov/articles/PMC5679279/`
- Use: partial reprogramming as a preclinical route hypothesis.
- Domains: `cellular-reprogramming`, `regenerative-medicine`, `longevity-evidence`, `cancer-screening-early-detection-continuity`.
- Model position: candidate age-state transition under dose, duration, identity and safety gates.
- Falsifier use: if identity retention, tumor risk or delivery control is missing, classify the route as cannot-evaluate or negative under safety gates.
- Boundary: does not prove human longevity benefit or systemic rejuvenation.

### `SA-HALLMARKS-CANCER-2022`

- Source: *Hallmarks of Cancer: New Dimensions*, 2022, `https://pubmed.ncbi.nlm.nih.gov/35022204/`
- Use: cancer mechanism taxonomy and negative-channel boundary for repair, regeneration and reprogramming routes.
- Domains: `cancer-screening-early-detection-continuity`, `cellular-reprogramming`, `genomic-stability-dna-repair`, `immune-maintenance`.
- Model position: tumor-risk mechanism and safety falsifier.
- Falsifier use: if a route increases proliferative or identity-changing pressure without cancer-risk governance, downgrade or block the route.
- Boundary: does not support a specific screening protocol, treatment choice or net survival benefit.

### `SA-KAPLAN-MEIER-1958`

- Source: *Nonparametric Estimation from Incomplete Observations*, 1958, `https://web.stanford.edu/~lutian/coursepdf/KMpaper.pdf`
- Use: aggregate survival-curve and censoring-aware visualization method.
- Domains: `longevity-evidence`, `future-waiting`, `biological-age-clocks-biomarker-validation`.
- Model position: survival function, censoring status, event-time accounting.
- Falsifier use: if a page infers individual remaining life from an aggregate curve, fail the boundary gate.
- Boundary: does not validate any scenario parameter, intervention or personal survival estimate.

### `SA-COX-1972`

- Source: *Regression Models and Life-Tables*, 1972, `https://www.jstor.org/stable/2985181`
- Use: hazard-function and covariate-risk model anchor.
- Domains: `longevity-evidence`, `biological-age-clocks-biomarker-validation`, `cardiovascular-resilience`.
- Model position: risk-function language, covariate-risk link and hazard boundary.
- Falsifier use: if a covariate association is treated as a do(A) effect, downgrade it to observational association.
- Boundary: does not establish causality, calibration or a specific intervention effect.

### `SA-TARGET-TRIAL-2022`

- Source: *A Framework for Causal Inference From Observational Data*, 2022, `https://pubmed.ncbi.nlm.nih.gov/36508210/`
- Use: intervention-versus-association boundary and target-trial design discipline.
- Domains: `longevity-evidence`, `cellular-reprogramming`, `nutrition-metabolic-health`, `cardiovascular-resilience`.
- Model position: intervention, comparator, eligibility, time zero and endpoint fields.
- Falsifier use: if no intervention, comparator, time zero or endpoint can be specified, mark the route cannot-evaluate for causal effect.
- Boundary: does not make weak data causal or remove confounding risk.

### `SA-TRIPOD-AI-2024`

- Source: *TRIPOD+AI statement: updated guidance for reporting clinical prediction models*, 2024, `https://www.bmj.com/content/385/bmj-2023-078378`
- Use: prediction-model reporting, validation and calibration boundary.
- Domains: `longevity-evidence`, `biological-age-clocks-biomarker-validation`, `future-waiting`.
- Model position: model card, predictor/outcome definition, validation, calibration and prohibited-output boundary.
- Falsifier use: if a model lacks validation, calibration, outcome definition or prohibited-output boundary, downgrade it to toy or exploratory status.
- Boundary: does not validate the current toy model, NCG protocol or any clinical prediction.

### `SA-CAPABILITY-APPROACH`

- Source: *Capability Approach*, living reference, `https://plato.stanford.edu/entries/capability-approach/`
- Use: normative anchor for function, agency, effective time and future choice.
- Domains: `longevity-evidence`, `future-waiting`, `brain-preservation-connectomics-emulation`, `neuro-continuity`, `biostasis-cryopreservation`.
- Model position: value objective, functioning state and option-value framing.
- Falsifier use: if a route extends time while destroying agency, cognition, function or choice, it fails the capability boundary.
- Boundary: does not prove empirical effectiveness of any biological, AI, social or physical route.

## Next Work

1. Extract the remaining 11 source anchors from the backfill register.
2. Split C1/C2 domain-level cards into exact claim, variable, endpoint, population and uncertainty rows.
3. Build reusable target-trial, prediction-model and biomarker endpoint templates for future route cards.
