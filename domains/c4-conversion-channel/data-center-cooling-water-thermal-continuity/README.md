# Data Center Cooling Water Thermal Continuity

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
