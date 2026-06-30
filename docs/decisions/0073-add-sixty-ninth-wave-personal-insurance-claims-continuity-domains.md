# ADR 0073: Add Sixty-Ninth-Wave Personal Insurance and Claims Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经有 `insurance-risk-transfer` 总域，也已经覆盖医疗保险参保、医疗理赔、寿险理赔、算法化保险承保和部分公共权益记录。但主体持续性中的风险转移并不只发生在医疗、寿险或公共福利里。车辆事故、住房火灾、盗窃、洪水、野火、地震、旅行中断、长期照护、残障收入和高额责任事件都会把主体的现金流、住房、移动能力、照护能力和未来选择权推入突发损失状态。

这些对象不能只放进 `insurance-risk-transfer`、`health-insurance-enrollment-renewal-continuity`、`claims-adjudication-eob-denial-continuity` 或 `life-insurance-beneficiary-claim-continuity`。总保险域关注风险池概念；医疗支付域关注医疗服务；寿险域关注死亡后的受益人理赔。本波关注的是非医疗个人保险和财产责任保险如何在损失发生后通过保单、coverage、deductible、claim、adjuster、proof of loss、appeal、complaint 和法律防御把冲击转化为可恢复过程。

## Decision

新增第 69 波 8 个个人保险、财产责任、灾害与理赔执行连续性域：

- `auto-insurance-liability-collision-claims-continuity`
- `homeowners-renters-property-insurance-claims-continuity`
- `flood-insurance-nfip-claims-continuity`
- `catastrophe-wind-wildfire-earthquake-insurance-continuity`
- `disability-income-insurance-claim-continuity`
- `long-term-care-insurance-benefit-activation-continuity`
- `travel-insurance-trip-protection-claims-continuity`
- `personal-liability-umbrella-insurance-defense-continuity`

## Consequences

- Human Infra 能把风险转移执行层拆成可审查域：汽车事故、住房财产、洪水、巨灾、残障收入、长期照护、旅行中断和个人责任防御。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明；不提供投保、保额选择、理赔、appeal、止损、法律防御、搬迁、灾害援助、保险欺诈、金融规划或法律建议。
- 后续若新增 NAIC、FEMA/NFIP、州保险监管机构、Ready.gov、U.S. DOT、CDC、State Department 或州法院资料，应优先进入对应细分域；只有医疗 claim 回到 `claims-adjudication-eob-denial-continuity`，只有死亡后寿险理赔回到 `life-insurance-beneficiary-claim-continuity`，只有算法化承保评分回到 `insurance-underwriting-algorithmic-risk-scoring-continuity`。
