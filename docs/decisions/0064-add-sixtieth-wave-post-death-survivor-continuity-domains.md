# ADR 0064: Add Sixtieth-Wave Post-Death Survivor Continuity Domains

## Status

Accepted.

## Context

Human Infra 已经覆盖失能代理、生命事件记录、急救健康信息、器官捐赠登记、遗产事务和数字遗产，但仍缺少一组专门处理“死亡事实发生后，证明、处置、遗属资源、账户关闭和幸存者恢复如何继续执行”的研究域。

这些对象不能只归入 `vital-records-life-event-continuity`、`trust-estate-affairs-succession-continuity`、`digital-legacy-data-succession` 或 `contract-subscription-billing-consent-continuity`。那些域分别关注生命事件记录、广义事务继承、数字资料继承和一般合同订阅；本波关注死亡边界后的执行链、行政证明、遗体处置、遗属福利、理赔、账户关闭和悲伤恢复。

## Decision

新增第 60 波 8 个死亡后与遗属连续性域：

- `death-certificate-registration-cause-of-death-record-continuity`
- `funeral-cremation-burial-disposition-continuity`
- `cemetery-memorial-remains-location-continuity`
- `bereavement-leave-grief-support-continuity`
- `survivor-benefits-death-notification-continuity`
- `life-insurance-beneficiary-claim-continuity`
- `estate-inventory-asset-liability-handoff-continuity`
- `post-death-account-closure-service-cancellation-continuity`

## Consequences

- Human Infra 能从“主体死亡边界是否被识别”继续追问到“死亡事实能否被证明、遗体能否被尊严处置、遗属能否获得福利和理赔、账户和资产负债能否关闭或交接、幸存者能否恢复行动能力”。
- 这些域只做公开资料整理、结构建模、证据边界和禁止用途声明，不提供死亡证明办理、丧葬安排、遗产法律、税务、保险理赔、账户关闭、心理治疗或个案建议。
- 后续若新增死亡证明、丧葬、墓地/遗体位置、遗属福利、寿险理赔、遗产清单或死亡后账户关闭资料，应先进入本波对应域，而不是散落在宽泛生命事件、继承、合同或数字遗产域中。
