# Add One Hundred Twenty Eighth Wave Sleep Wake Scheduling Domains

## Status

Accepted

## Context

Human Infra already has `sleep-circadian-recovery`, `fatigue-risk-alertness-continuity`, `sleep-disordered-breathing-screening-treatment-continuity`, and `chronic-insomnia-cbti-access-continuity`. These domains are necessary but still too broad for several distinct mechanisms that break subject continuity through sleep-wake scheduling failure: pathological wakefulness instability, excessive sleepiness without ordinary sleep debt framing, sensory-motor sleep disruption, circadian phase misalignment, externally imposed work-hour fatigue, and sleep-state behaviors that create household and public safety exposure.

The verified source signals for this wave come from NHLBI narcolepsy and circadian rhythm disorder materials, MedlinePlus pages on idiopathic hypersomnia, restless legs syndrome, sleepwalking, and sleep disorders, plus CDC/NIOSH materials on long work hours, fatigue, and sleep/work scheduling.

## Decision

Add six independent research domains:

- `domains/narcolepsy-daytime-sleepiness-continuity/`
- `domains/idiopathic-hypersomnia-excessive-sleepiness-continuity/`
- `domains/restless-legs-periodic-limb-movement-sleep-continuity/`
- `domains/circadian-rhythm-sleep-wake-disorder-continuity/`
- `domains/shift-work-long-hours-fatigue-continuity/`
- `domains/parasomnia-sleepwalking-behavior-safety-continuity/`

Each domain receives a `README.md` and `AGENTS.md`, and all root, docs, reference, and repository validation indexes are updated.

## Consequences

- Sleep recovery is no longer represented only as a generic circadian / insomnia / sleep-breathing bucket.
- Narcolepsy, idiopathic hypersomnia, restless legs / periodic limb movement, circadian rhythm sleep-wake disorders, shift work / long-hours fatigue, and parasomnia / sleepwalking can each carry their own mechanism, evidence boundary, service interface, safety exposure, and Human Infra value chain.
- The project can distinguish wakefulness maintenance, excessive sleepiness, sensory-motor sleep disruption, internal/external timing mismatch, external schedule fatigue, and sleep-state behavior safety.
- Downstream modeling can connect these domains to attention, reaction time, learning, work safety, transportation exposure, household risk, recovery debt, stigma, and effective-time loss without collapsing them into a single lifestyle category.

## Non-Goals

- Do not provide diagnosis or individual sleep test interpretation.
- Do not recommend stimulants, sedatives, melatonin, iron, light therapy, sleep devices, prescriptions, dosage, shift schedules, driving decisions, work-duty fitness decisions, home-safety action plans, legal claims, insurance claims, or employer compliance advice.
- Do not score personal risk from diaries, wearables, sleep videos, shift rosters, employer records, or self-reported symptoms.
- Do not treat these domains as medical advice, occupational-safety advice, legal advice, or an emergency response channel.

## Source Signals

- NHLBI narcolepsy: https://www.nhlbi.nih.gov/health/narcolepsy
- NHLBI circadian rhythm disorders: https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders
- NHLBI circadian rhythm disorder types: https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders/types
- MedlinePlus idiopathic hypersomnia: https://medlineplus.gov/ency/article/000803.htm
- MedlinePlus restless legs syndrome: https://medlineplus.gov/restlesslegs.html
- MedlinePlus sleepwalking: https://medlineplus.gov/ency/article/000808.htm
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm
- CDC/NIOSH fatigue and long work hours: https://www.cdc.gov/niosh/bulletin/2023/fatigue.html
- CDC/NIOSH sleep and work: https://www.cdc.gov/niosh/bulletin/2012/sleep-and-work.html
