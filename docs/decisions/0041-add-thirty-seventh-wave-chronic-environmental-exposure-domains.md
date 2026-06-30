# 0041 Add Thirty-Seventh Wave Chronic Environmental Exposure Domains

## Status

Accepted

## Context

Human Infra 已经覆盖空气质量、职业暴露、住房稳定、化学安全、感染监测、气候风险和灾害恢复。但有效永生 / 主体持续性最大化的先验追问还会遇到一组更日常、更慢性的环境损耗条件：噪声、光照节律、铅与重金属、氡与石棉、霉菌潮湿、病媒传播风险。

这些对象不能只并入一般 `air-quality-ventilation-exposure-control/`、`occupational-exposure-industrial-hygiene/` 或 `chemical-safety-poison-control-toxicology/`，因为它们各自有独立暴露机制、健康终点、监管体系、空间分布和公共治理边界。

## Decision

新增 6 个正式研究域：

- `domains/noise-exposure-acoustic-environment-continuity/`
- `domains/light-exposure-circadian-environment-continuity/`
- `domains/lead-heavy-metal-exposure-control/`
- `domains/radon-asbestos-indoor-hazard-continuity/`
- `domains/mold-dampness-indoor-biological-exposure/`
- `domains/vector-borne-disease-environmental-control/`

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

这些域只做研究域建模、资料索引、证据分层和禁止用途维护。它们不提供个体医疗诊断、检测解释、采样方案、设备购买、施工改造、农药操作、房产判断、法律索赔、现场处置、旅行安全、工作许可或公共机构替代建议。

## Consequences

- Human Infra 的外部环境层从急性灾害扩展到慢性日常暴露和微损耗条件。
- `air-quality-ventilation-exposure-control/`、`occupational-exposure-industrial-hygiene/`、`housing-built-environment-stability/`、`chemical-safety-poison-control-toxicology/` 和 `immunization-public-health-surveillance/` 的边界更清楚。
- 每个域都必须保留官方来源、适用对象、暴露边界、系统责任和禁止个人化建议的规则。
