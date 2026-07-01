# Add One-Hundred-Twenty-Ninth Wave Workplace Safety Execution Domains

## Status

Accepted.

## Context

`occupational-exposure-industrial-hygiene/` already covers chemical, physical, biological, dust, noise, heat, radiation, and skin exposure as a broad workplace exposure control layer. That is not enough for acute workplace safety execution failures. Falls from height, hazardous energy release, machine contact, powered industrial truck collisions, confined-space atmosphere failures, and sharps / bloodborne exposure each has a distinct hazard mechanism, official source base, control interface, evidence boundary, and prohibited-use boundary.

Human Infra needs these domains because workplace tasks can abruptly convert income, skill, health, identity, and family continuity into trauma, disability, infection risk, legal friction, and long recovery debt.

## Decision

Add six workplace acute-safety execution domains:

- `domains/workplace-fall-protection-height-safety-continuity/`
- `domains/hazardous-energy-lockout-tagout-continuity/`
- `domains/machine-guarding-amputation-prevention-continuity/`
- `domains/powered-industrial-truck-forklift-safety-continuity/`
- `domains/confined-space-entry-atmospheric-hazard-continuity/`
- `domains/bloodborne-pathogens-sharps-injury-worker-continuity/`

Each domain must keep `README.md` and `AGENTS.md` as its local truth source, and each must stay framed as research, literature, source-card, visualization, and boundary analysis rather than site-specific safety instruction.

## Consequences

- Workplace safety is no longer compressed into generic occupational exposure or labor-rights language.
- The project can separately model height, energy, machine, vehicle, atmospheric, and biological/sharps failure modes.
- The domains can share OSHA and CDC/NIOSH source families while retaining distinct non-goals.
- The safety boundary must remain strict because the same materials could be misused as operational advice.

## Non-Goals

- Do not provide PPE selection, anchor selection, scaffold/ladder setup, fall rescue, or site-specific fall-protection advice.
- Do not generate lockout/tagout procedures, energy-isolation steps, equipment operation steps, or incident investigation guidance.
- Do not design or bypass machine guards, interlocks, equipment controls, or maintenance procedures.
- Do not provide forklift or powered-industrial-truck driving, loading, route, certification, inspection, or traffic-control advice.
- Do not provide confined-space entry, atmospheric testing, ventilation, rescue, permit, or emergency action advice.
- Do not provide needlestick / sharps exposure treatment, PEP, vaccination, testing, wound care, medical, workers-compensation, legal, or OSHA compliance advice.

## Source Signals

- OSHA Fall Protection: <https://www.osha.gov/fall-protection>
- OSHA Control of Hazardous Energy: <https://www.osha.gov/control-hazardous-energy>
- OSHA Machine Guarding: <https://www.osha.gov/machine-guarding>
- OSHA Powered Industrial Trucks: <https://www.osha.gov/powered-industrial-trucks>
- OSHA Confined Spaces: <https://www.osha.gov/confined-spaces>
- OSHA Bloodborne Pathogens: <https://www.osha.gov/bloodborne-pathogens>
- CDC/NIOSH Bloodborne Infectious Diseases: <https://www.cdc.gov/niosh/topics/bbp/>
