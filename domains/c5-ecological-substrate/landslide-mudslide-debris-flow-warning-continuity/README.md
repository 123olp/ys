# Landslide Mudslide Debris Flow Warning Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/landslide-mudslide-debris-flow-warning-continuity` |
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


`landslide-mudslide-debris-flow-warning-continuity/` 研究滑坡、泥石流、碎屑流、降雨触发、火后坡面风险、道路阻断和撤离如何影响主体持续性。

> 核心问题：滑坡和碎屑流把地质、降雨、火灾后坡面、住房位置、道路可达和预警理解连接成高速物理冲击链。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖地基、道路、住房、通信和转移窗口
  -> 滑坡/泥石流会突然切断这些基础条件
  -> 若危险迹象、预警、撤离、道路封闭和灾后评估失败，短时地质事件会造成死亡、隔离和住房损失
  -> 因而滑坡泥石流预警与撤离是地质灾害执行连续性域
```

## 关注对象

- 滑坡、泥石流、碎屑流、火后坡面、强降雨、陡坡住房、道路阻断和基础设施破坏。
- 预警信号、危险迹象、撤离、封闭道路、灾后地质评估、临时安置和长期迁移。
- 与 `volcanic-ashfall-geohazard-continuity/` 的边界：该域关注火山灰与火山相关地质风险；本域关注降雨/坡面/火后触发的滑坡和泥石流执行链。

## Human Infra 模型链路

```text
滑坡泥石流预警与撤离系统 T
  -> 改变危险识别、坡面暴露、道路可达、撤离时间、住房安全和通信变量 X
  -> 改变主体在坡面灾害窗口中的位置和转移状态 S
  -> 改变创伤、掩埋、隔离、住房丧失和服务中断风险 λ(t)
  -> 影响急性生存、恢复成本、迁移压力和未来选择权
```

## 非目标

- 不提供坡体稳定判断、房屋安全鉴定、实时撤离路线、工程加固、购房选址、保险或法律建议。
- 不替代 USGS、地方地质调查、应急管理、交通、公用事业或公共安全机构。
- 不鼓励进入封闭滑坡区、挖掘塌方、穿越泥石流路径或传播未核实地质风险图。

## Source Signals

- USGS Landslide Hazards Program: https://www.usgs.gov/programs/landslide-hazards
- Ready.gov Landslides and Debris Flow: https://www.ready.gov/landslides-debris-flow
- NWS Debris Flow resources: https://www.weather.gov/safety/flood-after-fire

## 下一步

- 建立危险迹象、火后坡面、道路封闭、撤离和灾后安全评估 source card。
- 与 `wildfire-landscape-fire-resilience/`、`public-works-civil-infrastructure-asset-management/` 和 `disaster-temporary-housing-displacement-recovery-continuity/` 对齐。
