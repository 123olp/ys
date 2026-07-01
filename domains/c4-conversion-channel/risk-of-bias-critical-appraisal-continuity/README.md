# Risk of Bias and Critical Appraisal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/risk-of-bias-critical-appraisal-continuity` |
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

This domain studies study-level risk of bias, critical appraisal tools, applicability judgments and domain-specific quality assessment for randomized, non-randomized, diagnostic, prognostic and qualitative evidence.

Human Infra treats risk of bias as a claim downgrade mechanism: a study can be relevant and still be unsafe to use as a strong causal or predictive claim.

## Human Infra Chain

```text
study enters evidence set
  -> study design creates possible bias channels
  -> appraisal separates randomization, confounding, selection, measurement, missingness and reporting risks
  -> claim strength is downgraded or blocked before model ingestion
  -> interventions are not promoted because of weak, biased or inapplicable evidence
  -> subject-continuity decisions remain evidence-bounded
```

## Non-Goals

- No accusation that authors committed misconduct merely because a risk-of-bias domain is high.
- No legal, clinical, regulatory or journal-review service.
- No p-hacking, selective reporting, data fabrication, reanalysis manipulation or study discrediting strategy.
- No use of appraisal scores as automatic truth, fraud or treatment recommendations.

## Source Signals

- Cochrane RoB 2: https://methods.cochrane.org/risk-bias-2
- ROBINS-I: https://methods.cochrane.org/methods-cochrane/robins-i-tool
- QUADAS-2: https://www.bristol.ac.uk/population-health-sciences/projects/quadas/quadas-2/
- PROBAST: https://www.probast.org/
- CASP checklists: https://casp-uk.net/casp-tools-checklists/

## Next Notes

- Define risk-of-bias fields for source cards: tool, domain, judgment, rationale, applicability and model consequence.
- Connect randomized and non-randomized appraisal to `causal-inference-target-trial-emulation/`.
- Track failure modes: total-score misuse, tool mismatch, vague rationale, conflict of interest ignored and overgeneralized applicability.
