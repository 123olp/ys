# Water Resources Hydrology Flood Drought Management

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/water-resources-hydrology-flood-drought-management` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`water-resources-hydrology-flood-drought-management/` 研究水资源、水文观测、流域管理、地下水、水库、洪水、干旱和水安全如何支撑主体持续性。

> 核心问题：WASH 处理“水能否安全进入人和卫生系统”，但更上游的问题是水资源本身是否存在、可调度、可预警、可治理；水文系统失效会同时击穿饮水、农业、能源、交通、住房和灾害安全。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖饮水、卫生、食物、能源、冷却、医疗和居住安全
  -> 这些系统依赖水资源、水文观测、储蓄调度、流域治理和洪旱风险管理
  -> 洪水和干旱会改变死亡风险、疾病风险、迁移压力、价格和基础设施连续性
  -> 水资源治理失败会在 WASH 之前击穿主体持续性
```

## 关注对象

- 地表水、地下水、水库、流域、水文监测、水分配、水安全和跨部门用水。
- 洪水、干旱、河流预报、地下水枯竭、灌溉、城市雨洪和水基础设施韧性。
- 与 `water-sanitation-hygiene-continuity/` 的边界：WASH 域关注饮用水、卫生和污水服务；本域关注水资源和水文风险本身。
- 与 `weather-climate-observation-forecasting/` 的边界：天气域生成气象风险输入；本域关注水文系统、流域和水资源决策。

## Human Infra 模型链路

```text
水文观测和水资源治理
  -> 水量、水位、地下水、洪水和干旱风险可被识别
  -> 饮水、农业、能源、医疗、交通和住房系统获得调度窗口
  -> 洪旱暴露、断供、污染、迁移和恢复时间下降
  -> 主体持续性获得稳定水底座
```

## 非目标

- 不提供实时洪水逃生、船只通行、水库调度、工程设计、灌溉处方或法律水权建议。
- 不提供地下水开采、取水许可、跨境水争端、保险或农业投机建议。
- 不替代气象、水文、应急、水务或流域管理机构的官方信息。

## Source Signals

- WMO Water: https://wmo.int/topics/water
- World Bank Water Resources Management: https://www.worldbank.org/en/topic/waterresourcesmanagement
- UN-Water: https://www.unwater.org/

## 下一步

- 建立水资源变量表：可用水量、洪水暴露、干旱暴露、地下水、储水、调度、用水冲突和恢复时间。
- 整理 WMO、World Bank、UN-Water、国家水文机构和流域管理资料卡片。
- 与农业、WASH、能源、天气、灾害恢复和住房域建立接口。
