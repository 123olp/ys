# Research Misconduct Investigation Correction Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-misconduct-investigation-correction-continuity` |
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


`research-misconduct-investigation-correction-continuity/` 研究科研不端定义、调查、机构责任、资助方责任、纠错路径和记录状态如何影响 Human Infra 的证据可信度。

> 核心问题：主体持续性模型依赖长期证据积累；如果伪造、篡改、剽窃、调查状态和纠错结论不能被区分，模型会把污染证据当成未来技术窗口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把研究结论转化为可审查证据
  -> 研究结论可能受到 fabrication、falsification、plagiarism、调查程序和机构纠错影响
  -> 证据系统必须区分怀疑、调查、机构结论、期刊更正和正式撤稿
  -> 因此科研不端调查与纠错连续性是证据进入模型前的完整性门槛
```

## 关注对象

- 科研不端定义、调查管辖、机构程序、资助方要求、调查结论和公开纠错。
- fabrication、falsification、plagiarism、questionable research practices、authorship dispute 和 data availability failure 的边界。
- 研究机构、资助方、期刊、出版商、数据仓库、预印本平台和公众记录之间的纠错链。
- 与 `trustworthy-scientific-communication-peer-review/` 的边界：可信传播域关注审查和传播状态；本域关注不端指控、调查和纠错状态的制度化处理。
- 与 `retraction-expression-concern-correction-continuity/` 的边界：撤稿域关注出版物状态；本域关注调查和责任链。

## Human Infra 模型链路

```text
科研不端调查与纠错 T
  -> 改变研究完整性状态、调查状态、纠错状态、数据可信度和引用可用性变量 X
  -> 改变证据卡片、系统综述、模型输入和传播材料的可信状态 S
  -> 改变错误技术采用、污染证据累积、错误共识和资源错配风险 λ(t)
  -> 影响技术窗口判断、研究组合优先级和主体持续性路径选择
```

## 非目标

- 不提供不端指控代写、举报策略、法律意见、调查规避、数据清洗伪造、论文洗稿或责任规避方法。
- 不基于高偏倚、撤稿、利益冲突或统计异常自动断定作者故意不端。
- 不公开个人敏感信息、未公开调查材料、审稿记录或机构内部记录。

## Source Signals

- U.S. Office of Research Integrity: https://ori.hhs.gov/
- ORI research misconduct definition: https://ori.hhs.gov/definition-research-misconduct
- National Academies, Fostering Integrity in Research: https://nap.nationalacademies.org/catalog/21896/fostering-integrity-in-research
- COPE Core Practices: https://publicationethics.org/core-practices
- ICMJE Recommendations: https://www.icmje.org/recommendations/

## 下一步

- 给 Source Card 增加 `integrity_status`、`investigation_status`、`institutional_finding`、`publisher_action` 和 `correction_path` 字段。
- 与撤稿状态、风险偏倚、利益冲突和活证据更新域建立交叉引用。
