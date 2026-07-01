# 支付卡争议、错误交易与未授权扣款连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/payment-card-dispute-unauthorized-charge-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

本域研究信用卡、借记卡、电子资金转账、账单错误、未授权扣款、争议处理和错误解决机制如何影响主体资金访问、现金流和交易恢复。它关注支付系统纠错能力，而不是个案 chargeback、逃债、欺诈或金融法律建议。

## 研究对象

- 信用卡账单错误、未授权扣款、借记卡和电子资金转账错误、预付卡错误解决和交易争议。
- 争议时限、通知要求、临时贷记、调查、拒付、商家回应和记录保全。
- 支付记录、账单、收据、订单、物流、授权记录、账号安全和消费者投诉。
- 与银行账户访问、诈骗身份盗用、订阅账单、退款争议和预付储值余额的边界。

## 价值链路

```text
主体通过支付网络交换资源
  -> 账单、授权和错误解决机制决定资金异常后能否恢复
  -> 清晰争议流程和未授权扣款保护降低资金被锁定的持续损害
  -> 争议失败、时限错过、证据断裂或滥用风控会放大现金流风险
  -> 支付争议连续性把交易失败从不可逆损失转化为可审查的资金纠错机制
```

## 关键问题

- 信用卡、借记卡、EFT 和预付卡争议机制有什么不同的资金连续性后果？
- 未授权扣款、账单错误、未收到货和商家纠纷应如何区分？
- 支付争议如何与账号安全、身份盗用、订阅取消和消费者投诉连接？
- 过度拒付、滥用争议和商家风控会如何反向影响市场信任？

## 上游与下游

- 上游：`banking-deposit-account-access-continuity/`、`financial-inclusion-payment-systems/`、`contract-subscription-billing-consent-continuity/`、`digital-identity-security/`。
- 下游：`consumer-return-refund-dispute-resolution-continuity/`、`fraud-scams-consumer-protection/`、`gift-card-prepaid-stored-value-continuity/`、`credit-consumer-reporting-access-continuity/`。

## 非目标

- 不提供个案 chargeback、信用卡争议、借记卡争议、逃债、拒付策略、金融规划、诉讼或法律建议。
- 不判断某笔交易是否未授权、是否可争议、应由谁承担责任或争议胜率。
- 不协助虚假争议、退款套利、拒付滥用、洗钱、盗刷、规避 KYC、逃避债务或破坏商家支付系统。

## 初始资料入口

- CFPB: Credit card billing errors and charge disputes
- CFPB: Bank accounts and prepaid cards consumer materials
- FTC: Unauthorized charges and billing problem consumer materials
- Federal Reserve and official consumer financial protection materials
