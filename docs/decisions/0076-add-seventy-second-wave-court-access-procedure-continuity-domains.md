# 0076 Add Seventy-Second Wave Court Access Procedure Continuity Domains

Status: Accepted

Date: 2026-07-01

## Context

Human Infra already has broad `access-to-justice-legal-aid`, `court-notice-service-process-default-judgment-continuity`, consumer debt, victim rights, housing eviction, language access, disability access, and administrative-burden domains.

That still leaves a distinct execution layer: when a subject must interact with a court, the decisive failure points are often not the legal theory itself but whether the person can understand neutral court information, submit documents, attend hearings, obtain language and disability access, handle fees and fines, respond to jury service, or use simplified civil-dispute channels.

These are subject-continuity conditions because court-process failure can turn repairable disputes into housing loss, debt escalation, default judgments, license loss, work disruption, civic exclusion, or persistent resource damage.

## Decision

Add eight court access and civil-procedure execution continuity domains:

- `domains/c5-ecological-substrate/self-represented-litigant-court-self-help-continuity/`
- `domains/c5-ecological-substrate/court-efiling-document-submission-continuity/`
- `domains/c2-source-maintenance/remote-hybrid-court-hearing-access-continuity/`
- `domains/c3-generation-engine/court-language-access-interpreter-continuity/`
- `domains/c5-ecological-substrate/court-disability-accommodation-accessibility-continuity/`
- `domains/c5-ecological-substrate/court-fees-fines-ability-to-pay-continuity/`
- `domains/c6-local-unlocking/jury-service-summons-hardship-continuity/`
- `domains/c6-local-unlocking/small-claims-civil-dispute-resolution-continuity/`

## Consequences

- Court access is no longer treated only as abstract legal aid or notice/service of process.
- Court systems now have separate Human Infra interfaces for self-help, filing, hearings, language, disability, monetary obligations, jury service, and simplified civil disputes.
- These domains are documentation-only skeletons and must not provide legal advice, live-case strategy, document drafting, deadline calculation, court evasion, payment evasion, jury avoidance, or local procedural instructions.

## Sources

- National Center for State Courts access-to-justice, self-represented litigant, language access, remote hearing, jury, fines/fees, and civil justice materials.
- U.S. Courts public materials on representing yourself, CM/ECF/PACER, jury service, interpreters, and fees.
- DOJ and ADA.gov language access and disability access materials.
- Legal Services Corporation justice gap and legal aid access materials.
- FTC and CFPB consumer dispute materials where simplified civil disputes intersect consumer protection.
