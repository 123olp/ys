# 0099. Add Ninety-Fifth Wave Skin, Wound and Barrier Continuity Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已有 `skin-barrier-wound-healing/` 作为皮肤屏障与伤口愈合总域，但压力损伤、慢性伤口、伤口感染、糖尿病足、烧伤后恢复、手术切口、潮湿相关皮炎、湿疹、银屑病和皮肤护理用品分别对应不同的失效入口、证据来源、资源依赖和禁止用途。继续把它们放在一个总域中，会降低先验追问的精度。

## Decision

新增第九十五波 10 个皮肤屏障、伤口、压力损伤与皮肤病执行连续性研究域：

- `pressure-injury-prevention-repositioning-support-surface-continuity/`
- `chronic-wound-venous-diabetic-pressure-ulcer-continuity/`
- `wound-infection-cellulitis-sepsis-continuity/`
- `diabetic-foot-ulcer-amputation-prevention-continuity/`
- `burn-wound-aftercare-scar-function-continuity/`
- `surgical-wound-dehiscence-ssi-continuity/`
- `incontinence-associated-dermatitis-moisture-skin-continuity/`
- `eczema-atopic-dermatitis-itch-sleep-continuity/`
- `psoriasis-inflammatory-skin-systemic-burden-continuity/`
- `skin-care-supplies-dressings-barrier-products-continuity/`

每个域都必须包含 README 与 AGENTS，明确对象、Human Infra 链路、来源信号、非目标、上下游关系和禁止个体医疗建议边界。

## Consequences

- `skin-barrier-wound-healing/` 保持父域，不再承载所有执行层细节。
- 糖尿病足、压力损伤和伤口感染等域可以分别对接代谢、感觉、循环、照护、感染和康复系统。
- 后续可继续拆出皮肤癌、药疹、职业皮肤暴露、罕见皮肤病和皮肤微生物组等更细域。
