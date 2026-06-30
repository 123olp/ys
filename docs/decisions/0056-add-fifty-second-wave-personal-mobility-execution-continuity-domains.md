# 0056 Add Fifty Second Wave Personal Mobility Execution Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已覆盖交通可及、公共交通运营、道路安全、驾照车辆登记、能源和城市规划，但主体每天能否真实到达医疗、工作、照护、学习、食物和公共服务，还依赖更细的个人移动执行层：车辆是否可维护，燃料或充电是否可得，停车与路缘是否可用，步行骑行和微移动是否安全，paratransit/NEMT 是否可靠，出租车/网约车/需求响应交通是否可用，票卡/过路费/移动支付是否不中断，路线规划和实时导向信息是否可信。没有这层执行系统，宏观交通服务会停留在名义存在，不能稳定转化为主体行动。

## Decision

新增第 52 波 8 个个人移动执行连续性域：

- `personal-vehicle-maintenance-recall-repair-continuity/`
- `fuel-ev-charging-refueling-access-continuity/`
- `parking-curb-access-towing-impound-continuity/`
- `walking-bicycling-micromobility-continuity/`
- `paratransit-nemt-access-continuity/`
- `taxi-rideshare-demand-response-mobility-continuity/`
- `transit-fare-payment-toll-account-continuity/`
- `multimodal-trip-planning-real-time-wayfinding-continuity/`

## Boundary

这些域只研究个人车辆维护召回、燃料/充电入口、停车路缘拖车扣押、步行骑行微移动、ADA paratransit 与 NEMT、出租车网约车需求响应交通、交通票卡/过路费/账户、路线规划实时信息如何影响主体移动任务连续性，不提供车辆维修步骤、危险燃料处理、充电桩破解、逃避停车执法、交通违法、共享设备破解、NEMT 资格规避、报销欺诈、平台规避、逃票、票卡破解、过路费规避、路线跟踪或个案申诉/法律策略。

## Consequences

- `README.md`、`docs/README.md`、`domains/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md` 和 `tools/check_repository.py` 必须把这 8 个域纳入索引。
- 后续资料卡片应优先回到 NHTSA、DOE/AFDC、Energy.gov、FTA、FHWA、ADA.gov、Medicaid.gov、GTFS、CFPB、FDIC、FTC、MUTCD 和本地交通/消费者保护资料。
- 移动执行内容必须保持非操作化安全边界，只能讨论变量、证据、失败模式、治理和恢复路径。
