# 0035. Add Thirty-First-Wave Knowledge Governance And Technology Diffusion Domains

Date: 2026-06-30

## Status

Accepted.

## Context

Human Infra 已经补齐生物医学平台、定量方法学、社会基础设施、生命线服务和未来等待路径。下一层缺口不再是单个生理系统或单项公共服务，而是这些研究域如何被可信组织、隐私保护、文档审计、未来预警、组合排序和制度扩散。

若没有隐私保护计算，主体数据越多，隐私和权利暴露越大。若没有知识图谱和本体，研究域会变成不可查询的文档堆。若没有模型卡和审计文档，预测模型和图表会被误读为权威结论。若没有地平线扫描，未来技术窗口只能被新闻热度驱动。若没有研究组合治理，项目会在无限候选域中失焦。若没有知识产权和技术转移视角，技术成熟也不等于主体可获得。

这些能力不能仅归入 `health-data-privacy-governance/`、`research-infrastructure-open-science-translation/`、`standards-metrology-quality-infrastructure/` 或 `information-integrity-trust/`。它们各自具有独立机制、证据体系、失败模式和维护边界。

## Decision

Add six formal knowledge-governance and technology-diffusion domains:

- `domains/privacy-preserving-computation-federated-learning/`
- `domains/knowledge-graph-ontology-semantic-interoperability/`
- `domains/model-cards-ai-audit-documentation/`
- `domains/technology-foresight-horizon-scanning/`
- `domains/research-portfolio-prioritization-funding-governance/`
- `domains/intellectual-property-technology-transfer-access/`

Update root navigation, docs navigation, reference maps, radar, ethics boundaries, changelog and repository checks so the new domains are discoverable and validated.

## Consequences

- Human Infra now has a knowledge-governance layer between raw research domains and public-facing models.
- Sensitive data can be discussed through privacy-preserving computation instead of simple centralization.
- Domain knowledge can move toward machine-readable ontology and graph structures.
- Models, charts and AI-assisted research outputs have a formal documentation and audit domain.
- Future technology signals can be handled as horizon-scanning objects instead of hype.
- Research attention can be allocated through portfolio governance.
- Technology maturity can be separated from real access, licensing, production and affordability.

## Non-Goals

- No data re-identification, privacy attack, cryptographic implementation guidance or production security parameter advice.
- No clinical coding service, insurance coding, diagnosis mapping, or licensed terminology redistribution.
- No model certification, marketing claim, individual lifespan prediction, automated eligibility decision or medical decision support.
- No investment advice, market timing, company rating, lobbying, grant manipulation or patent/legal advice.
- No claim that these governance layers prove any technology is safe, effective, available or affordable.
