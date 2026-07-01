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
