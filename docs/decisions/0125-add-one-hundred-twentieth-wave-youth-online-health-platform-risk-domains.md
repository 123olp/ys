# 0125. Add One Hundred Twentieth Wave Youth Online Health Platform Risk Domains

## Status

Accepted

## Context

已有 `online-safety-digital-harm-prevention` 和 `children-teen-data-privacy-consent-continuity` 提供上位边界，但儿童青少年在线环境中的心理健康、平台安全设计、网络霸凌、线上性剥削、游戏商业机制和隐性广告各自有独立资料来源、伤害机制、平台接口和禁止用途。继续把这些问题留在一个总域内，会让风险链条难以审查，也难以解释它们如何影响注意力、睡眠、学习、关系、家庭资源和未来选择权。

## Decision

新增第 120 波儿童青少年线上健康与平台风险连续性研究域：

- `youth-social-media-mental-health-continuity/`
- `youth-online-safety-by-design-platform-governance-continuity/`
- `cyberbullying-online-harassment-reporting-continuity/`
- `online-child-sexual-exploitation-sextortion-reporting-continuity/`
- `gaming-loot-box-inapp-purchase-dark-pattern-continuity/`
- `child-stealth-advertising-influencer-marketing-continuity/`

这些域定位为未成年人数字环境的风险与治理接口，不提供心理诊断、危机干预、平台操作、法律申诉、个案调查、年龄规避、家长控制绕过、营销策略、平台规避、儿童内容处理或任何可能造成二次伤害的操作建议。

## Consequences

- `online-safety-digital-harm-prevention` 保持上位总域，新域承担高风险机制拆分。
- `children-teen-data-privacy-consent-continuity` 继续负责 COPPA、同意、年龄适配和数据足迹，新域侧重心理健康、安全设计、举报、消费与广告机制。
- 根 `README.md`、根 `AGENTS.md`、`domains/README.md`、`domains/AGENTS.md`、`docs/README.md`、`docs/AGENTS.md`、`docs/reference/domain-map.md`、`docs/reference/research-domain-atlas.md`、`docs/reference/research-domain-radar.md`、`docs/reference/applications-and-literature.md` 和 `docs/reference/ethics-and-safety-boundaries.md` 必须包含第 120 波入口或边界说明。
- `tools/check_repository.py` 必须把新域 README、AGENTS 和本决策纳入 required 文件检查。
