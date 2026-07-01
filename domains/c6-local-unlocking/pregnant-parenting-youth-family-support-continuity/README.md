# Pregnant Parenting Youth Family Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/pregnant-parenting-youth-family-support-continuity` |
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

怀孕与育儿青年家庭支持连续性，关注青少年或过渡年龄青年在怀孕、分娩、育儿、学校、住房、医保、托育、家庭关系、收入和亲职支持之间如何保持学习、健康、照护和未来选择权。

## 对象

- Pregnant and parenting youth
- School continuity and Title IX boundary
- Prenatal / postpartum service linkage
- Childcare and early childhood supports
- Housing and family support
- Income and nutrition benefits linkage
- Fatherhood / co-parenting support
- Confidentiality and consent boundaries

## Human Infra 价值

怀孕和育儿会把青年主体的身体、时间、注意力、收入、学习和关系资源重新分配。该域把“青年能否同时继续成长和照护下一代”建模为学校连续、医疗转接、托育、住房、营养、亲职支持和隐私边界的基础设施。

## 边界

- 不提供怀孕、分娩、育儿、亲子关系、学校权利、福利、托育、住房、医疗、心理、法律或家庭冲突建议。
- 不判断个人怀孕状态、亲职能力、儿童安全、家庭风险、学校义务或服务资格。
- 不替代医疗、学校、儿童福利、托育、法律援助、公共福利或危机服务。

## 上游与下游

- 上游：`contraception-family-planning-access-continuity/`、`pregnancy-parental-work-continuity/`、`maternal-newborn-child-development/`。
- 下游：`child-care-availability-affordability-continuity/`、`wic-benefit-redemption-infant-maternal-nutrition-continuity/`、`head-start-early-head-start-family-support-continuity/`。

## 初始资料线索

- Youth.gov pregnant and parenting young people resources.
- HHS / ACF family and youth service materials.
- U.S. Department of Education Title IX pregnancy and parenting student guidance.
