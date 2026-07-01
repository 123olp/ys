# Guideline Appraisal, Adaptation and Localization Continuity

## Scope

This domain studies guideline quality appraisal, adaptation, localization, contextual fit, update status, conflict handling and implementation transfer boundaries.

Human Infra treats guidelines as contextual artifacts: a guideline can be high quality in one setting and still be misapplied in another.

## Human Infra Chain

```text
guideline exists
  -> quality, currency, scope and conflicts must be appraised
  -> local context changes resources, population, regulation, equity and feasibility
  -> adaptation documents what transfers and what must be modified
  -> Human Infra can use guidelines as bounded evidence, not universal commands
  -> model and narrative outputs avoid context-blind authority transfer
```

## Non-Goals

- No clinical implementation plan, local policy mandate, medical advice or legal compliance assessment.
- No endorsement that a guideline is valid, current or applicable to a user.
- No adaptation used to bypass regulation, professional standards, patient consent or resource constraints.
- No manipulation of guideline appraisal scores or conflict disclosure.

## Source Signals

- AGREE Enterprise / AGREE II: https://www.agreetrust.org/
- GRADE-ADOLOPMENT resources: https://www.gradeworkinggroup.org/
- Guidelines International Network: https://g-i-n.net/
- WHO handbook for guideline development: https://www.who.int/publications/i/item/9789241548960

## Next Notes

- Define guideline-card fields: source, date, scope, population, recommendation strength, update status, appraisal result and localization limits.
- Connect to `evidence-to-decision-guideline-panel-continuity/`.
- Track failure modes: stale guideline, context mismatch, resource assumption mismatch, conflict omission and recommendation overreach.
