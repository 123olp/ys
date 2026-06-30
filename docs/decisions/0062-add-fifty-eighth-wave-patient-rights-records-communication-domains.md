# 0062. Add Fifty Eighth Wave Patient Rights Records Communication Domains

## Status

Accepted.

## Context

Human Infra 已经拆出门诊访问、临床服务执行、医疗支付、理赔、账单与成本保护连续性。但主体进入医疗系统之后，仍可能在患者门户、病历访问修正、结果通知、知情同意、语言沟通、残障便利、投诉救济和医疗民权层面被截断。

这些不是医疗服务可及性、保险支付或一般治理权利的重复项，而是医疗遭遇内部的主体可见性、理解权、表达权、纠错权、申诉权和反歧视条件。

## Decision

新增第 58 波 8 个患者权利、记录访问、临床沟通与医疗民权连续性域：

- `patient-portal-account-message-continuity`
- `medical-record-access-amendment-release-continuity`
- `clinical-results-notification-followup-continuity`
- `informed-consent-refusal-shared-decision-continuity`
- `healthcare-language-interpreter-effective-communication-continuity`
- `healthcare-disability-accommodation-accessibility-continuity`
- `patient-grievance-complaint-ombuds-continuity`
- `healthcare-civil-rights-nondiscrimination-continuity`

同步更新根 README、docs/domains 索引、domain map、research atlas、radar、applications/literature、ethics boundaries 和 repository structure check。

## Consequences

- 医疗链路从“服务可达”和“成本可承受”继续下钻到“主体在医疗制度内能否看见、理解、授权、拒绝、纠错、投诉和不被歧视”。
- 这些域只能整理公开资料、制度接口、失败模式和安全边界。
- 不提供医疗建议、法律意见、病历索取、HIPAA/ADA/Section 1557 个案判断、投诉代写、同意文件填写、门户设置或争议代理。

## Validation

- `tools/check_repository.py` 必须要求新增域 README/AGENTS 和 ADR 存在。
- `make check` 必须通过。
- 每个新增域必须能从 README、domain map、atlas、radar 和 ethics boundaries 找到入口。
