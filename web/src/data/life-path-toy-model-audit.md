# Life-Path Toy Model Audit

- Overall status: `PASS`
- Model path: `web/src/data/life-path-toy-model.json`
- Model SHA-256: `a4c92209d79d20579bf1f575d5ebf07ffe5be9ccaf6bf3f3eef08efa287b5377`
- Generated at: `2026-07-02T04:08:40.900253+00:00`

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
| `nhats-acquisition-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_acquisition_readiness.json |
| `nhats-acquisition-readiness-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-acquisition-readiness.v1' |
| `nhats-acquisition-readiness-identity` | `PASS` | readiness contract must bind NHATS source, Data Card, manifest and cannot-extract status |
| `nhats-acquisition-readiness-current-decision` | `PASS` | current decision must explicitly block acquisition, extraction scripts, raw repository data, calibration and individual prediction |
| `nhats-acquisition-readiness-source-coverage` | `PASS` | missing_source_ids=[] |
| `nhats-acquisition-readiness-source-urls` | `PASS` | official source refresh entries must use HTTPS URLs |
| `nhats-acquisition-readiness-source-facts` | `PASS` | official source refresh entries must include observed fact and model consequence |
| `nhats-acquisition-readiness-gate-coverage` | `PASS` | missing_gate_ids=[] |
| `nhats-acquisition-readiness-gate-status` | `PASS` | each gate must have a valid status, required evidence and next evidence |
| `nhats-acquisition-readiness-blocking-gates` | `PASS` | missing or partial gates must block extraction |
| `nhats-acquisition-readiness-gate-summary` | `PASS` | gate summary must keep all acquisition gates blocking until ready evidence exists |
| `nhats-acquisition-readiness-prohibited-actions` | `PASS` | readiness contract must prohibit premature download, scripts, raw data, public AI upload, individual death-date prediction and calibration claims |
| `nhats-acquisition-readiness-next-work` | `PASS` | next work must point to file-tier, Cross-Year Search variable confirmation and disclosure control |
| `nhats-file-tier-table-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_file_tier_table.json |
| `nhats-file-tier-table-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-file-tier-table.v1' |
| `nhats-file-tier-table-identity` | `PASS` | file-tier table must bind NHATS source, Data Card, manifest, acquisition readiness and candidate-only status |
| `nhats-file-tier-table-current-decision` | `PASS` | file-tier table must still block download, scripts, repository storage, public AI upload, calibration and individual prediction |
| `nhats-file-tier-table-round-window` | `PASS` | round-window candidate must remain R13/R14 candidate-only and extraction-blocked |
| `nhats-file-tier-table-row-coverage` | `PASS` | missing_row_ids=[] |
| `nhats-file-tier-table-row-shape` | `PASS` | each file row must expose file family, format, access tier, official path, planned use and blocking fields |
| `nhats-file-tier-table-source-paths` | `PASS` | file rows must point to official HTTPS pages and official /system/files paths |
| `nhats-file-tier-table-row-boundaries` | `PASS` | every row must keep download, extraction, repository storage and public AI upload blocked |
| `nhats-file-tier-table-tier-summary` | `PASS` | tier summary must match row counts and keep all download/extraction/storage/AI rows blocked |
| `nhats-file-tier-table-method-docs` | `PASS` | missing_method_doc_ids=[] |
| `nhats-file-tier-table-prohibited-actions` | `PASS` | file-tier table must prohibit premature download, prose-only variables, sensitive-file use, raw storage, public AI upload and individual prediction |
| `nhats-file-tier-table-next-work` | `PASS` | next work must point to canonical format, Colectica variables, weights, endpoint and disclosure-control work |
| `nhats-file-tier-table-source-trace` | `PASS` | source trace must include R13/R14 files, Cross-Year Search, methods documentation and Conditions of Use |
| `nhats-first-estimand-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_first_estimand_protocol.json |
| `nhats-first-estimand-protocol-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-first-estimand-protocol.v1' |
| `nhats-first-estimand-protocol-identity` | `PASS` | protocol must bind NHATS source, Data Card, manifest, variable dictionary, acquisition readiness and file-tier table |
| `nhats-first-estimand-protocol-current-decision` | `PASS` | protocol must block running, download, extraction scripts, post-outcome variable selection, calibration, validation and individual prediction |
| `nhats-first-estimand-protocol-estimand-boundary` | `PASS` | estimand must be cohort-level functional-survival and must not claim individual, causal, clinical or LEV proof use |
| `nhats-first-estimand-protocol-target-population` | `PASS` | target population must bind R13/R14, age 65+, public-use first pass and sensitive/restricted exclusion |
| `nhats-first-estimand-protocol-time-zero` | `PASS` | time zero must freeze R13 predictors, end at R14 follow-up and block outcome peeking |
| `nhats-first-estimand-protocol-outcome-definition` | `PASS` | outcome must define aggregate functional-survival state and forbid individual death-date output |
| `nhats-first-estimand-protocol-predictor-families` | `PASS` | missing_predictor_ids=[] |
| `nhats-first-estimand-protocol-censoring-missingness` | `PASS` | censoring rules must distinguish death, proxy, residential care, nonresponse and not-classifiable states before metrics |
| `nhats-first-estimand-protocol-survey-design` | `PASS` | survey design must require weights, strata, cluster/PSU and variance method before metrics |
| `nhats-first-estimand-protocol-analysis-boundary` | `PASS` | analysis plan must allow only aggregate diagnostics and prohibit row-level, small-cell, individual and validation/calibration outputs |
| `nhats-first-estimand-protocol-readiness-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-first-estimand-protocol-gate-summary` | `PASS` | gate summary must keep every estimand gate blocking until ready evidence exists |
| `nhats-first-estimand-protocol-source-trace` | `PASS` | source trace must include R13/R14 files, Cross-Year Search, methods documentation and Conditions of Use |
| `nhats-first-estimand-protocol-next-work` | `PASS` | next work must point to canonical files, Colectica/codebooks, cohort flow and disclosure control |
| `nhats-variable-confirmation-matrix-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_variable_confirmation_matrix.json |
| `nhats-variable-confirmation-matrix-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-variable-confirmation-matrix.v1' |
| `nhats-variable-confirmation-matrix-identity` | `PASS` | matrix must bind NHATS source, first estimand protocol, manifest and variable dictionary |
| `nhats-variable-confirmation-matrix-current-decision` | `PASS` | matrix must block exact-variable readiness, cohort flow, endpoint routing, survey design, download, extraction, calibration and individual prediction |
| `nhats-variable-confirmation-matrix-source-facts` | `PASS` | missing_fact_ids=[] |
| `nhats-variable-confirmation-matrix-round-rules` | `PASS` | round instantiation must bind R13/R14, # placeholder, candidate R13/R14 examples and candidate-pattern-only status |
| `nhats-variable-confirmation-matrix-variable-groups` | `PASS` | missing_group_ids=[] |
| `nhats-variable-confirmation-matrix-cohort-flow` | `PASS` | missing_steps=[] |
| `nhats-variable-confirmation-matrix-readiness-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-variable-confirmation-matrix-gate-summary` | `PASS` | gate summary must keep every variable-confirmation gate missing and blocking |
| `nhats-variable-confirmation-matrix-prohibited-actions` | `PASS` | matrix must prohibit download, extraction scripts, unconfirmed pattern names, outcome-peeking, public AI upload and individual outputs |
| `nhats-variable-confirmation-matrix-next-work` | `PASS` | next work must point to Colectica, cohort flow, survey design and disclosure control |
| `nhats-variable-confirmation-matrix-source-trace` | `PASS` | source trace must include Cross-Year Search, User Guide, Technical Paper 55, Conditions of Use and R13/R14 file pages |
| `nhats-cohort-flow-endpoint-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json |
| `nhats-cohort-flow-endpoint-protocol-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-cohort-flow-endpoint-protocol.v1' |
| `nhats-cohort-flow-endpoint-protocol-identity` | `PASS` | protocol must bind NHATS source, first estimand, variable matrix, manifest, file-tier table and cannot-extract status |
| `nhats-cohort-flow-endpoint-protocol-current-decision` | `PASS` | current decision must block cohort flow, endpoint routing, download, extraction scripts, weighted metrics, public export, calibration and individual prediction |
| `nhats-cohort-flow-endpoint-protocol-source-facts` | `PASS` | missing_fact_ids=[] |
| `nhats-cohort-flow-endpoint-protocol-flow-rows` | `PASS` | missing_row_ids=[] |
| `nhats-cohort-flow-endpoint-protocol-route-classes` | `PASS` | missing_route_ids=[] |
| `nhats-cohort-flow-endpoint-protocol-output-contracts` | `PASS` | missing_output_ids=[] |
| `nhats-cohort-flow-endpoint-protocol-disclosure-control` | `PASS` | disclosure control must enforce n<5 suppression, aggregate-only export, no row-level export and no public AI upload |
| `nhats-cohort-flow-endpoint-protocol-readiness-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-cohort-flow-endpoint-protocol-gate-summary` | `PASS` | gate summary must keep every cohort-flow and endpoint-routing gate missing and blocking |
| `nhats-cohort-flow-endpoint-protocol-prohibited-actions` | `PASS` | protocol must prohibit download, scripts, candidate-name routing, row-level export, individual death-date prediction, public AI upload, small-cell export and calibration claims |
| `nhats-cohort-flow-endpoint-protocol-next-work` | `PASS` | next work must point to Colectica route fields, canonical files, cohort-flow table, missingness map, disclosure control and survey design |
| `nhats-cohort-flow-endpoint-protocol-source-trace` | `PASS` | source trace must include Cross-Year Search, Conditions, User Guide, Technical Paper 55 and R13/R14 file pages |
| `nhats-disclosure-policy-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_disclosure_control_policy.json |
| `nhats-disclosure-test-cases-exist` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_disclosure_control_test_cases.json |
| `nhats-disclosure-validation-exists` | `PASS` | web/src/data/life-path-nhats-disclosure-control-validation.json |
| `nhats-disclosure-policy-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-disclosure-control-policy.v1' |
| `nhats-disclosure-policy-identity` | `PASS` | policy must bind NHATS source, cohort-flow protocol, first estimand, variable matrix and draft status |
| `nhats-disclosure-policy-current-decision` | `PASS` | policy must block public export, row-level export, public AI upload, small-cell export, calibration and individual prediction |
| `nhats-disclosure-policy-rules` | `PASS` | policy rules must require aggregate-only output, n<5 suppression, allowed aggregate outputs, forbidden unsafe outputs, row-level block and public-AI block |
| `nhats-disclosure-policy-source-trace` | `PASS` | policy source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55 |
| `nhats-disclosure-test-cases-schema` | `PASS` | test cases must bind NHATS source and synthetic-only policy status |
| `nhats-disclosure-test-cases-boundary` | `PASS` | test cases must be synthetic-only and prohibit calibration plus individual prediction |
| `nhats-disclosure-test-case-coverage` | `PASS` | missing_case_ids=[] |
| `nhats-disclosure-test-case-decision-mix` | `PASS` | synthetic cases must include both allowed and blocked examples |
| `nhats-disclosure-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-disclosure-control-validation.v1' |
| `nhats-disclosure-validation-source-hashes` | `PASS` | validation report must point back to current policy and test-case hashes |
| `nhats-disclosure-validation-summary` | `PASS` | validation report must pass every synthetic case and include both allowed and blocked outputs |
| `nhats-disclosure-validation-case-results` | `PASS` | missing_validation_case_ids=[] |
| `nhats-disclosure-validation-boundary` | `PASS` | validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries |
| `nhats-survey-design-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_protocol.json |
| `nhats-survey-design-test-cases-exist` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_test_cases.json |
| `nhats-survey-design-validation-exists` | `PASS` | web/src/data/life-path-nhats-survey-design-validation.json |
| `nhats-survey-design-protocol-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-survey-design-protocol.v1' |
| `nhats-survey-design-protocol-identity` | `PASS` | survey-design protocol must bind NHATS source, upstream readiness/file/estimand/variable/cohort/disclosure contracts and cannot-weight status |
| `nhats-survey-design-current-decision` | `PASS` | survey-design protocol must block weighted counts, weighted curves, variance estimation, population inference, public export, calibration and individual prediction |
| `nhats-survey-design-component-coverage` | `PASS` | missing_component_ids=[] |
| `nhats-survey-design-candidate-fields` | `PASS` | candidate field families must include weight, variance-unit and stratum patterns while staying candidate-pattern-only |
| `nhats-survey-design-readiness-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-survey-design-gate-summary` | `PASS` | gate summary must keep every survey-design gate missing and blocking |
| `nhats-survey-design-source-trace` | `PASS` | survey-design protocol source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55 |
| `nhats-survey-design-prohibited-actions` | `PASS` | survey-design protocol must prohibit premature weighted estimates, population inference, candidate-field overuse and individual outputs |
| `nhats-survey-design-test-cases-schema` | `PASS` | survey-design test cases must bind NHATS source and synthetic-only protocol status |
| `nhats-survey-design-test-cases-boundary` | `PASS` | survey-design test cases must be synthetic-only and prohibit calibration plus individual prediction |
| `nhats-survey-design-test-case-coverage` | `PASS` | missing_case_ids=[] |
| `nhats-survey-design-test-case-decision-mix` | `PASS` | synthetic survey-design cases must include both allowed diagnostics and blocked estimate examples |
| `nhats-survey-design-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-survey-design-validation.v1' |
| `nhats-survey-design-validation-source-hashes` | `PASS` | survey-design validation report must point back to current protocol and test-case hashes |
| `nhats-survey-design-validation-summary` | `PASS` | survey-design validation report must pass every synthetic case and include both allowed and blocked results |
| `nhats-survey-design-validation-case-results` | `PASS` | missing_validation_case_ids=[] |
| `nhats-survey-design-validation-boundary` | `PASS` | survey-design validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries |
| `nhats-missingness-route-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_protocol.json |
| `nhats-missingness-route-test-cases-exist` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_test_cases.json |
| `nhats-missingness-route-validation-exists` | `PASS` | web/src/data/life-path-nhats-missingness-route-validation.json |
| `nhats-missingness-route-protocol-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-missingness-route-protocol.v1' |
| `nhats-missingness-route-protocol-identity` | `PASS` | missingness-route protocol must bind NHATS source, upstream readiness/file/estimand/variable/cohort/disclosure/survey contracts and cannot-route status |
| `nhats-missingness-route-current-decision` | `PASS` | missingness-route protocol must block endpoint classification, missingness rates, weighted route counts, functional-survival curves, public export, calibration and individual prediction |
| `nhats-missingness-route-class-coverage` | `PASS` | missing_route_class_ids=[] |
| `nhats-missingness-route-field-coverage` | `PASS` | missing_route_field_ids=[] |
| `nhats-missingness-route-candidate-fields` | `PASS` | candidate field families must cover identity, interview status, proxy, residential, death and missing codes while staying candidate-pattern-only |
| `nhats-missingness-route-dominance-rules` | `PASS` | dominance rules must register death dominance, missingness blocking, proxy/facility separation, denominator handling and small-cell suppression |
| `nhats-missingness-route-readiness-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-missingness-route-gate-summary` | `PASS` | gate summary must keep every missingness-route gate missing and blocking |
| `nhats-missingness-route-source-trace` | `PASS` | missingness-route protocol source trace must include NHATS conditions, Colectica, R13/R14 files, User Guide and Technical Paper 55 |
| `nhats-missingness-route-prohibited-actions` | `PASS` | missingness-route protocol must prohibit premature routing, missingness-as-outcome, weighted route counts, public AI upload and individual death-date outputs |
| `nhats-missingness-route-test-cases-schema` | `PASS` | missingness-route test cases must bind NHATS source and synthetic-only protocol status |
| `nhats-missingness-route-test-cases-boundary` | `PASS` | missingness-route test cases must be synthetic-only and prohibit calibration plus individual prediction |
| `nhats-missingness-route-test-case-coverage` | `PASS` | missing_case_ids=[] |
| `nhats-missingness-route-test-case-decision-mix` | `PASS` | synthetic missingness-route cases must include both allowed route classifications and blocked endpoint examples |
| `nhats-missingness-route-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-missingness-route-validation.v1' |
| `nhats-missingness-route-validation-source-hashes` | `PASS` | missingness-route validation report must point back to current protocol and test-case hashes |
| `nhats-missingness-route-validation-summary` | `PASS` | missingness-route validation report must pass every synthetic case, include allow/block results and cover route classes |
| `nhats-missingness-route-validation-case-results` | `PASS` | missing_validation_case_ids=[] |
| `nhats-missingness-route-validation-route-coverage` | `PASS` | observed_route_classes=['alive_facility_or_residential_route', 'alive_proxy_interview', 'alive_self_interview', 'decedent_or_death_boundary', 'missing_or_nonresponse', 'not_classifiable', 'suppressed_small_cell'] |
| `nhats-missingness-route-validation-boundary` | `PASS` | missingness-route validation report must preserve synthetic-only, no-real-data, no-calibration and no-individual-prediction boundaries |
| `nhats-route-field-discovery-register-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_field_discovery_register.json |
| `nhats-route-field-discovery-validation-exists` | `PASS` | web/src/data/life-path-nhats-route-field-discovery-validation.json |
| `nhats-route-field-discovery-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-route-field-discovery-register.v1' |
| `nhats-route-field-discovery-identity` | `PASS` | register must bind NHATS, route protocol, variable confirmation matrix and cannot-route status |
| `nhats-route-field-discovery-current-decision` | `PASS` | crosswalk field discovery may be true, but Colectica, data download, classifier, endpoint, weighted counts, public export, calibration and individual prediction must remain false |
| `nhats-route-field-discovery-source-evidence` | `PASS` | missing_evidence_ids=[] |
| `nhats-route-field-discovery-field-families` | `PASS` | missing_field_ids=[] |
| `nhats-route-field-discovery-sensitive-death-exclusion` | `PASS` | sensitive_excluded=['dm13mthdied', 'dm13yrdied', 'dm14mthdied', 'dm14yrdied'] |
| `nhats-route-field-discovery-blocking-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-route-field-discovery-prohibited-actions` | `PASS` | register must block real routing, weighted counts, public AI upload, individual death dates and crosswalk-as-Colectica substitution |
| `nhats-route-field-discovery-source-trace` | `PASS` | sourceTrace must include official Colectica, conditions, User Guide and R13/R14 crosswalk URLs |
| `nhats-route-field-discovery-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-route-field-discovery-validation.v1' |
| `nhats-route-field-discovery-validation-source-hash` | `PASS` | route-field discovery validation must point back to current register hash |
| `nhats-route-field-discovery-validation-summary` | `PASS` | route-field discovery validation must pass with zero failed checks |
| `nhats-route-field-discovery-validation-boundary` | `PASS` | validation boundary must keep Colectica, weighted count and individual prediction gates blocked |
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

## NHATS Acquisition Readiness

- Acquisition readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_acquisition_readiness.json`
- Acquisition readiness SHA-256: `d6338729fac294557236ccebf26c049dab941e8ca1e74669b767c7c427805b19`
- Acquisition readiness status: `PASS`
- Boundary: the structured readiness contract keeps NHATS at cannot-extract-yet until registration, file-tier, Colectica variables, endpoint, survey design, disclosure control, AI boundary and storage/destruction gates are ready.

## NHATS File Tier Table

- File-tier table path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_file_tier_table.json`
- File-tier table SHA-256: `18c151512ffb6e075a134765e13d5b4b07252be10b9e55a211f7d890cefdc6f1`
- File-tier table status: `PASS`
- Boundary: the file-tier table maps official R13/R14 public and sensitive file families, but it still blocks download, extraction, repository storage, public AI upload, calibration and individual prediction.

## NHATS First Estimand Protocol

- First estimand protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_first_estimand_protocol.json`
- First estimand protocol SHA-256: `d939ef97e4a094036136d945e9739713e469b7b435c88857945e46a8f913e571`
- First estimand protocol status: `PASS`
- Boundary: the first estimand protocol pre-registers the R13/R14 aggregate functional-survival question, time-zero, outcome, censoring, survey-design and output boundaries, but it still blocks data download, extraction, calibration, validation and individual prediction.

## NHATS Variable Confirmation Matrix

- Variable confirmation matrix path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_variable_confirmation_matrix.json`
- Variable confirmation matrix SHA-256: `e6a459ac8560a5a40d29a0704ae3a0c9c3fa3a789663936b2f58cdcc899d33d6`
- Variable confirmation matrix status: `PASS`
- Boundary: the variable confirmation matrix records official source facts, candidate field patterns, variable groups and cohort-flow gates, but it still blocks data download, extraction scripts, unconfirmed pattern-derived variables, calibration and individual prediction.

## NHATS Cohort Flow Endpoint Protocol

- Cohort-flow endpoint protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`
- Cohort-flow endpoint protocol SHA-256: `e92a91ffda407cb8fab2e4c3991abadf0ab83c08642e3767802594ba4b037c00`
- Cohort-flow endpoint protocol status: `PASS`
- Boundary: the cohort-flow endpoint protocol pre-registers route classes, aggregate output contracts, disclosure control and blocking gates, but it still blocks download, extraction, endpoint routing, public export, calibration and individual prediction.

## NHATS Disclosure Control Validation

- Disclosure policy path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_disclosure_control_policy.json`
- Disclosure policy SHA-256: `f41f63332d409a234d6b9f49b08274ee8b472faa7cb14ea81c98c85494fc7573`
- Disclosure test cases path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_disclosure_control_test_cases.json`
- Disclosure test cases SHA-256: `0a9cccdbfbd951ba6d04eeb762b9387ba50a13336e4ee4ade43ed976acb4c9c5`
- Disclosure validation path: `web/src/data/life-path-nhats-disclosure-control-validation.json`
- Disclosure validation SHA-256: `452908c103e63bac9f2c4faf7d5c74e0e77c7fb001a4575bcc4f7737cca71c12`
- Disclosure validation status: `PASS`
- Boundary: disclosure-control validation proves only that synthetic output envelopes obey aggregate-only, n<5 suppression, row-level blocking, public-AI blocking and forbidden-output rules; it does not authorize real NHATS extraction, public export, calibration, validation or individual prediction.

## NHATS Survey Design Validation

- Survey-design protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_protocol.json`
- Survey-design protocol SHA-256: `fc36be4f7b5521f938a74063a7ba57f50a791b99008fe35bc1fd08b5a233d0ef`
- Survey-design test cases path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_test_cases.json`
- Survey-design test cases SHA-256: `a0d106ff0e70450ae96a4d8749037839cae27bfb7feb68bf2636681c46f500cc`
- Survey-design validation path: `web/src/data/life-path-nhats-survey-design-validation.json`
- Survey-design validation SHA-256: `24c8fbcfb219e25f8054a76345ef40c63cfb42f18303cceff055e895e4a5385f`
- Survey-design validation status: `PASS`
- Boundary: survey-design validation proves only that synthetic design-plan envelopes enforce weights, strata, PSU/variance-unit, variance-method, route-map and disclosure prerequisites; it does not authorize real NHATS weighted estimates, population inference, calibration, validation or individual prediction.

## NHATS Missingness Route Validation

- Missingness-route protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_protocol.json`
- Missingness-route protocol SHA-256: `e5f68ca68fd44aff81e2146eb2fa75534aab10440129b42f218f5473386e12fd`
- Missingness-route test cases path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_test_cases.json`
- Missingness-route test cases SHA-256: `38928543b47a1f950de5925c2bb329fc544df4516aa882015240e7047674b4be`
- Missingness-route validation path: `web/src/data/life-path-nhats-missingness-route-validation.json`
- Missingness-route validation SHA-256: `b99f9291f8f2933fd565fcfb10e11b3f64f57d2d6feefa453a67ca064c22b12b`
- Missingness-route validation status: `PASS`
- Boundary: missingness-route validation proves only that synthetic route envelopes separate death, self interview, proxy interview, facility route, missingness, conflicts and small-cell suppression; it does not authorize real NHATS route classification, weighted route counts, calibration, validation or individual prediction.

## NHATS Route Field Discovery

- Route-field discovery register path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_field_discovery_register.json`
- Route-field discovery register SHA-256: `32d86995a0438e2104e6850334eefa63b30176b0767dd2229bc73a517ef5ade4`
- Route-field discovery validation path: `web/src/data/life-path-nhats-route-field-discovery-validation.json`
- Route-field discovery validation SHA-256: `7175060ed0e50ad24fdafead0e2e5cc3082e6973aa4ef7cfca376e54d59cec2f`
- Route-field discovery validation status: `PASS`
- Boundary: route-field discovery records official R13/R14 crosswalk candidates, but it does not replace Colectica value-label confirmation, governed file access, classifier review, disclosure review, weighted route counts, calibration, validation or individual prediction.

## Sensitivity Analysis

- Sensitivity path: `web/src/data/life-path-sensitivity-analysis.json`
- Sensitivity SHA-256: `62a5a722d5a521fc3486395f42c8d9b459d3aa9fdd00e4f4a22a3ceb89b25b48`
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
