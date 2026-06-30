# 0042 Add Thirty Eighth Wave Decision Authority Fiduciary Continuity Domains

Status: Accepted

Date: 2026-06-30

## Context

Human Infra 已经覆盖法律身份、司法可及、患者倡导、数字遗产、照护、福利和金融接入，但仍缺少一组专门处理“主体暂时或长期无法亲自决策和执行任务时，谁能在何种边界下延续其意愿、访问、资源和责任”的域。

这些问题不能简单放进医疗、法律援助、数字身份或福利域：医疗代理、支持性决策、HIPAA personal representative、财务授权、代表收款人和事务继承分别有独立制度、文件、角色、监督、滥用风险和禁止用途。

## Decision

新增第 38 波 6 个正式研究域：

- `advance-care-planning-medical-decision-continuity/`
- `supported-decision-making-guardianship-rights/`
- `healthcare-personal-representative-hipaa-access-continuity/`
- `financial-fiduciary-power-of-attorney-continuity/`
- `representative-payee-benefits-management-continuity/`
- `trust-estate-affairs-succession-continuity/`

同步更新根目录 README、AGENTS、`domains/` 索引、`docs/reference/` 地图、radar、atlas、应用文献、安全边界和 `tools/check_repository.py`。

## Boundary

这些域只做资料、角色、制度、风险和边界整理，不提供个案医疗、法律、财务、税务、投资、福利、遗产、授权表填写、法院策略、隐私投诉、资格判断、资产分配、账户转移或家庭纠纷建议。

## Consequences

Human Infra 的“主体持续性”从身体、认知、环境和服务连续性进一步扩展到失能、不能表达和死亡边界附近的决策权、代理权、受托责任、资料访问、收入管理和事务继承连续性。
