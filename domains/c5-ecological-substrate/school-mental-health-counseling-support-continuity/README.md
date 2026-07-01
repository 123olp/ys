# School Mental Health Counseling Support Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-mental-health-counseling-support-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`school-mental-health-counseling-support-continuity` 研究学校心理健康、咨询、社工、学校心理师、危机转介、社区照护衔接和隐私同意如何影响学生情绪稳定、出勤、学习和恢复能力。

> 核心问题：学生心理健康支持是学习系统的恢复层；恢复层缺失时，压力、创伤、孤立和危机会直接压缩学习轮次和未来选择权。

## 关注对象

- 学校咨询、school-based mental health、社工、心理师、转介、危机响应和家庭沟通。
- 抑郁、焦虑、创伤、物质使用风险、自伤风险、行为危机和同伴支持环境。
- 机构能力、人员比例、隐私同意、保险/社区服务衔接、缺勤复学和慢性压力。
- 心理健康与纪律、欺凌、暴力、儿童保护、残障支持、学校健康服务和社会连接的交叉。

## Human Infra 链路

```text
学校心理健康支持连续
  -> 学生压力、创伤、危机和关系断裂获得早期识别与转介
  -> 缺勤、纪律化、学习中断、自伤风险和家庭负担下降
  -> 情绪稳定、恢复能力、学习参与和求助能力增强
  -> 主体长期行动能力和未来选择权更可持续
```

## 非目标

- 不提供个人心理诊断、治疗、危机处置、安全计划、用药、学校投诉、转介选择或医疗/法律建议。
- 不替代 988、急救、学校心理健康团队、医生、治疗师、家长、儿童保护或危机服务。
- 不收集学生心理健康、危机、家庭、纪律、残障或医疗资料。

## Source Signals

- SAMHSA school and youth mental health resources.
- CDC school mental health and Healthy Schools resources.
- U.S. Department of Education school-based mental health and student support resources.
- State education and behavioral health agency school mental health guidance.

## 下一步

- 建立 `stress/need -> school support -> referral/recovery -> learning continuity` 变量表。
- 区分学校支持、临床治疗、危机响应、纪律系统、儿童保护和同伴关系。
- 与 `mental-health-affective-stability`、`suicide-crisis-response-continuity`、`school-discipline-exclusion-restraint-continuity` 和 `school-climate-bullying-violence-prevention-continuity` 建立边界。
