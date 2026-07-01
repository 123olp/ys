# Data Center Cooling Water Thermal Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-center-cooling-water-thermal-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`data-center-cooling-water-thermal-continuity/` 研究数据中心冷却、液冷、水资源、热管理、PUE/WUE、废热、可靠性和环境约束如何影响 AI 与数字基础设施的持续可用性。

> 核心问题：算力不是只消耗电，也消耗散热能力和环境承载。冷却失败、水约束或热失控会把 AI 基础设施从增长系统变成脆弱负载。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI、云服务、数字记忆和科研计算长期在线
  -> 这些系统依赖数据中心电力、冷却、水和热管理
  -> 冷却瓶颈会导致硬件故障、算力降频、停机和环境冲突
  -> 因此数据中心冷却水热管理是数字主体基础设施的热约束域
```

## 关注对象

- Air cooling、liquid cooling、immersion cooling、thermal design、water usage effectiveness、PUE、heat reuse、cooling redundancy 和 climate exposure。
- 高密度 AI 机柜、液冷运维、漏液风险、水压力、热浪风险、环境许可、停机恢复和区域资源冲突。
- 与 `compute-data-center-ai-infrastructure/` 的边界：算力基础设施域是总域；本域专门拆出冷却、水和热可靠性。
- 与 `water-resources-hydrology-flood-drought-management/` 的关系：水资源域关注流域和供水；本域关注数据中心用水和热管理接口。

## Human Infra 模型链路

```text
数据中心冷却水热管理 T
  -> 改变散热能力、水耗、机柜密度、故障率、PUE/WUE 和停机概率 X
  -> 改变 AI、云服务、数字档案和科研计算运行状态 S
  -> 改变算力中断、硬件损坏、成本上升和环境许可风险 λ(t)
  -> 影响主体可获得的 AI 工具、数字记忆、科研服务和长期协作能力
```

## 非目标

- 不提供数据中心设计施工、冷却系统改造、运维操作、采购或许可建议。
- 不把 PUE、WUE 或液冷路线图写成自动可持续证明。
- 不替代能源、电网、数据中心总域或水资源域。

## Source Signals

- IEA Electricity 2024 data centres discussion: https://www.iea.org/reports/electricity-2024
- DOE Data Centers and Servers: https://www.energy.gov/eere/amo/data-centers-and-servers
- ASHRAE Datacom Series: https://www.ashrae.org/technical-resources/bookstore/datacom-series
- Open Compute Project Cooling Environments: https://www.opencompute.org/

## 下一步

- 建立 Cooling Continuity Card：cooling class, power density, water source, redundancy, climate exposure, thermal failure mode, community constraint, compute impact。
