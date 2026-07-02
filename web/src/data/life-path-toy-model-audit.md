# Life-Path Toy Model Audit

- Overall status: `PASS`
- Model path: `web/src/data/life-path-toy-model.json`
- Model SHA-256: `05c981d4526bcbd23c83ad535e40e6545d0c191a8b3a44ff12c6f018b208c6cc`
- Generated at: `2026-07-02T00:46:22.749565+00:00`

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

## Calibration Readiness

- Readiness path: `domains/c1-boundary-rewriting/longevity-evidence/data/manual/life_path_calibration_readiness.json`
- Readiness SHA-256: `5640fa8b3c5466de351e3ba5763da7477a1b40657d102cdaee7486a174d63166`
- Readiness status: `PASS`
- Boundary: readiness fields are present, but no real cohort, calibration, external validation, or individual use is available.

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
