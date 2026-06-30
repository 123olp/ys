# ADR 0069: Add Sixty-Fifth-Wave Companion Service Animal Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经有 `animal-health-zoonotic-interface-one-health`，用于承载动物健康、人兽共患风险、食品动物、野生动物和 One Health 公共卫生界面。但主体持续性还需要另一层更贴近家庭和行动系统的动物域：伴侣动物、服务动物、宠物身份、兽医可及、食药供应、灾害撤离、收容再安置和动物福利报告。

这些对象不能只归入 One Health。One Health 关注动物-人类-环境界面的上游公共卫生风险；本波关注动物如何直接进入人的关系支持、残障辅助、家庭日常、灾害准备、经济压力、动物福利和服务断点。

## Decision

新增第 65 波 8 个伴侣动物、服务动物与宠物照护连续性域：

- `human-animal-bond-companion-care-continuity`
- `veterinary-care-access-cost-continuity`
- `service-animal-disability-access-continuity`
- `pet-identification-microchip-reunification-continuity`
- `pet-food-medication-supply-safety-continuity`
- `pet-disaster-evacuation-sheltering-continuity`
- `animal-shelter-rescue-rehoming-continuity`
- `animal-welfare-cruelty-reporting-continuity`

## Consequences

- Human Infra 能把动物从单一公共卫生风险对象，扩展为关系支持、辅助技术、家庭运行、灾害撤离和福利保护中的真实主体持续性变量。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明；不提供动物诊疗、训练、购买、领养、繁育、救助行动、法律策略、实时灾害指挥、举报取证或个案动物福利处理。
- 后续若新增 NIH、AVMA、CDC、ADA.gov、FDA、FEMA/Ready.gov、USDA APHIS、地方动物控制或动物福利资料，应先进入对应细分域；只有动物-人类-环境上游公共卫生风险才回到 `animal-health-zoonotic-interface-one-health`。
