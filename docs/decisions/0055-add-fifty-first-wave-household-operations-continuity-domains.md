# 0055 Add Fifty First Wave Household Operations Continuity Domains

Date: 2026-06-30

## Status

Accepted

## Context

Human Infra 已覆盖个人数字操作、账号、设备、云服务和任务协调，但主体每天能否继续行动还依赖更本地、更物理的家庭运行条件：能否进入住所，家用设备是否可维护，食物能否安全冷藏和烹饪，衣物与卫生是否可持续，家庭环境能否清洁并控制害虫，邮件包裹能否抵达，住房和设备故障能否被可信维修。没有这层家庭物理操作系统，寿命、账号、文件和工具都可能在本地入口、食物、卫生、设备或维修断点上失效。

## Decision

新增第 51 波 8 个家庭物理运行连续性域：

- `home-access-lock-key-entry-continuity/`
- `household-appliance-maintenance-repair-continuity/`
- `home-refrigeration-food-storage-continuity/`
- `cooking-meal-preparation-kitchen-safety-continuity/`
- `laundry-clothing-footwear-hygiene-continuity/`
- `household-cleaning-disinfection-pest-control-continuity/`
- `postal-parcel-delivery-pickup-continuity/`
- `household-maintenance-repair-contractor-continuity/`

## Boundary

这些域只研究住所进入、家电维护、冷藏保鲜、烹饪备餐、衣物鞋履卫生、家庭清洁消毒害虫控制、邮件包裹接收和家庭维修服务如何影响主体任务执行连续性，不提供开锁、入侵、危险维修、燃气/电气施工、食品处置、化学品混合、杀虫剂使用、邮件拦截、冒领、承包商规避、个体购买建议、理赔策略或法律意见。

## Consequences

- `README.md`、`docs/README.md`、`domains/README.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md` 和 `tools/check_repository.py` 必须把这 8 个域纳入索引。
- 后续资料卡片应优先回到 NFPA、CPSC、DOE、ENERGY STAR、USDA FSIS、FDA、CDC、EPA、NPIC、Poison Help、USPS、UPU、FTC、FEMA 和本地住房/消费者保护资料。
- 家庭物理运行内容必须保持非操作化安全边界，只能讨论变量、证据、失败模式、治理和恢复路径。
