# Meta-Analysis, Effect Size and Heterogeneity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/meta-analysis-effect-size-heterogeneity-continuity` |
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

This domain studies effect-size extraction, synthesis models, heterogeneity, subgroup analysis, sensitivity analysis, prediction intervals and quantitative evidence synthesis.

Human Infra treats meta-analysis as a synthesis layer, not a certainty machine: pooled estimates can compress evidence, but they can also hide incompatible populations, methods and outcomes.

## Human Infra Chain

```text
multiple studies estimate related effects
  -> effect sizes require compatible outcomes, populations and time horizons
  -> synthesis model combines estimates with uncertainty and heterogeneity
  -> sensitivity analyses test robustness to assumptions and exclusions
  -> model inputs gain bounded aggregate estimates instead of isolated claims
  -> long-horizon projections avoid single-study overreach
```

## Non-Goals

- No statistical consulting for clinical decisions, investments, legal disputes or regulatory submissions.
- No cherry-picking models, forcing significant results, p-hacking or undisclosed exclusion.
- No claim that a pooled estimate overrides poor study quality, bad measurement or population mismatch.
- No individual medical prediction or treatment comparison.

## Source Signals

- Cochrane Handbook synthesis chapters: https://training.cochrane.org/handbook/current
- PRISMA 2020: https://www.prisma-statement.org/
- Cochrane Training resources: https://training.cochrane.org/
- Campbell Collaboration methods resources: https://www.campbellcollaboration.org/

## Next Notes

- Define fields for effect measure, transformation, fixed/random model, heterogeneity, prediction interval and sensitivity checks.
- Connect with `uncertainty-quantification-model-calibration/` for propagation into life-path models.
- Track failure modes: incompatible endpoints, duplicate cohorts, unexplained heterogeneity, subgroup fishing and publication bias ignored.
