# 0007 Add Third Wave Research Domains

## Status

Accepted.

## Context

The first two waves established domains for biological maintenance, neural continuity, waiting paths, cognition, recovery, environment, tools, governance and measurement. Continued source review surfaced additional conditions that are not adequately owned by existing domains:

- nutrition and metabolic state determine energy, repair materials and chronic disease risk;
- physical activity and mobility convert biological survival into repeated action;
- cardiovascular failure is a central termination path for subject continuity;
- musculoskeletal integrity determines load-bearing, falls, pain and independence;
- social connection and relational support convert isolated individuals into recoverable subjects;
- substance exposure and addiction reshape mortality risk and agency;
- health literacy and navigation determine whether external services can be used at all;
- oral health connects nutrition, pain, infection, communication and dignity.

## Decision

Add third-wave domain skeletons for:

- `nutrition-metabolic-health/`
- `physical-activity-mobility/`
- `cardiovascular-resilience/`
- `musculoskeletal-integrity/`
- `social-connection-relational-infra/`
- `substance-exposure-control/`
- `health-literacy-navigation/`
- `oral-health-continuity/`

Each domain starts with only `README.md` and `AGENTS.md`. No data, scripts, product folders or operational protocols are created.

## Alternatives Considered

- Keep all third-wave directions in `research-domain-radar.md`: rejected because each direction has independent mechanisms, evidence systems, failure modes and communication risks.
- Put them under `longevity-evidence/` only: rejected because nutrition, movement, social connection, literacy and oral health are not merely longevity interventions; they are subject-runtime infrastructure.
- Create evidence pipelines now: rejected because source-card work and evidence matrices are not yet mature.

## Consequences

- The domain system now covers energy input, movement, circulation, structure, relationships, exposure control, navigation and oral function.
- The project can discuss common population-health determinants without collapsing them into personal advice.
- Future work can add Source Cards, evidence matrices and model variables per domain without changing the top-level architecture.

## Safety And Evidence Boundary

These domains must not provide medical diagnosis, treatment instructions, medication advice, dental treatment advice, training plans, dietary prescriptions, illegal substance guidance, crisis-service replacement, insurance/legal advice or individualized risk predictions. They only provide high-level research boundaries, evidence organization and model variables.
