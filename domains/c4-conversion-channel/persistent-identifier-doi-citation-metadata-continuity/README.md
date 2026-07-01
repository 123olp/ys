# Persistent Identifier, DOI and Citation Metadata Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/persistent-identifier-doi-citation-metadata-continuity` |
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

This domain studies persistent identifiers, DOI metadata, citation graphs, versioned scholarly objects and long-term reference stability.

Human Infra treats persistent identifiers as a memory substrate: if research objects cannot be found, cited, versioned and resolved over time, then evidence chains decay and future reasoning loses its anchors.

## Human Infra Chain

```text
research object is produced
  -> object needs stable identity beyond a file path or platform URL
  -> DOI and metadata registries preserve resolvable reference points
  -> citation, attribution, reuse, correction and replication become traceable
  -> knowledge remains inspectable across time, systems and institutions
  -> subject-level learning and project memory can compound
```

## Non-Goals

- No citation gaming, fake DOI creation, paper mill support or metric manipulation.
- No advice on evading publisher policies or access controls.
- No claim that a DOI proves quality, peer review, correctness or legal reuse rights.
- No collection of private manuscript, reviewer or editorial system records.

## Source Signals

- DOI Foundation: https://www.doi.org/
- Crossref: https://www.crossref.org/
- DataCite: https://datacite.org/
- Crossref metadata best practices: https://www.crossref.org/documentation/

## Next Notes

- Compare DOI, Handle, ARK, accession number and repository-local identifiers.
- Track failure modes: broken landing pages, version ambiguity, retractions, corrections and metadata drift.
- Link this domain to source cards, research data repositories and software citation.
