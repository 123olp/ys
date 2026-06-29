# 0008 Add Fourth Wave Molecular Maintenance Domains

## Status

Accepted.

## Context

The first three waves covered subject continuity, major body systems, function, recovery, environment, tools, governance, navigation and common population-health determinants. Continued review of aging biology and health-system sources surfaced another class of domains: molecular and organ-maintenance substrates that sit beneath visible disease categories.

These directions are not simply "longevity interventions"; they define upstream state variables that constrain repair, cancer risk, cognition, fatigue, drug safety, tissue renewal and future treatment windows.

## Decision

Add fourth-wave domain skeletons for:

- `genomic-stability-dna-repair/`
- `telomere-maintenance/`
- `proteostasis-autophagy/`
- `mitochondrial-bioenergetics/`
- `cellular-senescence-clearance/`
- `microbiome-ecology/`
- `stem-cell-reserve-renewal/`
- `renal-hepatic-clearance/`

Each domain starts with only `README.md` and `AGENTS.md`. No data, scripts, product folders, experiment instructions or operational protocols are created.

## Alternatives Considered

- Keep all molecular aging mechanisms inside `longevity-evidence/`: rejected because the mechanisms have distinct variables, evidence boundaries and failure modes.
- Put these domains under `cellular-reprogramming/`: rejected because reprogramming is one intervention family, not the owner for all cellular maintenance mechanisms.
- Create wet-lab or data pipelines now: rejected because the current goal is domain architecture and research intake, not operational experimentation.

## Consequences

- The project can now separate lifestyle/population determinants from molecular maintenance substrates.
- High-risk interpretation boundaries are explicit: no protocols, no dosing, no human application claims.
- Future source-card work can map each mechanism to variables, evidence classes, model edges and safety gates.

## Safety And Evidence Boundary

These domains must not provide gene editing steps, cell culture protocols, drug or supplement protocols, dosing, testing interpretation, medical diagnosis, stem-cell procedures, microbiome interventions, dialysis/transplant guidance or personalized treatment advice. They only provide high-level research boundaries, evidence organization and model variables.
