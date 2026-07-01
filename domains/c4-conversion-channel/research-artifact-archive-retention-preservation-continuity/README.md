# Research Artifact Archive, Retention and Preservation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-artifact-archive-retention-preservation-continuity` |
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

This domain studies long-term preservation of research artifacts: papers, preprints, datasets, code, protocols, figures, supplementary files, notebooks, model cards, Web pages and provenance records.

Human Infra treats artifact preservation as memory infrastructure: research that cannot be retrieved, verified or migrated becomes unavailable to future subjects and future models.

## Human Infra Chain

```text
research produces many artifact types
  -> artifacts live across journals, repositories, code hosts, lab systems and Web pages
  -> archive, retention and migration practices preserve retrievability and context
  -> future reviewers can inspect original materials and compare later interpretations
  -> evidence remains usable across platform decay, file-format drift and link rot
  -> long-term learning capacity increases
```

## Non-Goals

- No archival of copyrighted, private, restricted, personal or confidential materials without permission.
- No bypass of repository access controls, publisher systems or data-use restrictions.
- No advice on preserving hazardous operational protocols or sensitive dual-use materials.
- No guarantee that preservation implies validity, permission or ethical reuse.

## Source Signals

- LOCKSS: https://www.lockss.org/
- CLOCKSS: https://clockss.org/
- Zenodo: https://zenodo.org/
- Software Heritage: https://www.softwareheritage.org/
- Internet Archive scholarly services: https://archive.org/services/

## Next Notes

- Map artifact classes and retention needs for Human Infra source cards and Web papers.
- Connect to long-term digital preservation, DOI metadata and research software archiving.
- Track link rot, format drift, access restrictions, copyright boundaries and preservation provenance.
