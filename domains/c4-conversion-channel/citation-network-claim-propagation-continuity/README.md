# Citation Network Claim Propagation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/citation-network-claim-propagation-continuity` |
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


`citation-network-claim-propagation-continuity/` 研究引用网络、主张传播、引用语境、二次引用和错误共识如何影响 Human Infra 的知识图谱。

> 核心问题：错误不是只出现在单篇论文；它会沿引用网络传播，形成看似稳固的共识、综述句式和政策叙事。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要从文献网络中抽取机制、变量、效应和边界
  -> 引用经常只传播结论标签，而丢失原始条件、反证和限制
  -> 错误引用和断章引用会形成伪共识
  -> 因此引用网络与主张传播连续性是知识图谱纠错门槛
```

## 关注对象

- Citation context、citation sentiment、claim extraction、reference lineage、citation cascade、secondary citation 和 consensus formation。
- 引用是否支持原文主张、是否误引、是否引用撤稿、是否从新闻稿/综述绕过原始研究。
- 与 `knowledge-graph-ontology-semantic-interoperability/` 的边界：知识图谱域关注语义结构；本域关注主张如何在引用网络中传播和变形。
- 与 `persistent-identifier-doi-citation-metadata-continuity/` 的边界：DOI 域关注对象解析；本域关注引用语境和主张链。

## Human Infra 模型链路

```text
引用网络与主张传播 T
  -> 改变 citation_context、claim_support、reference_lineage、misquotation_signal 变量 X
  -> 改变知识图谱、Source Card 和综述结论的可信状态 S
  -> 改变伪共识、错误机制归因、过度外推和撤稿后继续引用风险 λ(t)
  -> 影响模型变量、技术采用判断和主体持续性研究方向
```

## 非目标

- 不提供刷引用、操控引用网络、影响因子游戏、论文 SEO、引用农场或声誉攻击。
- 不把引用次数写成证据强度。
- 不抓取受限全文或绕过出版访问控制。

## Source Signals

- Crossref Cited-by: https://www.crossref.org/services/cited-by/
- Crossref Event Data: https://www.crossref.org/services/event-data/
- OpenAlex: https://openalex.org/
- scite citation statements: https://scite.ai/
- Retraction Watch Database: https://retractiondatabase.org/

## 下一步

- 给 Source Card 增加 `citation_context`、`claim_support_status`、`cites_retracted_work` 和 `lineage_depth` 字段。
- 在知识图谱中区分“被引用很多”与“被原文支持”。
