# 0111. Add One-Hundred-Sixth Wave Assistive Device Operational Continuity Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖屈光矫正、低视力、DME、康复、跌倒预防、睡眠呼吸和贴身耗材，但仍需要把若干高依赖度个人辅助设备拆成独立运行连续性域。原因是这些设备不是单纯治疗对象，也不是抽象“辅助技术”：它们有供电、适配、维修、耗材、供应商、运输、连接、通知和替换等待等独立失败模式。

## Decision

新增 6 个正式研究域：

- `domains/eyeglasses-prescription-repair-replacement-continuity/`
- `domains/wheelchair-scooter-battery-repair-access-continuity/`
- `domains/walker-cane-crutch-fit-maintenance-continuity/`
- `domains/prosthetic-limb-orthotic-fit-repair-continuity/`
- `domains/cpap-pap-device-mask-supply-power-continuity/`
- `domains/fall-detection-emergency-response-device-continuity/`

这些域共同构成“个人辅助设备运行连续性”视角，关注视觉、移动、身体-工具耦合、夜间呼吸支持和跌倒后求助链如何持续可用。

## Boundaries

- 不提供验光、设备处方、参数调整、康复训练、维修教程、品牌推荐、购买建议、医保/保险个案或急救分诊。
- 不替代 NEI、MedlinePlus、Medicare、CMS、CDC、FDA、NHLBI、康复专业人员、DME 供应商或 EMS。
- 每个域必须保留 `device state -> dependency -> task -> continuity outcome` 的链路，而不是写成产品清单。

## Consequences

- 根 README、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `assistive-technology-access`、`durable-medical-equipment-supplier-repair-continuity` 和疾病/康复域保持上下游关系，但不合并。
