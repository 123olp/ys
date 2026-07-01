# Household Maintenance Repair Contractor Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-maintenance-repair-contractor-continuity` |
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

`household-maintenance-repair-contractor-continuity` 研究家庭维修、承包商、服务预约、报价、许可、消费者保护、维修记录和应急修复如何影响住房、设备、水电、卫生和安全连续性。

> 核心问题：家庭系统坏了以后，真正的断点往往不是“知道坏了”，而是找不到可信维修、排不上服务、被诈骗、缺记录、缺许可或修复责任不清。

## 关注对象

- 管道、电气、暖通、屋顶、门窗、排水、家电、网络、害虫、霉菌、水损和灾后小修复的服务链。
- 维修请求、服务预约、报价、合同、许可、保险、保修、验收、维修记录、投诉和召回接口。
- 租住/业主/物业/承包商责任边界、紧急维修、脆弱人群、无障碍修复和消费者保护。
- 与住房稳定、公共工程、公用事业、家电维护、产品召回、诈骗防护和灾后恢复的接口。

## Human Infra 链路

```text
家庭维修服务连续
  -> 居住空间、设备、水电、卫生和安全故障能被发现、排程、修复和记录
  -> 延误、诈骗、无证服务、责任不清和重复故障造成的恢复成本下降
  -> 住房从被动损耗对象转化为可维护的生活基础设施
  -> 睡眠、卫生、温控、照护、工作和家庭韧性增强
```

## 非目标

- 不提供 DIY 危险维修、电气/燃气/结构施工、承包商规避、虚假索赔、合同争议策略或法律意见。
- 不替代本地许可、建筑规范、保险、消费者保护、物业、房东/租客法律或专业承包商判断。
- 不推荐具体承包商、价格、维修方案、理赔路径或投诉策略。

## Source Signals

- FTC Home Improvement Scams: https://consumer.ftc.gov/articles/how-spot-avoid-and-report-home-improvement-scams
- CPSC Recalls: https://www.cpsc.gov/Recalls
- FEMA Disaster Recovery: https://www.fema.gov/assistance/individual
- DOE Weatherization Assistance Program: https://www.energy.gov/scep/wap/weatherization-assistance-program

## 下一步

- 建立 `household fault -> responsible party -> service request -> repair evidence -> recurrence prevention` 变量表。
- 区分业主自住、租住、物业管理、灾后修复、紧急维修、无障碍改造和低收入援助场景。
- 与 `housing-built-environment-stability`、`household-appliance-maintenance-repair-continuity`、`product-safety-recall-systems` 和 `fraud-scams-consumer-protection` 建立边界。
