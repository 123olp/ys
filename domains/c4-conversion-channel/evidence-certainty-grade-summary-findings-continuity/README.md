# Evidence Certainty, GRADE and Summary of Findings Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/evidence-certainty-grade-summary-findings-continuity` |
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

This domain studies evidence certainty, GRADE judgments, summary-of-findings tables, outcome importance, certainty downgrading/upgrading and recommendation strength prerequisites.

Human Infra treats evidence certainty as the gate between evidence synthesis and model claims: a large effect estimate is not enough if certainty is low.

## Human Infra Chain

```text
synthesis produces outcome estimates
  -> certainty depends on risk of bias, inconsistency, indirectness, imprecision and reporting bias
  -> GRADE-style judgments summarize how much confidence a claim deserves
  -> Human Infra model inputs receive strength labels and downgrade reasons
  -> speculative claims stay separate from high-confidence interventions
  -> subject-continuity planning avoids false precision
```

## Non-Goals

- No treatment recommendation, clinical guideline writing, insurance coverage decision or legal-standard claim.
- No conversion of low-certainty evidence into strong public claims.
- No hiding downgrade reasons, manipulating outcome importance or overstating certainty.
- No individual risk prediction, diagnosis or therapy ranking.

## Source Signals

- GRADE Handbook: https://gdt.gradepro.org/app/handbook/handbook.html
- GRADE Working Group: https://www.gradeworkinggroup.org/
- GRADEpro: https://www.gradepro.org/
- Cochrane Handbook: https://training.cochrane.org/handbook

## Next Notes

- Define source-card fields for certainty, downgrade domains, outcome importance and summary-of-findings link.
- Connect with `risk-of-bias-critical-appraisal-continuity/` and `meta-analysis-effect-size-heterogeneity-continuity/`.
- Track failure modes: certainty-label inflation, indirect population mismatch, imprecision ignored and outcome importance drift.
