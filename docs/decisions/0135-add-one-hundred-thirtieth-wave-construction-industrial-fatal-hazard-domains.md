# Add One-Hundred-Thirtieth Wave Construction Industrial Fatal Hazard Domains

## Status

Accepted.

## Context

`occupational-exposure-industrial-hygiene/` provides the broad workplace exposure layer, and the 129th wave added acute workplace safety execution domains for falls, hazardous energy, machine guarding, powered industrial trucks, confined spaces, and bloodborne/sharps exposures.

That still leaves several construction and industrial site fatal mechanisms under-modeled. Trenching cave-ins, crane/rigging suspended-load failures, occupational electrical shock and arc flash, welding/hot-work fume and fire, respirable crystalline silica, and demolition structural collapse each has a distinct event window, official source base, evidence boundary, operational-misuse risk, and downstream continuity effect.

Human Infra needs these domains because construction and industrial work can convert skill, income, built-environment repair, and infrastructure renewal into sudden death, crushing injury, burns, chronic lung disease, community risk, and long recovery debt.

## Decision

Add six construction and industrial site fatal-hazard execution domains:

- `domains/c6-local-unlocking/trenching-excavation-cave-in-worker-continuity/`
- `domains/c6-local-unlocking/crane-derrick-hoist-rigging-suspended-load-continuity/`
- `domains/c5-ecological-substrate/occupational-electrical-shock-arc-flash-continuity/`
- `domains/c6-local-unlocking/welding-cutting-brazing-fume-fire-continuity/`
- `domains/c6-local-unlocking/respirable-crystalline-silica-dust-worker-continuity/`
- `domains/c6-local-unlocking/demolition-structural-collapse-debris-continuity/`

Each domain must keep `README.md` and `AGENTS.md` as its local truth source, and each must stay framed as research, source-card, model, visualization, and boundary analysis rather than site-specific safety instruction.

## Consequences

- Construction and industrial fatal hazards are no longer compressed into generic occupational exposure language.
- The project can separately model cave-in, suspended-load, electrical, hot-work, silica-dust, and demolition-collapse pathways.
- These domains can share OSHA source families while retaining different non-goals and misuse boundaries.
- The safety boundary must remain strict because operational details could be misused as site instructions or compliance substitutes.

## Non-Goals

- Do not provide trenching/excavation design, shoring, sloping, benching, shields, soil classification, underground utility locating, rescue, permit, or construction advice.
- Do not provide lift plans, rigging calculations, load-chart use, signaling, crane operation, inspection, certification, or equipment maintenance advice.
- Do not provide electrical work, energized work, arc-flash calculations, PPE categories, lockout/tagout steps, troubleshooting, wiring, or electrical repair advice.
- Do not provide welding/cutting/brazing instructions, hot-work permits, ventilation design, respirator selection, gas-cylinder handling, fire watch, confined-space entry, or fire response advice.
- Do not provide silica exposure-monitoring plans, engineering controls, respiratory protection selection, medical-surveillance interpretation, occupational-disease diagnosis, or compliance advice.
- Do not provide demolition plans, engineering sequencing, structural assessment, support design, debris removal, hazardous-material handling, permit, insurance, or legal advice.

## Source Signals

- OSHA Trenching and Excavation: <https://www.osha.gov/trenching-excavation>
- OSHA Crane, Derrick and Hoist Safety: <https://www.osha.gov/cranes-derricks>
- OSHA Electrical: <https://www.osha.gov/electrical>
- OSHA Welding, Cutting, and Brazing: <https://www.osha.gov/welding-cutting-brazing>
- OSHA Silica, Crystalline: <https://www.osha.gov/silica-crystalline>
- OSHA Demolition: <https://www.osha.gov/demolition>
