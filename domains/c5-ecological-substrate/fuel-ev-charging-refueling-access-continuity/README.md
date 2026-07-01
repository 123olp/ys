# Fuel EV Charging Refueling Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/fuel-ev-charging-refueling-access-continuity` |
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


`fuel-ev-charging-refueling-access-continuity` 研究汽油、柴油、替代燃料、EV 充电、支付、站点可达性、停电、排队、价格波动和应急燃料如何影响主体移动任务能否持续。

> 核心问题：车能动不等于路能走；如果燃料或充电入口断裂，医疗、工作、照护、撤离和关键物资获取都会被能源入口截断。

## 关注对象

- 加油站、EV 充电站、替代燃料站、家庭充电、公共充电、支付账户、连接器、站点可用性和排队。
- 停电、灾害、价格冲击、燃料短缺、低收入能源负担、长距离出行和撤离场景。
- 与能源韧性、电网、燃料服务、交通、家庭应急和财务韧性的接口。

## Human Infra 链路

```text
移动能源入口连续
  -> 车辆和微移动工具可被持续供能
  -> 医疗、工作、照护、采购和撤离任务不会被燃料/充电断点截断
  -> 移动系统从设备拥有转化为可执行路径
  -> 主体行动半径和危机恢复能力增强
```

## 非目标

- 不提供燃料储存、危险加注、绕过充电计费、盗电、破解充电桩、规避排队或应急燃料囤积建议。
- 不替代 DOE、AFDC、能源公司、充电网络、消防、应急管理、保险或专业电工。
- 不收集车辆位置、充电账户、支付凭证、家庭电气信息或站点运营敏感数据。

## Source Signals

- DOE Alternative Fuels Data Center: https://afdc.energy.gov/
- DOE Alternative Fueling Station Locator: https://afdc.energy.gov/stations
- Energy.gov Electric Vehicles: https://www.energy.gov/energysaver/electric-vehicles
- Ready.gov Power Outages: https://www.ready.gov/power-outages

## 下一步

- 建立 `trip need -> vehicle energy type -> station/charger availability -> payment -> recovery option` 变量表。
- 区分日常通勤、长途出行、灾害撤离、医疗出行和低收入能源负担。
- 与 `electric-grid-reliability-resilience-continuity`、`fuel-thermal-energy-service-continuity`、`energy-access-resilience` 和 `transportation-access-mobility` 建立边界。
