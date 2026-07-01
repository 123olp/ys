# Journal Editorial Policy Peer Review Integrity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/journal-editorial-policy-peer-review-integrity-continuity` |
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

`journal-editorial-policy-peer-review-integrity-continuity/` 研究期刊编辑政策、同行评审完整性、审稿透明度、编辑纠错和出版伦理如何影响证据进入 Human Infra。

> 核心问题：同行评审不是二元开关；审稿模式、编辑政策、数据可得性、利益冲突和纠错程序会改变论文可用性。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要把论文状态转化为可审查证据等级
  -> 期刊编辑政策和同行评审流程决定论文是否经过最低质量控制
  -> 审稿失灵、编辑冲突和政策缺位会让错误结论获得权威外观
  -> 因此期刊编辑政策与同行评审完整性是证据权威性的制度门槛
```

## 关注对象

- Editorial policy、peer review model、review transparency、data availability policy、conflict policy、correction policy 和 appeals process。
- Open peer review、registered reports、reviewer identity protection、editorial independence 和 publication ethics。
- 与 `preregistration-registered-report-study-plan-continuity/` 的边界：预注册域关注研究计划；本域关注期刊和审稿制度。
- 与 `risk-of-bias-critical-appraisal-continuity/` 的边界：偏倚域评价研究本身；本域评价出版和审稿管道。

## Human Infra 模型链路

```text
期刊编辑与同行评审完整性 T
  -> 改变 editorial_policy、review_model、transparency、data_policy、correction_capacity 变量 X
  -> 改变论文证据等级、可信传播状态和复核优先级 S
  -> 改变权威外观误导、审稿失灵、数据不可查和结论过度使用风险 λ(t)
  -> 影响系统综述、模型输入和主体持续性路径判断
```

## 非目标

- 不提供伪造审稿、推荐审稿人操控、投稿策略、审稿规避、编辑申诉代写或期刊排名服务。
- 不把期刊影响因子当作质量替代指标。
- 不公开非公开审稿意见、编辑系统记录或审稿人身份。

## Source Signals

- COPE Core Practices: https://publicationethics.org/core-practices
- ICMJE Recommendations: https://www.icmje.org/recommendations/
- EQUATOR Network: https://www.equator-network.org/
- Open Peer Review taxonomy, F1000Research: https://f1000research.com/articles/6-588
- Registered Reports, Center for Open Science: https://www.cos.io/initiatives/registered-reports

## 下一步

- 为 Source Card 增加 `peer_review_model`、`editorial_policy_signal`、`data_availability_policy` 和 `correction_policy_signal` 字段。
- 与预注册、风险偏倚、利益冲突和撤稿状态域建立复核链。
