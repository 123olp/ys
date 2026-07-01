# Fall Risk Prevention Home Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/fall-risk-prevention-home-safety-continuity` |
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

`fall-risk-prevention-home-safety-continuity/` 研究跌倒风险筛查、药物/视力/平衡/环境因素、家居安全、社区项目、跌倒后恢复和恐惧回避如何影响主体持续性。

> 核心问题：跌倒不是单次意外，而是视觉、前庭、肌力、药物、环境、认知和照护系统共同失稳的结果。有效永生需要把跌倒预防建模为避免骨折、脑损伤、恐惧回避和行动半径收缩的日常基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖安全站立、转移、行走和家居移动维持独立生活
  -> 跌倒会把轻微环境摩擦转化为骨折、TBI、恐惧和机构化风险
  -> 结果取决于风险识别、家居环境、药物审查、视力/平衡/肌力和社区支持
  -> 因此跌倒风险预防是行动连续性和居家安全的执行域
```

## 关注对象

- Fall risk screening, STEADI-like workflows, home safety, medication review, vision/balance/strength interfaces, fear of falling, post-fall follow-up。
- 与 `musculoskeletal-integrity/` 和 `vestibular-balance-spatial-orientation/` 的边界：这些域关注身体结构与平衡机制；本域关注跌倒风险如何在家居和社区执行层被识别、降低和复盘。
- 与 `built-environment-accessibility-universal-design/` 的关系：家居和公共空间设计是跌倒风险控制的外部条件。

## Human Infra 模型链路

```text
跌倒风险预防系统 T
  -> 改变风险筛查、家居安全、药物审查、视力/平衡/肌力接口和复盘变量 X
  -> 改变跌倒概率、损伤严重度、移动信心和独立生活状态 S
  -> 改变骨折、TBI、机构化、照护负担和有效时间损失 λ(t)
  -> 影响主体行动半径、自主性和未来选择权
```

## 非目标

- 不提供个人跌倒风险判断、家庭改造、训练动作、药物调整、辅具选择、驾驶/活动许可、急救或康复建议。
- 不生成家居安全个案清单、设备购买、监控布置、责任判断、保险或法律建议。
- 不收集个案居住平面、跌倒史、药物、影像、视频、位置或诊疗资料。

## Source Signals

- CDC STEADI: https://www.cdc.gov/steadi/
- CDC older adult fall prevention: https://www.cdc.gov/falls/
- NIA falls and fractures: https://www.nia.nih.gov/health/falls-and-falls-prevention

## 下一步

- 建立 Fall Prevention Card：screening, medication, vision/balance/strength, home safety, post-fall review, fear of falling。
- 与 `musculoskeletal-integrity/`、`vestibular-balance-spatial-orientation/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 和 `built-environment-accessibility-universal-design/` 建立接口。
