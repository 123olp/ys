# Motion Sickness Transport Virtual Environment Tolerance Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/motion-sickness-transport-virtual-environment-tolerance-continuity` |
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

Motion sickness, transport, and virtual environment tolerance continuity studies sensory conflict, nausea, disorientation, simulator sickness, and travel intolerance as constraints on mobility, training, remote work, VR/AR, and future spatial interfaces.

核心问题：

> 主体进入未来并不只靠更快交通和更强屏幕；如果交通、模拟器、VR/AR 和复杂视觉运动让身体持续不适，技术接口本身会变成行动障碍。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能承受交通、屏幕、模拟器和虚拟空间
  -> 前庭、视觉和本体感觉不一致会造成恶心、头晕和定向失衡
  -> 运动病和模拟器病会限制出行、训练、远程协作和沉浸式工具使用
  -> 因而运动/虚拟环境耐受是未来空间接口的可用性条件
```

## 关注对象

- 运动病、晕车/晕船/晕机、模拟器病、VR/AR 不适、视觉运动冲突和恢复时间。
- 通勤、旅行、驾驶/乘坐、训练模拟器、远程协作、游戏、XR 工具和空间计算。
- 与 `transportation-access-mobility/` 的关系：交通域关注服务可达；本域关注主体对交通运动的生理耐受。
- 与 `robotics-embodied-assistance-care-automation/` 的关系：机器人域关注具身辅助；本域关注虚拟/远程具身接口耐受。

## Human Infra 模型链路

```text
界面设计 / 暴露管理 / 交通适配 / 恢复支持 T
  -> 改变感官冲突、恶心、眩晕、定向不适和恢复时间 X
  -> 改变出行、训练、XR 使用、远程协作和学习工作状态 S
  -> 改变行动受限、技术排除、有效时间损耗和任务放弃风险 λ(t)
  -> 影响未来工具可及性、行动半径和可能性空间
```

## 非目标

- 不提供药物、补剂、暴露训练、驾驶/旅行适配、VR 设备推荐或个体耐受判断。
- 不根据个人晕动描述判断疾病、禁忌、旅行安全或设备适合度。
- 不替代临床、航空/海事医学、职业健康、交通安全或设备合规评估。

## Source Signals

- CDC Yellow Book motion sickness resources。
- NASA human research and space motion sickness context。
- Human factors literature on simulator sickness and cybersickness as research context。
