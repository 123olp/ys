# 0016 Add Twelfth Wave Treatment Service Rights Domains

Date: 2026-06-30

## Status

Accepted

## Context

The Research Domain Atlas now treats Human Infra as a transcendental map of subject-continuity conditions. Recent source signals show another set of conditions that cannot be safely collapsed into existing domains:

- treatment execution depends on medicines, labels, shortages, coverage, pharmacy continuity, and medication safety;
- care continuity depends on patient record access, interoperability, authorized data sharing, and cross-institution exchange;
- medical access increasingly depends on telehealth, remote patient monitoring, home devices, and escalation paths;
- social support depends on resource discovery, referral, closed-loop follow-up, and local service navigation;
- public services depend on language access, plain communication, cognitive accessibility, and culturally competent communication;
- work depends not only on work design but on enforceable labor standards, wage/hour protection, safety rights, anti-discrimination, and complaint channels.

These are not simply subtopics of `healthcare-access-continuity/`, `resource-social-infra/`, `health-literacy-navigation/`, or `occupational-work-design/`. Each has independent mechanisms, evidence systems, failure modes, and safety boundaries.

## Decision

Add six new domain skeletons:

- `domains/medicine-access-treatment-continuity/`
- `domains/patient-data-interoperability/`
- `domains/telehealth-remote-monitoring-access/`
- `domains/community-resource-navigation/`
- `domains/language-access-plain-communication/`
- `domains/labor-rights-workplace-protection/`

Each domain starts with only `README.md` and `AGENTS.md`.

## Rationale

- Medicine access and treatment continuity determine whether medical decisions become sustained treatment rather than a one-time recommendation.
- Patient data interoperability determines whether care, insurance, caregiving, and measurement can follow the subject across institutions.
- Telehealth and remote monitoring determine whether care can cross distance, mobility, chronic-disease follow-up, and home-continuity gaps.
- Community resource navigation determines whether fragmented local resources can be discovered, matched, referred, and confirmed.
- Language access and plain communication determine whether services, risks, rights, and tasks are understandable enough to become usable.
- Labor rights and workplace protection determine whether work is a resource amplifier or a long-term source of health, time, wage, dignity, and rights depletion.

## Boundaries

- No medical diagnosis, medication advice, dosing, alternative drugs, stopping advice, device selection, triage, or remote-care recommendation.
- No medical record interpretation, insurance benefit judgment, privacy bypass, portal cracking, unauthorized data scraping, or third-party app endorsement.
- No eligibility judgment, benefit application advice, real-time resource availability guarantee, crisis replacement, or sensitive personal data routing.
- No legal advice, labor dispute strategy, wage calculation, employment classification judgment, organizing tactics, or litigation prediction.
- No certified translation replacement, legal/medical interpretation replacement, or simplification that removes rights, risks, limits, or uncertainty.

## Consequences

- Update root README, root AGENTS, `domains/README.md`, `domains/AGENTS.md`, domain map, atlas, radar, ethics boundaries, and repository structure checks.
- Keep the domains as documentation skeletons until source cards or structured variables justify additional files.
- Do not create data, scripts, apps, or empty pipeline folders for these domains in this slice.
