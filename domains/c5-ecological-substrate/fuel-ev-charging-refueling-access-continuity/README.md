# Fuel EV Charging Refueling Access Continuity

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
