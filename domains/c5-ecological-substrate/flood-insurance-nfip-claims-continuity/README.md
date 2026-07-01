# 洪水保险、NFIP 与理赔连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/flood-insurance-nfip-claims-continuity` |
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

本域研究洪水保险、National Flood Insurance Program、private flood insurance、flood maps、waiting period、coverage limits、proof of loss、claim、appeal 和 mitigation 如何影响主体住房恢复、财产恢复和灾后现金流。它关注洪水风险转移的专门执行层，而不是投保建议、理赔代办或法律建议。

## 研究对象

- NFIP、private flood insurance、flood hazard maps、Special Flood Hazard Area、lender requirement 和 waiting period。
- Building coverage、contents coverage、coverage limits、deductible、exclusions、elevation、mitigation 和 policy renewal。
- Flood claim、adjuster、proof of loss、appeal、ICC coverage、灾后援助和重复损失风险。
- 与房主险、灾害住房恢复、水文洪水控制、房贷和地方土地使用的边界。

## 价值链路

```text
主体住房暴露于洪水风险
  -> 洪水保险把普通房主险之外的水灾损失转移到专门保单和 NFIP 执行链
  -> flood map、coverage 和 proof of loss 决定灾后是否能获得恢复资金
  -> waiting period、限额、除外责任或理赔失败会把洪水事件变成长期住房断裂
  -> 洪水保险连续性把水灾风险纳入可审查的住房恢复和风险分摊系统
```

## 关键问题

- 洪水保险为什么不能被普通房主险自动覆盖？
- flood map、lender requirement 和 waiting period 如何影响保险可用性？
- proof of loss、adjuster 和 appeal 如何决定灾后资金恢复？
- 洪水保险如何与 FEMA 援助、房贷、重建和迁居选择连接？

## 上游与下游

- 上游：`water-resources-hydrology-continuity/`、`dams-levees-flood-control-assets/`、`real-property-title-deed-record-continuity/`。
- 下游：`disaster-housing-recovery-rebuilding-continuity/`、`homeowners-renters-property-insurance-claims-continuity/`、`public-works-asset-management/`、`urban-planning-land-use-zoning-continuity/`。

## 非目标

- 不提供洪水保险购买、保额选择、地图申诉、proof of loss 填写、理赔、appeal、重建、搬迁或法律建议。
- 不判断某处房产是否需要洪水保险、某张 flood map 是否正确、某笔 claim 是否应赔或赔多少。
- 不协助虚假洪水损失、伪造 proof of loss、夸大灾损、隐瞒既有损害、保险欺诈、绕过 lender 要求或骗取灾害援助。

## 初始资料入口

- FEMA FloodSmart / National Flood Insurance Program
- FEMA flood maps and flood insurance claim materials
- State insurance department flood insurance materials
- Ready.gov flood preparedness materials
