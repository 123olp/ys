# Scholarly Identity, ORCID and Affiliation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/scholarly-identity-orcid-affiliation-continuity` |
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

This domain studies how researchers, contributors, labs and institutions remain identifiable across publications, datasets, code, grants, reviews, employment changes and long-lived research programs.

Human Infra treats scholarly identity continuity as a research infrastructure condition: if people cannot be reliably linked to their work, then credit, accountability, collaboration, reproducibility and long-term knowledge accumulation degrade.

## Human Infra Chain

```text
subject creates research work
  -> work requires durable attribution and institutional context
  -> identifiers such as ORCID and ROR reduce name ambiguity and affiliation drift
  -> credit, review, funding, provenance and collaboration become linkable
  -> research memory survives job changes, name changes, platform changes and archive migration
  -> subject capacity for cumulative inquiry and future collaboration increases
```

## Non-Goals

- No academic career advice, hiring advice or grant strategy.
- No identity fabrication, affiliation misrepresentation or authorship padding.
- No scraping of private researcher profiles, personnel records or grant records.
- No claim that identifiers alone prove authorship, responsibility, research quality or integrity.

## Source Signals

- ORCID researcher identifiers: https://orcid.org/
- Research Organization Registry: https://ror.org/
- Crossref metadata and contributor identifiers: https://www.crossref.org/
- DataCite metadata and contributor identifiers: https://datacite.org/

## Next Notes

- Build source cards for ORCID, ROR, Crossref and DataCite metadata fields.
- Map name change, affiliation change and contributor disambiguation failure modes.
- Link this domain to contributor roles, persistent identifiers and research data repositories.
