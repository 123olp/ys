# 0102 Add Ninety Eighth Wave Household Personal Emergency Preparedness Domains

## Status

Accepted

## Context

Human Infra 已有灾害响应、公共预警、家庭应急准备、社区韧性、停电、电网、食物、水和医疗设备等上位域，但个人和家庭层面的应急执行条件仍需要拆成可审查的前置环节。物资包、通信团聚、撤离、就地避险、备用电、食水、温控药品/医疗设备、金融文件、残障功能需求和老年照护者准备各自拥有不同官方来源、执行主体、隐私边界、失败模式和禁止用途。

## Decision

新增第九十八波 10 个家庭与个人应急准备执行连续性域：

- `emergency-supply-kit-go-bag-rotation-continuity/`
- `family-emergency-communication-reunification-continuity/`
- `evacuation-route-transportation-shelter-plan-continuity/`
- `shelter-in-place-clean-air-room-indoor-protection-continuity/`
- `backup-power-battery-generator-safety-continuity/`
- `emergency-food-water-storage-treatment-continuity/`
- `refrigerated-medication-medical-device-power-outage-continuity/`
- `emergency-financial-document-cash-readiness-continuity/`
- `disability-access-functional-needs-personal-preparedness-continuity/`
- `older-adult-caregiver-disaster-preparedness-continuity/`

## Consequences

- 家庭应急准备不再只是宽泛 checklist，而是拆成物资、关系、移动、空间、电力、食水、治疗、资料、无障碍和照护者这些可被模型化的执行层。
- 每个域只整理公开资料、变量链路、证据边界和禁止用途，不提供个人撤离、物资、医疗、用电、财务、法律、照护或灾害现场行动建议。
- 根目录、`domains/`、`docs/reference/` 和结构检查脚本必须同步索引。
