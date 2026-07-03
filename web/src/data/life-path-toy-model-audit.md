# Life-Path Toy Model Audit

- Overall status: `PASS`
- Model path: `web/src/data/life-path-toy-model.json`
- Model SHA-256: `a4c92209d79d20579bf1f575d5ebf07ffe5be9ccaf6bf3f3eef08efa287b5377`
- Generated at: `2026-07-03T09:15:36.983643+00:00`

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
| `readiness-public-aggregate-mortality-anchor` | `PASS` | public mortality anchor must remain aggregate-only and calibration-blocked |
| `readiness-public-linked-mortality-aggregate-pilot` | `PASS` | public linked mortality pilot must remain aggregate-only, source-bound and calibration-blocked |
| `readiness-validation-plan` | `PASS` | validation plan must include internal/external validation fields and not-started status |
| `readiness-calibration-plan` | `PASS` | calibration plan must include diagnostics and not-started status |
| `readiness-sensitivity-plan` | `PASS` | sensitivity analysis plan must define required analyses |
| `readiness-bias-applicability-plan` | `PASS` | bias and applicability plan must define risk domains |
| `readiness-reporting-plan` | `PASS` | reporting plan must define required artifacts beyond Web visualization |
| `readiness-prohibited-uses` | `PASS` | prohibited uses must block individual death-date prediction and medical advice |
| `readiness-upgrade-gate` | `PASS` | upgrade gate must keep the current decision at cannot-calibrate-yet |
| `nhanes-public-lmf-aggregate-pilot-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_aggregate_pilot.json |
| `nhanes-public-lmf-aggregate-pilot-validation-exists` | `PASS` | web/src/data/life-path-nhanes-public-lmf-aggregate-pilot-validation.json |
| `nhanes-public-lmf-aggregate-pilot-schema` | `PASS` | schemaVersion='human-infra.nhanes-public-lmf-aggregate-pilot.v1' |
| `nhanes-public-lmf-source-hashes` | `PASS` | public LMF, DEMO XPT and CDC R read-in program hashes must be recorded |
| `nhanes-public-lmf-boundary` | `PASS` | aggregate pilot must block rows, individual prediction, death dates, calibration, survey inference and causal claims |
| `nhanes-public-lmf-aggregate-cells` | `PASS` | aggregate output must contain 8 unsuppressed sex × age-band cells totaling 5809 adults and 145 deaths |
| `nhanes-public-lmf-validation-source-hash` | `PASS` | validation must point back to the current aggregate pilot path and sha256 |
| `nhanes-public-lmf-validation-boundary` | `PASS` | validation must preserve aggregate-only, non-calibrated and non-individual-use boundaries |
| `nhanes-public-lmf-non-proof-note` | `PASS` | validation must state that it does not prove calibration, survey inference or individual use |
| `nhanes-public-lmf-survey-design-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_survey_design_readiness.json |
| `nhanes-public-lmf-survey-design-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhanes-public-lmf-survey-design-readiness-validation.json |
| `nhanes-public-lmf-survey-design-readiness-schema` | `PASS` | schemaVersion='human-infra.nhanes-public-lmf-survey-design-readiness.v1' |
| `nhanes-public-lmf-survey-design-fields` | `PASS` | readiness must bind WTMEC2YR, SDMVPSU and SDMVSTRA |
| `nhanes-public-lmf-survey-design-boundary` | `PASS` | readiness must block weighted inference, calibration, individual prediction and medical advice |
| `nhanes-public-lmf-survey-design-gate-summary` | `PASS` | gate summary must keep weighted inference blocked despite official design-field readiness |
| `nhanes-public-lmf-survey-design-validation-source-hash` | `PASS` | validation must point back to current readiness path and sha256 |
| `nhanes-public-lmf-survey-design-non-proof-boundary` | `PASS` | validation must state that readiness does not prove weighted inference, calibration or individual prediction |
| `nhanes-public-lmf-domain-rule-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json |
| `nhanes-public-lmf-domain-rule-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.json |
| `nhanes-public-lmf-domain-rule-readiness-schema` | `PASS` | schemaVersion='human-infra.nhanes-public-lmf-domain-subpopulation-rule-readiness.v1' |
| `nhanes-public-lmf-domain-rule-boundary` | `PASS` | domain rule must require full design input and block row-drop subgroup filtering as estimator |
| `nhanes-public-lmf-domain-rule-gate-summary` | `PASS` | gate summary must keep weighted domain inference blocked despite official domain-rule documentation |
| `nhanes-public-lmf-domain-rule-source-findings` | `PASS` | source findings must include CDC/NCHS domain/subpopulation mechanisms and upstream NHANES design fields |
| `nhanes-public-lmf-domain-rule-validation-source-hash` | `PASS` | validation must point back to current domain-rule readiness path and sha256 |
| `nhanes-public-lmf-domain-rule-non-proof-boundary` | `PASS` | validation must state that domain-rule readiness does not prove weighted inference or individual prediction |
| `nhanes-public-lmf-eligible-base-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_eligible_base_readiness.json |
| `nhanes-public-lmf-eligible-base-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhanes-public-lmf-eligible-base-readiness-validation.json |
| `nhanes-public-lmf-eligible-base-readiness-schema` | `PASS` | schemaVersion='human-infra.nhanes-public-lmf-eligible-base-readiness.v1' |
| `nhanes-public-lmf-eligible-base-rule-boundary` | `PASS` | eligible-base rule must require WTMEC2YR > 0, full design input, no row drop and no weighted inference |
| `nhanes-public-lmf-eligible-base-diagnostics` | `PASS` | positive-weight diagnostics must preserve 5809 eligible adults, 145 deaths, 15 strata and no lonely strata |
| `nhanes-public-lmf-eligible-base-gate-summary` | `PASS` | gate summary must keep weighted domain inference blocked despite positive-weight eligible-base diagnostics |
| `nhanes-public-lmf-eligible-base-source-findings` | `PASS` | source findings must include DEMO_J WTMEC2YR distribution, non-zero design input and no row-drop guidance |
| `nhanes-public-lmf-eligible-base-validation-source-hash` | `PASS` | validation must point back to current eligible-base readiness path and sha256 |
| `nhanes-public-lmf-eligible-base-validation-summary` | `PASS` | validation summary must expose positive-weight eligible count while keeping weighted inference blocked |
| `nhanes-public-lmf-eligible-base-non-proof-boundary` | `PASS` | validation must state that eligible-base readiness does not prove weighted inference or individual prediction |
| `nhanes-public-lmf-weighted-estimator-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_estimator_readiness.json |
| `nhanes-public-lmf-weighted-estimator-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhanes-public-lmf-weighted-estimator-readiness-validation.json |
| `nhanes-public-lmf-weighted-estimator-readiness-schema` | `PASS` | schemaVersion='human-infra.nhanes-public-lmf-weighted-estimator-readiness.v1' |
| `nhanes-public-lmf-weighted-estimator-backend-boundary` | `PASS` | backend must select R survey/svydesign while blocking custom estimators and weighted output |
| `nhanes-public-lmf-weighted-estimator-design-object-contract` | `PASS` | design-object contract must bind WTMEC2YR, SDMVPSU, SDMVSTRA, nest=true and post-design domain evaluation |
| `nhanes-public-lmf-weighted-estimator-gate-summary` | `PASS` | gate summary must select backend while keeping runtime smoke, estimator implementation and domain inference blocked |
| `nhanes-public-lmf-weighted-estimator-source-findings` | `PASS` | source findings must include CDC/NCHS R svydesign guidance, CRAN survey backend and DOF warning |
| `nhanes-public-lmf-weighted-estimator-validation-source-hash` | `PASS` | validation must point back to current weighted-estimator readiness path and sha256 |
| `nhanes-public-lmf-weighted-estimator-validation-summary` | `PASS` | validation summary must expose backend selection while keeping estimator execution and domain inference blocked |
| `nhanes-public-lmf-weighted-estimator-non-proof-boundary` | `PASS` | validation must state that backend selection does not prove runtime availability, weighted output or individual prediction |
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
| `nhats-acquisition-readiness-gate-summary` | `PASS` | gate summary must keep only official-source-refresh ready, registration template partial, and 9 gates extraction-blocking |
| `nhats-acquisition-readiness-prohibited-actions` | `PASS` | readiness contract must prohibit premature download, scripts, raw data, public AI upload, individual death-date prediction and calibration claims |
| `nhats-acquisition-readiness-next-work` | `PASS` | next work must point to file-tier, Cross-Year Search variable confirmation and disclosure control |
| `nhats-acquisition-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhats-acquisition-readiness-validation.json |
| `nhats-acquisition-readiness-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-acquisition-readiness-validation.v1' |
| `nhats-acquisition-readiness-validation-source-hash` | `PASS` | validation must point back to the current acquisition-readiness register path and sha256 |
| `nhats-acquisition-readiness-validation-pass` | `PASS` | overallStatus='PASS' summary={'pass': 13, 'fail': 0} |
| `nhats-acquisition-readiness-validation-blocking-gates` | `PASS` | validation must keep official-source-refresh ready while 9 acquisition-readiness gates remain blocking |
| `nhats-acquisition-readiness-validation-boundary` | `PASS` | validation must keep acquisition, extraction, raw repository data, calibration and individual prediction blocked |
| `nhats-acquisition-readiness-validation-non-proof-note` | `PASS` | validation must state that it does not prove registration, storage, downloads, extraction, calibration or prediction |
| `nhats-registration-evidence-template-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_registration_evidence_template.json |
| `nhats-registration-evidence-template-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-registration-evidence-template.v1' |
| `nhats-registration-evidence-template-identity` | `PASS` | template must bind NHATS acquisition readiness while remaining template-only |
| `nhats-registration-evidence-template-boundary` | `PASS` | template may be ready, but registration, download, extraction, raw data, public AI upload, calibration and individual prediction must remain false |
| `nhats-registration-evidence-template-slots` | `PASS` | missing=[] |
| `nhats-registration-evidence-template-gate-impact` | `PASS` | template may only create a partial registration gate and must keep extraction, calibration and individual prediction blocked |
| `nhats-registration-evidence-template-prohibited-actions` | `PASS` | template must prohibit credentials, raw data, public AI upload, calibration and individual prediction |
| `nhats-registration-evidence-template-validation-exists` | `PASS` | web/src/data/life-path-nhats-registration-evidence-template-validation.json |
| `nhats-registration-evidence-template-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-registration-evidence-template-validation.v1' |
| `nhats-registration-evidence-template-validation-source-hash` | `PASS` | validation must point back to the current registration evidence template path and sha256 |
| `nhats-registration-evidence-template-validation-pass` | `PASS` | overallStatus='PASS' summary={'pass': 11, 'fail': 0} |
| `nhats-registration-evidence-template-validation-boundary` | `PASS` | validation must keep registration, download, extraction, raw data, public AI upload, calibration and individual prediction blocked |
| `nhats-registration-evidence-template-validation-non-proof-note` | `PASS` | validation must state that it does not prove NHATS registration, data access, workspace execution or model readiness |
| `nhats-controlled-storage-validation-exists` | `PASS` | web/src/data/life-path-nhats-controlled-storage-destruction-validation.json |
| `nhats-controlled-storage-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-controlled-storage-destruction-plan-validation.v1' |
| `nhats-controlled-storage-validation-source-hash` | `PASS` | validation must point back to current storage/destruction plan and acquisition-readiness hashes |
| `nhats-controlled-storage-validation-pass` | `PASS` | overallStatus='PASS' summary={'pass': 15, 'fail': 0} |
| `nhats-controlled-storage-validation-impact` | `PASS` | validation may only move storage/destruction to partial while keeping download, extraction and calibration blocked |
| `nhats-controlled-storage-validation-boundary` | `PASS` | validation must keep execution, download, extraction, raw repository data, public AI, calibration and individual prediction blocked |
| `nhats-controlled-storage-validation-non-proof-note` | `PASS` | validation must state that it does not prove registration, workspace provisioning, download, extraction, calibration or prediction |
| `nhats-synthetic-storage-drill-validation-exists` | `PASS` | web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json |
| `nhats-synthetic-storage-drill-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-synthetic-storage-destruction-drill-validation.v1' |
| `nhats-synthetic-storage-drill-validation-source-hash` | `PASS` | validation must point back to current drill, storage/destruction plan and acquisition-readiness hashes |
| `nhats-synthetic-storage-drill-validation-pass` | `PASS` | overallStatus='PASS' summary={'pass': 13, 'fail': 0} |
| `nhats-synthetic-storage-drill-validation-impact` | `PASS` | synthetic drill may only complete the dry-run while storage/destruction remains partial and data/model actions stay blocked |
| `nhats-synthetic-storage-drill-validation-boundary` | `PASS` | validation must keep official files, raw data, row-level data, public AI, calibration and individual prediction blocked |
| `nhats-synthetic-storage-drill-validation-non-proof-note` | `PASS` | validation must state that it proves only synthetic drill consistency, not registration, download, extraction, calibration or prediction |
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
| `nhats-file-tier-table-validation-exists` | `PASS` | web/src/data/life-path-nhats-file-tier-table-validation.json |
| `nhats-file-tier-table-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-file-tier-table-validation.v1' |
| `nhats-file-tier-table-validation-source-hash` | `PASS` | validation must point back to current file-tier table and acquisition-readiness paths and sha256 hashes |
| `nhats-file-tier-table-validation-pass` | `PASS` | overallStatus='PASS' summary={'pass': 17, 'warn': 0, 'fail': 0} |
| `nhats-file-tier-table-validation-row-summary` | `PASS` | validation must summarize 16 file rows while keeping all download/extraction/storage/public-AI counts at 0 |
| `nhats-file-tier-table-validation-boundary` | `PASS` | validation must keep file-tier readiness, download, extraction, raw repository data, public AI upload, calibration and individual prediction blocked |
| `nhats-file-tier-table-validation-non-proof-note` | `PASS` | validation must state that it does not prove registration, data access approval, governed storage, Colectica confirmation or model readiness |
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
| `nhats-colectica-value-label-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_protocol.json |
| `nhats-colectica-value-label-validation-exists` | `PASS` | web/src/data/life-path-nhats-colectica-value-label-validation.json |
| `nhats-colectica-value-label-protocol-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-value-label-review-protocol.v1' |
| `nhats-colectica-value-label-protocol-identity` | `PASS` | protocol must bind NHATS, route-field discovery, missingness route, variable matrix and value-labels-not-reviewed status |
| `nhats-colectica-value-label-decision-boundary` | `PASS` | only protocol readiness may be true; Colectica login, labels, question text, route crosswalk, classifier, endpoint, weighted counts, export, calibration and individual prediction must remain false |
| `nhats-colectica-value-label-source-evidence` | `PASS` | missing_evidence_ids=[] |
| `nhats-colectica-value-label-review-artifacts` | `PASS` | missing_artifact_ids=[] |
| `nhats-colectica-value-label-review-units` | `PASS` | missing_unit_ids=[] |
| `nhats-colectica-value-label-sensitive-death-exclusion` | `PASS` | sensitive_excluded=['dm13mthdied', 'dm13yrdied', 'dm14mthdied', 'dm14yrdied'] |
| `nhats-colectica-value-label-blocking-gates` | `PASS` | missing_gate_ids=[] |
| `nhats-colectica-value-label-prohibited-actions` | `PASS` | protocol must block unreviewed value-label tables, crosswalk-as-values, route classifier, weighted counts and public AI upload |
| `nhats-colectica-value-label-no-confirmed-map` | `PASS` | prohibited_keys=[] |
| `nhats-colectica-value-label-source-trace` | `PASS` | sourceTrace must include official Colectica, conditions, User Guide and R13/R14 crosswalk URLs |
| `nhats-colectica-value-label-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-value-label-validation.v1' |
| `nhats-colectica-value-label-validation-source-hash` | `PASS` | Colectica value-label validation must point back to current protocol hash |
| `nhats-colectica-value-label-validation-summary` | `PASS` | Colectica value-label validation must pass with zero failed checks |
| `nhats-colectica-value-label-validation-boundary` | `PASS` | validation boundary must keep value labels, route-value crosswalk and individual prediction blocked |
| `nhats-colectica-value-label-execution-register-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_execution_register.json |
| `nhats-colectica-value-label-execution-validation-exists` | `PASS` | web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json |
| `nhats-colectica-value-label-execution-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-value-label-review-execution-register.v1' |
| `nhats-colectica-value-label-execution-identity` | `PASS` | execution register must bind NHATS, current protocol, current route-field register and login-required partial execution status |
| `nhats-colectica-value-label-execution-boundary` | `PASS` | field trace and standard negative-code family may be prepared, but login, labels, crosswalk, signoff, classifier, weighted counts, export, calibration and individual prediction must remain blocked |
| `nhats-colectica-value-label-execution-no-confirmed-map` | `PASS` | prohibited_keys=[] |
| `nhats-colectica-value-label-execution-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-value-label-review-execution-validation.v1' |
| `nhats-colectica-value-label-execution-validation-source-hash` | `PASS` | execution validation must point back to current register, protocol and route-field register hashes |
| `nhats-colectica-value-label-execution-validation-summary` | `PASS` | Colectica execution validation must pass with zero failed checks |
| `nhats-colectica-value-label-execution-validation-boundary` | `PASS` | execution validation boundary must preserve field-trace-only status and block labels, route maps, classifier, export, calibration and individual prediction |
| `nhats-colectica-access-route-probe-register-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_access_route_probe_register.json |
| `nhats-colectica-access-route-probe-validation-exists` | `PASS` | web/src/data/life-path-nhats-colectica-access-route-probe-validation.json |
| `nhats-colectica-access-route-probe-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-access-route-probe-register.v1' |
| `nhats-colectica-access-route-probe-boundary` | `PASS` | access route may be probed, but account, login, variable pages, labels, export, calibration and individual prediction must remain blocked |
| `nhats-colectica-access-route-probe-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-access-route-probe-validation.v1' |
| `nhats-colectica-access-route-probe-validation-source-hash` | `PASS` | access-route validation must point back to current probe register and execution register hashes |
| `nhats-colectica-access-route-probe-validation-boundary` | `PASS` | validation must prove only public access-route probing while keeping authenticated capture and model admission blocked |
| `nhats-colectica-authenticated-capture-template-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_authenticated_capture_template.json |
| `nhats-colectica-authenticated-capture-template-validation-exists` | `PASS` | web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json |
| `nhats-colectica-authenticated-capture-template-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-authenticated-capture-template.v1' |
| `nhats-colectica-authenticated-capture-template-boundary` | `PASS` | template may be ready, but account status, login, captures, labels, classifier, export, calibration and individual prediction must remain blocked |
| `nhats-colectica-authenticated-capture-template-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-authenticated-capture-template-validation.v1' |
| `nhats-colectica-authenticated-capture-template-validation-source-hash` | `PASS` | capture-template validation must point back to current template, access-route probe, execution register, protocol and route-field register hashes |
| `nhats-colectica-authenticated-capture-template-validation-boundary` | `PASS` | validation must prove only template readiness while keeping authenticated capture and model admission blocked |
| `nhats-colectica-capture-task-register-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_capture_task_register.json |
| `nhats-colectica-capture-task-register-validation-exists` | `PASS` | web/src/data/life-path-nhats-colectica-capture-task-register-validation.json |
| `nhats-colectica-capture-task-register-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-capture-task-register.v1' |
| `nhats-colectica-capture-task-register-identity` | `PASS` | capture task register must remain task-register-only and not claim authenticated capture completion |
| `nhats-colectica-capture-task-register-boundary` | `PASS` | task register may be ready, but capture, labels, classifier, extraction, aggregation, export, calibration and individual prediction must remain blocked |
| `nhats-colectica-capture-task-register-task-shape` | `PASS` | group_count=9; task_count=39 |
| `nhats-colectica-capture-task-register-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-colectica-capture-task-register-validation.v1' |
| `nhats-colectica-capture-task-register-validation-source-hash` | `PASS` | capture-task validation must point back to current register, route-field, capture-template and route-classifier readiness hashes |
| `nhats-colectica-capture-task-register-validation-boundary` | `PASS` | validation must prove task readiness while keeping authenticated capture and model admission blocked |
| `nhats-route-classifier-readiness-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_classifier_readiness.json |
| `nhats-route-classifier-readiness-validation-exists` | `PASS` | web/src/data/life-path-nhats-route-classifier-readiness-validation.json |
| `nhats-route-classifier-readiness-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-route-classifier-readiness.v1' |
| `nhats-route-classifier-readiness-identity` | `PASS` | readiness gate must be the blocked NHATS R13/R14 route-classifier readiness contract |
| `nhats-route-classifier-readiness-boundary` | `PASS` | route-field candidates may be known, but labels, crosswalk, classifier code, real extraction, aggregation, export, calibration and individual prediction must remain blocked |
| `nhats-route-classifier-readiness-gates` | `PASS` | readiness contract must hold 9 input families and 12 route-classifier blocking gates |
| `nhats-route-classifier-readiness-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-route-classifier-readiness-validation.v1' |
| `nhats-route-classifier-readiness-validation-source-hash` | `PASS` | readiness validation must point back to current readiness and upstream source hashes |
| `nhats-route-classifier-readiness-validation-summary` | `PASS` | readiness validation must pass with zero failures and preserve input-family/gate counts |
| `nhats-route-classifier-readiness-validation-boundary` | `PASS` | validation boundary must keep classifier, extraction, aggregation, weighted counts, export, calibration and individual prediction blocked |
| `nhats-l2-variable-family-admission-register-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_l2_variable_family_admission_register.json |
| `nhats-l2-variable-family-admission-validation-exists` | `PASS` | web/src/data/life-path-nhats-l2-variable-family-admission-validation.json |
| `nhats-l2-variable-family-admission-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-l2-variable-family-admission.v1' |
| `nhats-l2-variable-family-admission-boundary` | `PASS` | L2 candidate family mapping may be ready, but exact variables, data access, extraction, L4, calibration and individual prediction must remain blocked |
| `nhats-l2-variable-family-admission-summary` | `PASS` | summary must preserve six L2 families and zero L4/L5 admissions |
| `nhats-l2-variable-family-admission-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-l2-variable-family-admission-validation.v1' |
| `nhats-l2-variable-family-admission-validation-source-hash` | `PASS` | L2 family validation must point back to current estimand, variable matrix, model-admission contract, candidate registry and capture template hashes |
| `nhats-l2-variable-family-admission-validation-boundary` | `PASS` | validation must prove only L2 family mapping while keeping L4, calibration and individual prediction blocked |
| `nhats-preoutcome-aggregation-protocol-exists` | `PASS` | domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_preoutcome_aggregation_protocol.json |
| `nhats-preoutcome-aggregation-validation-exists` | `PASS` | web/src/data/life-path-nhats-preoutcome-aggregation-validation.json |
| `nhats-preoutcome-aggregation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-preoutcome-aggregation-protocol.v1' |
| `nhats-preoutcome-aggregation-boundary` | `PASS` | pre-outcome rules may be frozen, but real aggregation, weighted estimates, public export, L4, calibration and individual prediction must remain blocked |
| `nhats-preoutcome-aggregation-summary` | `PASS` | summary must freeze eight rules and keep real, weighted, L4, calibration and individual uses blocked |
| `nhats-preoutcome-aggregation-validation-schema` | `PASS` | schemaVersion='human-infra.life-path-nhats-preoutcome-aggregation-validation.v1' |
| `nhats-preoutcome-aggregation-validation-source-hash` | `PASS` | pre-outcome aggregation validation must point back to current upstream protocol hashes |
| `nhats-preoutcome-aggregation-validation-boundary` | `PASS` | validation must prove only pre-outcome L2 rule freezing while keeping real aggregation, L4, calibration and individual prediction blocked |
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
- Readiness SHA-256: `03a6edabcadaefda990f3989e19604e7391d42613f1a09e7c9e74139c4c8d8d6`
- Readiness status: `PASS`
- Boundary: readiness fields are present, but no real cohort, calibration, external validation, or individual use is available.

## NHANES Public LMF Aggregate Pilot

- Aggregate path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_aggregate_pilot.json`
- Aggregate SHA-256: `d817c2907d71a820baac846f5a41c28db6eeee5cb8e57ed20a47d87aa9efce0f`
- Validation path: `web/src/data/life-path-nhanes-public-lmf-aggregate-pilot-validation.json`
- Validation SHA-256: `0c669963b8462de7e98fa50131b9253eb88b959a767c87e612159884f260bf7f`
- Aggregate pilot status: `PASS`
- Boundary: this proves only a public real-data aggregate join and endpoint smoke test; it does not prove calibrated prediction, survey-weighted inference, causal effects, medical advice or individual usefulness.

## NHANES Public LMF Survey-Design Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_survey_design_readiness.json`
- Readiness SHA-256: `0c914cdecd72587bf62ea0b59c4445ac5bfa72c587cc845264f79c5363935170`
- Validation path: `web/src/data/life-path-nhanes-public-lmf-survey-design-readiness-validation.json`
- Validation SHA-256: `9229cc9bead05fe42dbd0d52f65a082d29fa92f07b5a5f697fc2257afeaba0a6`
- Readiness status: `PASS`
- Boundary: official WTMEC2YR, SDMVPSU and SDMVSTRA readiness is documented, but weighted population inference, design-based intervals, calibration and individual prediction remain blocked.

## NHANES Public LMF Domain/Subpopulation Rule Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_domain_subpopulation_rule_readiness.json`
- Readiness SHA-256: `4a7cb6d07dd55b12253c06640e124cc9948c8403b2107b6148e85b504a43e8d5`
- Validation path: `web/src/data/life-path-nhanes-public-lmf-domain-subpopulation-rule-readiness-validation.json`
- Validation SHA-256: `f99b524e97801466ed784d96346f50c85c284fdea5111e430213870d37bba26a`
- Readiness status: `PASS`
- Boundary: official domain/subpopulation analysis mechanisms are documented, but row-drop subgroup filtering is not an estimator and weighted domain inference remains blocked until a reviewed estimator, eligible-base rule, DOF review and disclosure gate exist.

## NHANES Public LMF Eligible-Base Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_eligible_base_readiness.json`
- Readiness SHA-256: `2abd4af214d1bbe6eb8c4c5109b33864fd9025e55ada972b8bcb51d13d97674b`
- Validation path: `web/src/data/life-path-nhanes-public-lmf-eligible-base-readiness-validation.json`
- Validation SHA-256: `ba048657cc05401ae68d4767d267fdb8914862f66f5b3df3594a653976d95bb5`
- Readiness status: `PASS`
- Boundary: positive WTMEC2YR eligible-base diagnostics are recorded without persisting rows, but weighted domain inference, design-based intervals, calibration and individual prediction remain blocked.

## NHANES Public LMF Weighted-Estimator Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhanes_public_lmf_weighted_estimator_readiness.json`
- Readiness SHA-256: `469d6cdcdc846bfed97a449f9a8a3bd2e197bfe214b996cb121c800979f5ef4a`
- Validation path: `web/src/data/life-path-nhanes-public-lmf-weighted-estimator-readiness-validation.json`
- Validation SHA-256: `42f6a4449352e0250e5d87b1e95b1e68c5492744f5f5b3d341e1c8e19d09e880`
- Readiness status: `PASS`
- Boundary: R survey/svydesign is selected as the mature complex-survey backend and the design-object contract is bound, but runtime smoke, domain indicator tests, DOF/sparse-domain review, public disclosure review, weighted outputs, calibration and individual prediction remain blocked.

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
- Manifest SHA-256: `330287572ddfedad7a62f9cf4dfc3d81eb13d49fdd9f7895bcadaedcb817ae88`
- Manifest status: `PASS`
- Boundary: the manifest is a pre-extraction gate; it blocks scripts, downloads, field inference, calibration, validation, raw-data exposure and unsafe individual outputs until official file-level requirements are complete.

## NHATS Acquisition Readiness

- Acquisition readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_acquisition_readiness.json`
- Acquisition readiness SHA-256: `15d8f2ce1144fe40d3a7132bb38d49fa496368f2a339dc0f769a87624225dd94`
- Acquisition readiness status: `PASS`
- Boundary: the structured readiness contract keeps NHATS at cannot-extract-yet until registration, file-tier, Colectica variables, endpoint, survey design, disclosure control, AI boundary and storage/destruction gates are ready.

## NHATS Registration Evidence Template

- Registration evidence template path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_registration_evidence_template.json`
- Registration evidence template SHA-256: `403925b01f1fef53518448c27d14504d69532dc06f53ede474fb64f0033fff16`
- Registration evidence template status: `PASS`
- Boundary: the template defines redacted evidence slots for registration and access governance; it does not prove registration, authorize download, authorize extraction, or open calibration.

## NHATS Controlled Storage / Destruction

- Storage/destruction validation path: `web/src/data/life-path-nhats-controlled-storage-destruction-validation.json`
- Storage/destruction validation SHA-256: `dea15482deb7810fef89d4db5f50393bb3da1fd788437ae397e287108a7eade3`
- Storage/destruction validation status: `PASS`
- Boundary: the controlled storage/destruction plan is machine-validated but real governed workspace execution, download, extraction, calibration and individual prediction remain blocked.

## NHATS Synthetic Storage / Destruction Drill

- Synthetic drill validation path: `web/src/data/life-path-nhats-synthetic-storage-destruction-drill-validation.json`
- Synthetic drill validation SHA-256: `1a9ea93bba8e622aa002b8fbbc72482957d2c02bf4170ac7cb4acf9130462ff4`
- Synthetic drill validation status: `PASS`
- Boundary: the synthetic create-hash-delete drill proves only dry-run mechanics; it does not prove NHATS registration, governed workspace provisioning, data access, extraction, calibration or individual prediction.

## NHATS File Tier Table

- File-tier table path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_file_tier_table.json`
- File-tier table SHA-256: `18c151512ffb6e075a134765e13d5b4b07252be10b9e55a211f7d890cefdc6f1`
- File-tier table status: `PASS`
- File-tier validation path: `web/src/data/life-path-nhats-file-tier-table-validation.json`
- File-tier validation SHA-256: `5df2dfa3dcd0e72c437cbc9a066829078243782fc5ec56ce96aff712c4f4bed7`
- File-tier validation status: `PASS`
- Boundary: the file-tier table maps official R13/R14 public and sensitive file families, and the validator binds it to current upstream access records while still blocking download, extraction, repository storage, public AI upload, calibration and individual prediction.

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
- Disclosure validation SHA-256: `39e784e9e2cb59ab526c4944a100967e1bad3aeb258ed9aee81a8601840b5cac`
- Disclosure validation status: `PASS`
- Boundary: disclosure-control validation proves only that synthetic output envelopes obey aggregate-only, n<5 suppression, row-level blocking, public-AI blocking and forbidden-output rules; it does not authorize real NHATS extraction, public export, calibration, validation or individual prediction.

## NHATS Survey Design Validation

- Survey-design protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_protocol.json`
- Survey-design protocol SHA-256: `fc36be4f7b5521f938a74063a7ba57f50a791b99008fe35bc1fd08b5a233d0ef`
- Survey-design test cases path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_survey_design_test_cases.json`
- Survey-design test cases SHA-256: `a0d106ff0e70450ae96a4d8749037839cae27bfb7feb68bf2636681c46f500cc`
- Survey-design validation path: `web/src/data/life-path-nhats-survey-design-validation.json`
- Survey-design validation SHA-256: `f397dd1e4e167e022867345123611ddd26755a8cd8a2b41c5f6302d58c948a17`
- Survey-design validation status: `PASS`
- Boundary: survey-design validation proves only that synthetic design-plan envelopes enforce weights, strata, PSU/variance-unit, variance-method, route-map and disclosure prerequisites; it does not authorize real NHATS weighted estimates, population inference, calibration, validation or individual prediction.

## NHATS Missingness Route Validation

- Missingness-route protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_protocol.json`
- Missingness-route protocol SHA-256: `e5f68ca68fd44aff81e2146eb2fa75534aab10440129b42f218f5473386e12fd`
- Missingness-route test cases path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_missingness_route_test_cases.json`
- Missingness-route test cases SHA-256: `38928543b47a1f950de5925c2bb329fc544df4516aa882015240e7047674b4be`
- Missingness-route validation path: `web/src/data/life-path-nhats-missingness-route-validation.json`
- Missingness-route validation SHA-256: `d29236c9b286365614d4296ad0a100fdedee8d35550452a268fa63bf7231b65b`
- Missingness-route validation status: `PASS`
- Boundary: missingness-route validation proves only that synthetic route envelopes separate death, self interview, proxy interview, facility route, missingness, conflicts and small-cell suppression; it does not authorize real NHATS route classification, weighted route counts, calibration, validation or individual prediction.

## NHATS Route Field Discovery

- Route-field discovery register path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_field_discovery_register.json`
- Route-field discovery register SHA-256: `32d86995a0438e2104e6850334eefa63b30176b0767dd2229bc73a517ef5ade4`
- Route-field discovery validation path: `web/src/data/life-path-nhats-route-field-discovery-validation.json`
- Route-field discovery validation SHA-256: `a0119e75eaa639674723e0907a6d9af80e27fd42df6f3a95daeb842e063742e2`
- Route-field discovery validation status: `PASS`
- Boundary: route-field discovery records official R13/R14 crosswalk candidates, but it does not replace Colectica value-label confirmation, governed file access, classifier review, disclosure review, weighted route counts, calibration, validation or individual prediction.

## NHATS Colectica Value-Label Review

- Colectica value-label protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_protocol.json`
- Colectica value-label protocol SHA-256: `bd5130152b3c57d5a6d8cdc767df85bc8a10e19e1225738f13940bd3734ff416`
- Colectica value-label validation path: `web/src/data/life-path-nhats-colectica-value-label-validation.json`
- Colectica value-label validation SHA-256: `1bdd202417ebd4d12b56bf593327aa337578d0eabf20a33a656f0f077291f236`
- Colectica value-label validation status: `PASS`
- Boundary: Colectica value-label review protocol defines the next evidence gate, but it does not contain confirmed value-label maps, question text, skip logic, route-value crosswalks, classifier promotion, weighted route counts, public export, calibration, validation or individual prediction.

## NHATS Colectica Value-Label Review Execution

- Colectica execution register path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_value_label_review_execution_register.json`
- Colectica execution register SHA-256: `de6d17f9470a563346f92884cead1eec35cf5a954245751b0135efc60672b042`
- Colectica execution validation path: `web/src/data/life-path-nhats-colectica-value-label-review-execution-validation.json`
- Colectica execution validation SHA-256: `afa11c451935ac3ee3559d553245cc6c0094a09f5bce0b067a1b115de147a328`
- Colectica execution validation status: `PASS`
- Boundary: Colectica execution now records official source trace, field-level source-trace skeleton and standard negative-code family only; it still blocks login-derived value labels, question text, universe/skip logic, route-value maps, classifier promotion, weighted route counts, public export, calibration, validation and individual prediction.

## NHATS Colectica Access-Route Probe

- Colectica access-route probe register path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_access_route_probe_register.json`
- Colectica access-route probe register SHA-256: `58941fde2c6a1c5488437a1ad447cb3dae2032739ef1ed579e29da98b96aaa89`
- Colectica access-route probe validation path: `web/src/data/life-path-nhats-colectica-access-route-probe-validation.json`
- Colectica access-route probe validation SHA-256: `47d693d56ad3bab3e038d3f0dfebbb00801938ae94f7d37e4c7a6d00fa13f46d`
- Colectica access-route probe validation status: `PASS`
- Boundary: access-route probing verifies the public entry point, anonymous login boundary and technical-guide workflow only; it still blocks account status, authenticated variable page capture, value labels, question text, exports, calibration and individual prediction.

## NHATS Colectica Authenticated Capture Template

- Colectica authenticated capture template path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_colectica_authenticated_capture_template.json`
- Colectica authenticated capture template SHA-256: `dc097acfcb44007b42a25ce500c6cb1d23b1154f6620a7797445293817313eeb`
- Colectica authenticated capture template validation path: `web/src/data/life-path-nhats-colectica-authenticated-capture-template-validation.json`
- Colectica authenticated capture template validation SHA-256: `a0dee1b0f2beb1be003e9d8624ec4454536d6ae670c4cda4e5c708fc16b5a528`
- Colectica authenticated capture template validation status: `PASS`
- Boundary: authenticated capture template validation proves only that the next capture evidence slots are complete; it still blocks account status, login, authenticated variable pages, value labels, question text, universe/skip logic, route classifiers, public export, calibration and individual prediction.

## NHATS Route Classifier Readiness

- Route-classifier readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_route_classifier_readiness.json`
- Route-classifier readiness SHA-256: `f0c0224317c9ee20e8de56dcddeadba85ae24d67b736782ba22de90e83109296`
- Route-classifier readiness validation path: `web/src/data/life-path-nhats-route-classifier-readiness-validation.json`
- Route-classifier readiness validation SHA-256: `b31d32313afe68d12d7336c8a2b5d477f3440813a9a70f853d1554248bb87187`
- Route-classifier readiness validation status: `PASS`
- Boundary: route-classifier readiness validation proves only that a blocked gate exists between route-field candidates and any real classifier; it still blocks Colectica value labels, route-value crosswalks, variable-specific missing maps, real extraction, aggregation, weighted counts, public export, calibration and individual prediction.

## NHATS L2 Variable Family Admission

- L2 variable-family admission register path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_l2_variable_family_admission_register.json`
- L2 variable-family admission register SHA-256: `da1d444f452482f37aa7d7d12cd97c9deb0b2d6006540f76c5d2588389dffce3`
- L2 variable-family admission validation path: `web/src/data/life-path-nhats-l2-variable-family-admission-validation.json`
- L2 variable-family admission validation SHA-256: `b4130cf7df0fc5c7152ce3800f63479de2377ca8d168cbd6f8fae669a3be2c56`
- L2 variable-family admission validation status: `PASS`
- Boundary: L2 variable-family admission validation proves only that the narrow estimand is mapped to six candidate families; it still blocks exact variables, governed data access, extraction, L4 admission, calibration and individual prediction.

## NHATS Pre-Outcome Aggregation

- Pre-outcome aggregation protocol path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`
- Pre-outcome aggregation protocol SHA-256: `a2917d4bbb1682f5de6251fe919afae5da5bad681168475845a3a9c0a9a0747d`
- Pre-outcome aggregation validation path: `web/src/data/life-path-nhats-preoutcome-aggregation-validation.json`
- Pre-outcome aggregation validation SHA-256: `4db638f424568b7ac6b779d969fbdbe35c21e702db59c9d43ad37def20f23489`
- Pre-outcome aggregation validation status: `PASS`
- Boundary: pre-outcome aggregation validation proves only that L2 aggregation rules are frozen before outcome inspection; it still blocks real aggregation, weighted estimates, public export, L4 admission, calibration and individual prediction.

## Sensitivity Analysis

- Sensitivity path: `web/src/data/life-path-sensitivity-analysis.json`
- Sensitivity SHA-256: `ffefdb40db2268009d147260570ae2fb9b5a4d019715cb7a7938474d6cedbe20`
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
