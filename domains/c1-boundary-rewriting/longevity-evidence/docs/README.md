# Longevity Evidence Docs

This directory stores the Longevity Evidence domain model, data source plans, collection history, and MVP roadmap.

## Documents

- `product-brief.md`: product positioning, users, value, and non-goals.
- `evidence-model.md`: interventions, claims, evidence, trials, and scoring model.
- `data-sources.md`: source priority and public data access rules.
- `data-inventory.md`: maintained data domains, fields, refresh cadence, and quality gates.
- `lev-enabling-resources.md`: indirect LEV resource layer covering time, attention, cognition, skill, memory, AI, money, social support, environment, and higher-order effects.
- `lev-higher-order-effects-discovery.md`: second-order and multi-order effect discovery notes, probability gates, positive/negative chains, and source signals.
- `lev-route-card-template.md`: reusable route-card contract for new LEV routes.
- `lev-source-cards.md`: first source-card batch for LEV higher-order effect modeling.
- `lev-mainstream-routes.md`: mainstream longevity escape velocity route map, source signals, and cross-domain routing.
- `life-path-data-source-cards.md`: candidate source cards for HRS, NCHS linked mortality, UK Biobank, All of Us, NHATS, ELSA, SHARE, and Framingham before real model calibration.
- `life-path-data-card-template.md`: required governance and study-design template before any candidate source can be used for calibration, validation, benchmarking, or display.
- `life-path-data-card-nhats.md`: first NHATS Data Card draft for late-life functional-survival and effective-time modeling admission review.
- `life-path-variable-dictionary-nhats.md`: first NHATS variable-family dictionary draft mapping function, cognition, support, environment, design and endpoint fields to Human Infra model roles.
- `life-path-extraction-manifest-nhats-draft.md`: pre-extraction NHATS manifest draft that blocks scripts and downloads until file names, variables, weights, missing codes, access tiers, endpoints and output rules are governed.
- `../data/manual/life_path_nhats_official_source_refresh_register.json`: machine-readable NHATS official-source refresh register that records current public official page/PDF reachability and hashes without authorizing download, extraction, calibration, or individual prediction.
- `../data/manual/life_path_nhats_registration_evidence_template.json`: machine-readable NHATS registration/access evidence template that fixes required redacted account, permitted-user, conditions-of-use, file-tier, controlled-workspace and second-reviewer slots before any real registration proof can be accepted.
- `../data/manual/life_path_nhats_acquisition_readiness.json`: machine-readable NHATS acquisition-readiness contract that keeps official-source refresh, registration, file-tier, Colectica, survey-design, endpoint, disclosure-control, AI-boundary and storage gates auditable before any extraction work.
- `../data/manual/life_path_nhats_file_tier_table.json`: machine-readable NHATS R13/R14 file-tier table for public annual files, clock images, sensitive SP/OP files, seasonality weights, method-document dependencies and blocked extraction boundaries.
- `../../../../web/src/data/life-path-nhats-file-tier-table-validation.json`: generated NHATS file-tier validation report that hash-binds the table and upstream access records while keeping download, extraction, repository storage, public AI upload, calibration and individual prediction blocked.
- `../data/manual/life_path_nhats_first_estimand_protocol.json`: machine-readable first NHATS estimand protocol that pre-registers the R13/R14 aggregate functional-survival question, target population, time zero, outcome, predictor families, censoring, survey design and aggregate-only output boundary.
- `../data/manual/life_path_nhats_variable_confirmation_matrix.json`: machine-readable NHATS variable-confirmation matrix that records official source facts, candidate field patterns, variable groups, cohort-flow template, readiness gates and blocked extraction boundaries.
- `../data/manual/life_path_nhats_cohort_flow_endpoint_protocol.json`: machine-readable NHATS cohort-flow and endpoint-routing protocol that records R13/R14 route rows, endpoint route classes, aggregate-only output contracts, disclosure control and blocked readiness gates before extraction.
- `../data/manual/life_path_nhats_disclosure_control_policy.json`: machine-readable NHATS disclosure-control policy for aggregate-only export, n < 5 suppression, row-level blocking, public-AI blocking, allowed output types and forbidden output types.
- `../data/manual/life_path_nhats_disclosure_control_test_cases.json`: synthetic-only NHATS disclosure-control test cases for proving allow/block behavior without any real NHATS data.
- `../data/manual/life_path_nhats_preoutcome_aggregation_protocol.json`: machine-readable NHATS pre-outcome aggregation protocol that freezes L2-only aggregation rules, synthetic allow/block cases, required evidence gates and L4/calibration/individual-use blockers before real aggregation.
- `../data/manual/life_path_nhats_colectica_capture_task_register.json`: machine-readable NHATS Colectica capture task register that expands the authenticated capture template into 9 route-field groups and 39 pending variable/output tasks while keeping login, real capture, classifier, extraction, calibration, and individual prediction blocked.
- `../data/manual/life_path_nhats_route_classifier_readiness.json`: machine-readable NHATS route-classifier readiness contract that keeps route-field candidates separated from real classifier code, extraction, aggregation, weighted counts, calibration, and individual prediction until Colectica, survey-design, disclosure, and second-review gates pass.
- `../../../../web/src/data/life-path-nhats-colectica-capture-task-register-validation.json`: generated NHATS Colectica capture-task validation report that hash-binds the task register to route-field discovery, authenticated capture template, and route-classifier readiness while keeping real classifier and extraction actions blocked.
- `../../../../web/src/data/life-path-nhats-route-classifier-readiness-validation.json`: generated NHATS route-classifier readiness validation report that hash-binds the readiness contract to route-field, Colectica, missingness-route, and pre-outcome aggregation upstreams while keeping real classifier and extraction actions blocked.
- `mvp-roadmap.md`: first 0-6 week product path.
- `collection-run-2026-05-29.md`: first MVP collection run.
- `collection-run-2026-05-29-expanded.md`: expanded core data collection run.

## Boundary

These documents belong only to the Longevity Evidence domain. Cross-domain principles belong in `../../../../docs/`.
