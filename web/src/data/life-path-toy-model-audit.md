# Life-Path Toy Model Audit

- Overall status: `PASS`
- Model path: `web/src/data/life-path-toy-model.json`
- Model SHA-256: `d8e159031625099446ab769439d6e0296516cdc8e33e983373fdf05a2a110253`
- Generated at: `2026-07-02T00:37:24.662528+00:00`

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

## Standard Alignment

| Standard | Local gate | Status | Boundary |
| --- | --- | --- | --- |
| TRIPOD+AI | model card + schema + transparent scenario output | `PARTIAL` | toy model only; no development/validation cohort |
| PROBAST / PROBAST+AI | bias/applicability placeholders and prohibited-use boundary | `PARTIAL` | formal risk-of-bias assessment requires real study design and data |
| ISPOR modeling good practices | versioned inputs, executable model, generated outputs, audit artifact | `PARTIAL` | no decision model, calibration, cost model, or sensitivity analysis yet |
| MRC complex interventions framework | mechanism chain and context boundary in maturity roadmap | `PARTIAL` | stakeholder process and implementation evaluation are not started |

## Boundary

This audit proves only that the synthetic toy model output satisfies the local reporting and sanity contract. It does not prove clinical validity, predictive validity, causal validity, or individual usefulness.
