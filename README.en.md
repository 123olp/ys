# Human Infra

[![Check](https://github.com/tradecatlabs/human_infra/actions/workflows/check.yml/badge.svg)](https://github.com/tradecatlabs/human_infra/actions/workflows/check.yml)
[![Pages](https://github.com/tradecatlabs/human_infra/actions/workflows/pages.yml/badge.svg)](https://github.com/tradecatlabs/human_infra/actions/workflows/pages.yml)

[中文](README.md) · [Website](https://tradecatlabs.github.io/human_infra/) · [Research map](https://tradecatlabs.github.io/human_infra/research-map/) · [Evidence map](https://tradecatlabs.github.io/human_infra/evidence-map/) · [LLM entry](https://tradecatlabs.github.io/human_infra/llms.txt) · [Machine knowledge index](https://tradecatlabs.github.io/human_infra/knowledge-index.json)

Human Infra is an evidence-governed research knowledge base for engineering **subject continuity**: the conditions that let a human continue to exist, perceive, act, learn, recover, choose, and reach the future.

Its core proposition is that every goal, judgment, creation, and value presupposes an available subject. That subject is not a fixed given. It is a finite system jointly supported by life, cognition, memory, attention, time, tools, AI, medicine, resources, environment, institutions, and collaboration.

> Human Infra turns the continued availability of the subject into an engineering problem.

## C0-C6

`C0` is the value origin: subject continuity itself. The six implementation lines below are classified by their control over possibility space, rootness, and long-horizon effect, not by present-day feasibility or market maturity.

| Tier | Function | Central question |
| --- | --- | --- |
| C1 | Boundary rewriting | Can lifespan, death, time, identity continuity, or future-access boundaries be changed? |
| C2 | Source maintenance | Can the body, brain, and living systems that generate possibilities be maintained? |
| C3 | Generation engine | Can cognition, learning, attention, AI collaboration, and path generation be strengthened? |
| C4 | Conversion channel | Can knowledge, technology, rights, and services become executable paths? |
| C5 | Ecological substrate | Can resources, environments, institutions, and infrastructure sustain action? |
| C6 | Local unlocking | Can concrete last-mile blockers in tasks, processes, and life be removed? |

```text
C0 subject continuity
  -> C1 rewrite boundaries
  -> C2 maintain the source body
  -> C3 strengthen generation
  -> C4 open conversion channels
  -> C5 sustain the ecology
  -> C6 unlock local blockers
```

## Research system

- `domains/` contains the physical C1-C6 research-domain tree.
- `domains/_possibility-space-control/classification.tsv` is the tier and path source of truth.
- `docs/reference/` contains project boundaries, evidence policy, claim-evidence matrices, and review registers.
- `web/` publishes research narratives, working papers, synthetic models, and machine-readable knowledge.
- `tools/` contains repository and evidence-governance auditors.

## Evidence boundary

A registered domain is a research object, not evidence that an intervention works. A working-paper hypothesis does not prove physical or engineering feasibility. Synthetic life-path models do not provide individual lifespan predictions or medical advice.

Strong claims must be traceable to a source, context, evidence role, transfer boundary, falsifier, and review state. See:

- [Project boundary](docs/reference/project-boundary-v0.1.md)
- [Evidence policy](docs/reference/evidence-policy.md)
- [Ethics and safety boundaries](docs/reference/ethics-and-safety-boundaries.md)
- [Core claim-evidence matrix](docs/reference/human-infra-core-claim-evidence-matrix.md)
- [GEO publication contract](web/GEO.md)

## Machine access

- [`llms.txt`](https://tradecatlabs.github.io/human_infra/llms.txt): concise canonical context.
- [`llms-full.txt`](https://tradecatlabs.github.io/human_infra/llms-full.txt): full project and domain context.
- [`knowledge-index.json`](https://tradecatlabs.github.io/human_infra/knowledge-index.json): project, tier, domain, source-path, and boundary entities.
- [`evidence-graph.json`](https://tradecatlabs.github.io/human_infra/evidence-graph.json): bounded claim, source-anchor, endpoint, falsifier, and transfer-boundary relations.
- [`geo-metrics.json`](https://tradecatlabs.github.io/human_infra/geo-metrics.json): measurement and attribution contract.
- [`geo-prompt-bank.json`](https://tradecatlabs.github.io/human_infra/geo-prompt-bank.json): reproducible external AI sampling prompts.

## Local verification

```bash
make check
cd web
npm ci
npm run audit:geo
```

Publisher: **tradecatlabs**. Community: [Telegram](https://t.me/human_infra).

The evidence graph is a repository-register projection, not an independent fresh review or calibrated model input.
