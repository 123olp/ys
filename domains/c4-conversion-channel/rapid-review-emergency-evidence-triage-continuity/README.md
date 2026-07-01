# Rapid Review and Emergency Evidence Triage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/rapid-review-emergency-evidence-triage-continuity` |
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

This domain studies rapid reviews, evidence maps, crisis evidence triage, abbreviated review methods, uncertainty disclosure and time-constrained synthesis boundaries.

Human Infra treats rapid review as a constrained response mode: when decisions cannot wait for a full systematic review, shortcuts must be explicit, reversible and visible.

## Human Infra Chain

```text
urgent question appears
  -> full systematic review may be too slow
  -> rapid review defines which shortcuts are used
  -> uncertainty, omitted databases and screening limits are disclosed
  -> provisional claims remain separate from stable evidence
  -> Human Infra can act on weak signals without pretending they are settled facts
```

## Non-Goals

- No emergency medical advice, disaster command, public-health order, legal directive or crisis triage decision.
- No concealment of shortcuts, selective search, rushed certainty inflation or pressure to publish.
- No automated recommendation for individuals, institutions or governments.
- No replacement for official emergency, clinical, regulatory or public-health authorities.

## Source Signals

- Cochrane Rapid Reviews Methods Group: https://methods.cochrane.org/rapidreviews/
- WHO guideline development handbook: https://www.who.int/publications/i/item/9789241548960
- Campbell Collaboration evidence synthesis resources: https://www.campbellcollaboration.org/
- JBI evidence synthesis resources: https://jbi.global/

## Next Notes

- Define rapid-review-card fields: review type, shortcuts, omitted sources, screening depth, uncertainty level and expiry date.
- Connect to `living-evidence-surveillance-update-continuity/` for escalation from provisional triage to updated evidence.
- Track failure modes: speed laundering, missing harms, shortcut concealment, overconfident headline and failure to update.
