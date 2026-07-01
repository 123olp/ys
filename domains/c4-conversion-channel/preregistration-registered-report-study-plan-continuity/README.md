# Preregistration, Registered Report and Study Plan Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/preregistration-registered-report-study-plan-continuity` |
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

This domain studies preregistration, registered reports, analysis plans, protocol transparency, deviation tracking and study-plan continuity.

Human Infra treats preregistration as an anti-retrofitting mechanism: it preserves what a study meant to test before results were known, making evidence less vulnerable to hindsight rewriting.

## Human Infra Chain

```text
study asks a question
  -> methods and analysis decisions can drift after results appear
  -> preregistration records the planned question, design and analysis before outcome inspection
  -> deviations and exploratory analyses can be separated from confirmatory claims
  -> evidence enters the model with clearer uncertainty and bias boundaries
  -> long-term decision systems become less dependent on narrative strength
```

## Non-Goals

- No claim that preregistration guarantees quality, ethics, replication or correct analysis.
- No guidance for gaming preregistration, selective reporting or p-hacking concealment.
- No clinical, legal or regulatory advice on trial registration obligations.
- No storage of private protocols, unpublished data or confidential review material.

## Source Signals

- Center for Open Science preregistration: https://www.cos.io/initiatives/prereg
- OSF Registries: https://osf.io/registries
- Registered Reports overview: https://www.cos.io/initiatives/registered-reports
- ClinicalTrials.gov: https://clinicaltrials.gov/

## Next Notes

- Build a study-plan card that separates confirmatory, exploratory and post hoc claims.
- Connect to target trial emulation, survival analysis and intervention evidence review.
- Track deviation disclosure, timestamp integrity and protocol versioning.
