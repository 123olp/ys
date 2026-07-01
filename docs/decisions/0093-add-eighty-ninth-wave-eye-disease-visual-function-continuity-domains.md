# ADR 0093: Add Eighty-Ninth-Wave Eye Disease Visual-Function Continuity Domains

## Status

Accepted

## Date

2026-07-01

## Context

Human Infra 已经有 `vision-eye-health-continuity/` 作为视觉总域，但白内障、青光眼、糖尿病视网膜病变、年龄相关性黄斑变性、屈光不正、低视力康复、干眼、眼外伤、儿童弱视筛查和视网膜脱离具有不同机制、时间窗口、服务入口、证据来源、功能后果和禁止用途边界。如果继续只放在泛视觉域中，后续 Source Card、模型变量、可视化和安全边界会把可恢复视觉、不可逆视野、代谢性视网膜损伤、中央视觉、基础矫正、补偿康复、慢性眼表摩擦、急性伤害、儿童发育窗口和急性转诊混成一个概念桶。

官方资料来源包括 National Eye Institute 的 cataract、glaucoma、diabetic retinopathy、age-related macular degeneration、refractive errors、low vision、dry eye、eye injuries、amblyopia、retinal detachment resources，以及 CDC Vision Health 和 WHO blindness / visual impairment 资料。

## Decision

新增第八十九波 10 个正式研究域：

- `domains/cataract-vision-restoration-continuity/`
- `domains/glaucoma-visual-field-protection-continuity/`
- `domains/diabetic-retinopathy-screening-treatment-continuity/`
- `domains/age-related-macular-degeneration-central-vision-continuity/`
- `domains/refractive-error-glasses-contact-lens-continuity/`
- `domains/low-vision-rehabilitation-assistive-technology-continuity/`
- `domains/dry-eye-ocular-surface-comfort-continuity/`
- `domains/eye-injury-urgent-vision-protection-continuity/`
- `domains/pediatric-vision-screening-amblyopia-continuity/`
- `domains/retinal-detachment-urgent-referral-continuity/`

每个域只创建 `README.md` 和 `AGENTS.md`。本轮不创建诊断工具、验光处方、眼底图判读、AI 筛查结论、设备推荐、眼科手术建议、急诊分诊、儿童家庭治疗方案、产品推荐、驾驶/工作资格判断或个体医疗系统。

## Consequences

- 视觉输入从总域扩展为可恢复视觉、不可逆视野保护、代谢视网膜筛治、中央视觉、基础屈光矫正、低视力补偿、眼表舒适、急性眼伤、儿童视觉发育和急性视网膜转诊这些可独立审查的持续性条件。
- 后续证据卡可以分别追踪视觉清晰度、视野、眼底筛查、中央视力、矫正可及性、任务补偿、屏幕耐受、眼部防护、儿童筛查和急转窗口。
- 所有相关资料必须保留来源、适用对象、不确定性和禁止用途。
- 仓库结构检查必须把 10 个新目录、20 个新域文件和本 ADR 纳入 required set。
