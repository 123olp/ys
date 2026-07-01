# 0112. Add One-Hundred-Seventh Wave Household Water Wastewater Execution Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖公共水务、公共饮水、应急饮水、灾后恢复、家庭维修和室内环境，但家庭端仍存在若干独立失败模式：私人井不是公共水厂，滤水器不是一次性保护，铅服务线需要采样通知和替换，建筑内部回流会破坏使用点安全，化粪池把污水处理责任下沉到家庭，地下室进水和潮湿恢复会把一次性水害变成长期住房损耗。

## Decision

新增 6 个正式研究域：

- `domains/private-well-water-testing-treatment-continuity/`
- `domains/household-water-treatment-filter-maintenance-continuity/`
- `domains/lead-service-line-lead-copper-drinking-water-continuity/`
- `domains/premise-plumbing-backflow-cross-connection-continuity/`
- `domains/septic-system-maintenance-sewage-backup-continuity/`
- `domains/basement-flooding-sump-pump-moisture-recovery-continuity/`

这些域共同构成“家庭水与污水执行连续性”视角，关注家庭端水源、处理、管线、回流、污水和水害恢复如何持续支撑饮水、烹饪、卫生、住房和健康。

## Boundaries

- 不提供水质结果判断、饮水许可、滤水器购买、井施工、管道施工、回流装置安装、化粪池维修、抽水操作、霉菌清理、保险索赔、法律责任或个案住房建议。
- 不替代 EPA、CDC、地方卫生/环境部门、水务公司、认证实验室、持证 plumber、septic professional、FEMA、保险或应急管理。
- 每个域必须保留 `water/wastewater state -> household dependency -> task -> continuity outcome` 的链路，而不是写成家庭维修教程。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `water-sanitation-hygiene-continuity`、`water-wastewater-utility-service-continuity`、`public-drinking-water-hydration-access-continuity`、`household-maintenance-repair-contractor-continuity` 和 `disaster-recovery-relief-continuity` 保持上下游关系，但不合并。
