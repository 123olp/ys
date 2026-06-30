# 0043 Add Thirty Ninth Wave Algorithmic Access Screening Domains

Status: Accepted

Date: 2026-06-30

## Context

Human Infra 已经覆盖金融、住房、就业、保险、福利、数据治理和 AI 审计，但仍缺少一组专门处理“主体进入这些系统之前，被报告、筛查、评分、匹配和自动化资格判定拦截”的域。

这些对象不能只放进对应服务域：信用报告、租房筛查、背景记录筛查、招聘算法、保险算法评分和公共福利自动资格系统各自有独立数据来源、准入机制、错误模式、监管边界、申诉路径和禁止用途。

## Decision

新增第 39 波 6 个正式研究域：

- `credit-consumer-reporting-access-continuity/`
- `tenant-screening-rental-access-continuity/`
- `background-check-record-screening-continuity/`
- `employment-algorithmic-hiring-screening-continuity/`
- `insurance-underwriting-algorithmic-risk-scoring-continuity/`
- `public-benefits-eligibility-automated-decision-continuity/`

同步更新根目录 README、AGENTS、`domains/` 索引、`docs/reference/` 地图、radar、atlas、应用文献、安全边界和 `tools/check_repository.py`。

## Boundary

这些域只做准入判定机制、资料来源、错误模式、权利边界、申诉/更正结构和禁止用途整理，不提供信用修复、租房、就业、背景调查规避、保险、福利、法律、税务、投资、申诉策略、资格判断、产品选择或个案行动建议。

## Consequences

Human Infra 的“主体持续性”从服务可及进一步扩展到服务入口前的判定层：主体能否进入金融、住房、工作、保险和福利系统，取决于可观察、可纠错、可监督、可申诉的报告、筛查和自动化资格基础设施。
