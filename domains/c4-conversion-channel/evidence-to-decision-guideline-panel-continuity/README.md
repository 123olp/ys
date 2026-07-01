# Evidence-to-Decision and Guideline Panel Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/evidence-to-decision-guideline-panel-continuity` |
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


## Scope

This domain studies evidence-to-decision frameworks, guideline panels, recommendation strength, values and preferences, resource use, equity, acceptability, feasibility and implementation prerequisites.

Human Infra treats evidence-to-decision as the bridge from "what evidence suggests" to "what a system may responsibly recommend or adopt."

## Human Infra Chain

```text
evidence certainty is summarized
  -> decisions require values, harms, benefits, resources, equity, acceptability and feasibility
  -> guideline panels document judgments and recommendation strength
  -> Human Infra separates evidence facts from adoption decisions
  -> interventions are evaluated as system choices, not magic variables
  -> future-option models preserve ethical and resource constraints
```

## Non-Goals

- No clinical guideline authoring service, treatment advice, insurance coverage advice, legal compliance opinion or policy lobbying.
- No claim that a panel recommendation applies to an individual person.
- No manipulation of panel composition, conflicts, voting, patient representation or recommendation wording.
- No replacement for official public-health, clinical, regulatory or payer decision processes.

## Source Signals

- GRADE Evidence to Decision frameworks: https://www.gradeworkinggroup.org/
- WHO handbook for guideline development: https://www.who.int/publications/i/item/9789241548960
- NICE health technology evaluations manual: https://www.nice.org.uk/process/pmg36
- Guidelines International Network: https://g-i-n.net/

## Next Notes

- Define decision-card fields: benefits, harms, certainty, values, resources, equity, acceptability, feasibility and recommendation strength.
- Connect to `health-economics-value-assessment/` without reducing subject value to cost alone.
- Track failure modes: evidence-to-recommendation leap, conflict dominance, equity omission, feasibility fantasy and population mismatch.
