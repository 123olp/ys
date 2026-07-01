# Evidence Certainty, GRADE and Summary of Findings Continuity

## Scope

This domain studies evidence certainty, GRADE judgments, summary-of-findings tables, outcome importance, certainty downgrading/upgrading and recommendation strength prerequisites.

Human Infra treats evidence certainty as the gate between evidence synthesis and model claims: a large effect estimate is not enough if certainty is low.

## Human Infra Chain

```text
synthesis produces outcome estimates
  -> certainty depends on risk of bias, inconsistency, indirectness, imprecision and reporting bias
  -> GRADE-style judgments summarize how much confidence a claim deserves
  -> Human Infra model inputs receive strength labels and downgrade reasons
  -> speculative claims stay separate from high-confidence interventions
  -> subject-continuity planning avoids false precision
```

## Non-Goals

- No treatment recommendation, clinical guideline writing, insurance coverage decision or legal-standard claim.
- No conversion of low-certainty evidence into strong public claims.
- No hiding downgrade reasons, manipulating outcome importance or overstating certainty.
- No individual risk prediction, diagnosis or therapy ranking.

## Source Signals

- GRADE Handbook: https://gdt.gradepro.org/app/handbook/handbook.html
- GRADE Working Group: https://www.gradeworkinggroup.org/
- GRADEpro: https://www.gradepro.org/
- Cochrane Handbook: https://training.cochrane.org/handbook

## Next Notes

- Define source-card fields for certainty, downgrade domains, outcome importance and summary-of-findings link.
- Connect with `risk-of-bias-critical-appraisal-continuity/` and `meta-analysis-effect-size-heterogeneity-continuity/`.
- Track failure modes: certainty-label inflation, indirect population mismatch, imprecision ignored and outcome importance drift.
