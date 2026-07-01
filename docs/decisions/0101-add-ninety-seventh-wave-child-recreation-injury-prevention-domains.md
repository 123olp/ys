# 0101 Add Ninety Seventh Wave Child Recreation Injury Prevention Domains

## Status

Accepted

## Context

Human Infra 已有道路交通、居家伤害、儿童保护、TBI、公园娱乐和产品安全域，但儿童、运动和娱乐活动中的伤害预防仍被分散在过宽的上位桶里。溺水、泳池/水疗池屏障、船艇、儿童乘员约束、轮式运动头部伤害、游乐场、运动脑震荡、婴儿安全睡眠、枪支安全储存和 ATV/OHV 各自拥有不同官方来源、风险窗口、执行主体、证据边界和禁止用途。

## Decision

新增第九十七波 10 个儿童、运动与娱乐伤害预防执行连续性域：

- `drowning-water-safety-supervision-continuity/`
- `pool-spa-barrier-drain-entrapment-safety-continuity/`
- `boating-life-jacket-watercraft-safety-continuity/`
- `child-passenger-safety-car-seat-restraint-continuity/`
- `bicycle-helmet-wheeled-sports-head-injury-prevention-continuity/`
- `playground-surface-equipment-fall-injury-prevention-continuity/`
- `sports-concussion-return-to-play-protocol-continuity/`
- `infant-safe-sleep-suid-risk-reduction-continuity/`
- `firearm-safe-storage-injury-prevention-continuity/`
- `atv-off-highway-vehicle-injury-prevention-continuity/`

## Consequences

- 儿童、运动和娱乐伤害不再只放在宽泛安全或娱乐域中，而是拆成能被索引、审查和治理的执行层。
- 每个域只做公开资料整理、变量建模、来源信号和禁止用途边界，不提供救援、驾驶、武器、产品、施工、医疗、法律、保险或个体活动建议。
- 根目录、`domains/`、`docs/reference/` 和结构检查脚本必须同步索引。
