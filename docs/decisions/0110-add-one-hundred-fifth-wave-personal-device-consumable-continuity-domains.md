# 0110 Add One Hundred Fifth Wave Personal Device Consumable Continuity Domains

## Status

Accepted

## Context

Human Infra 的先验追问继续从“主体如何持续行动”下钻到更低层的日常耗材、贴身设备和适配物。已有 `laundry-clothing-footwear-hygiene-continuity/` 覆盖衣物、鞋履、洗衣和一般卫生，但它不能承载隐形眼镜感染、助听设备维护、月经用品、失禁吸收用品、糖尿病治疗鞋/卸载、压迫用品这些具有独立证据体系、失败模式和伦理边界的窄域。

这些对象的共同点是：它们看似是“用品”，实际是把感官、排泄、移动、皮肤、体液回流、尊严和公共空间参与维持住的低层基础设施。

## Decision

新增第 105 波 6 个研究域：

- `contact-lens-hygiene-eye-infection-continuity/`
- `hearing-aid-maintenance-battery-access-continuity/`
- `menstrual-product-access-safety-continuity/`
- `incontinence-absorbent-product-supply-dignity-continuity/`
- `diabetic-therapeutic-footwear-offloading-continuity/`
- `compression-garment-lymphedema-venous-continuity/`

## Boundaries

- 不把这些域写成购买指南、产品推荐、设备调参、医保个案、诊断治疗或照护操作建议。
- 不替代眼科、听力学、妇科、泌尿、足病、伤口、淋巴水肿治疗、DME 供应商或公共卫生指导。
- 不把贴身耗材、设备记录、月经/失禁状态或残障辅助用品变成监控、羞辱、资格排除或服务惩罚工具。

## Consequences

- Human Infra 的“主体持续性”地图从衣物卫生大域进一步细分到个人设备和耗材运行层。
- 这些域补齐了感官输入、排泄尊严、足部移动、体液回流和贴身用品供应的独立断点。
- 后续可在定量模型中加入 `supply continuity`、`fit continuity`、`maintenance latency`、`dignity loss`、`participation interruption` 和 `infection/risk escalation` 等变量。
