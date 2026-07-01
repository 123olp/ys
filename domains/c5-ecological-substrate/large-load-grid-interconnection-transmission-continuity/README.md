# Large Load Grid Interconnection Transmission Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/large-load-grid-interconnection-transmission-continuity` |
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

`large-load-grid-interconnection-transmission-continuity/` 研究大型用电负载、数据中心、工业设施、输电扩建、并网队列、互联研究和电网规划如何影响 AI、制造和生命线基础设施的持续扩展。

> 核心问题：未来技术扩张首先要接上电网。并网排队、输电瓶颈和规划滞后会让算力、制造、医疗和居住韧性卡在“有设备但没有电”的状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI、制造、医疗、冷却、交通和居住系统持续供能
  -> 大型负载扩张依赖输电容量、并网流程和电网规划
  -> 并网延迟或输电不足会限制技术部署和区域服务可用性
  -> 因此大型负载并网与输电是技术扩散的电力接入约束域
```

## 关注对象

- Load growth、interconnection queue、transmission planning、grid upgrade、connection study、large load forecasting、capacity adequacy 和 reliability coordination。
- 数据中心并网、工业电气化、制造用电、输电许可、排队延迟、成本分摊、区域容量和电力服务可得性。
- 与 `electric-grid-reliability-resilience-continuity/` 的边界：电网可靠性域关注运行可靠性；本域关注新负载接入、输电扩容和并网排队。
- 与 `ai-resource-cost-latency-budget-continuity/` 的关系：AI 预算域关注使用侧；本域关注物理电力接入。

## Human Infra 模型链路

```text
大型负载并网与输电 T
  -> 改变电力接入时间、输电容量、升级成本、区域可用容量和可靠性约束 X
  -> 改变数据中心、制造、医疗设施和关键服务扩展状态 S
  -> 改变算力短缺、建设延迟、服务不可达和区域不平等风险 λ(t)
  -> 影响主体可获得的 AI、制造、医疗、冷却和长期基础服务
```

## 非目标

- 不提供并网申请、项目开发、能源采购、投融资、选址或规避电力监管建议。
- 不把新增负载写成必然进步，也不把输电扩建写成无成本方案。
- 不替代电网可靠性、能源可及、数据中心或公用事业可负担性域。

## Source Signals

- DOE Interconnection Innovation e-Xchange: https://www.energy.gov/eere/i2x/interconnection-innovation-e-xchange
- Lawrence Berkeley National Laboratory Interconnection Queue: https://emp.lbl.gov/queues
- FERC Electric Transmission: https://www.ferc.gov/industries-data/electric
- NERC Reliability Assessments: https://www.nerc.com/pa/RAPA/Pages/default.aspx

## 下一步

- 建立 Large Load Interconnection Card：load type, requested capacity, queue status, transmission dependency, upgrade risk, reliability impact, equity boundary。
