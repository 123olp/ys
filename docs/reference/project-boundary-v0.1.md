# Project Boundary v0.1

## Purpose

This document freezes the first public boundary for Human Infra. It tells readers what the project is, what it is not, and how current work should be organized before the repository moves into heavier quantitative modeling.

Version `v0.1` is not a release tag. It is a working boundary for the current knowledge base.

## One-Sentence Definition

Human Infra is a docs-as-code research knowledge base for engineering subject continuity: the systems that keep humans able to exist, act, learn, recover, revise decisions, and enter future possibility windows over time.

## Core Position

Human Infra treats subject continuity as a boundary condition for value creation.

```text
value / goal / creation
  -> requires an acting subject
  -> subject depends on life, cognition, tools, environment, resources, institutions, and collaboration
  -> those supports are degraded by aging, disease, damage, scarcity, risk, and death
  -> maintaining the subject is therefore a higher-order infrastructure problem
```

This boundary keeps the project broader than a longevity note collection and narrower than a generic "everything about humans" archive.

## Included In v0.1

| Area | Current role |
| --- | --- |
| Subject continuity theory | Defines why lifespan, agency, cognition, recovery, resources, and future option value belong together |
| Multi-perspective value explanation | Keeps both the subject-continuity lens and the resource-budget expansion lens |
| Genealogy and narrative | Uses Noah's Ark as the continuity metaphor, while preserving theory, institution, and counter-genealogy boundaries |
| Life-path prediction model | Defines how interventions can affect state transitions, hazards, survival curves, effective time, subjective time, relative time, and option value |
| Research and visualization toolkit | Records literature-reading, model-reporting, causal-inference, survival-analysis, and Astro / D3 guidance |
| Application and literature map | Collects real systems, standards, institutions, cases, and literature that support Human Infra |
| Domain structure | Keeps longevity evidence, future waiting, disembodied CNS, and memory editing as separate subdomains |
| Web presentation | Uses `web/` as the formal Astro + D3 application for public research narrative and interactive visualizations |

## Excluded From v0.1

Human Infra v0.1 does not provide:

- medical diagnosis, treatment plans, or individualized medication advice;
- claims that any intervention guarantees immortality or permanent life extension;
- deterministic forecasts of a person's death or life outcome;
- instructions for invasive neural, memory, or life-support experiments;
- investment advice, policy prescriptions, or legal advice;
- employee, insurance, credit, policing, or coercive ranking systems;
- scraped private data, personal health profiles, or non-consensual monitoring.

## Current Deliverables

| Deliverable | File or directory | Status |
| --- | --- | --- |
| Project entry | `README.md` | Stable public entry |
| Documentation map | `docs/README.md` | Stable navigation |
| Domain map | `docs/reference/domain-map.md` | Stable reference |
| Evidence rules | `docs/reference/evidence-policy.md` | Stable reference |
| Safety boundary | `docs/reference/ethics-and-safety-boundaries.md` | Stable reference |
| Prediction model explanation | `docs/explanations/life-path-prediction-model.md` | Stable explanation |
| Prediction model contract | `docs/reference/life-path-prediction-model-contract.md` | Stable contract |
| Prediction model governance | `docs/reference/life-path-prediction-model-governance.md` | Stable governance |
| Research visualization toolkit | `docs/reference/research-model-visualization-toolkit.md` | Stable reference |
| Genealogy | `docs/explanations/noah-ark-genealogy.md` | Stable explanation |
| Source card system | `docs/reference/source-card-system.md` | Stable operating rule |
| Formal web app | `web/` | Active implementation |

## Placement Rules

| Material type | Correct location |
| --- | --- |
| Raw learning notes, transcripts, pasted material | `docs/source-notes/` |
| Stable maps, rules, contracts, standards | `docs/reference/` |
| Conceptual essays and theory synthesis | `docs/explanations/` |
| Repeatable task procedures | `docs/how-to/` |
| Reusable document shapes | `docs/templates/` |
| Domain-specific data, scripts, and product notes | `domains/*/` |
| Public interactive pages and visualizations | `web/` |
| One-off static prototypes | Repository root only when explicitly retained as prototypes |

## v0.1 Success Criteria

The current phase is successful when a reader can answer five questions without asking the maintainer:

1. What is Human Infra?
2. Why is subject continuity the main boundary condition?
3. Which domains are inside the project and why?
4. How does qualitative material become quantitative model input?
5. Which uses are explicitly outside the project boundary?

## Next Version Direction

`v0.2` should focus on evidence ingestion:

- use research cards for papers, books, tools, and cases;
- map cards to model variables and domain pages;
- separate conceptual claims from parameterizable claims;
- prepare small curated datasets or JSON structures for Web use.

`v0.3` should focus on model prototypes:

- encode one or two toy cohorts;
- implement survival or multi-state examples;
- document calibration limits;
- keep outputs at research and population-model level.

## Source Traceability

This boundary consolidates existing repository decisions and documents:

- [Domain Map](domain-map.md)
- [Evidence Policy](evidence-policy.md)
- [Ethics and Safety Boundaries](ethics-and-safety-boundaries.md)
- [Life-Path Prediction Model Contract](life-path-prediction-model-contract.md)
- [Life-Path Prediction Model Governance](life-path-prediction-model-governance.md)
- [Research Model and Visualization Toolkit](research-model-visualization-toolkit.md)
- [Noah Ark Genealogy](../explanations/noah-ark-genealogy.md)

## Maintenance

- Owner: Human Infra maintainers.
- Review trigger: README scope change, new domain, new model output, new Web route, safety boundary change, or release tagging.
- Related files: [README](../../README.md), [Documentation Map](../README.md), [Source Card System](source-card-system.md).
