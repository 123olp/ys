# 0114. Add One-Hundred-Ninth Wave Household Waste Disposal Execution Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖家庭清洁消毒、灾后废弃物清理、危险材料总域、未用药回收、电池火灾和水污水公用事业，但家庭和邻里日常运行仍存在一个独立下游条件：任务产生的残余物必须离开居住空间或进入安全处置路径。日常固废收运、家庭危险废物、居家锐器、电子废弃物和电池、厨余堆肥、非法倾倒邻里卫生，分别对应不同证据来源、风险函数、服务入口和禁止用途。

## Decision

新增 6 个正式研究域：

- `domains/residential-solid-waste-collection-bin-sanitation-continuity/`
- `domains/household-hazardous-waste-chemical-disposal-continuity/`
- `domains/home-sharps-medical-waste-disposal-continuity/`
- `domains/e-waste-battery-recycling-disposal-continuity/`
- `domains/food-scrap-composting-pest-odor-continuity/`
- `domains/illegal-dumping-litter-neighborhood-sanitation-continuity/`

这些域共同构成“家庭废弃物与处置执行连续性”视角，关注生活垃圾、危险废物、医疗锐器、带电设备残余物、厨余和邻里异常废弃物如何影响卫生、安全、隐私、火灾、害虫、环境正义、资源循环和任务恢复。

## Boundaries

- 不提供垃圾分类执法规避、非法倾倒、焚烧、危险废物处理、化学混合、锐器处理、注射操作、电池拆解、损坏电池处置、堆肥配方、虫害处理、现场清理、邻里冲突、举报对抗、法律策略或个案住房建议。
- 不替代 EPA、FDA、CDC、地方固废部门、地方 HHW 项目、药房/医疗机构回收、物业、公共卫生、消防、环境执法、毒物控制、害虫控制、数据安全或法律渠道。
- 每个域必须保留 `waste stream -> container/pathway state -> risk/exposure/service state -> household/neighborhood task -> continuity outcome` 的链路，而不是写成处理教程或地方服务目录。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `household-cleaning-disinfection-pest-control-continuity`、`waste-management-hazardous-materials-continuity`、`disaster-debris-waste-sanitation-cleanup-continuity`、`unused-medicine-takeback-disposal-continuity` 和 `battery-thermal-runaway-fire-hazard-continuity` 保持上下游关系，但不合并。
