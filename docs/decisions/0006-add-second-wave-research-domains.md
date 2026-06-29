# 0006 Add Second Wave Research Domains

## Status

Accepted.

## Context

The first Research Domain Atlas established domains for biological substrate maintenance, neural continuity, time-window extension, cognition, risk, resources, governance and feedback. Continued research surfaced additional conditions that are not adequately owned by existing domains:

- function can collapse even when biological survival continues;
- mental health and motivation can terminate agency without terminating the body;
- sleep and circadian recovery are core repair schedulers;
- assistive technology can convert impairment into compensated capability;
- antimicrobial resistance threatens the medical substrate itself;
- planetary and environmental systems set upstream exposure and resource conditions;
- sensory systems are core feedback channels for agency;
- pain and suffering define whether extended time remains valuable and bearable.

## Decision

Add second-wave domain skeletons for:

- `rehabilitation-functioning/`
- `mental-health-affective-stability/`
- `sleep-circadian-recovery/`
- `assistive-technology-access/`
- `antimicrobial-resilience/`
- `planetary-health-environment/`
- `sensory-continuity/`
- `pain-suffering-control/`

Each domain starts with only `README.md` and `AGENTS.md`. No data, scripts, product folders or operational protocols are created.

## Alternatives Considered

- Keep all second-wave directions in `research-domain-radar.md`: rejected because these directions have independent mechanisms, evidence systems and failure modes.
- Put them under existing domains only: rejected because that would bury function, mental health, sleep, assistive technology, antimicrobial resilience, environment, sensory continuity and suffering under overly broad buckets.
- Create evidence pipelines now: rejected because source-card work and evidence matrices are not yet mature.

## Consequences

- The domain system now covers survival, function, agency, recovery, environment, tools, governance and subjective quality.
- Existing domains remain lightweight and navigable.
- Future work can add Source Cards and evidence matrices per domain without changing the top-level architecture again.

## Safety And Evidence Boundary

These domains must not provide medical diagnosis, treatment instructions, medication advice, crisis-service replacement, device prescription, pathogen handling steps, dangerous environment guidance or legal advice. They only provide high-level research boundaries, evidence organization and model variables.
