# ADR 0094: Add Ninetieth-Wave Auditory Communication Execution Continuity Domains

## Status

Accepted.

## Context

The existing `hearing-auditory-communication-continuity/` domain captures the broad claim that hearing and auditory communication are conditions for language, relationship, service comprehension, warning signals, and social participation.

That parent domain was too coarse for the next stage of Human Infra's transcendental domain mapping. Auditory continuity fails through different mechanisms: age-related hearing loss, preventable noise injury, tinnitus burden, child middle-ear disease, sudden hearing loss, cochlear implant maintenance, newborn screening follow-up, auditory processing load, assistive alerting devices, and caption/relay access. These are not interchangeable because they have different time windows, evidence sources, service pathways, devices, legal accessibility interfaces, and safety boundaries.

## Decision

Add ten auditory communication execution continuity domains:

- `age-related-hearing-loss-hearing-aid-continuity/`
- `noise-induced-hearing-loss-prevention-continuity/`
- `tinnitus-sound-tolerance-sleep-continuity/`
- `otitis-media-child-hearing-development-continuity/`
- `sudden-hearing-loss-urgent-referral-continuity/`
- `cochlear-implant-communication-continuity/`
- `newborn-hearing-screening-language-development-continuity/`
- `auditory-processing-listening-effort-continuity/`
- `hearing-assistive-devices-alerting-access-continuity/`
- `captions-relay-service-communication-access-continuity/`

Each domain receives a `README.md` and `AGENTS.md`, and the root README, domain indexes, research atlas, radar, domain map, ethics boundaries, applications/literature map, and repository check script are updated.

## Consequences

- Human Infra can now distinguish the broad hearing/auditory communication substrate from concrete execution-layer failure modes.
- Hearing-related domains can be modeled as task-resource constraints: audibility, listening effort, sleep burden, language development windows, device continuity, urgent referral, and non-auditory communication access.
- The domains remain research and governance maps, not hearing diagnosis, audiogram interpretation, hearing-aid fitting, cochlear implant programming, tinnitus treatment, urgent triage, caption compliance certification, legal advice, or individual medical guidance.

## Source Signals

- NIDCD age-related hearing loss and hearing aids resources.
- NIDCD and CDC/NIOSH noise-induced hearing loss prevention resources.
- NIDCD tinnitus, ear infections in children, sudden deafness, cochlear implants, newborn hearing screening, auditory processing disorder, assistive devices, and captions resources.
- ADA effective communication and FCC telecommunications relay service resources.
