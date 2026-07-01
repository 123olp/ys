# Afterschool Snack Supper Meal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/afterschool-snack-supper-meal-continuity` |
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

该域研究放学后 snack、supper 和 at-risk afterschool meals 如何在学校日结束后维持儿童能量、监督照护、学习参与和家庭晚间安排。它关注的是课后时间段中“孩子在哪里、吃什么、谁承担成本、怎样低摩擦接续”。

## 核心问题

- 放学后项目是否提供足够、可靠、符合规则的点心或晚餐。
- 课后餐食是否与活动时段、接送、交通、家庭工作时间和社区安全匹配。
- 项目资格、报销、餐食采购、现场记录和 staffing 是否影响项目持续运行。

## 对象

- CACFP at-risk afterschool meals、NSLP afterschool snacks、课后项目和社区活动点。
- 点心、晚餐、餐食时段、接送窗口、活动参与、出勤记录和报销接口。
- 儿童注意力、晚间学习、家庭晚餐压力、照护者工作时间和社区安全。

## Human Infra 价值

课后餐食把学校日之后的高摩擦时间段接住，避免儿童在放学后到睡前之间因饥饿、交通、活动成本和家庭排班冲突而损失学习轮次和恢复能力。

## 边界

- 只整理公开项目结构、餐食连续性变量、照护时间断点和证据线索。
- 不推荐课后项目、不规划接送、不设计菜单、不判断资格、不提供项目运营或报销建议。
- 不收集儿童出勤、项目名单、家庭排班、活动记录或消费记录。

## 上游与下游

- 上游：`out-of-school-time-afterschool-summer-learning-continuity`、`school-meals-nutrition-access-continuity`、`cacfp-child-adult-care-food-program-continuity`。
- 下游：`childcare-family-continuity`、`time-allocation-effective-time`、`food-security-nutrition-access`。

## 初始资料线索

- USDA FNS CACFP At-Risk Afterschool Meals.
- USDA FNS National School Lunch Program Afterschool Snacks.
- 21st Century Community Learning Centers public materials.
