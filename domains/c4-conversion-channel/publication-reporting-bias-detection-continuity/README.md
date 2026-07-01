# Publication and Reporting Bias Detection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/publication-reporting-bias-detection-continuity` |
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

This domain studies publication bias, selective outcome reporting, small-study effects, missing studies, trial registry discrepancies, outcome switching and evidence suppression signals.

Human Infra treats reporting bias as a hidden evidence attrition layer: what is visible in journals may not represent what was actually studied.

## Human Infra Chain

```text
research is conducted
  -> only some protocols, outcomes and results become visible
  -> registries, protocols, reports and synthesis diagnostics reveal missing or shifted evidence
  -> apparent effects are downgraded when non-publication or selective reporting is plausible
  -> model claims avoid mistaking visibility for truth
  -> future decisions become less vulnerable to publication-system distortion
```

## Non-Goals

- No accusation of fraud, misconduct or intent without direct authoritative evidence.
- No strategy for hiding outcomes, evading registries, manipulating funnel plots or manufacturing negative/positive studies.
- No legal, journal, regulatory or institutional complaint service.
- No individual medical recommendation based on bias diagnostics.

## Source Signals

- Cochrane Handbook reporting bias chapters: https://training.cochrane.org/handbook/current
- ClinicalTrials.gov: https://clinicaltrials.gov/
- WHO ICTRP: https://trialsearch.who.int/
- COMPare Trials project: https://www.compare-trials.org/
- EQUATOR Network: https://www.equator-network.org/

## Next Notes

- Define fields for registry match, prespecified outcomes, reported outcomes, missing results, small-study signal and downgrade consequence.
- Connect to `clinical-trials-regulatory-science-translation/` and `preregistration-registered-report-study-plan-continuity/`.
- Track failure modes: registry absence, outcome switching, delayed publication, selective harms reporting and funnel-plot overinterpretation.
