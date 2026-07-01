# 0040 Add Thirty-Sixth Wave Planetary, Geophysical, and Heat-Risk Domains

## Status

Accepted

## Context

Human Infra 已经覆盖天气气候观测、建筑消防生命安全、灾害恢复、公用事业韧性和关键基础设施互依赖。但有效永生 / 主体持续性最大化的先验追问还会遇到一组低频高后果外部边界：空间天气、近地天体、火山灰、地震、海啸和极端高温。

这些对象不能只放进泛化 `risk-engineering/` 或 `emergency-preparedness-response/`，因为它们各自有独立监测体系、物理机制、预警窗口、基础设施失效模式和公共治理边界。

## Decision

新增 6 个正式研究域：

- `domains/c5-ecological-substrate/space-weather-geomagnetic-storm-resilience/`
- `domains/c6-local-unlocking/planetary-defense-near-earth-object-risk/`
- `domains/c5-ecological-substrate/volcanic-ashfall-geohazard-continuity/`
- `domains/c5-ecological-substrate/earthquake-seismic-risk-built-environment-continuity/`
- `domains/c5-ecological-substrate/tsunami-warning-coastal-evacuation-continuity/`
- `domains/c4-conversion-channel/extreme-heat-cooling-public-health-continuity/`

并同步更新：

- 根 `README.md` / `AGENTS.md`
- `domains/README.md` / `domains/AGENTS.md`
- `docs/README.md` / `docs/AGENTS.md`
- `docs/reference/domain-map.md`
- `docs/reference/research-domain-atlas.md`
- `docs/reference/research-domain-radar.md`
- `docs/reference/ethics-and-safety-boundaries.md`
- `docs/reference/applications-and-literature.md`
- `tools/check_repository.py`

## Boundary

这些域只做研究域建模、资料索引、证据分层和禁止用途维护。它们不提供实时预警、地震预测、海啸撤离路线、火山避难命令、太阳风暴操作建议、近地天体撞击预测、个人急救、建筑安全、工程设计、保险、投资或公共安全替代建议。

## Consequences

- Human Infra 的外部风险层从一般灾害叙事扩展到行星、地球物理和极端热风险。
- `weather-climate-observation-forecasting/`、`risk-engineering/`、`emergency-alerts-communications/`、`critical-infrastructure-lifeline-interdependency-resilience/` 和 `disaster-recovery-relief-continuity/` 的边界更清楚。
- 每个域都必须保留权威来源、适用范围和不可替代应急/工程/公共卫生机构的边界。
