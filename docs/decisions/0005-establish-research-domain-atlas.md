# 0005 Establish Research Domain Atlas

## Status

Accepted.

## Context

Human Infra 的目标已从单一长寿证据仓库扩展为“有效永生 / 主体持续性最大化”的研究系统。此前子域主要围绕已有材料逐步生成，容易出现两个问题：

- 看到一个热门技术就建域，导致目录膨胀；
- 把不同机制混入长寿证据，导致证据、风险和伦理边界混乱。

项目需要一套稳定规则：从先验追问出发，判断哪些条件是主体持续性成立的必要条件，并把这些条件映射为研究域。

## Decision

Create `docs/reference/research-domain-atlas.md` as the canonical map for research-domain generation.

Add domain skeletons for:

- `regenerative-medicine/`
- `cancer-control/`
- `immune-maintenance/`
- `neuro-continuity/`
- `biostasis-cryopreservation/`
- `cognitive-augmentation/`
- `risk-engineering/`
- `resource-social-infra/`
- `governance-rights/`
- `measurement-feedback/`

Each domain starts with only `README.md` and `AGENTS.md`. No empty data, scripts, services, or product folders are created.

## Alternatives Considered

- Keep all candidates inside `docs/reference/domain-map.md`: rejected because the map would become too dense and would not give each domain a local boundary.
- Create only one broad `effective-immortality/` domain: rejected because it would reproduce the old “one bucket explains everything” problem.
- Create data and script folders for every domain now: rejected because most domains do not yet have evidence pipelines or productized workflows.

## Consequences

- Research domains now follow a first-principles condition map instead of ad hoc topic expansion.
- New domains are visible and navigable but remain lightweight until real evidence work justifies more files.
- Existing domains keep their boundaries: `longevity-evidence/` remains the evidence ledger, while mechanism and infrastructure domains get their own ownership.

## Safety And Evidence Boundary

Domain creation does not imply any technology is proven, safe, clinically available, or capable of delivering effective immortality. High-risk domains must not include operational protocols, medical instructions, invasive procedures, harmful guidance, or individual predictions.
