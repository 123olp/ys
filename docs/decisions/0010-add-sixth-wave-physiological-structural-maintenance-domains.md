# 0010 Add Sixth Wave Physiological Structural Maintenance Domains

## Status

Accepted.

## Context

The prior domain waves covered longevity evidence, molecular maintenance, major disease risks, neuro-continuity, tools, governance, resources, external technology risks and future-waiting paths. Continued first-principles tracing exposed another missing layer: basic physiological transport, signaling, barrier, material and clearance systems that sit between molecular mechanisms and visible disease categories.

These systems are not ordinary disease pages. They define cross-organ constraints on oxygen delivery, hormonal coordination, blood transport, external boundary integrity, tissue material aging and waste/fluid clearance.

## Decision

Add sixth-wave domain skeletons for:

- `respiratory-oxygenation/`
- `endocrine-hormonal-regulation/`
- `blood-oxygen-hemostasis/`
- `skin-barrier-wound-healing/`
- `extracellular-matrix-glycation/`
- `lymphatic-glymphatic-clearance/`

Each domain starts with only `README.md` and `AGENTS.md`. No data pipelines, diagnostic tools, treatment protocols, device instructions, dosing guides or operational care procedures are created.

## Alternatives Considered

- Keep respiratory, blood and endocrine variables inside existing cardiovascular/metabolic domains: rejected because each system has independent mechanisms and failure modes.
- Keep skin, ECM and lymphatic topics inside regenerative medicine: rejected because these are maintenance substrates and recovery constraints, not just repair technologies.
- Create clinical-care instructions now: rejected because the repository is a research-domain atlas, not a medical advice product.

## Consequences

- Human Infra can now model oxygenation, hormonal signaling, blood transport, tissue barrier, structural matrix and clearance networks as first-class continuity conditions.
- Cross-domain edges become clearer: breathing links to sleep and cognition, hormones link to metabolism and mood, blood links to oxygen and thrombosis, skin links to infection and care, ECM links to organ stiffness, lymphatics link to immune and brain clearance.
- Safety boundaries remain explicit: no diagnosis, no individual treatment, no acute-care instructions.

## Safety And Evidence Boundary

These domains must not provide diagnosis, lab interpretation, oxygen therapy, ventilator use, hormone protocols, anticoagulant or hemostatic dosing, transfusion advice, wound-care instructions, pressure-injury management, supplement protocols, device use, lymphatic drainage procedures or personalized medical recommendations. They only provide high-level research boundaries, evidence organization and model variables.
