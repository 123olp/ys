# Workers Compensation Occupational Injury Benefit Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/workers-compensation-occupational-injury-benefit-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


Workers Compensation Occupational Injury Benefit Continuity 关注工伤、职业病、伤害记录、雇主报告、医疗与工资替代给付、职业康复、争议处理和 OSHA 记录如何在工作伤害后维持主体恢复、收入和行动能力。

## 对象

- Work-related injury and illness records、workers compensation claims、medical benefits、wage replacement、return-to-work、vocational rehabilitation、appeals、OSHA logs 和职业病记录。
- 雇主、保险人、州工伤系统、联邦工伤项目、医疗机构、OSHA recordkeeping 和职业安全监管机构。
- 工作伤害、职业暴露、医疗照护、收入替代、残障、复工和长期功能结果之间的关系。

## Human Infra 价值

```text
主体可能在完成任务过程中受伤或患职业病
-> 工伤和职业病记录把工作造成的损害转化为医疗、工资替代和恢复支持
-> 报告缺失、记录错误、争议延迟、复工压力或职业病识别失败会把伤害转化为长期失能
-> 可记录、可核验、可申诉、可衔接康复的工伤系统降低工作风险对主体持续性的破坏
-> 主体在伤害后更可能保留收入、治疗、功能恢复和重返任务的机会
```

## 边界

- 本域不提供工伤索赔、医疗诊断、职业病认定、赔偿金额、复工许可、雇佣争议、法律、保险或个人案件建议。
- 不判断任何伤害是否构成工伤、责任归属、赔偿范围、诉讼策略、医学因果或劳动能力。
- 不帮助伪造伤害记录、隐瞒事故、规避报告、欺诈索赔、报复规避或操纵 OSHA / workers compensation 记录。
- 只整理公开记录机制、报告流程、福利类型、复工与康复衔接、职业安全数据、争议边界和伦理风险。

## 上游与下游

- 上游：`labor-rights-workplace-protection/`、`occupational-exposure-industrial-hygiene/`、`road-traffic-injury-prevention-safe-mobility/`、`insurance-risk-transfer/`。
- 下游：`rehabilitation-functioning/`、`disability-services-independent-living/`、`financial-resilience-access/`、`patient-advocacy-shared-decision-making/`。

## 初始资料线索

- U.S. Department of Labor Office of Workers' Compensation Programs resources.
- OSHA injury and illness recordkeeping resources.
- State workers compensation agency materials and occupational injury surveillance resources.
- Occupational injury, work disability prevention, return-to-work and workers compensation administration literature.
