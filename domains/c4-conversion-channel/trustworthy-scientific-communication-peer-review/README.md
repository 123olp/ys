# Trustworthy Scientific Communication Peer Review

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/trustworthy-scientific-communication-peer-review` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
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

`trustworthy-scientific-communication-peer-review/` 研究同行评审、预印本、期刊编辑、撤稿、勘误、引用语境、利益冲突和科研传播，如何影响 Human Infra 对证据的理解、传播和纠错能力。

> 核心问题：未来技术不会只通过实验室出现，也会通过论文、预印本、新闻稿、推文、公司披露和综述进入公共叙事。若传播链不能区分“假说、证据、审查状态和撤回信号”，主体持续性研究会被错误信号牵引。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要持续识别哪些技术窗口真实可用
  -> 技术窗口通过论文、预印本、同行评审、媒体和社区传播进入判断系统
  -> 传播链中的夸大、撤稿、引用断章、利益冲突和选择性报道会污染证据状态
  -> 因此可信科研传播与同行评审是证据进入 Human Infra 的语义过滤域
```

## 关注对象

- 同行评审、编辑标准、作者责任、利益冲突、勘误、表达关注、撤稿和出版伦理。
- 预印本、期刊论文、新闻稿、公司公告、综述、媒体传播和社交平台二次传播。
- 引用语境、主张边界、证据状态、版本状态、撤回信号和二次引用偏差。
- 与 `research-infrastructure-open-science-translation/` 的边界：开放科学域关注研究生态和开放转化；本域关注研究结果进入公共认知时的传播、审查和纠错链。
- 与 `source-card-system` 的关系：本域为 Source Card 增加 publication status、review status、retraction status、claim scope 和 conflict note 字段。

## Human Infra 模型链路

```text
可信科研传播与同行评审 T
  -> 改变审查状态、引用语境、撤稿信号、利益冲突披露和公众理解变量 X
  -> 改变证据进入模型、README、论文页和传播材料的可信状态 S
  -> 改变错误技术采用、虚假确定性、过度传播和证据污染风险 λ(t)
  -> 影响研究组合优先级、公众理解、技术采用判断和主体持续性路径选择
```

## 非目标

- 不提供论文代写、伪造审稿、操控引用、规避撤稿、洗白学术不端或刷影响力策略。
- 不把预印本、新闻稿、单一公司披露或媒体报道写成已验证结论。
- 不把同行评审状态写成绝对真理，也不把未评审状态写成必然错误。

## Source Signals

- ICMJE Recommendations: https://www.icmje.org/recommendations/
- COPE Core Practices: https://publicationethics.org/core-practices
- Retraction Watch: https://retractionwatch.com/
- National Academies Reproducibility and Replicability in Science: https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science
- Crossref Crossmark: https://www.crossref.org/services/crossmark/

## 下一步

- 给 Source Card 增加 publication status、peer review status、correction/retraction status、conflict disclosure 和 citation context 字段。
- 与 `model-cards-ai-audit-documentation/`、`research-portfolio-prioritization-funding-governance/` 和 `technology-foresight-horizon-scanning/` 建立审查接口。
