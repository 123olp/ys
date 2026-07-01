# 0022. Add Eighteenth-Wave Lab, Blood, Waste, Radiation, Chemical And Critical Materials Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已经覆盖生物维护、服务连续性、公共卫生、应急、制造、采购、One Health、算力和供应链。但继续做先验追问后，仍有一组基础条件没有独立归属：

- 风险需要被实验室和诊断系统确认。
- 血液、器官、组织等外部生物材料需要安全供应、追踪和警戒。
- 废弃物和危险材料需要被处理，避免生活系统反向制造暴露。
- 辐射与核风险需要监测、防护和应急治理。
- 化学暴露和中毒风险需要毒理、毒物中心和化学安全体系。
- AI、能源、医疗设备、制造和通信需要关键矿物与材料输入。

这些方向不能只放进 `immunization-public-health-surveillance/`、`blood-oxygen-hemostasis/`、`water-sanitation-hygiene-continuity/`、`risk-engineering/`、`substance-exposure-control/` 或 `supply-chain-continuity/`，因为它们各自有独立机制、来源体系、失败模式和禁止用途边界。

## Decision

新增第十八波 6 个研究域骨架：

- `domains/c4-conversion-channel/public-health-laboratory-diagnostic-capacity/`
- `domains/c2-source-maintenance/blood-organ-tissue-biovigilance-transplantation/`
- `domains/c6-local-unlocking/waste-management-hazardous-materials-continuity/`
- `domains/c2-source-maintenance/radiation-nuclear-safety-protection/`
- `domains/c6-local-unlocking/chemical-safety-poison-control-toxicology/`
- `domains/c5-ecological-substrate/critical-minerals-materials-resilience/`

每个域只创建 `README.md` 与 `AGENTS.md`，作为长期研究容器和边界说明，不新增数据、脚本、模型或操作协议。

## Consequences

- Research Domain Atlas 和 Domain Map 能把“风险确认、生物材料供应、残余物治理、不可见高能风险、化学暴露、关键材料输入”纳入主体持续性成立条件。
- 伦理边界需要新增实验室诊断、人体材料、废弃物、辐射核安全、化学毒理和关键材料的禁止用途。
- 仓库检查脚本需要把 6 个域和本 ADR 纳入 required files / dirs。

## Non-Goals

- 不提供实验室样本、检测、病原体、化学品、危险废物、放射源、核材料、人体材料或关键矿物的操作步骤。
- 不提供个体诊断、治疗、移植、输血、中毒处理、辐射事故处置、采购、投资或监管规避建议。
- 不把这些高风险域写成个人可执行方案。
