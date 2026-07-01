# Living Evidence Surveillance and Update Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/living-evidence-surveillance-update-continuity` |
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

This domain studies living systematic reviews, surveillance searches, update triggers, evidence monitoring, versioned conclusions and stale-claim retirement.

Human Infra treats evidence as time-sensitive: a claim that was reasonable when written can become unsafe when new trials, harms, retractions or guidelines appear.

## Human Infra Chain

```text
claim is published
  -> new studies, registries, safety reports and retractions continue to appear
  -> surveillance rules decide when evidence must be revisited
  -> versioned conclusions separate old confidence from current confidence
  -> Human Infra pages can retire, downgrade or update claims
  -> long-horizon models avoid becoming fossilized around stale evidence
```

## Non-Goals

- No real-time medical alerting, clinical monitoring, trading signal, emergency recommendation or automated treatment change.
- No scraping restricted databases, redistributing copyrighted content or bypassing publisher access.
- No claim that a living review is always superior to a conventional review.
- No manipulation of update triggers to preserve preferred conclusions.

## Source Signals

- Cochrane living evidence resources: https://www.cochrane.org/
- Cochrane Handbook: https://training.cochrane.org/handbook
- Living systematic review methods literature: https://www.bmj.com/content/362/bmj.k2925
- Retraction Watch database: https://retractiondatabase.org/

## Next Notes

- Define update-card fields: surveillance interval, sources, trigger type, version, change type and claim consequence.
- Connect to `research-artifact-archive-retention-preservation-continuity/` for versioned Web papers.
- Track failure modes: stale search, silent conclusion drift, update fatigue, missed safety signal and retraction ignored.
