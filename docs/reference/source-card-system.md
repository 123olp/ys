# Source Card System

## Purpose

The source card system defines how Human Infra turns papers, books, tools, cases, standards, and datasets into reusable project material.

It exists because the repository is moving from qualitative organization toward quantitative modeling. A source should not jump directly from "interesting" to "model input." It must pass through a card that states what the source says, where it fits, what it can support, and what it cannot support.

## Intake Flow

```text
source
  -> research card
  -> source note or reference update
  -> domain mapping
  -> model variable mapping
  -> web narrative or visualization
```

The card is the bridge between raw material and stable project knowledge.

## Card Types

| Type | Examples | Main use |
| --- | --- | --- |
| Paper card | Journal article, preprint, review, guideline paper | Extract variables, methods, endpoints, evidence boundaries |
| Book card | Future studies, theory, philosophy, public science book | Extract concepts, narrative frames, hidden assumptions |
| Tool card | D3, Observable, lifelines, Stan, OpenAlex, PubMed | Decide whether a tool belongs in the workflow |
| Case card | Blueprint, Seed Vault, public health program, AI safety framework | Map real systems to Human Infra domains |
| Standard card | TRIPOD, PROBAST, FAIR, NIST AI RMF, ISO 22301 | Convert external standards into repository rules |
| Dataset card | ClinicalTrials.gov, NHANES, UK Biobank, HAGR, openFDA | Clarify fields, license, population, limits, and model use |

## Required Fields

Every source card must answer:

| Field | Question |
| --- | --- |
| Source identity | What is the exact source, version, date, and URL or local path? |
| Source type | Paper, book, tool, case, standard, dataset, or mixed source |
| One-sentence claim | What is the source useful for in one sentence? |
| Human Infra mapping | Which subject-continuity variable, domain, or narrative layer does it support? |
| Model position | Does it affect state variables, transitions, hazards, observation, policy, time accounting, or governance? |
| Evidence role | Is it mechanism, association, endpoint evidence, method standard, or narrative support? |
| Transfer boundary | What cannot be inferred from this source? |
| Action | Should this update a reference doc, domain doc, Web page, data file, or remain as background? |

## Evidence Handling

Source cards do not automatically upgrade claims. They classify evidence before a stable document uses it.

| Evidence role | Allowed output |
| --- | --- |
| Mechanism | Conceptual pathway or candidate variable |
| Association | Risk factor or hypothesis, not an intervention effect by itself |
| Endpoint evidence | Candidate model estimate, if population and horizon match |
| Method standard | Reporting, bias review, validation, or workflow requirement |
| Narrative support | Public explanation, genealogy, analogy, or theory framing |
| Tool evidence | Implementation choice, not a scientific conclusion |

## Model Mapping

A source can enter the life-path model only when it identifies at least one model location:

```text
state variable X_t
state transition P(X_{t+1} | X_t, A_t)
hazard lambda(t | X_t, A_t)
observation process O_t
action policy pi(A_t | history_t)
time accounting: lifespan / healthspan / effective time / subjective time / relative time
option value or recovery capacity
```

If no location can be identified, the source remains qualitative support.

## Review Rules

Before a card updates a stable document, check:

1. The source identity is recoverable.
2. The claim is narrower than the source's rhetoric.
3. The Human Infra mapping is explicit.
4. The model position is not guessed.
5. The transfer boundary is written.
6. Any safety-sensitive claim links back to evidence and governance rules.

## File Naming

Use semantic, lower-case filenames:

```text
YYYY-MM-DD-short-source-name-card.md
```

Examples:

```text
2026-06-27-kurzweil-singularity-is-nearer-card.md
2026-06-27-tripod-ai-card.md
2026-06-27-d3-data-driven-documents-card.md
```

Cards may live in `docs/source-notes/` while they are being processed. Stable distilled rules belong in `docs/reference/` or domain documents.

## Template

Use [research-card.md](../templates/research-card.md) for new cards.

## Source Traceability

This system connects:

- [Source Management](source-management.md)
- [Evidence Policy](evidence-policy.md)
- [Life-Path Prediction Model Contract](life-path-prediction-model-contract.md)
- [Research Model and Visualization Toolkit](research-model-visualization-toolkit.md)

## Maintenance

- Owner: Human Infra maintainers.
- Review trigger: new source-note workflow, new model variables, new Web data pipeline, or change in evidence policy.
- Related files: [Source Note Template](../templates/source-note.md), [Research Card Template](../templates/research-card.md).
