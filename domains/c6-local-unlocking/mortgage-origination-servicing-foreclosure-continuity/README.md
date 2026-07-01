# 房贷发放、服务、止赎与住房连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/mortgage-origination-servicing-foreclosure-continuity` |
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


本域研究抵押贷款申请、Loan Estimate、Closing Disclosure、放款、托管账户、贷款服务、服务商转移、付款处理、宽限、损失缓解和止赎如何影响主体住房稳定、长期现金流和家庭基础设施。它关注住房连续性的金融管线，而不是房贷推荐、购房建议、止赎应对或法律建议。

## 研究对象

- 房贷申请、承保、估价、Loan Estimate、Closing Disclosure、利率、点数、费用和 closing costs。
- 托管账户、税费保险、服务商转移、付款处理、账单、差错处理和信用报告。
- 逾期、宽限、forbearance、loss mitigation、loan modification、短售、止赎和搬迁风险。
- 与不动产权属、住房保障、灾害住房、债务义务和信用报告的边界。

## 价值链路

```text
主体通过房贷获得长期住房入口
  -> 放款条件、披露、托管和服务把住房稳定绑定到多年现金流
  -> 稳定服务、准确账单和损失缓解降低住房中断风险
  -> 服务错误、付款错配、逾期升级或止赎会破坏家庭基础设施
  -> 房贷连续性把住房从一次性购买转化为长期金融服务系统
```

## 关键问题

- Loan Estimate、Closing Disclosure 和 APR 如何影响住房成本理解？
- 服务商转移、托管账户和付款处理如何造成住房连续性风险？
- 宽限、损失缓解和止赎程序如何改变主体恢复窗口？
- 房贷服务问题与产权记录、租住保障和债务催收如何分界？

## 上游与下游

- 上游：`real-property-title-deed-record-continuity/`、`housing-shelter-stability/`、`credit-consumer-reporting-access-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`disaster-housing-recovery-rebuilding-continuity/`、`household-budget-cashflow-continuity/`、`public-assistance-benefits-continuity/`。

## 非目标

- 不提供购房、贷款产品选择、利率锁定、再融资、forbearance、loan modification、止赎防御、搬迁或法律建议。
- 不判断某个房贷、房产、服务商、止赎行动或损失缓解选项是否适合个人。
- 不协助虚假贷款申请、收入资产造假、产权欺诈、抵押贷款欺诈、逃债、规避止赎、伪造文件或规避 KYC/AML。

## 初始资料入口

- CFPB: Mortgages consumer tools
- CFPB: Loan Estimate and Closing Disclosure materials
- CFPB: Mortgage servicing and foreclosure prevention materials
- HUD and state housing finance / foreclosure prevention materials
