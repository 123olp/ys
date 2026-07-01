# Student Financial Aid Grant Scholarship Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/student-financial-aid-grant-scholarship-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`student-financial-aid-grant-scholarship-continuity` 研究 FAFSA、Title IV aid、Pell Grant、federal loans、work-study、州与机构奖助学金、verification、satisfactory academic progress 和资助发放如何影响学生持续学习、生活稳定和债务风险。

> 核心问题：高等教育机会只有在资金流连续、规则可理解、资格可维护、账单可承受时，才能转化为真实学习窗口；资助断裂会把学习路径迅速变成债务、退学和信用风险。

## 关注对象

- FAFSA、学生援助指数、家庭贡献资料、dependency status、verification、appeal 和特殊情况调整。
- Pell Grant、Direct Loans、Federal Work-Study、州助学金、机构奖学金、应急助学金、学费减免和外部奖学金。
- Satisfactory Academic Progress、注册学分、退课、重复课程、停学、返校、退款、overpayment 和 financial hold。
- 学费、生活费、cost of attendance、net price、债务负担、还款风险和资助通知可理解性。

## Human Infra 链路

```text
学生资助与奖助学金连续
  -> 学费、生活费和学习材料成本被制度性缓冲
  -> 因现金流、账单、资格和证明摩擦导致的停学退学下降
  -> 学习时间、校园参与、健康恢复和职业准备更稳定
  -> 主体长期能力资本、收入路径和债务风险治理能力增强
```

## 非目标

- 不提供 FAFSA 填报、贷款选择、奖学金申请、债务策略、税务、投资、学校选择、个人资格或法律建议。
- 不替代 Federal Student Aid、高校 financial aid office、loan servicer、州资助机构、税务专业人士或法律援助。
- 不收集或处理学生/家庭财务资料、SSN、税务资料、FSA ID、资助账号、移民身份或银行资料。

## Source Signals

- Federal Student Aid official student aid and FAFSA resources: https://studentaid.gov/
- Federal Student Aid partner guidance and handbook materials: https://fsapartners.ed.gov/
- College Scorecard cost, debt and outcomes data: https://collegescorecard.ed.gov/
- NCES/IPEDS student financial aid and institutional finance data: https://nces.ed.gov/ipeds/

## 下一步

- 建立 `eligibility -> aid offer -> disbursement -> SAP -> persistence -> debt risk` 变量表。
- 区分 grant、loan、work-study、scholarship、emergency aid、waiver、refund、hold 和 repayment。
- 与 `debt-obligation-collection-relief-continuity`、`financial-resilience-access`、`social-protection-benefits-delivery` 和本轮高教域建立边界。
