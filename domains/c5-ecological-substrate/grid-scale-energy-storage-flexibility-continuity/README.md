# Grid Scale Energy Storage Flexibility Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/grid-scale-energy-storage-flexibility-continuity` |
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

`grid-scale-energy-storage-flexibility-continuity/` 研究电网级储能、长时储能、需求响应、灵活负荷、备用容量和调度机制如何支撑高比例可再生能源、AI 负载和关键服务连续性。

> 核心问题：电力系统不仅需要发电，还需要时间上的可调度性。储能和灵活性不足会让能源充足性在关键时刻变成服务中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要医疗、通信、AI、冷却、居住和交通系统持续供电
  -> 高波动负载和可再生能源需要储能、灵活性和调度缓冲
  -> 缓冲不足会导致价格尖峰、停电、负载削减和关键服务降级
  -> 因此电网级储能与灵活性是能源连续性的时间缓冲域
```

## 关注对象

- Battery storage、long-duration energy storage、pumped hydro、thermal storage、demand response、virtual power plant、reserve margin 和 grid services。
- 容量、持续时长、循环寿命、安全、并网、调度、退化、供应链、回收和关键负载保障。
- 与 `energy-access-resilience/` 的边界：能源可及域关注用户能否获得能源；本域关注电网尺度时间缓冲和灵活性。
- 与 `large-load-grid-interconnection-transmission-continuity/` 的关系：并网域关注接入；本域关注接入后的可调度性。

## Human Infra 模型链路

```text
电网储能与灵活性 T
  -> 改变备用容量、持续时长、负荷转移、频率服务和停电恢复变量 X
  -> 改变医疗、通信、数据中心、住房和交通供能状态 S
  -> 改变停电、价格尖峰、关键服务削减和恢复失败风险 λ(t)
  -> 影响主体安全、工具可用性、环境控制和长期行动能力
```

## 非目标

- 不提供储能系统安装、消防处置、项目投资、交易套利或采购建议。
- 不把储能写成无风险、无资源约束或万能替代输电的方案。
- 不替代电网可靠性、能源可及、消防安全或关键材料域。

## Source Signals

- DOE Office of Electricity Energy Storage: https://www.energy.gov/oe/energy-storage
- NREL Energy Storage: https://www.nrel.gov/grid/energy-storage.html
- IEA Energy Storage: https://www.iea.org/energy-system/electricity/grid-scale-storage
- Sandia Energy Storage: https://www.sandia.gov/ess-ssl/

## 下一步

- 建立 Storage Flexibility Card：storage class, duration, dispatch role, safety boundary, degradation, supply dependency, critical-service coupling。
