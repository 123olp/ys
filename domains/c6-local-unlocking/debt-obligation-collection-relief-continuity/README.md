# 债务义务、催收与债务救济连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/debt-obligation-collection-relief-continuity` |
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


本域研究债务义务、催收、信用后果、破产和债务救济机制如何影响主体资源、心理负担、住房、就业、家庭和未来选择权。它关注的是债务压力如何改变主体持续性，而不是个人还款、谈判、破产或法律建议。

## 研究对象

- 消费债务、医疗债务、学生贷款、税务债务、住房相关债务和罚金费用。
- 催收、诉讼、工资扣押、留置、抵押品收回、信用报告和错误记录。
- 债务重组、债务救济、破产、暂停执行、申诉和消费者保护。
- 债务压力与健康、时间、注意力、住房稳定、家庭关系和工作能力的相互作用。

## 价值链路

```text
主体需要把收入和资产转化为未来行动能力
  -> 债务义务会占用现金流、注意力、时间、信用入口和法律风险预算
  -> 催收、诉讼、扣押和记录错误会把财务压力扩散到住房、就业和医疗
  -> 债务救济、纠错、申诉和破产制度提供风险重组和重新开始路径
  -> 债务连续性研究把债务从单一金额问题转化为主体持续性的约束函数
```

## 关键问题

- 债务如何通过压力、时间贫困、账户扣押、信用报告和法律程序影响有效时间？
- 医疗债务、学生贷款、住房债务和消费债务分别有哪些独立失败模式？
- 催收和自动化记录如何制造错误、身份混淆、骚扰和程序摩擦？
- 债务救济和破产制度如何在不鼓励逃避义务的前提下保护主体重新行动能力？

## 上游与下游

- 上游：`financial-resilience-access/`、`credit-consumer-reporting-access-continuity/`、`banking-deposit-account-access-continuity/`、`healthcare-access-continuity/`。
- 下游：`housing-built-environment-stability/`、`tenant-screening-rental-access-continuity/`、`employment-algorithmic-hiring-screening-continuity/`、`mental-health-affective-stability/`、`access-to-justice-legal-aid/`。

## 非目标

- 不提供个人还款、债务谈判、债务整合、破产申请、学生贷款、税务债务、催收应对或法律建议。
- 不判断个人债务是否合法、是否应偿还、是否可免除、是否可破产或是否可申诉。
- 不协助逃债、隐匿资产、规避法院命令、伪造记录、骚扰催收方或利用债务系统套利。

## 初始资料入口

- CFPB: Debt collection
- CFPB: Medical debt, credit reporting and consumer complaints
- U.S. Courts: Bankruptcy basics
- Federal Student Aid: Student loan repayment and relief materials
- Federal Trade Commission: Debt collection and consumer protection materials
