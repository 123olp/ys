# Guideline Appraisal, Adaptation and Localization Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/guideline-appraisal-adaptation-localization-continuity` |
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

This domain studies guideline quality appraisal, adaptation, localization, contextual fit, update status, conflict handling and implementation transfer boundaries.

Human Infra treats guidelines as contextual artifacts: a guideline can be high quality in one setting and still be misapplied in another.

## Human Infra Chain

```text
guideline exists
  -> quality, currency, scope and conflicts must be appraised
  -> local context changes resources, population, regulation, equity and feasibility
  -> adaptation documents what transfers and what must be modified
  -> Human Infra can use guidelines as bounded evidence, not universal commands
  -> model and narrative outputs avoid context-blind authority transfer
```

## Non-Goals

- No clinical implementation plan, local policy mandate, medical advice or legal compliance assessment.
- No endorsement that a guideline is valid, current or applicable to a user.
- No adaptation used to bypass regulation, professional standards, patient consent or resource constraints.
- No manipulation of guideline appraisal scores or conflict disclosure.

## Source Signals

- AGREE Enterprise / AGREE II: https://www.agreetrust.org/
- GRADE-ADOLOPMENT resources: https://www.gradeworkinggroup.org/
- Guidelines International Network: https://g-i-n.net/
- WHO handbook for guideline development: https://www.who.int/publications/i/item/9789241548960

## Next Notes

- Define guideline-card fields: source, date, scope, population, recommendation strength, update status, appraisal result and localization limits.
- Connect to `evidence-to-decision-guideline-panel-continuity/`.
- Track failure modes: stale guideline, context mismatch, resource assumption mismatch, conflict omission and recommendation overreach.
