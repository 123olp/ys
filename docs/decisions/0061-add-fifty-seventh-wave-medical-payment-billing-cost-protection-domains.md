# 0061 Add Fifty-Seventh-Wave Medical Payment Billing Cost Protection Domains

## Status

Accepted

## Context

Human Infra 已有 `insurance-risk-transfer`、`healthcare-access-continuity`、`pharmacy-benefit-formulary-prior-authorization-continuity` 和第 56 波门诊访问执行域。

这些域能解释风险池、医疗入口、处方药福利和门诊服务执行为什么重要，但仍缺少医疗支付执行层：主体如何参保续保、核验权益、穿过医疗服务授权、理解理赔和 EOB、承受账单、获得价格估算、受到意外账单保护，并在高额医疗债务前获得经济援助。

若这一层失败，医疗服务即使已经发生，也可能转化为债务、失保、拒付、延期治疗、行政负担和未来选择权损失。

## Decision

新增第 57 波 8 个医疗支付、理赔、账单与成本保护连续性域：

- `health-insurance-enrollment-renewal-continuity`
- `insurance-eligibility-benefits-verification-continuity`
- `medical-service-prior-authorization-utilization-management-continuity`
- `claims-adjudication-eob-denial-continuity`
- `patient-billing-payment-plan-continuity`
- `price-transparency-good-faith-estimate-continuity`
- `surprise-billing-balance-bill-protection-continuity`
- `charity-care-financial-assistance-medical-debt-continuity`

每个域只建立最小 `README.md` 和 `AGENTS.md`，同步更新根目录、docs、domain map、atlas、radar、applications、ethics 和 repository check，不新增数据目录、采集脚本或 Web 产品入口。

## Consequences

- Human Infra 能从“有保险/有医疗服务”继续追问到“覆盖是否持续、权益是否可核验、授权是否通过、理赔是否闭环、账单是否可承受、价格是否可预期、意外账单是否受保护、医疗债务是否有缓冲”。
- 医疗支付层被拆成独立执行接口，避免把高额成本和行政摩擦混入泛化的保险、财务或医疗可及叙事。
- 新域必须严格禁止个体保险建议、理赔/申诉代写、账单谈判、法律策略、信用修复、虚假材料、规避保险规则和敏感健康/保险/财务资料采集。

## Validation

- `python3 tools/check_repository.py`
- `git diff --check`
- `make check`
