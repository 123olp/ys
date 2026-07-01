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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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
