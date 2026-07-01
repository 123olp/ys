# Disaster Debris Waste Sanitation Cleanup Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/disaster-debris-waste-sanitation-cleanup-continuity` |
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

`disaster-debris-waste-sanitation-cleanup-continuity/` 研究灾后碎片废弃物、建筑残骸、污染物、卫生垃圾、清理协调和公共卫生风险如何影响主体返回、修复和恢复。

> 核心问题：灾后废弃物不是背景噪声，而是道路、住房、饮水、空气、感染、伤害和心理恢复的瓶颈；清理失败会让可返回空间继续不可行动。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体恢复需要安全道路、可进入住房、卫生环境和可工作的公共空间
  -> 灾害产生建筑残骸、危险废物、污水、腐败物、粉尘和尖锐物
  -> 废弃物清理决定返回、修复、交通、供水和公共卫生恢复速度
  -> 因此灾后废弃物与卫生清理是主体恢复连续性的环境域
```

## 关注对象

- EPA natural disaster debris、FEMA Public Assistance debris removal、地方固废系统、危险废物、污水、饮用水和公共卫生清理。
- 分类、收集、运输、处置、危险暴露、工人安全、公共通知、环境正义和二次污染。
- 与 `water-sanitation-hygiene-systems` 的边界：该域关注长期 WASH；本域关注灾害后的清理和废弃物恢复。

## Human Infra 模型链路

```text
灾后废弃物与卫生清理系统 T
  -> 改变道路清通、空间可进入、污染暴露、卫生和修复速度变量 X
  -> 改变主体返回与环境安全状态 S
  -> 改变伤害、感染、污染、住房延迟和经济恢复失败风险 λ(t)
  -> 影响恢复窗口、有效时间和长期选择权
```

## 非目标

- 不提供个人清理操作、危险废物处理、霉菌移除、结构安全判断、承包商建议或现场防护指导。
- 不收集房屋位置、污染类型、废弃物清单、承包商信息或保险资料。
- 不替代 EPA、FEMA、地方固废/公共卫生部门、持证修复承包商或职业安全专业人员。

## Source Signals

- EPA Planning for Natural Disaster Debris: https://www.epa.gov/homeland-security-waste/planning-natural-disaster-debris
- FEMA Public Assistance Debris Removal: https://www.fema.gov/assistance/public/process/debris-removal
- CDC Cleanup and Safety After a Disaster: https://www.cdc.gov/natural-disasters/safety/index.html
