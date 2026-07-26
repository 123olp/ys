# Human Infra

[![Check](https://github.com/tradecatlabs/human_infra/actions/workflows/check.yml/badge.svg)](https://github.com/tradecatlabs/human_infra/actions/workflows/check.yml)

[中文](README.md) · [Local Wiki](wiki/README.md) · [Research domains](domains/README.md) · [Evidence references](docs/reference/README.md)

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
- `web/` contains research data and audit scripts only. It is not a website and must not be deployed.
- `archive/retired-research-narrative-site/` is a permanently retired historical implementation.
- `tools/` contains repository and evidence-governance auditors.

## Evidence boundary

A registered domain is a research object, not evidence that an intervention works. A working-paper hypothesis does not prove physical or engineering feasibility. Synthetic life-path models do not provide individual lifespan predictions or medical advice.

Strong claims must be traceable to a source, context, evidence role, transfer boundary, falsifier, and review state. See:

- [Project boundary](docs/reference/project-boundary-v0.1.md)
- [Evidence policy](docs/reference/evidence-policy.md)
- [Ethics and safety boundaries](docs/reference/ethics-and-safety-boundaries.md)
- [Core claim-evidence matrix](docs/reference/human-infra-core-claim-evidence-matrix.md)
- [Local Wiki](wiki/README.md)
- [Retired site record](archive/retired-research-narrative-site/README.md)

## Public products

Only the Human Infra technology tree and Wiki are eligible for public deployment. The retired Research Narrative site is excluded from all build and deployment paths.

## Local verification

```bash
make check
```

Publisher: **tradecatlabs**. Community: [Telegram](https://t.me/human_infra).

The evidence graph is a repository-register projection, not an independent fresh review or calibrated model input.
