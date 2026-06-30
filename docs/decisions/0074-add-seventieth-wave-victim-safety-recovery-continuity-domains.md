# ADR 0074: Add Seventieth-Wave Victim Safety and Recovery Continuity Domains

## Status

Accepted.

## Context

Human Infra already had `personal-safety-violence-prevention/`, but that domain was too broad for repeated research work. Domestic violence, sexual assault response, stalking/protection orders, victim-witness notification, compensation, survivor housing, trafficking services, and missing-person resolution have different official sources, failure modes, privacy risks, evidence boundaries, and prohibited uses.

## Decision

Add eight victim safety and recovery execution domains:

- `domestic-violence-coercive-control-safety-continuity/`
- `sexual-assault-forensic-exam-advocacy-continuity/`
- `stalking-harassment-protection-order-continuity/`
- `victim-witness-rights-notification-continuity/`
- `crime-victim-compensation-restitution-continuity/`
- `survivor-safe-housing-emergency-transfer-continuity/`
- `human-trafficking-victim-identification-services-continuity/`
- `missing-persons-unidentified-remains-resolution-continuity/`

These domains model safety and recovery as infrastructure: help entry, confidentiality, medical forensic care, rights notification, compensation, housing transfer, trafficking service referral, missing-person identity resolution, and survivor-centered continuity.

## Consequences

- `personal-safety-violence-prevention/` remains the broad parent domain.
- New work on DV/IPV, sexual assault, stalking, victim rights, victim compensation, survivor housing, trafficking, or missing-person identity resolution should route to the more specific domain first.
- All domains must maintain strict boundaries: no individual safety plans, legal strategy, evidence strategy, shelter location, doxxing, stalking, retaliation, trafficking methods, private investigation, or identifiable victim/person data.
