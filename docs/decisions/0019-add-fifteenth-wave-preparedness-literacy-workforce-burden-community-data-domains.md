# 0019 Add Fifteenth Wave Preparedness Literacy Workforce Burden Community Data Domains

Date: 2026-06-30

## Status

Accepted

## Context

The Research Domain Atlas treats Human Infra domains as transcendental conditions for subject continuity. The previous waves covered biological maintenance, service access, public services, emergency communication, disaster recovery, financial inclusion, and workforce entry. A further pass shows six additional conditions that should not remain hidden inside broader domains:

- household preparedness determines whether a subject can bridge the time between a shock and external response;
- media and information literacy plus public libraries determine whether a subject can find, judge, understand, and use trusted information;
- health workforce capacity determines whether medical knowledge and infrastructure can become actual care;
- administrative burden and procedural friction determine whether rights and services can pass through forms, proof, waiting, renewal, and appeal;
- community health workers and peer support determine whether clinical and social services are translated into trusted daily support;
- civic data and open government transparency determine whether public systems are observable, reviewable, reusable, and accountable.

Each condition has distinct evidence sources, variables, failure modes, and safety boundaries. Collapsing them into `emergency-preparedness-response/`, `information-integrity-trust/`, `healthcare-access-continuity/`, `public-service-design-accessibility/`, `community-resource-navigation/`, or `governance-rights/` would hide independent mechanisms.

## Decision

Add six new domain skeletons:

- `domains/household-emergency-preparedness-resilience/`
- `domains/media-information-literacy-public-libraries/`
- `domains/health-workforce-capacity/`
- `domains/administrative-burden-procedural-friction/`
- `domains/community-health-workers-peer-support/`
- `domains/civic-data-open-government-transparency/`

Each domain starts with only `README.md` and `AGENTS.md`.

## Rationale

- Household preparedness is the pre-response resilience layer for family plans, supplies, medication continuity, backup communication, documents, and special needs.
- Media and information literacy plus public libraries are the public knowledge layer for judgment, learning, digital support, and civic information access.
- Health workforce capacity is the human capacity layer beneath diagnosis, treatment, prevention, rehabilitation, public health, and long-term care.
- Administrative burden is the procedural cost layer that turns nominal rights into time, attention, proof, waiting, renewal, appeal, or abandonment.
- Community health workers and peer support are the trusted intermediary layer between institutional systems and daily life.
- Civic data and open government transparency are the observability layer for public systems, accountability, service improvement, and community feedback.

## Boundaries

- No real-time disaster command, evacuation routing, emergency medical advice, dangerous storage, weaponized survivalism, or panic hoarding.
- No propaganda, microtargeting, influence operation, content forgery, platform evasion, or information warfare guidance.
- No individual provider ranking, credentialing, employment, immigration, wage, staffing, or labor dispute advice.
- No individual application strategy, false proof, benefits advice, legal advice, tax advice, or procedural evasion.
- No medical, counseling, crisis, legal, welfare, or eligibility advice through CHW or peer-support framing.
- No doxxing, privacy attack, surveillance targeting, access-control bypass, sensitive data release, or FOIA case legal advice.

## Consequences

- Update root README, root AGENTS, `domains/README.md`, `domains/AGENTS.md`, docs indexes, domain map, atlas, radar, ethics boundaries, changelog, and repository structure checks.
- Keep these domains as documentation skeletons until source cards, variable contracts, or structured datasets justify additional files.
- Do not create data, scripts, apps, or empty pipeline folders for these domains in this slice.
