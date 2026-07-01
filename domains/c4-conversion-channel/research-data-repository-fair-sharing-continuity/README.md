# Research Data Repository and FAIR Sharing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-data-repository-fair-sharing-continuity` |
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

This domain studies research data repositories, FAIR principles, metadata, data management plans, access levels, retention, reuse conditions and repository selection.

Human Infra treats research data continuity as a condition for quantitative modeling: without findable, accessible, interoperable and reusable data, lifespan, healthspan, risk and intervention models cannot be audited or improved.

## Human Infra Chain

```text
research produces data
  -> data requires metadata, repository placement, access rules and preservation
  -> FAIR practices make data findable, accessible, interoperable and reusable
  -> models and claims can be rechecked, pooled, compared and updated
  -> evidence becomes cumulative instead of disappearing into local files
  -> subject-continuity modeling gains stronger empirical substrate
```

## Non-Goals

- No dataset scraping, re-identification, unauthorized access or privacy bypass.
- No claim that public data is automatically ethical, complete, unbiased or reusable.
- No advice on evading consent, IRB, data use agreements or repository restrictions.
- No storage of protected health information, human-subject raw data or private participant records in this repo.

## Source Signals

- FAIR Principles / GO FAIR: https://www.go-fair.org/fair-principles/
- NIH Data Management and Sharing Policy: https://sharing.nih.gov/data-management-and-sharing-policy
- NIH selecting a data repository: https://sharing.nih.gov/data-management-and-sharing-policy/sharing-scientific-data/selecting-a-data-repository
- DataCite: https://datacite.org/

## Next Notes

- Build repository evaluation cards: metadata, access, licensing, embargo, retention, privacy and versioning.
- Link to source-card templates and quantitative model evidence contracts.
- Keep human-subject data governance separate from generic open data enthusiasm.
