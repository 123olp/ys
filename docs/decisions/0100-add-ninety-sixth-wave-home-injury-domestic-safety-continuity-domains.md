# 0100 Add Ninety Sixth Wave Home Injury Domestic Safety Continuity Domains

## Status

Accepted

## Context

Human Infra 已有 `fall-risk-prevention-home-safety-continuity/`、`building-fire-life-safety-codes/`、`chemical-safety-poison-control-toxicology/`、`product-safety-recall-systems/` 和家庭物理运行域，但居家伤害预防的执行层仍过宽：浴室、楼梯、夜间路径、卧室转移、烟雾报警、一氧化碳报警、家具倾倒、家庭毒物、窗饰拉绳和热水烫伤拥有不同官方来源、风险窗口、材料接口、照护场景和禁止用途。

## Decision

新增第九十六波 10 个居家伤害预防与家庭安全执行连续性域：

- `bathroom-bathing-toileting-transfer-fall-safety-continuity/`
- `stairs-steps-handrail-threshold-fall-safety-continuity/`
- `home-lighting-nighttime-pathway-visibility-continuity/`
- `bedroom-bed-transfer-entrapment-safety-continuity/`
- `smoke-alarm-home-fire-escape-readiness-continuity/`
- `carbon-monoxide-alarm-combustion-appliance-safety-continuity/`
- `furniture-tv-tip-over-anchoring-child-safety-continuity/`
- `household-poison-storage-child-resistant-packaging-continuity/`
- `window-covering-cord-strangulation-child-safety-continuity/`
- `hot-water-scald-burn-prevention-continuity/`

## Consequences

- 家居安全不再只作为宽泛“跌倒预防”或“建筑消防”存在，而是拆成可索引、可审查、可保持禁止用途边界的执行层。
- 每个域只做公开资料整理、变量建模和证据边界，不提供施工、产品推荐、家庭改造、急救、儿童监控、保险、法律或个体安全建议。
- 根目录、`domains/`、`docs/reference/` 和结构检查脚本必须同步索引。
