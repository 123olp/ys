# 0103 Add Ninety Ninth Wave Disaster Recovery Execution Continuity Domains

## Status

Accepted.

## Context

第九十八波已经把家庭与个人应急准备拆成灾前准备变量，但主体持续性还会在灾害发生后的恢复阶段被重新定义。灾后恢复不是单一“救助”，而是援助导航、临时住房、恢复中心、长期个案管理、收入接续、法律援助、废弃物清理、霉菌湿气恢复、心理健康和志愿捐赠协调共同构成的多系统恢复链。

如果只保留 `household-emergency-preparedness-resilience` 或 `emergency-preparedness-response` 这样的宽域，会把灾前准备、灾中避险、灾后恢复和长期重建混成一个桶，无法识别恢复阶段的制度入口、服务接口、环境清理、住房稳定和心理恢复变量。

## Decision

新增第九十九波 10 个灾后恢复执行连续性研究域：

- `disaster-individual-assistance-benefits-navigation-continuity`
- `disaster-temporary-housing-displacement-recovery-continuity`
- `disaster-recovery-center-service-access-continuity`
- `disaster-case-management-long-term-recovery-continuity`
- `disaster-unemployment-income-disruption-continuity`
- `disaster-legal-aid-rights-claims-continuity`
- `disaster-debris-waste-sanitation-cleanup-continuity`
- `post-flood-mold-moisture-indoor-recovery-continuity`
- `disaster-behavioral-health-distress-recovery-continuity`
- `disaster-volunteer-donations-management-continuity`

每个域只承载公开研究、变量拆解、证据入口和伦理边界，不提供个案救助、法律意见、医疗诊断、保险理赔、清理操作、志愿派遣、捐赠收款或实时灾害指挥。

## Consequences

- `README.md`、`AGENTS.md`、`domains/`、`docs/`、`docs/reference/` 和 `tools/check_repository.py` 必须同步索引。
- 灾害恢复类内容必须明确区分灾前准备、灾中响应、灾后短期援助、长期恢复和重建治理。
- 任何涉及身份、地址、灾损、收入、法律案件、保险、健康、创伤经历、志愿者或受助者资料的内容都不得进入仓库。
