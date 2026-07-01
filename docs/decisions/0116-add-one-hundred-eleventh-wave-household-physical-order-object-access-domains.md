# 0116. Add One-Hundred-Eleventh Wave Household Physical Order Object Access Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖家庭伤害、家庭水电热、废弃物和室内空气执行层，但家庭空间还有一组更低层的物理秩序与物品访问接口：通道是否被杂物占用，线缆是否穿越路径，储物系统是否稳定，高处任务是否可达，居家办公工位是否适配人体，儿童玩具小零件是否被分区和召回。这些不是抽象“家居安全”，也不是收纳、装修、产品导购或医疗处方，而是主体在家庭内完成移动、学习、工作、照护、清洁、维修和儿童活动时持续消耗的基础摩擦层。

## Decision

新增 6 个正式研究域：

- `domains/home-clutter-pathway-trip-fall-continuity/`
- `domains/household-cord-cable-trip-entanglement-continuity/`
- `domains/home-shelving-cabinet-storage-stability-continuity/`
- `domains/household-ladder-step-stool-reach-task-continuity/`
- `domains/home-office-workstation-ergonomics-continuity/`
- `domains/toy-small-parts-choking-ingestion-continuity/`

这些域共同构成“家庭物理秩序、物品访问与执行摩擦连续性”视角，关注家庭空间中的物品流、连接线、储物、够取、高负荷工位和儿童小零件如何改变主体行动半径、有效时间、注意力、照护负担和伤害风险。

## Boundaries

- 不提供家庭改造、收纳服务、产品购买、梯子操作、电气维修、家具安装、货架承重、儿童监控、急救、医疗诊断、工伤法律、托育合规、保险或现场安全认证。
- 不替代 CDC、NIA、CPSC、OSHA、NIOSH、USFA、Poison Help、职业治疗师、医疗人员、消防、电工、物业、托育监管或产品召回系统。
- 每个域必须保留 `household physical interface -> exposure/access/friction state -> task burden/safety outcome -> continuity outcome` 的链路，而不是写成清洁整理教程、装修指南、产品导购、医疗建议或个案安全判断。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `fall-risk-prevention-home-safety-continuity`、`home-lighting-nighttime-pathway-visibility-continuity`、`furniture-tv-tip-over-anchoring-child-safety-continuity`、`window-covering-cord-strangulation-child-safety-continuity`、`residential-electrical-wiring-outlet-safety-continuity`、`human-factors-ergonomics-task-system-continuity`、`product-safety-recall-systems` 和 `household-cleaning-disinfection-pest-control-continuity` 保持上下游关系，但不合并。
