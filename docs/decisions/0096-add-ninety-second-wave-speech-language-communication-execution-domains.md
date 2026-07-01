# ADR 0096: Add Ninety-Second-Wave Speech Language Communication Execution Domains

## Status

Accepted.

## Context

The existing `speech-language-communication-continuity/` domain captures the broad claim that speech, language, and communication are conditions for preference expression, consent, help-seeking, relationship continuity, education, work, and social participation.

That parent domain was too coarse for Human Infra's transcendental domain mapping. Communication continuity fails through different mechanisms: acquired language loss, motor speech intelligibility failure, speech motor planning disruption, voice and phonation limits, stuttering and fluency participation barriers, developmental language disorder, speech sound and phonology difficulty, AAC access, social-pragmatic communication mismatch, and cognitive-communication breakdown. These are not interchangeable because they have different source signals, age windows, participation consequences, assistive interfaces, and safety boundaries.

## Decision

Add ten speech language communication execution continuity domains:

- `aphasia-language-access-recovery-continuity/`
- `dysarthria-speech-intelligibility-continuity/`
- `apraxia-of-speech-motor-planning-continuity/`
- `voice-disorders-phonation-communication-continuity/`
- `stuttering-fluency-participation-continuity/`
- `developmental-language-disorder-child-communication-continuity/`
- `speech-sound-disorder-articulation-phonology-continuity/`
- `augmentative-alternative-communication-aac-continuity/`
- `social-communication-pragmatic-language-continuity/`
- `cognitive-communication-disorder-executive-language-continuity/`

Each domain receives a `README.md` and `AGENTS.md`, and the root README, domain indexes, research atlas, radar, domain map, ethics boundaries, applications/literature map, and repository check script are updated.

## Consequences

- Human Infra can now distinguish the broad speech-language substrate from concrete expression, understanding, fluency, phonation, AAC, pragmatics, and cognitive-communication failure modes.
- Communication domains can be modeled as task-resource constraints: language access, intelligibility, motor planning, voice endurance, participation confidence, child language development, speech sound clarity, expression-channel redundancy, pragmatic context, and executive-language support.
- The domains remain research and governance maps, not diagnosis, therapy plan generation, speech exercise prescription, device prescription, school eligibility determination, work clearance, prognosis, legal capacity assessment, or individual medical guidance.

## Source Signals

- NIDCD aphasia, voice, stuttering, developmental language disorder, and assistive device resources.
- ASHA practice materials for aphasia, dysarthria, apraxia of speech, voice disorders, fluency disorders, child language, speech sound disorders, AAC, social communication, and cognitive-communication.
- Stroke, TBI, child development, neurodiversity, education access, and assistive technology literature as research context.
