# Citation Network Claim Propagation Continuity

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
