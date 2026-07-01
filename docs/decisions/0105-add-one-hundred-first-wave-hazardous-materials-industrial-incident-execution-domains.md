# 0105 Add One Hundred First Wave Hazardous Materials Industrial Incident Execution Domains

## Status

Accepted

## Context

Human Infra 已有 `waste-management-hazardous-materials-continuity/`、`radiation-nuclear-safety-protection/`、`chemical-safety-poison-control-toxicology/`、`occupational-exposure-industrial-hygiene/`、`building-fire-life-safety-codes/` 和 `emergency-preparedness-response/` 等相关域。

这些域覆盖危险材料治理、核辐射防护、化学毒理、职业暴露、建筑消防和总体应急，但仍缺少一个事故执行层：当危险材料、工业过程、运输、油污或电池热失控风险进入现实事故时，公众如何收到信息、机构如何协作、响应者如何持续行动、暴露者如何进入医疗恢复系统、社区如何恢复。

## Decision

新增第 101 波危险材料与工业事故执行连续性域：

- `chemical-release-shelter-evacuation-continuity/`
- `community-right-to-know-chemical-risk-disclosure-continuity/`
- `hazmat-incident-command-emergency-response-continuity/`
- `industrial-process-safety-management-continuity/`
- `toxic-plume-air-monitoring-risk-communication-continuity/`
- `hazwoper-responder-ppe-safety-continuity/`
- `decontamination-exposure-triage-continuity/`
- `hazardous-materials-transportation-erg-continuity/`
- `oil-spill-hazardous-release-response-recovery-continuity/`
- `battery-thermal-runaway-fire-hazard-continuity/`

这些域不替代既有化学、辐射、废弃物、消防或应急总域，而是把危险材料事故执行链拆成可审查接口：风险披露、过程安全、事故指挥、公众避险、羽流监测、响应者安全、暴露后去污分诊、运输事故、油污恢复和电池热失控。

## Consequences

- `chemical-safety-poison-control-toxicology/` 继续作为化学暴露与毒理总域。
- 新域只处理事故执行连续性，不输出化学品操作、事故处置、PPE 穿脱、现场指挥、去污步骤、运输操作、清理方法、设施侦察、规避监管或个体医疗建议。
- `docs/reference/ethics-and-safety-boundaries.md` 必须同步新增禁止用途边界，防止资料被转化为事故制造、规避监管、恐慌传播或现场操作。
- `tools/check_repository.py` 必须把新域 README/AGENTS 和本 ADR 纳入结构检查。

## Source Signals

- Ready.gov chemical emergencies: https://www.ready.gov/chemical
- EPA EPCRA: https://www.epa.gov/epcra
- EPA Risk Management Program: https://www.epa.gov/rmp
- OSHA Process Safety Management: https://www.osha.gov/process-safety-management
- OSHA HAZWOPER: https://www.osha.gov/hazwoper
- PHMSA Emergency Response Guidebook: https://www.phmsa.dot.gov/hazmat/erg/emergency-response-guidebook-erg
- FEMA National Incident Management System: https://www.fema.gov/emergency-managers/nims
- EPA CAMEO / ALOHA: https://www.epa.gov/cameo
- HHS CHEMM: https://chemm.hhs.gov/
- NOAA Office of Response and Restoration: https://response.restoration.noaa.gov/
