# 0126. Add One Hundred Twenty First Wave Public Benefits Redetermination Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra already tracks social protection, SNAP redemption, health insurance enrollment, unemployment wage records, disability income and public-benefits eligibility automation. Those domains cover broad welfare delivery or payment endpoints, but they do not fully isolate program-specific administrative chains where a subject can lose food, medical coverage or income support through renewal, redetermination, identity proofing, review, sanction, appeal or payment execution failures.

The first-principles question is: if subject continuity depends on anti-scarcity infrastructure, which public-benefit execution paths must remain observable, restorable and contestable when the subject is under stress?

## Decision

Add six public-benefits redetermination and execution domains:

- `snap-eligibility-recertification-abawd-continuity/`
- `medicaid-chip-renewal-redetermination-continuity/`
- `medicare-enrollment-coverage-transition-continuity/`
- `ssi-ssdi-disability-review-appeal-continuity/`
- `tanf-cash-assistance-work-support-continuity/`
- `unemployment-insurance-claim-appeal-identity-continuity/`

Each domain gets an independent `README.md` and `AGENTS.md`, and is indexed in the root README, domain map, research atlas, research radar, applications/literature index, ethics boundary document and repository validation script.

## Boundaries

- These domains are research and modeling domains, not benefit application tools.
- They must not provide individual eligibility determinations, filing advice, appeal strategy, identity-proofing workarounds, false-material generation, benefit-maximization tactics, legal advice, tax advice, immigration advice or medical advice.
- They reuse official public sources such as USDA FNS, CMS/Medicaid.gov, Medicare.gov, SSA, ACF/OFA and DOL/ETA where available.
- They remain separate from payment-redemption domains: SNAP eligibility is upstream of EBT redemption; Medicaid/CHIP and Medicare enrollment are upstream of provider billing, claims and prior authorization.

## Consequences

- The anti-scarcity layer becomes more precise: public support is no longer a single abstract welfare bucket, but a set of program-specific continuity chains.
- Future quantitative work can model failure points such as recertification loss, procedural termination, identity proofing failure, payment delay, review burden, appeal window and sanctions.
- Documentation maintenance burden increases, so all six domains are added to `tools/check_repository.py` required files and directories.
