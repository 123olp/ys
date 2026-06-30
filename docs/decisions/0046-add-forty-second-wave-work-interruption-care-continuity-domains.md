# 0046. Add Forty-Second-Wave Work Interruption and Care Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

The forty-first wave covered how income, tax, social-insurance, retirement, unemployment, and workers-compensation records convert past labor into future entitlements. The next first-principles condition is more immediate: subjects do not only need records after work has happened; they also need mechanisms that prevent illness, pregnancy, parenting, disability, caregiving, and recovery events from forcing them out of work, income, insurance, and social-role systems.

Existing domains such as `labor-rights-workplace-protection/`, `caregiving-long-term-care/`, `childcare-family-continuity/`, `insurance-risk-transfer/`, `disability-services-independent-living/`, and `workers-compensation-occupational-injury-benefit-continuity/` cover adjacent territory, but they do not own the specific continuity mechanisms around job-protected leave, wage replacement during leave, pregnancy/parental work continuity, workplace accommodation, disability income/work-capacity boundaries, and family caregiver respite.

## Decision

Add six domains:

- `family-medical-leave-job-protection-continuity/`
- `paid-sick-family-leave-wage-replacement-continuity/`
- `pregnancy-parental-work-continuity/`
- `workplace-accommodation-return-to-work-continuity/`
- `disability-income-work-capacity-benefit-continuity/`
- `family-caregiver-respite-work-continuity/`

Each domain receives a `README.md` and `AGENTS.md`. Root, docs, reference, and domain indexes are updated so these domains are discoverable and validated by the repository structure check.

## Consequences

- Work interruption and care events become first-class Human Infra domains rather than subnotes under labor rights, social protection, or caregiving.
- The project can distinguish job protection, wage replacement, pregnancy/parental continuity, reasonable accommodation, disability income, and caregiver respite instead of treating them as one generic “leave” or “care” problem.
- The domains remain research and documentation surfaces only. They do not provide personal legal, HR, benefits, tax, insurance, medical, claims, appeals, or employer compliance advice.

## Source Anchors

- U.S. Department of Labor, Family and Medical Leave Act.
- U.S. Department of Labor, PUMP at Work.
- U.S. Equal Employment Opportunity Commission, Pregnant Workers Fairness Act.
- U.S. Equal Employment Opportunity Commission, ADA reasonable accommodation guidance.
- U.S. Department of Labor, Office of Disability Employment Policy.
- Social Security Administration disability benefits materials.
- Administration for Community Living caregiver support and respite programs.
