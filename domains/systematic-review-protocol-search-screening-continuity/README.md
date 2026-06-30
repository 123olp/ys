# Systematic Review Protocol, Search and Screening Continuity

## Scope

This domain studies systematic review protocols, eligibility criteria, database search strategies, deduplication, screening workflows, PRISMA flow reporting and review registration.

Human Infra treats systematic review infrastructure as an evidence intake layer: if search and screening are not transparent, the model only sees a selected fragment of the literature.

## Human Infra Chain

```text
model depends on literature claims
  -> literature claims depend on complete and reproducible search
  -> protocols define population, intervention, comparator, outcomes and eligibility
  -> screening records show why studies entered or left the evidence set
  -> evidence gaps and selection boundaries become visible
  -> life-path claims can be downgraded before they become false certainty
```

## Non-Goals

- No ghostwriting, paper mill support, fake screening, fabricated PRISMA diagrams or review registration manipulation.
- No medical recommendation, treatment ranking, diagnosis, trial enrollment advice or personal life-extension conclusion.
- No database access circumvention, copyrighted full-text redistribution or scraping restricted sources.
- No claim that a systematic review protocol alone proves an intervention works.

## Source Signals

- PRISMA 2020: https://www.prisma-statement.org/
- PROSPERO: https://www.crd.york.ac.uk/prospero/
- Cochrane Handbook: https://training.cochrane.org/handbook
- EQUATOR Network: https://www.equator-network.org/

## Next Notes

- Define a source-card field for search date, databases, strings, eligibility criteria, screening counts and exclusions.
- Connect this domain to `preregistration-registered-report-study-plan-continuity/` without treating review registration as proof of quality.
- Track failure modes: selective database choice, outdated search, vague exclusion, duplicate records and unreconciled screening conflicts.
