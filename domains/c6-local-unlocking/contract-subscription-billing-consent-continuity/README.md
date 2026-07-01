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
