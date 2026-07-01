# 0113. Add One-Hundred-Eighth Wave Household Energy Thermal Safety Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖公共电网、燃料服务、备电、CO 报警、消防、极端冷热、家庭水与污水等基础条件，但家庭内部仍存在独立执行层：电气线路和插座决定设备能否安全用电，供暖设备和排气决定冬季热支持是否安全，制冷和热泵决定高温下睡眠与慢病管理是否连续，燃气/丙烷决定高能量燃料接口是否可识别和专业恢复，温控器决定设备能力是否转化为真实室内温度，天气化与围护结构决定热量、湿气和空气交换是否长期可控。

## Decision

新增 6 个正式研究域：

- `domains/residential-electrical-wiring-outlet-safety-continuity/`
- `domains/home-heating-equipment-chimney-vent-maintenance-continuity/`
- `domains/home-cooling-heat-pump-air-conditioning-maintenance-continuity/`
- `domains/natural-gas-propane-leak-shutoff-continuity/`
- `domains/thermostat-temperature-control-thermal-comfort-continuity/`
- `domains/weatherization-insulation-air-sealing-thermal-envelope-continuity/`

这些域共同构成“家庭能源与热安全执行连续性”视角，关注住宅内部电气、供暖、制冷、燃气、温控和热边界如何持续支撑照明、通信、睡眠、照护、烹饪、医疗设备、工作学习和恢复。

## Boundaries

- 不提供电工维修、接线、配电箱操作、供暖/空调维修、燃气关阀、泄漏判断、冷媒操作、温控器安装、保温施工、通风设计、设备购买、能效审计、补贴申请、保险索赔、法律责任或个案住房建议。
- 不替代持证电工、HVAC 专业人员、燃气公司、丙烷供应商、消防部门、911、能源援助、地方建筑/电气/燃气规范、房东维修义务或公共卫生建议。
- 每个域必须保留 `household energy/thermal interface -> control/maintenance state -> task dependency -> continuity outcome` 的链路，而不是写成家庭维修教程。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `electric-grid-reliability-resilience-continuity`、`energy-access-resilience`、`fuel-thermal-energy-service-continuity`、`backup-power-battery-generator-safety-continuity`、`carbon-monoxide-alarm-combustion-appliance-safety-continuity`、`extreme-heat-cooling-public-health-continuity` 和 `winter-storm-cold-exposure-power-continuity` 保持上下游关系，但不合并。
