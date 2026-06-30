# ADR 0063: Add Fifty-Ninth-Wave Emergency Health Handoff Domains

## Status

Accepted.

## Context

Human Infra 已经覆盖患者权利、病历访问、知情同意、医疗代理、急救系统、灾害准备和慢病照护，但仍缺少一组专门处理“主体在急救、灾害、失能或无法表达时，哪些最小健康信息必须被看见、携带、确认和转交”的研究域。

这些对象不能只归入 `emergency-medical-services-prehospital-care`、`medical-record-access-amendment-release-continuity`、`medication-reconciliation-regimen-adherence-continuity` 或 `emergency-preparedness-response`。那些域分别关注系统响应、病历权利、常规用药一致性和家庭/社区准备；本波关注的是急救交接窗口中的个人关键资料、通知链、风险标签和预置行动条件。

## Decision

新增第 59 波 8 个急救健康信息与紧急交接连续性域：

- `emergency-contact-next-of-kin-notification-continuity`
- `personal-health-record-emergency-summary-continuity`
- `medical-id-allergy-critical-alert-continuity`
- `medication-list-implant-device-emergency-continuity`
- `chronic-condition-emergency-action-plan-continuity`
- `immunization-record-proof-continuity`
- `organ-donor-registry-anatomical-gift-continuity`
- `access-functional-needs-emergency-registry-continuity`

## Consequences

- Human Infra 能从“医疗系统能不能响应”继续追问到“主体无法表达时，关键联系人、健康摘要、过敏和关键病情、药物和植入设备、慢病行动计划、免疫记录、器官捐赠意愿和功能需求能否被可靠读取与转交”。
- 这些域只做公开资料整理、结构建模、证据边界和禁止用途声明，不提供个人急救、医疗解释、病历整理、联系通知、器官捐赠登记、法律、灾害报名或临床决策建议。
- 后续若新增急救卡、医疗 ID、免疫凭证、设备清单、特殊需求登记或器官捐赠资料，应先进入本波对应域，而不是散落在宽泛急救或医疗记录域中。
