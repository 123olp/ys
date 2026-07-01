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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
