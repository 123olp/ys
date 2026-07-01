# 消费贷款发放、APR 披露与还款义务连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/consumer-loan-origination-apr-disclosure-continuity` |
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


本域研究个人贷款、分期贷款和一般消费信贷的申请、核准、放款、APR 披露、费用、还款计划、服务转移和逾期如何影响主体现金流、资源可及性和长期负担。它关注贷款义务如何把未来收入绑定到当前资源，而不是贷款申请、产品推荐、再融资或金融法律建议。

## 研究对象

- 个人贷款、分期贷款、无抵押消费贷款、担保消费贷款和平台放款。
- 申请、承保、信用审查、不利行动通知、放款、APR、费用、还款计划和提前还款条款。
- 贷款服务、账单、自动扣款、服务商转移、逾期、违约、催收和信用报告。
- 与信用卡、BNPL、发薪日贷款、债务催收和信用报告的边界。

## 价值链路

```text
主体通过消费贷款获得当前资源
  -> 发放条件、APR、费用和还款计划把未来收入变成偿付义务
  -> 清晰披露、稳定服务和可追踪付款降低跨期资源误判
  -> 费用隐藏、服务错误、逾期和催收会把资源桥接变成长期约束
  -> 消费贷款连续性把借款决策纳入可审查的跨期义务系统
```

## 关键问题

- APR、费用和还款期限如何共同决定真实跨期成本？
- 承保、披露和不利行动通知如何影响公平信贷入口？
- 贷款服务转移、自动扣款和账单错误如何造成还款连续性断裂？
- 何时应将一般消费贷款与高成本小额贷款、信用卡或 BNPL 分开建模？

## 上游与下游

- 上游：`credit-consumer-reporting-access-continuity/`、`financial-inclusion-payment-systems/`、`banking-deposit-account-access-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`credit-card-revolving-credit-cost-continuity/`、`payday-small-dollar-title-loan-continuity/`、`buy-now-pay-later-installment-financing-continuity/`。

## 非目标

- 不提供贷款申请、产品选择、利率谈判、再融资、债务整合、还款安排、催收应对或法律建议。
- 不判断某笔贷款是否合适、是否违法、是否应提前还款、是否应违约或是否应诉讼。
- 不协助虚假申请、收入造假、资产隐瞒、逃债、规避催收、规避 KYC、伪造材料、洗钱或欺诈。

## 初始资料入口

- CFPB: Consumer loans and credit materials
- CFPB: Truth in Lending and APR disclosure materials
- CFPB: Credit reports and debt collection materials
- FTC consumer finance and lending materials
