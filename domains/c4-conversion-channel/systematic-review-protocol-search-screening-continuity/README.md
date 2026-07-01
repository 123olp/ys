# Systematic Review Protocol, Search and Screening Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/systematic-review-protocol-search-screening-continuity` |
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

This domain studies systematic review protocols, eligibility criteria, database search strategies, deduplication, screening workflows, PRISMA flow reporting and review registration.

Human Infra treats systematic review infrastructure as an evidence intake layer: if search and screening are not transparent, the model only sees a selected fragment of the literature.

## Human Infra Chain

```text
model depends on literature claims
  -> literature claims depend on complete and reproducible search
  -> protocols define population, intervention, comparator, outcomes and eligibility
  -> screening records show why studies entered or left the evidence set
  -> evidence gaps and selection boundaries become visible
  -> life-path claims can be downgraded before they become false certainty
```

## Non-Goals

- No ghostwriting, paper mill support, fake screening, fabricated PRISMA diagrams or review registration manipulation.
- No medical recommendation, treatment ranking, diagnosis, trial enrollment advice or personal life-extension conclusion.
- No database access circumvention, copyrighted full-text redistribution or scraping restricted sources.
- No claim that a systematic review protocol alone proves an intervention works.

## Source Signals

- PRISMA 2020: https://www.prisma-statement.org/
- PROSPERO: https://www.crd.york.ac.uk/prospero/
- Cochrane Handbook: https://training.cochrane.org/handbook
- EQUATOR Network: https://www.equator-network.org/

## Next Notes

- Define a source-card field for search date, databases, strings, eligibility criteria, screening counts and exclusions.
- Connect this domain to `preregistration-registered-report-study-plan-continuity/` without treating review registration as proof of quality.
- Track failure modes: selective database choice, outdated search, vague exclusion, duplicate records and unreconciled screening conflicts.
