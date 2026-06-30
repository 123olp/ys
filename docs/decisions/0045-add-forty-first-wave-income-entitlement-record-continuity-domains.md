# 0045 Add Forty First Wave Income Entitlement Record Continuity Domains

Status: Accepted

Date: 2026-06-30

## Context

Human Infra 已经覆盖劳动权利、就业服务、金融包容、算法化准入、福利递送、保险风险转移和资格证明，但仍缺少一组专门处理“主体如何把过去劳动、缴费、纳税、受伤和账户记录持续转化为未来权益”的研究域。

这些对象不能只放进金融、福利、劳动权利或身份域：工资与雇佣记录、税务记录、社会保险收入记录、退休计划、失业保险工资记录和工伤记录各自有独立报送系统、行政账户、纠错路径、隐私边界、欺诈风险、申诉机制和长期权益映射。

## Decision

新增第 41 波 6 个正式研究域：

- `income-payroll-employment-record-continuity/`
- `tax-administration-filing-record-continuity/`
- `social-security-earnings-benefit-record-continuity/`
- `retirement-pension-savings-plan-continuity/`
- `unemployment-insurance-wage-record-continuity/`
- `workers-compensation-occupational-injury-benefit-continuity/`

同步更新根目录 README、AGENTS、`domains/` 索引、`docs/reference/` 地图、radar、atlas、应用文献、安全边界和 `tools/check_repository.py`。

## Boundary

这些域只做工资/雇佣记录、税务记录、社会保险收入与福利记录、退休计划、失业保险工资记录和工伤职业病权益记录的公开资料、机制、证据、纠错、可携带性、隐私、行政负担、反欺诈和禁止用途整理，不提供税务申报、工资索赔、福利申请、退休规划、投资、失业保险申领、工伤索赔、医疗诊断、法律、财务、移民、保险或个人案件建议。

## Consequences

Human Infra 的“主体持续性”从资格证明进一步扩展到权益证明层：主体不只需要证明自己是谁、会什么、被授权做什么，也需要让过去劳动、缴费、纳税、失业和工作伤害记录在未来仍能被制度承认、纠错、保护并转化为资源与保障。
