# 0130 Add One-Hundred-Twenty-Fifth Wave Longevity Intervention Governance Domains

Date: 2026-07-01

Status: Accepted

## Context

Human Infra 已有 `longevity-evidence/`、`nutrition-metabolic-health/`、`physical-activity-mobility/`、`biological-age-clocks-biomarker-validation/`、`survival-analysis-healthspan-risk-modeling/` 和多个药品/医疗安全域，但“可执行长寿干预”仍缺少中间治理层。

抗衰药物再利用、补剂、抗阻训练、心肺适能、热量限制/禁食和冷热应激都经常被传播为“延寿方法”。这些对象确实可能影响主体持续性变量，例如炎症、代谢、肌力、VO2max、恢复能力、心血管风险和有效时间；但它们也带来证据错配、剂量/强度错误、离标签使用、补剂污染、营养不良、进食障碍、心血管事件、热伤害和冷暴露风险。

如果不拆出独立域，这些干预会被混入泛泛的“健康管理”或“长寿知识库”，导致 Human Infra 的预测模型把干预 T 直接写成寿命收益，而不是审查它通过什么变量、证据、概率门和风险扣减影响生命路径分布。

## Decision

新增第一百二十五波 6 个长寿干预执行与证据治理连续性域：

- `domains/geroprotective-drug-repurposing-trial-governance-continuity/`
- `domains/dietary-supplement-nutraceutical-evidence-safety-continuity/`
- `domains/resistance-training-muscle-strength-sarcopenia-continuity/`
- `domains/cardiorespiratory-fitness-vo2max-aerobic-capacity-continuity/`
- `domains/caloric-restriction-fasting-energy-balance-governance-continuity/`
- `domains/thermal-stress-sauna-cold-exposure-hormesis-governance-continuity/`

这些域只整理公开资料、证据等级、变量接口、终点、风险门槛、实施条件和禁止用途，不提供药物、补剂、训练、禁食、冷热暴露、测试、处方、购买、剂量、频率、个体医疗或运动建议。

## Consequences

- Human Infra 可以把长寿干预建模为 `T -> X -> S -> lambda(t) -> healthspan / effective time / future option value` 的审查链，而不是把干预名称当成神奇变量。
- `longevity-evidence/` 保持证据账本位置；新增域负责把常见干预拆成试验治理、标签安全、功能储备、能量平衡和高扰动风险这些可维护接口。
- 项目边界更严格：任何个体用药、补剂、训练、饮食、禁食、冷热暴露或医学/运动决策都必须留在禁止区。
