# Falsifier Source Card Field Extraction v0.1

This pack promotes all current anchors from
[`human-infra-falsifier-source-card-backfill.json`](../reference/human-infra-falsifier-source-card-backfill.json)
into field-level Source Cards.

It follows the [`Source Card System`](../reference/source-card-system.md): each source must say what it supports, where it fits in Human Infra, what model position it can occupy, and what it cannot support.

## Scope

| Item | Status |
| --- | --- |
| Selected source anchors | 21 |
| Backfill anchors remaining | 0 |
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
| `SA-HALLMARKS-AGING-2013` | Baseline aging-mechanism taxonomy | Biological-maintenance state families | Historical taxonomy is not intervention proof |
| `SA-NCI-SCREENING-BIAS` | Screening endpoint and bias boundary | Detection, mortality and harm interpretation | Earlier detection is not automatically life extension |
| `SA-IMMUNOSENESCENCE-2024` | Immune aging and inflammaging scaffold | Immune-maintenance state and risk channels | Immune vocabulary is not intervention efficacy |
| `SA-PERSONAL-INFORMATICS-2010` | Self-tracking workflow | Observation, reflection and action stages | Data collection alone is not continuity gain |
| `SA-DYNAMIC-DIGITAL-TWIN-2022` | Life-course digital twin architecture | Subject-state modeling and simulation readiness | Architecture is not validated deployment |
| `SA-EXTENDED-MIND-1998` | Tool and memory extension genealogy | Cognitive support and agency boundary | Conceptual extension is not empirical tool benefit |
| `SA-BRAIN-PRESERVATION-2024` | Structural brain preservation hypothesis | Preservation fidelity and identity boundary | Preservation is not revival or continuity proof |
| `SA-GPS-RELATIVITY-2003` | Relativistic clock accounting | Proper-time and reference-observer discipline | Weak-field GPS evidence is not strong-redshift waiting feasibility |
| `SA-NASA-BLACK-HOLES` | Public black-hole context and hazard boundary | Metaphor control and hazard vocabulary | Explainer context is not a waiting-room protocol |
| `SA-NIST-AI-RMF-2023` | AI risk-management boundary | Trustworthiness, monitoring and failure modes | Framework citation does not certify a tool |
| `SA-WHO-CONSTITUTION` | Multidimensional health value anchor | Physical, mental and social health-state dimensions | Normative health definition is not intervention evidence |

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

### `SA-HALLMARKS-AGING-2013`

- Source: *The Hallmarks of Aging*, 2013, `https://pmc.ncbi.nlm.nih.gov/articles/PMC3836174/`
- Use: baseline aging-hallmark taxonomy for original biological-maintenance domains.
- Domains: `genomic-stability-dna-repair`, `biological-age-clocks-biomarker-validation`, `proteostasis-autophagy`, `mitochondrial-bioenergetics`, `cellular-senescence-clearance`, `stem-cell-reserve-renewal`.
- Model position: biological-maintenance state families and conceptual deterioration mechanisms.
- Falsifier use: if hallmark status is cited as proof of lifespan extension, downgrade to mechanism-level support.
- Boundary: does not prove that targeting a hallmark improves human survival, function or effective time.

### `SA-NCI-SCREENING-BIAS`

- Source: *What Cancer Screening Statistics Really Tell Us*, official NCI explainer, `https://www.cancer.gov/about-cancer/screening/research/what-screening-statistics-mean`
- Use: endpoint and bias boundary for early-detection claims.
- Domains: `cancer-screening-early-detection-continuity`, `longevity-evidence`, `biological-age-clocks-biomarker-validation`.
- Model position: screening observation, lead-time bias, overdiagnosis, mortality endpoint and harm-benefit fields.
- Falsifier use: if earlier detection or longer post-diagnosis survival is treated as mortality benefit without bias review, downgrade the claim.
- Boundary: does not endorse or reject individual screening.

### `SA-IMMUNOSENESCENCE-2024`

- Source: *Immunosenescence: Aging and Immune System Decline*, 2024, `https://pubmed.ncbi.nlm.nih.gov/39771976/`
- Use: immune aging, inflammaging and immune-function tradeoff scaffold.
- Domains: `immune-maintenance`, `longevity-evidence`, `cancer-screening-early-detection-continuity`, `cellular-senescence-clearance`.
- Model position: immune reserve, inflammation, infection risk, vaccine response and immune surveillance.
- Falsifier use: if an immune route lacks infection, inflammation, cancer-surveillance and adverse-activation boundaries, mark it incomplete.
- Boundary: does not prove lifespan benefit, individual immune status or intervention safety.

### `SA-PERSONAL-INFORMATICS-2010`

- Source: *A Stage-Based Model of Personal Informatics Systems*, 2010, `https://dl.acm.org/doi/10.1145/1753326.1753409`
- Use: self-tracking workflow from preparation and collection through reflection and action.
- Domains: `longevity-evidence`, `neuro-continuity`, `nutrition-metabolic-health`, `cardiovascular-resilience`.
- Model position: observation process, feedback delay, reflection quality and action-loop completion.
- Falsifier use: if a data tool stops at collection and cannot support reflection or action, downgrade it to observation-only.
- Boundary: does not prove a tool improves health, cognition, effective time or survival.

### `SA-DYNAMIC-DIGITAL-TWIN-2022`

- Source: *Dynamic Digital Twin: Diagnosis, Treatment, Prediction, and Prevention of Disease During the Life Course*, 2022, `https://www.jmir.org/2022/9/e35675`
- Use: life-course subject-state modeling architecture.
- Domains: `longevity-evidence`, `biological-age-clocks-biomarker-validation`, `neuro-continuity`, `cardiovascular-resilience`.
- Model position: multimodal state model, simulation scope, prediction horizon and implementation barriers.
- Falsifier use: if a page says digital twin but lacks data, update loop, validation and deployment boundary, downgrade to architecture-only.
- Boundary: does not prove an operational human digital twin or calibrated life-path model exists.

### `SA-EXTENDED-MIND-1998`

- Source: *The Extended Mind*, 1998, `https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8284.00096`
- Use: conceptual support for external tools, memory systems and environments as possible cognitive supports.
- Domains: `memory-editing`, `neuro-continuity`, `brain-preservation-connectomics-emulation`, `disembodied-cns`.
- Model position: cognitive support, tool integration, external memory and agency boundary.
- Falsifier use: if a tool is unreliable, unavailable, unauditable or agency-eroding, it cannot count as stable cognitive extension.
- Boundary: does not prove any specific AI, memory or automation tool improves long-term subject continuity.

### `SA-BRAIN-PRESERVATION-2024`

- Source: *Structural brain preservation: a potential bridge to future medical technologies*, 2024, `https://pmc.ncbi.nlm.nih.gov/articles/PMC11416988/`
- Use: structural-preservation bridge hypothesis for neuro-continuity routes.
- Domains: `brain-preservation-connectomics-emulation`, `biostasis-cryopreservation`, `neuro-continuity`, `future-waiting`.
- Model position: structural fidelity, memory trace preservation, repair window and identity-continuity boundary.
- Falsifier use: if preserved structure cannot support memory, agency or functional reconstruction claims, downgrade to anatomical archive.
- Boundary: does not prove uploading, revival, identity continuity, service quality or personal actionability.

### `SA-GPS-RELATIVITY-2003`

- Source: *Relativity in the Global Positioning System*, 2003, `https://link.springer.com/article/10.12942/lrr-2003-1`
- Use: relativistic clock accounting and reference-observer discipline.
- Domains: `future-waiting`, `longevity-evidence`.
- Model position: proper-time differential, reference observer, clock-rate correction and weak-field boundary.
- Falsifier use: if a waiting scenario lacks metric, worldline or observer definition, classify it cannot-evaluate.
- Boundary: does not prove strong-gravity waiting, artificial black holes, safe orbiting, exit or life support.

### `SA-NASA-BLACK-HOLES`

- Source: *Black Holes - NASA Science*, official explainer, `https://science.nasa.gov/universe/black-holes/`
- Use: public black-hole context and hazard boundary.
- Domains: `future-waiting`, `biostasis-cryopreservation`.
- Model position: strong-gravity context, event-horizon boundary, hazard vocabulary and metaphor control.
- Falsifier use: if black-hole context is used to imply reachable, safe or reversible waiting, downgrade to metaphor-only.
- Boundary: does not prove controlled redshift zones, safe human proximity, communication, exit, life support or recursive upgrading.

### `SA-NIST-AI-RMF-2023`

- Source: *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, 2023, `https://www.nist.gov/itl/ai-risk-management-framework`
- Use: AI governance, risk framing and trustworthiness boundary.
- Domains: `longevity-evidence`, `neuro-continuity`, `future-waiting`, `brain-preservation-connectomics-emulation`.
- Model position: AI tool state, risk management, monitoring, failure modes and human accountability.
- Falsifier use: if an AI route lacks risk management, monitoring, accountability or failure response, downgrade or block it.
- Boundary: does not certify any AI system, model, agent, dashboard or clinical decision support tool.

### `SA-WHO-CONSTITUTION`

- Source: *Constitution of the World Health Organization*, official reference, `https://www.who.int/about/governance/constitution`
- Use: health as multidimensional subject support rather than absence of disease alone.
- Domains: `longevity-evidence`, `nutrition-metabolic-health`, `cardiovascular-resilience`, `neuro-continuity`.
- Model position: physical, mental and social health-state dimensions.
- Falsifier use: if a route improves survival while destroying mental, social or functional support, downgrade under effective-life boundaries.
- Boundary: does not validate any medical, policy, AI or social intervention.

## Next Work

1. Split C1/C2 domain-level cards into exact claim, variable, endpoint, population and uncertainty rows.
2. Build reusable target-trial, prediction-model and biomarker endpoint templates for future route cards.
3. Promote field-level source cards into domain-level Claim-Evidence Matrices where claims are strong enough to enter papers or Web pages.
