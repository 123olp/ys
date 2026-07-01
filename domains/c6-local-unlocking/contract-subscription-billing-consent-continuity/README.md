# 合同、订阅、账单与持续同意连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/contract-subscription-billing-consent-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

本域研究合同、服务条款、订阅、自动续费、账单、取消、争议和持续同意如何影响主体时间、金钱和注意力预算。它关注的是交易关系如何长期消耗或支撑主体资源，而不是个人合同、消费、退款或法律建议。

## 研究对象

- 合同、服务条款、订阅、自动续费、trial、negative option 和取消机制。
- 账单、自动扣款、费用通知、价格变更、服务中断、争议和退款机制。
- 持续同意、授权撤回、用户可理解性、暗黑模式和行政摩擦。
- 合同记录与银行账户、信用报告、住房、公用事业、通信、医疗、保险和数字服务的关系。

## 价值链路

```text
主体需要把交易关系保持在可理解、可控制、可退出状态
  -> 合同、订阅和账单把服务接入、资金流和持续同意绑定在一起
  -> 清晰通知、可取消性、争议机制和账单记录降低持续资源泄漏
  -> 隐性续费、暗黑模式、账单错误、取消摩擦或同意失效会吞噬时间和资金
  -> 合同账单连续性把交易关系从被动消耗转化为可审查的资源编排
```

## 关键问题

- 订阅和账单摩擦如何通过小额高频消耗改变长期资源预算？
- 持续同意、价格变更、取消入口和通知可理解性如何影响主体控制权？
- 银行账户、信用报告、合同记录和消费者投诉如何共同构成交易纠错系统？
- 哪些服务合同是主体持续性关键入口，如通信、公用事业、保险、医疗、云服务和教育平台？

## 上游与下游

- 上游：`banking-deposit-account-access-continuity/`、`financial-inclusion-payment-systems/`、`public-service-design-accessibility/`、`information-integrity-trust/`。
- 下游：`utility-affordability-shutoff-protection-continuity/`、`telecommunications-network-resilience-continuity/`、`digital-identity-security/`、`fraud-scams-consumer-protection/`、`administrative-burden-procedural-friction/`。

## 非目标

- 不提供个人合同审查、订阅取消、退款、投诉、诉讼、信用卡争议、服务选择、商业谈判或法律建议。
- 不判断个人合同是否有效、费用是否应付、是否可退款、是否欺诈或是否应取消。
- 不协助规避付款、滥用退款、伪造同意、绕过服务条款、批量套利或操控商家系统。

## 初始资料入口

- FTC: Negative option and subscription practices materials
- FTC: Consumer advice on subscriptions and unwanted charges
- CFPB: Consumer complaints and payments materials
- FCC: Consumer billing and communications service materials
- State consumer protection agencies and attorneys general official materials
