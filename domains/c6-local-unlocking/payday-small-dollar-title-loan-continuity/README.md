# 发薪日贷款、小额高成本贷款与汽车抵押贷款连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/payday-small-dollar-title-loan-continuity` |
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


本域研究发薪日贷款、小额高成本贷款、汽车抵押贷款、滚续、费用、银行账户访问、抵押物和债务循环如何影响主体应急现金、账户稳定、车辆移动和未来选择权。它关注短期流动性危机如何转化为高成本跨期约束，而不是借款、续借、规避还款或法律建议。

## 研究对象

- Payday loans、small-dollar loans、title loans、deposit advance、rollover、renewal 和分期式高成本小额贷款。
- 费用、APR、期限、自动扣款、post-dated check、账户访问、抵押车辆、逾期和收车风险。
- 债务循环、重复借款、银行透支、催收、信用报告和替代应急资金入口。
- 与消费贷款、车贷、债务催收、银行账户和反诈骗保护的边界。

## 价值链路

```text
主体在现金缺口中寻求短期资金
  -> 高成本小额贷款把应急现金转换成近未来收入和抵押物风险
  -> 清晰费用、可终止扣款和替代入口降低短期危机扩散
  -> 滚续、重复借款、账户透支或收车会把一次危机变成长期束缚
  -> 小额高成本贷款连续性把应急资源桥接纳入债务循环风险治理
```

## 关键问题

- 发薪日贷款、title loan 和一般分期消费贷款的风险结构如何不同？
- 滚续、自动扣款和账户访问如何放大现金流断裂？
- 车辆抵押贷款如何把金融失败转化为移动能力失败？
- 监管披露、费用上限和替代金融入口如何影响主体恢复窗口？

## 上游与下游

- 上游：`financial-inclusion-payment-systems/`、`household-budget-cashflow-continuity/`、`banking-deposit-account-access-continuity/`。
- 下游：`debt-obligation-collection-relief-continuity/`、`auto-loan-lease-servicing-repossession-continuity/`、`fraud-scams-consumer-protection/`、`public-assistance-benefits-continuity/`。

## 非目标

- 不提供发薪日贷款、title loan、小额贷款申请、续借、债务谈判、催收应对、收车应对或法律建议。
- 不判断某个高成本贷款是否合法、是否适合、是否应还款、是否应违约或是否应诉讼。
- 不协助虚假申请、支票欺诈、隐藏车辆、逃债、规避自动扣款、规避催收、伪造收入、洗钱或贷款欺诈。

## 初始资料入口

- CFPB: Payday loans consumer tools
- FTC: Payday loans consumer materials
- CFPB: Small-dollar and high-cost loan materials
- State attorney general and regulator consumer lending materials
