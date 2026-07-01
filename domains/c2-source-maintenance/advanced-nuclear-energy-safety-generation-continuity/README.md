# Advanced Nuclear Energy Safety Generation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/advanced-nuclear-energy-safety-generation-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

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

`advanced-nuclear-energy-safety-generation-continuity/` 研究核能、先进反应堆、小型模块化反应堆、核燃料供应、许可、安全监管、废物管理和低碳可靠发电如何影响长期能源、算力和工业连续性。

> 核心问题：长时间尺度的技术文明需要可靠、低碳、可调度能源；核能可能是其中一条路径，但其价值必须经过安全、监管、废物、燃料和社会许可约束。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要医疗、AI、制造、冷却、交通和居住系统长期可靠供能
  -> 核能提供低碳可调度电力的候选路径
  -> 安全、许可、燃料、废物和成本失败会把能源收益转化为尾部风险
  -> 因此先进核能是能源连续性中的高收益高约束候选域
```

## 关注对象

- Nuclear power generation、advanced reactors、SMR、fuel cycle、licensing、safety oversight、waste management、decommissioning 和 grid integration。
- 可靠发电、低碳负荷、工业热、数据中心供能、应急准备、社会许可、成本风险和核安全边界。
- 与 `radiation-nuclear-safety-protection/` 的边界：辐射核安全域关注防护和应急；本域关注发电连续性及其监管约束。
- 与 `energy-access-resilience/` 的关系：能源可及域关注终端能源；本域关注核能作为供给侧候选路径。

## Human Infra 模型链路

```text
先进核能 T
  -> 改变可靠低碳电力、燃料供应、监管许可、安全冗余和废物责任变量 X
  -> 改变数据中心、医疗、制造、城市供能和电网稳定状态 S
  -> 改变能源短缺、碳约束、事故尾部风险和成本失控风险 λ(t)
  -> 影响主体可获得的长期能源、技术扩张速度和环境稳定性
```

## 非目标

- 不提供核设施设计、核材料处理、安保绕过、应急操作、项目投资或选址建议。
- 不把先进核能写成已证明的低风险万能能源。
- 不替代辐射安全、应急准备、电网可靠性或能源可及域。

## Source Signals

- U.S. DOE Office of Nuclear Energy: https://www.energy.gov/ne/office-nuclear-energy
- U.S. NRC Power Reactors: https://www.nrc.gov/reactors/power.html
- IAEA Nuclear Energy: https://www.iaea.org/topics/nuclear-energy
- OECD NEA: https://www.oecd-nea.org/

## 下一步

- 建立 Advanced Nuclear Card：reactor class, licensing stage, safety case, fuel dependency, waste path, grid role, tail risk, continuity value。
