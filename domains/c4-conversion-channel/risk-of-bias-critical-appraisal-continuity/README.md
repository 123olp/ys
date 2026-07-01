# Risk of Bias and Critical Appraisal Continuity

## Scope

This domain studies study-level risk of bias, critical appraisal tools, applicability judgments and domain-specific quality assessment for randomized, non-randomized, diagnostic, prognostic and qualitative evidence.

Human Infra treats risk of bias as a claim downgrade mechanism: a study can be relevant and still be unsafe to use as a strong causal or predictive claim.

## Human Infra Chain

```text
study enters evidence set
  -> study design creates possible bias channels
  -> appraisal separates randomization, confounding, selection, measurement, missingness and reporting risks
  -> claim strength is downgraded or blocked before model ingestion
  -> interventions are not promoted because of weak, biased or inapplicable evidence
  -> subject-continuity decisions remain evidence-bounded
```

## Non-Goals

- No accusation that authors committed misconduct merely because a risk-of-bias domain is high.
- No legal, clinical, regulatory or journal-review service.
- No p-hacking, selective reporting, data fabrication, reanalysis manipulation or study discrediting strategy.
- No use of appraisal scores as automatic truth, fraud or treatment recommendations.

## Source Signals

- Cochrane RoB 2: https://methods.cochrane.org/risk-bias-2
- ROBINS-I: https://methods.cochrane.org/methods-cochrane/robins-i-tool
- QUADAS-2: https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-2/
- PROBAST: https://www.probast.org/
- CASP checklists: https://casp-uk.net/casp-tools-checklists/

## Next Notes

- Define risk-of-bias fields for source cards: tool, domain, judgment, rationale, applicability and model consequence.
- Connect randomized and non-randomized appraisal to `causal-inference-target-trial-emulation/`.
- Track failure modes: total-score misuse, tool mismatch, vague rationale, conflict of interest ignored and overgeneralized applicability.
