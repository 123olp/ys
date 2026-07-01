# 0117. Add One-Hundred-Twelfth Wave Household Operating Metadata Handoff Domains

Date: 2026-07-01

## Status

Accepted

## Context

Human Infra 已经覆盖家庭水、电、热、空气、废弃物、物理秩序和若干应急准备域，但仍缺少一组更基础的“家庭运行可读性”对象：关键位置是否有标签，回路和水路是否可被专业人员理解，设备身份是否能匹配召回，服务联系人是否能被临时代理找到，家庭运行知识是否从单点记忆变成可交接资料。

这些对象不是保修、维修、收纳、灾后财务文件或家庭通信计划的重复。它们关注的是家庭系统的操作元数据：哪些资料让家庭基础设施在失能、住院、旅行、灾害、维修、租赁交接、照护交接和死亡后事务中保持可读、可恢复、可代理执行。

## Decision

新增 6 个正式研究域：

- `domains/c5-ecological-substrate/home-utility-shutoff-location-labeling-continuity/`
- `domains/c5-ecological-substrate/household-circuit-breaker-panel-labeling-continuity/`
- `domains/c5-ecological-substrate/home-water-valve-plumbing-labeling-continuity/`
- `domains/c4-conversion-channel/household-equipment-serial-model-recall-record-continuity/`
- `domains/c5-ecological-substrate/home-service-provider-emergency-contact-directory-continuity/`
- `domains/c5-ecological-substrate/household-operating-map-handoff-continuity/`

这批域共同构成“家庭运行元数据、位置标识、服务入口与交接地图连续性”视角，关注家庭关键设施、设备和服务网络如何从隐性知识变成可审查、可更新、可撤权、可交接的资料结构。

## Boundaries

- 不提供水电燃气关断操作、电气面板操作、阀门操作、管线维修、灾后返家许可、个案维修、服务商推荐、价格判断、保险理赔、法律意见、医疗处方、家庭监控、定位追踪、门禁共享或个人资料模板。
- 不收集住址、照片、设施位置、面板/阀门细节、设备序列号、账户、门禁、联系人、家庭成员、药品、资产或照护对象资料。
- 不替代公用事业公司、消防部门、持证电工、持证 plumber/HVAC、房东/物业、保险、Poison Help、消费者保护机构、医疗人员、法律文件或应急服务。
- 每个域必须保留 `household operating metadata -> readable handoff state -> restoration/agency path -> continuity outcome` 的链路，而不是写成操作教程、家庭模板、产品导购或个人安全建议。

## Consequences

- 根 README、docs 路由、domain map、domain atlas、radar、伦理边界和应用文献表都需要同步新增入口。
- `tools/check_repository.py` 必须把 6 个目录、README、AGENTS 和本 ADR 纳入结构门禁。
- 这批域与 `natural-gas-propane-leak-shutoff-continuity`、`residential-electrical-wiring-outlet-safety-continuity`、`premise-plumbing-backflow-cross-connection-continuity`、`product-safety-recall-systems`、`consumer-warranty-service-contract-repair-continuity`、`right-to-repair-parts-manuals-access-continuity`、`family-emergency-communication-reunification-continuity`、`emergency-financial-document-cash-readiness-continuity` 和 `estate-inventory-asset-liability-handoff-continuity` 保持上下游关系，但不合并。
