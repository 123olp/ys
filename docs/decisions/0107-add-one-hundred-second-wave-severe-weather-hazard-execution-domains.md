# ADR 0107: Add One-Hundred-Second Wave Severe Weather Hazard Execution Domains

## Status

Accepted.

## Context

Human Infra 已经有 `weather-climate-observation-forecasting/`、`household-emergency-preparedness-resilience/`、`emergency-alerts-communications/`、`disaster-recovery-relief-continuity/`、`earthquake-seismic-risk-built-environment-continuity/`、`tsunami-warning-coastal-evacuation-continuity/`、`volcanic-ashfall-geohazard-continuity/`、`extreme-heat-cooling-public-health-continuity/`、`wildfire-landscape-fire-resilience/` 和 `water-resources-hydrology-flood-drought-management/`。

这些域覆盖观测预报、通用家庭准备、灾后恢复、部分地球物理 hazard、极端热、景观野火和水文资源管理。但常见强天气和自然 hazard 中的“预警 -> 理解 -> 避险/撤离/就地庇护 -> 暴露控制 -> 服务连续性”仍缺少独立执行层。

从主体持续性看，自然 hazard 的关键不只是 hazard 是否存在，而是官方预警能否被主体接收、理解、信任，并转化为可执行行动。该层既不能被上游气象观测替代，也不能被下游灾后恢复替代。

## Decision

新增第 102 波 10 个 severe weather hazard execution continuity domains：

- `river-flash-flood-warning-evacuation-continuity/`
- `hurricane-storm-surge-evacuation-shelter-continuity/`
- `tornado-warning-safe-room-shelter-continuity/`
- `winter-storm-cold-exposure-power-continuity/`
- `drought-water-restriction-household-health-continuity/`
- `landslide-mudslide-debris-flow-warning-continuity/`
- `wildfire-smoke-clean-air-respiratory-continuity/`
- `thunderstorm-lightning-outdoor-safety-continuity/`
- `coastal-flooding-erosion-inundation-continuity/`
- `severe-weather-watch-warning-risk-communication-continuity/`

这些域共同覆盖洪水、飓风风暴潮、龙卷风、冬季风暴、干旱水限制、滑坡泥石流、野火烟雾、雷暴闪电、沿海洪水和强天气风险沟通。

## Boundaries

- 不发布实时预警、撤离路线、庇护点选择、道路判断、设施操作、工程方案、保险理赔、医疗急救或个案法律/金融建议。
- 不替代 NWS/NOAA、FEMA、CDC、EPA、USGS、Drought.gov、地方应急管理、公共卫生、交通、公用事业或公共安全机构。
- 不把官方安全材料改写成个体指令；只整理为 Human Infra 研究域、证据入口、变量链路和禁止用途边界。
- 不把这些域并入 `weather-climate-observation-forecasting/`，因为观测预报不等于行动执行。
- 不把这些域并入 `disaster-recovery-relief-continuity/`，因为灾后恢复不覆盖 hazard 到来前和到来时的短窗口保护行动。

## Source Signals

- NWS Weather Safety: https://www.weather.gov/safety/
- NWS Flood Safety: https://www.weather.gov/safety/flood
- NWS Hurricane Safety: https://www.weather.gov/safety/hurricane
- NWS Tornado Safety: https://www.weather.gov/safety/tornado
- NWS Winter Weather Safety: https://www.weather.gov/safety/winter
- NWS Lightning Safety: https://www.weather.gov/safety/lightning
- Ready.gov Alerts and natural hazards: https://www.ready.gov/alerts
- AirNow Wildfire Smoke: https://www.airnow.gov/wildfires/
- CDC Wildfires: https://www.cdc.gov/wildfires/
- EPA Wildfire Smoke and Indoor Air: https://www.epa.gov/indoor-air-quality-iaq/wildfires-and-indoor-air-quality-iaq
- USGS Landslide Hazards Program: https://www.usgs.gov/programs/landslide-hazards
- Drought.gov: https://www.drought.gov/
- NOAA High Tide Flooding: https://oceanservice.noaa.gov/facts/high-tide-flooding.html

## Consequences

- 自然 hazard 研究从“观测/准备/恢复”补齐到“执行动作转换层”。
- `domain-map.md`、`research-domain-atlas.md`、`research-domain-radar.md`、`ethics-and-safety-boundaries.md` 和 `applications-and-literature.md` 需要同步索引。
- `tools/check_repository.py` 必须把新增域 README/AGENTS 和本 ADR 纳入结构检查。
- 后续 source card 应优先整理官方来源术语、禁止用途、行动边界和与既有准备/恢复域的上下游关系。
