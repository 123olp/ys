# Meta-Analysis, Effect Size and Heterogeneity Continuity

## Scope

This domain studies effect-size extraction, synthesis models, heterogeneity, subgroup analysis, sensitivity analysis, prediction intervals and quantitative evidence synthesis.

Human Infra treats meta-analysis as a synthesis layer, not a certainty machine: pooled estimates can compress evidence, but they can also hide incompatible populations, methods and outcomes.

## Human Infra Chain

```text
multiple studies estimate related effects
  -> effect sizes require compatible outcomes, populations and time horizons
  -> synthesis model combines estimates with uncertainty and heterogeneity
  -> sensitivity analyses test robustness to assumptions and exclusions
  -> model inputs gain bounded aggregate estimates instead of isolated claims
  -> long-horizon projections avoid single-study overreach
```

## Non-Goals

- No statistical consulting for clinical decisions, investments, legal disputes or regulatory submissions.
- No cherry-picking models, forcing significant results, p-hacking or undisclosed exclusion.
- No claim that a pooled estimate overrides poor study quality, bad measurement or population mismatch.
- No individual medical prediction or treatment comparison.

## Source Signals

- Cochrane Handbook synthesis chapters: https://training.cochrane.org/handbook/current
- PRISMA 2020: https://www.prisma-statement.org/
- Cochrane Training resources: https://training.cochrane.org/
- Campbell Collaboration methods resources: https://www.campbellcollaboration.org/

## Next Notes

- Define fields for effect measure, transformation, fixed/random model, heterogeneity, prediction interval and sensitivity checks.
- Connect with `uncertainty-quantification-model-calibration/` for propagation into life-path models.
- Track failure modes: incompatible endpoints, duplicate cohorts, unexplained heterogeneity, subgroup fishing and publication bias ignored.
