# Life-Path Toy Model Audit

- Overall status: `PASS`
- Model path: `web/src/data/life-path-toy-model.json`
- Model SHA-256: `a4c92209d79d20579bf1f575d5ebf07ffe5be9ccaf6bf3f3eef08efa287b5377`
- Generated at: `2026-07-02T01:57:08.979450+00:00`

## Checks

| Check | Status | Detail |
| --- | --- | --- |
| `schema-version` | `PASS` | schemaVersion='human-infra.life-path-toy-results.v1' |
| `source-hash` | `PASS` | source path and sha256 must point back to the scenario input |
| `model-card-required-fields` | `PASS` | required=['evidenceBoundary', 'modelClass', 'modelName', 'nonUses', 'purpose', 'upgradeGate'] |
| `prohibited-use-boundary` | `PASS` | model card must explicitly prohibit death-date or individual prediction use |
| `synthetic-evidence-boundary` | `PASS` | model card must state the synthetic evidence boundary |
| `scenario-count` | `PASS` | scenario_count=4 |
| `scenario-id-unique` | `PASS` | ids=['baseline', 'assisted', 'convergence', 'escape'] |
| `baseline-scenario-present` | `PASS` | baseline scenario must be present for comparison |
| `metrics-required-fields` | `PASS` | each scenario must expose required metrics |
| `survival-curve-monotonic` | `PASS` | scenario survival curves must be monotonic non-increasing |
| `probability-ranges` | `PASS` | survival and health-quality values must remain in [0, 1] |
| `resource-budget-ranges` | `PASS` | resource budget percentages must remain in [0, 100] |
| `lev-open-boundary-contract` | `PASS` | LEV >= 1 must be reported as open boundary |
| `no-individual-death-date-fields` | `PASS` | prohibited_keys=[] |
| `readiness-schema-version` | `PASS` | schemaVersion='human-infra.life-path-calibration-readiness.v1' |
| `readiness-honest-current-boundary` | `PASS` | readiness contract must explicitly say real cohort, calibration, external validation, and individual use are unavailable |
| `readiness-method-anchors` | `PASS` | missing_standards=[] |
| `readiness-required-sections` | `PASS` | missing_sections=[] |
| `readiness-target-population` | `PASS` | target population must define minimum real-cohort fields and current placeholder |
| `readiness-time-zero` | `PASS` | time zero must define index-date rule fields before calibration |
| `readiness-outcome-boundary` | `PASS` | outcomes must include primary cohort outcomes and forbid individual death-date output |
| `readiness-estimands` | `PASS` | estimands must define scenario-level questions before calibration |
| `readiness-data-missing-boundary` | `PASS` | data requirements must state that real cohort and endpoint follow-up are missing |
| `readiness-validation-plan` | `PASS` | validation plan must include internal/external validation fields and not-started status |
| `readiness-calibration-plan` | `PASS` | calibration plan must include diagnostics and not-started status |
| `readiness-sensitivity-plan` | `PASS` | sensitivity analysis plan must define required analyses |
| `readiness-bias-applicability-plan` | `PASS` | bias and applicability plan must define risk domains |
| `readiness-reporting-plan` | `PASS` | reporting plan must define required artifacts beyond Web visualization |
| `readiness-prohibited-uses` | `PASS` | prohibited uses must block individual death-date prediction and medical advice |
| `readiness-upgrade-gate` | `PASS` | upgrade gate must keep the current decision at cannot-calibrate-yet |
| `data-sources-schema-version` | `PASS` | schemaVersion='human-infra.life-path-data-source-candidates.v1' |
| `data-sources-candidate-only-boundary` | `PASS` | registry must state no data download, access grant, individual data, calibration claim, or causal claim |
| `data-sources-candidate-count` | `PASS` | candidate_count=8 |
| `data-sources-candidate-id-unique` | `PASS` | ids=['hrs', 'nchs-linked-mortality-nhanes-nhis', 'uk-biobank', 'all-of-us', 'nhats', 'elsa', 'share', 'framingham-heart-study'] |
| `data-sources-required-fields` | `PASS` | required=['accessStatus', 'ageFrame', 'cohortType', 'coverageTags', 'geography', 'governanceStatus', 'id', 'limitations', 'modelRoles', 'name', 'officialUrl', 'outcomeSupport', 'populationFrame', 'predictorSupport', 'prohibitedClaims', 'sourceAuthority', 'strengths'] |
| `data-sources-official-https-urls` | `PASS` | each candidate must use an official HTTPS URL |
| `data-sources-access-governance` | `PASS` | each candidate must state access and governance status |
| `data-sources-coverage-tags` | `PASS` | missing_tags=[] |
| `data-sources-coverage-summary` | `PASS` | coverage summary must map required model needs to candidate IDs |
| `data-sources-prohibited-claims` | `PASS` | each candidate must block individual prediction and calibration/causal overclaim |
| `data-sources-next-work` | `PASS` | registry must point toward Source Cards, variable dictionaries, data cards, and governed acquisition |
| `source-cards-doc-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-source-cards.md |
| `data-card-template-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-card-template.md |
| `source-cards-cover-candidate-ids` | `PASS` | missing_ids=[] |
| `source-cards-cover-official-urls` | `PASS` | missing_urls=[] |
| `source-cards-boundary-language` | `PASS` | source cards must preserve candidate-only, no-data, no-calibration, no-individual-prediction, and no-validation boundaries |
| `data-card-template-required-sections` | `PASS` | missing_sections=[] |
| `data-card-template-prohibited-outputs` | `PASS` | data card template must block individual death-date prediction, personal medical advice, personal longevity ranking, and premature calibration claims |
| `nhats-data-card-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-card-nhats.md |
| `nhats-variable-dictionary-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-variable-dictionary-nhats.md |
| `nhats-data-card-identity` | `PASS` | NHATS Data Card must identify source_card_id, source name, draft status, and data_card_id |
| `nhats-data-card-boundaries` | `PASS` | NHATS Data Card must block individual prediction, medical advice, personal ranking, premature calibration, and raw-data AI upload |
| `nhats-data-card-source-trace` | `PASS` | NHATS Data Card must cite overview, data access, conditions of use, user guide, and sample design sources |
| `nhats-data-card-decision` | `PASS` | NHATS Data Card must keep the current decision at cannot-evaluate-yet and name effective_time_proxy plus abort conditions |
| `nhats-variable-dictionary-boundaries` | `PASS` | NHATS variable dictionary must remain candidate-only and block extraction/calibration/individual-prediction claims |
| `nhats-variable-dictionary-core-examples` | `PASS` | NHATS variable dictionary must include design, decedent, and cognition example fields while still marking them as candidates |
| `nhats-variable-dictionary-model-roles` | `PASS` | NHATS variable dictionary must map variable families to Human Infra model roles and keep decision at cannot-calibrate-yet |
| `nhats-extraction-manifest-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-extraction-manifest-nhats-draft.md |
| `nhats-extraction-manifest-identity` | `PASS` | manifest must bind NHATS source card, data card, variable dictionary, manifest ID, and cannot-extract status |
| `nhats-extraction-manifest-access-terms` | `PASS` | manifest must record registration, sensitive/restricted application, Colectica, aggregate reporting, n<5, and public AI upload boundaries |
| `nhats-extraction-manifest-official-source-refresh` | `PASS` | manifest must record current official NHATS access, Colectica, AI-upload, temporary-file-availability and restricted-file facts |
| `nhats-extraction-manifest-no-data-boundary` | `PASS` | manifest must explicitly block download, extraction script, raw repository data, calibration/validation claim, and individual death-date prediction |
| `nhats-extraction-manifest-acquisition-readiness-gates` | `PASS` | manifest must expose acquisition-readiness gates before any governed NHATS extraction |
| `nhats-extraction-manifest-variable-groups` | `PASS` | manifest must include identity, weight/design, endpoint, cognition, effective-time and derived-output variables |
| `nhats-extraction-manifest-extraction-rules` | `PASS` | manifest must block scripts, downloads, sensitive/restricted use, metrics, unsafe display, and prose-only variable inference |
| `nhats-extraction-manifest-required-slots` | `PASS` | manifest must expose the blank slots required before governed extraction |
| `nhats-extraction-manifest-abort-conditions` | `PASS` | manifest must define abort gates for access, Colectica, weights/design, endpoint ambiguity, disclosure suppression, raw-data leakage, and unsafe outputs |
| `nhats-extraction-manifest-source-trace` | `PASS` | manifest must cite official NHATS overview, access, terms, cross-year search, files, user guide, and sample design sources |
| `sensitivity-analysis-exists` | `PASS` | web/src/data/life-path-sensitivity-analysis.json |
| `sensitivity-schema-version` | `PASS` | schemaVersion='human-infra.life-path-sensitivity.v1' |
| `sensitivity-source-model-hash` | `PASS` | sensitivity output must point back to the generated model path and sha256 |
| `sensitivity-boundary-language` | `PASS` | sensitivity analysis must preserve synthetic/no-real-cohort/no-calibration/no-individual-use boundaries |
| `sensitivity-parameter-coverage` | `PASS` | missing_parameters=[] |
| `sensitivity-result-count` | `PASS` | expected=48, actual=48 |
| `sensitivity-result-shape` | `PASS` | directions=['high', 'low'], scenarios=['assisted', 'baseline', 'convergence', 'escape'] |
| `sensitivity-result-ranges` | `PASS` | sensitivity result metrics must keep survival/option probabilities in [0, 1] and numeric summary fields present |
| `sensitivity-stability-summary` | `PASS` | stability summary must cover every scenario, boundary stability, ranges, and most-sensitive parameter |
| `sensitivity-sanity-checks` | `PASS` | sensitivity sanity checks must bind expected result count and suppress death-date / individual prediction |
| `sensitivity-no-individual-death-date-fields` | `PASS` | prohibited_keys=[] |

## Calibration Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_calibration_readiness.json`
- Readiness SHA-256: `ca9bc83693b29f198d803bb0741cad4a136884e24d290073fcbe235712326bd2`
- Readiness status: `PASS`
- Boundary: readiness fields are present, but no real cohort, calibration, external validation, or individual use is available.

## Data Source Candidates

- Registry path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_data_source_candidates.json`
- Registry SHA-256: `da21ba7fa51d964ca86913b7a1820159a981a25cced8d3f304f4efd24f35d82e`
- Registry status: `PASS`
- Boundary: candidate sources are mapped, but no data has been downloaded, accessed, fitted, calibrated, or validated.

## Source Card Docs

- Source Cards path: `domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-source-cards.md`
- Source Cards SHA-256: `178013a5d3a45388d735c297df0c566415dc28d6aeec8891823a1d21dedb7b68`
- Data Card template path: `domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-card-template.md`
- Data Card template SHA-256: `2ad38f8931e365e78b471ef03087f7eeb1624f87ff96be615d950c890fae94c2`
- Source Card docs status: `PASS`
- Boundary: source cards and the data-card template only prove data-governance readiness scaffolding; they do not prove data access, field availability, calibration, or validation.

## NHATS Data Admission

- NHATS Data Card path: `domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-data-card-nhats.md`
- NHATS Data Card SHA-256: `d368611ca03032e5ab1c5f728299b6584b01a659ab8f0cf2e1f2d755ed57d417`
- NHATS variable dictionary path: `domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-variable-dictionary-nhats.md`
- NHATS variable dictionary SHA-256: `906b7648dac9dda5c43b83bab2c44b58e53aab7e79aa13da4e77adc879b06ea8`
- NHATS data admission status: `PASS`
- Boundary: NHATS is only a draft admission candidate for late-life effective-time modeling; no data access, extraction, calibration, validation, or individual prediction is claimed.

## NHATS Extraction Manifest

- Manifest path: `domains/c1-boundary-rewriting/longevity-evidence/docs/life-path-extraction-manifest-nhats-draft.md`
- Manifest SHA-256: `a667200dc19d1c1e22f221bd68ef9560cb8bd33e683e771bdaa8bd525c6388ac`
- Manifest status: `PASS`
- Boundary: the manifest is a pre-extraction gate; it blocks scripts, downloads, field inference, calibration, validation, raw-data exposure and unsafe individual outputs until official file-level requirements are complete.

## Sensitivity Analysis

- Sensitivity path: `web/src/data/life-path-sensitivity-analysis.json`
- Sensitivity SHA-256: `73ce504931ad39a88f012185a1959cf6d617b98804a691e167e111a83281e10c`
- Sensitivity status: `PASS`
- Boundary: sensitivity analysis is synthetic one-factor-at-a-time stress testing; it does not prove empirical parameter values, causal effects, calibrated prediction, or individual usefulness.

## Standard Alignment

| Standard | Local gate | Status | Boundary |
| --- | --- | --- | --- |
| TRIPOD+AI | model card + schema + transparent scenario output + calibration readiness fields | `PARTIAL` | toy model only; no development, calibration, or validation cohort |
| PROBAST / PROBAST+AI | bias/applicability plan and prohibited-use boundary | `PARTIAL` | formal risk-of-bias assessment requires real study design and data |
| ISPOR modeling good practices | versioned inputs, executable model, generated outputs, audit artifact, planned sensitivity fields | `PARTIAL` | no decision model, calibration, cost model, or executed sensitivity analysis yet |
| MRC complex interventions framework | mechanism chain and context boundary in maturity roadmap | `PARTIAL` | stakeholder process and implementation evaluation are not started |
| OHDSI Patient-Level Prediction | target population, time zero, outcome, predictor, time-at-risk and validation placeholders | `PARTIAL` | no OHDSI dataset, package execution, or patient-level prediction study is claimed |

## Boundary

This audit proves only that the synthetic toy model output satisfies the local reporting and sanity contract. It does not prove clinical validity, predictive validity, causal validity, or individual usefulness.
