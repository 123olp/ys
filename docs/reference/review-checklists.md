# Review Checklists

Use these checklists when reviewing changes to this repository.

## Documentation Review

- File is in the correct Diataxis location.
- Filename is semantic and stable.
- The document has one primary job.
- Navigation files are updated.
- Local Markdown links pass `make check`.
- The document does not duplicate a nearby document without adding a clear role.

## Evidence Review

- Claims are separated from evidence and speculation.
- Source traceability is preserved.
- Health, neural, memory, or identity claims state uncertainty.
- Mechanism evidence is not presented as clinical proof.
- AI summaries are not used as primary facts.

## Quantitative Model Review

- Prediction claims define population, intervention, comparator, outcome, horizon, and uncertainty.
- The model identifies whether the claimed effect changes state transition, event hazard, observation, or action policy.
- Causal assumptions are explicit through target-trial framing, causal graph, or equivalent note.
- Biomarker, mechanism, disease endpoint, mortality, safety, and transferability evidence are separated.
- Effective time, subjective time, relative time, and option value are not collapsed into simple lifespan claims.
- The model does not output deterministic death dates or personal treatment recommendations.
- Validation, calibration, sensitivity analysis, and prohibited uses are visible before publication.
- Research-facing model changes identify the model family: survival, multi-state, competing-risk, causal, Bayesian, or decision model.
- Research-facing model changes state the required performance checks: calibration, discrimination, Brier score, RMST difference, sensitivity analysis, or external validation.

## Frontend Chart Review

- Custom prediction charts use D3 for scales, axes, paths, joins, and annotations when standard HTML or simple Canvas drawing would hide model structure.
- Study-material dashboards separate source notes, Human Infra translation, model contract, and visualization output.
- Primary prediction charts stay focused on model output and direct parameter response.
- Primary prediction charts exclude curve-level assumption labels, per-metric evidence badges, deterministic-death-date warning banners, and uncertainty interval bands.
- Governance, evidence, uncertainty, and safety boundaries stay in model documentation or review artifacts when needed.
- Chart interaction must preserve the user's ability to compare baseline and intervention output without visual ambiguity.
- Research charts define the chart task, data type, mark, encoding, scale, unit, and validation method before implementation.
- Standard statistical charts should prefer declarative specs or reproducible chart configuration unless D3 customization is needed for mechanism, state, or threshold visualization.

## Safety Review

- No medical diagnosis or personal treatment instruction is added.
- No invasive neural, memory manipulation, or human experimentation procedure is added.
- No executable black-hole approach, extreme orbital, or human space survival procedure is added.
- No organizational monitoring or coercive control pattern is normalized.
- Consent, exit, dignity, and audit boundaries are preserved for high-risk topics.

## Domain Boundary Review

- The change belongs in the selected domain.
- Cross-domain rules stay under `docs/`.
- Domain-specific material stays under `domains/<domain>/`.
- New domains update `docs/reference/domain-map.md`.
- `AGENTS.md` files reflect architecture changes.
- Speculative physics paths are kept separate from biomedical evidence and neural intervention domains.

## Data Pipeline Review

- Script output stays under `domains/*/data/raw/` or `domains/*/data/processed/`.
- Generated data is not treated as authored knowledge.
- Network scripts have timeouts and bounded retries.
- Source IDs, retrieval time, URL, and raw hash are preserved where practical.
- Data refresh does not silently overwrite curated conclusions.
