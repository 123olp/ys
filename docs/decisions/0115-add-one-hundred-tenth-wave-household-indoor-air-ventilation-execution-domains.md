# 0115. Add One-Hundred-Tenth Wave Household Indoor Air Ventilation Execution Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖空气质量总域、暴发通风过滤、野火烟雾清洁空气房、霉菌潮湿、家庭能源热安全、CO 报警和家庭废弃物处置。但家庭端室内空气仍存在一组独立执行层：滤网是否维护、房间级过滤是否可用、烹饪是否能排风、湿度是否可控、灰尘过敏原是否能源控制、VOC/香氛/产品释放是否能减少。这些不是抽象空气质量，也不是 HVAC 工程、医疗诊断或产品购买，而是居住空间能否持续支持睡眠、学习、工作、照护和恢复的低层接口。

## Decision

新增 6 个正式研究域：

- `domains/c3-generation-engine/home-hvac-filter-maintenance-indoor-air-continuity/`
- `domains/c3-generation-engine/portable-air-cleaner-room-filtration-continuity/`
- `domains/c3-generation-engine/cooking-ventilation-range-hood-indoor-air-continuity/`
- `domains/c5-ecological-substrate/home-humidity-dehumidifier-moisture-control-continuity/`
- `domains/c5-ecological-substrate/household-dust-allergen-source-control-continuity/`
- `domains/c5-ecological-substrate/household-voc-fragrance-product-emission-continuity/`

这些域共同构成“家庭室内空气与通风执行连续性”视角，关注室内空气管理如何在家庭端拆成滤网、房间过滤、烹饪排风、湿度、过敏原源控制和产品释放源控制这些可执行、可维护、可失败的基础设施。

## Boundaries

- 不提供 HVAC 设计维修、滤网/净化器购买、CADR/MERV 处方、抽油烟机安装、燃气维修、湿度处方、霉菌清理、过敏诊断、药物建议、化学检测判读、装修施工、产品推荐、现场安全认证、租房纠纷、保险或法律建议。
- 不替代 EPA、CDC、DOE、ASHRAE、USFA、地方公共卫生、住房部门、物业、HVAC 专业人员、医疗人员、毒物控制、消防或环境检测机构。
- 每个域必须保留 `household indoor-air interface -> source/control/maintenance state -> occupant task burden -> continuity outcome` 的链路，而不是写成设备指南、家装教程、医疗建议或产品导购。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `air-quality-ventilation-exposure-control`、`indoor-ventilation-filtration-outbreak-control-continuity`、`wildfire-smoke-clean-air-respiratory-continuity`、`mold-dampness-indoor-biological-exposure`、`home-cooling-heat-pump-air-conditioning-maintenance-continuity`、`home-heating-equipment-chimney-vent-maintenance-continuity`、`carbon-monoxide-alarm-combustion-appliance-safety-continuity` 和 `household-cleaning-disinfection-pest-control-continuity` 保持上下游关系，但不合并。
