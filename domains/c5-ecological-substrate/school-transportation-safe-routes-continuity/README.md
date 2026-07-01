# School Transportation Safe Routes Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-transportation-safe-routes-continuity` |
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

`school-transportation-safe-routes-continuity` 研究校车、步行骑行安全路线、无障碍交通、交通资格、到校距离和道路安全如何影响出勤、学习时间、安全风险和家庭时间成本。

> 核心问题：儿童不能安全、可靠、可负担地到达学校，教育权就会退化为纸面资格。

## 关注对象

- 校车安全、路线规划、交通资格、接送点、迟到缺勤、天气灾害和服务中断。
- Safe Routes to School、步行、骑行、道路设计、速度风险、可见性和交叉口安全。
- 残障学生交通、临时住所/寄养/迁居交通、农村距离、家庭工作时间和照护负担。
- 通学交通与出勤、纪律、特殊教育、环境暴露、交通伤害和公共交通运营的交叉。

## Human Infra 链路

```text
通学交通与安全路线连续
  -> 学生到校路径更可靠、可达、安全和低摩擦
  -> 缺勤、迟到、交通伤害、家庭时间成本和安全焦虑下降
  -> 学习时间、恢复时间、家庭工作连续性和社区可达性增强
  -> 儿童能力积累和长期未来选择权更稳定
```

## 非目标

- 不提供个人路线、驾驶、校车申诉、交通资格、道路工程、事故责任、残障交通、法律或安全实时建议。
- 不替代学校交通部门、DOT、NHTSA、FHWA、地方交通机构、警务、急救或法律服务。
- 不收集学生住址、路线、家庭安排、残障资料或定位数据。

## Source Signals

- Federal Highway Administration Safe Routes to School resources.
- National Highway Traffic Safety Administration school bus safety resources.
- State and local school transportation and road safety guidance.
- Local education agency transportation policies and accessibility requirements.

## 下一步

- 建立 `route reliability -> arrival continuity -> exposure/risk -> learning time` 变量表。
- 区分学校交通、公共交通、道路安全、家庭接送、残障交通和灾害交通。
- 与 `transportation-access-mobility`、`road-traffic-injury-prevention-safe-mobility`、`school-enrollment-attendance-continuity` 和 `special-education-iep-504-accommodation-continuity` 建立边界。
