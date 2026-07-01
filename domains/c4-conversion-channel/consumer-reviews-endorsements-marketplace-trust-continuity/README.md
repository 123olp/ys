# 消费者评价、背书与市场信任连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/consumer-reviews-endorsements-marketplace-trust-continuity` |
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

本域研究在线评价、虚假评价、背书、网红披露、评价压制、推荐排名和市场信任如何影响主体选择质量、信息成本和交易风险。它关注评价与背书作为市场信任基础设施，而不是营销、刷评、声誉操控或个案评论建议。

## 研究对象

- 在线评价、评分、推荐、testimonials、endorsements、influencer disclosure、affiliate disclosure 和广告标识。
- 虚假评价、评价购买、评价压制、负评删除、平台排序、商家回应和声誉系统。
- 消费者认知成本、市场信任、证据质量、利益冲突和信息完整性。
- 与信息完整性、平台账号治理、诈骗消费者保护、产品安全和价格披露的边界。

## 价值链路

```text
主体需要在有限时间内选择交易对象
  -> 评价、背书和推荐系统压缩搜索成本并塑造信任
  -> 真实披露、反虚假评价和可审查声誉降低选择错误
  -> 刷评、隐性广告、评价压制和推荐操控会污染决策输入
  -> 市场信任连续性把交易选择从噪声判断转化为可审查的信息基础设施
```

## 关键问题

- 虚假评价、隐性背书和评价压制如何改变主体的搜索成本与风险判断？
- 利益披露、广告标识和平台审核如何影响市场信任？
- 评价系统如何与产品安全、诈骗识别、价格披露和平台治理连接？
- 评价可信度下降会如何提高弱势消费者、时间贫困者和高风险采购者的任务成本？

## 上游与下游

- 上游：`information-integrity-trust/`、`online-safety-digital-harm-prevention/`、`consumer-return-refund-dispute-resolution-continuity/`、`product-safety-recall-systems/`。
- 下游：`fraud-scams-consumer-protection/`、`price-fee-disclosure-junk-fee-continuity/`、`online-retail-order-shipping-fulfillment-continuity/`、`platform-account-suspension-appeals-continuity/`。

## 非目标

- 不提供营销策略、刷评、删评、声誉操控、竞品攻击、评论模板、网红投放、爬取个人评价或个案平台申诉建议。
- 不判断某条评论是否违法、某个背书是否合规、某个平台排序是否公平或某个商家是否可信。
- 不协助制造虚假评价、评价轰炸、操纵评分、隐藏利益关系、骚扰评论者或规避平台审核。

## 初始资料入口

- FTC: Endorsement Guides
- FTC: Consumer Reviews and Testimonials Rule
- FTC: Business guidance on advertising and endorsements
- Platform transparency reports and official marketplace trust materials as contextual sources
