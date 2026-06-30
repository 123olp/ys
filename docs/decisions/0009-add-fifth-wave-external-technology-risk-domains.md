# 0009 Add Fifth Wave External Technology Risk Domains

## Status

Accepted.

## Context

Previous waves established the biological, functional, cognitive, time-waiting, environmental, resource and governance foundations of Human Infra. Continued first-principles domain tracing surfaced another class of necessary conditions: external technical systems that can either extend subject continuity or sever it.

These domains are not ordinary feature extensions. Digital identity, AI agency, supply-chain continuity, synthetic biology biosecurity and extreme habitation each have independent mechanisms, evidence systems, failure modes and safety boundaries.

## Decision

Add fifth-wave domain skeletons for:

- `digital-identity-security/`
- `ai-agency-safety/`
- `supply-chain-continuity/`
- `synthetic-biology-biosecurity/`
- `space-extreme-habitation/`

Each domain starts with only `README.md` and `AGENTS.md`. No data pipelines, automation agents, exploit examples, wet-lab protocols, survival guides or mission procedures are created.

## Alternatives Considered

- Keep all five directions inside `risk-engineering/`: rejected because each direction has distinct technical objects and governance contracts.
- Keep `ai-agency-safety/` under `cognitive-augmentation/`: rejected because AI agents are no longer only cognitive tools once they receive permissions and external action interfaces.
- Keep `digital-identity-security/` under `governance-rights/`: rejected because digital identity has its own authentication, recovery, account continuity and service-entry failure modes.
- Keep `synthetic-biology-biosecurity/` inside biology domains: rejected because biosecurity governs the tail-risk side of biological capability, not a single therapeutic mechanism.
- Create operational tooling now: rejected because the current goal is domain architecture, not high-risk execution.

## Consequences

- Human Infra can now model external technical substrates as first-class continuity conditions.
- Digital, AI, supply-chain, biosecurity and extreme-environment risks can be routed without overloading existing domains.
- Safety boundaries are explicit before any source-card, model-card or web narrative work is added.

## Safety And Evidence Boundary

These domains must not provide hacking, credential theft, authentication bypass, jailbreaks, malicious automation, procurement evasion, pathogen engineering, wet-lab protocols, dangerous-environment procedures, life-support construction steps or personalized legal/medical/financial advice. They only provide high-level research boundaries, evidence organization, risk variables and governance contracts.
