# 0011 Add Seventh Wave Homeostasis Choice Domains

## Status

Accepted

## Context

Research Domain Atlas 已把 Human Infra 的域生成规则定义为先验条件追溯：凡是主体持续性成立所需的必要条件、支撑条件、风险条件或反馈条件，都可以被抽象为研究域。

第六波覆盖呼吸、血液、内分泌、皮肤、细胞外基质和淋巴清除后，仍有五类基础条件没有独立承载：

- 营养和水分必须被消化、吸收，并通过肠道屏障进入系统。
- 内部化学环境必须维持水分、电解质、渗透压和酸碱平衡。
- 主体必须在可承受温度范围内运行。
- 排泄控制、泌尿安全、性功能和尊严影响有效时间与社会参与。
- 生育力、生殖衰老和生殖自主性影响未来选择权和长期人生路径。

这些方向不能被简单塞进营养、肾脏、环境、心理或权利域，因为它们有独立机制、证据体系、失败模式和伦理边界。

## Decision

新增第七波 5 个基础稳态与未来选择权研究域：

- `gastrointestinal-barrier-absorption/`
- `fluid-electrolyte-acid-base-homeostasis/`
- `thermal-homeostasis-resilience/`
- `urogenital-continuity/`
- `reproductive-fertility-continuity/`

每个域先只创建 `README.md` 和 `AGENTS.md`，不创建空数据、脚本或复杂目录。

## Consequences

- `domains/` 可以更完整承载身体基础运行条件，而不是只覆盖寿命、生物标志物和器官疾病。
- `research-domain-atlas.md`、`research-domain-radar.md` 和 `domain-map.md` 增加第七波域的先验位置、来源信号和禁止用途。
- 仓库结构检查脚本把第七波目录和文件纳入必需项。

## Non-goals

- 不提供胃肠诊疗、饮食处方、补液电解质、酸碱处理、热病急救、泌尿感染处理、盆底训练、生育治疗、辅助生殖、妊娠管理或避孕建议。
- 不把生殖连续性等同于主体持续性本身；它只作为未来选择权和长期计划维度进入 Human Infra。
- 不新增临床数据采集脚本或个人预测模型。
