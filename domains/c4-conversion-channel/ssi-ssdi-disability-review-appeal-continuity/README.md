# SSI SSDI Disability Review Appeal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/ssi-ssdi-disability-review-appeal-continuity` |
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


`ssi-ssdi-disability-review-appeal-continuity` 研究 SSI/SSDI 残障收入支持从申请、医学/工作证据、初始决定、appeal、continuing disability review、work reporting 到支付维护的连续性问题，以及它如何影响收入、医疗入口、住房、照护和主体长期行动能力。

## 核心问题

当身体或认知能力下降时，主体的持续性不只取决于治疗，还取决于收入支持是否能够承认失能事实、持续支付并允许纠错。错误拒付、复审断点、资料缺失和工作报告摩擦会把健康问题扩大为生活系统崩溃。

## 对象

- SSI、SSDI、disability determination、medical evidence、work history、Substantial Gainful Activity 和 appeals。
- Continuing Disability Review、work reporting、overpayment、benefit suspension 和 payment continuity。
- 与 Medicaid、Medicare、housing、SNAP、representative payee 和 supported decision-making 的接口。
- 与 `disability-income-work-capacity-benefit-continuity` 的分工：本域聚焦 SSA 程序链路和复审/申诉。

## Human Infra 价值

- 把残障收入支持视为能力下降后的主体持续性保险层。
- 解释行政证据、复审和申诉摩擦如何影响有效时间、治疗可及、住房稳定和照护安排。
- 为“主体连续性”提供一个制度承认层：能力变化后仍能保留资源和未来选择权。

## 边界

- 不提供 SSI/SSDI 资格判断、申请策略、医学证明、工作能力判断、appeal、CDR 回复、overpayment 处理、律师选择或法律建议。
- 不代写表格、病历摘要、功能报告、appeal、work report 或机构沟通材料。
- 不收集 SSN、医疗记录、工作记录、收入、家庭资产、案件号、SSA 账户或代表人信息。
- 不判断某人残障、可工作、应申请、应上诉、应复工或有胜诉概率。

## 上游与下游

- 上游：`disability-income-work-capacity-benefit-continuity`、`supported-decision-making-guardianship-rights`、`medical-record-access-amendment-release-continuity`。
- 下游：`medicaid-chip-renewal-redetermination-continuity`、`medicare-enrollment-coverage-transition-continuity`、`representative-payee-benefits-management-continuity`、`housing-choice-voucher-public-housing-continuity`。

## 初始资料线索

- SSA Disability Benefits: https://www.ssa.gov/benefits/disability/
- SSA SSI: https://www.ssa.gov/ssi/
- SSA appeal a decision: https://www.ssa.gov/apply/appeal-decision-we-made
- SSA continuing disability reviews publication: https://www.ssa.gov/pubs/EN-05-10053.pdf
