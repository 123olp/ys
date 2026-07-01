# ADR 0095: Add Ninety-First-Wave Vestibular Balance Execution Continuity Domains

## Status

Accepted.

## Context

The existing `vestibular-balance-spatial-orientation/` domain captures the broad claim that vestibular function, balance, spatial orientation, mobility confidence, and fall avoidance are conditions for embodied task execution.

That parent domain was too coarse for Human Infra's transcendental domain mapping. Vestibular continuity fails through different mechanisms: brief positional vertigo, episodic Meniere attacks, acute vestibular neuritis or labyrinthitis, persistent postural-perceptual dizziness, vestibular migraine, bilateral vestibular hypofunction, rehabilitation and compensation pathways, gait and balance screening, motion sickness in transport or virtual environments, and vestibular ototoxicity from medications or chemicals. These are not interchangeable because they have different triggers, time windows, evidence sources, exposure interfaces, recovery pathways, and safety boundaries.

## Decision

Add ten vestibular balance execution continuity domains:

- `bppv-positional-vertigo-continuity/`
- `menieres-disease-episodic-vertigo-continuity/`
- `vestibular-neuritis-labyrinthitis-acute-vertigo-continuity/`
- `persistent-postural-perceptual-dizziness-continuity/`
- `vestibular-migraine-dizziness-sensory-load-continuity/`
- `bilateral-vestibular-hypofunction-gaze-gait-stability-continuity/`
- `vestibular-rehabilitation-balance-compensation-continuity/`
- `gait-balance-assessment-fall-screening-continuity/`
- `motion-sickness-transport-virtual-environment-tolerance-continuity/`
- `vestibular-ototoxicity-medication-chemical-risk-continuity/`

Each domain receives a `README.md` and `AGENTS.md`, and the root README, domain indexes, research atlas, radar, domain map, ethics boundaries, applications/literature map, and repository check script are updated.

## Consequences

- Human Infra can now distinguish the broad vestibular-balance substrate from concrete execution-layer failure modes.
- Vestibular domains can be modeled as task-resource constraints: positional triggers, attack unpredictability, acute recovery, visual-motion sensitivity, sensory load, gaze stability, compensation pathways, fall screening, transport/VR tolerance, and toxic exposure risk.
- The domains remain research and governance maps, not diagnosis, canalith repositioning instructions, vestibular exercise prescription, medication advice, emergency triage, driving or work clearance, device recommendation, occupational exposure determination, or individual medical guidance.

## Source Signals

- NIDCD balance disorders and Meniere's disease resources.
- CDC STEADI fall prevention materials.
- APTA / Academy of Neurologic Physical Therapy vestibular rehabilitation clinical practice guidance.
- CDC Yellow Book motion sickness material and NASA human research context for space motion sickness.
- CDC/NIOSH occupational noise and ototoxic chemical exposure resources.
