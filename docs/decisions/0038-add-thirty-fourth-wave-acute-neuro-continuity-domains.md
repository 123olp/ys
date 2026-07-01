# 0038 Add Thirty Fourth Wave Acute Neuro Continuity Domains

## Status

Accepted

## Context

Human Infra 已经有 `neuro-continuity/`、`dementia-cognitive-decline-care-continuity/`、`brain-preservation-connectomics-emulation/` 和 `brain-computer-interface-neurotechnology-governance/`。继续沿着先验追问往上追溯，会出现一组更急性的神经连续性条件：主体如何避免意识、注意、语言、运动、记忆和行动窗口在短时间内被脑血流失败、创伤、谵妄、意识障碍、发作、自主神经失衡或头痛负担截断。

这些方向不能只留在上位 `neuro-continuity/` 中。卒中、TBI、谵妄、意识障碍、癫痫、自主神经稳态和偏头痛分别拥有不同机制、证据体系、失败模式、临床路径和禁止用途。

## Decision

新增第三十四波 7 个正式研究域：

- `domains/c2-source-maintenance/cerebrovascular-stroke-brain-perfusion-resilience/`
- `domains/c2-source-maintenance/traumatic-brain-injury-neurotrauma-recovery/`
- `domains/c2-source-maintenance/delirium-acute-cognitive-failure-prevention/`
- `domains/c2-source-maintenance/disorders-of-consciousness-coma-recovery/`
- `domains/c2-source-maintenance/epilepsy-seizure-network-stability/`
- `domains/c2-source-maintenance/autonomic-nervous-system-homeostasis/`
- `domains/c6-local-unlocking/migraine-headache-effective-time-burden/`

同步更新根 README、AGENTS、`domains/` 索引、`docs/` 索引、域地图、研究域图谱、潜在域雷达、伦理边界、真实应用与文献索引，以及仓库结构检查脚本。

## Alternatives Considered

- Option A: 全部归入 `neuro-continuity/`。拒绝，因为上位神经连续性会被具体急性机制淹没，后续无法建模卒中窗口、创伤恢复、谵妄诱因、意识障碍伦理、发作频率、自主神经变量和头痛有效时间损耗。
- Option B: 归入 `cardiovascular-resilience/`、`risk-engineering/`、`pain-suffering-control/` 或 `dementia-cognitive-decline-care-continuity/`。拒绝，因为这些域只能覆盖部分变量，无法承载完整的神经连续性失败链。
- Option C: 暂留 radar。拒绝，因为这些方向已有成熟公共资料、临床指南、疾病负担证据和独立安全边界，满足正式域晋升条件。

## Consequences

更容易：

- 把神经连续性从抽象身份问题拆成可观察、可建模、可治理的急性失败模式。
- 在有效永生模型中区分死亡风险、失能风险、意识失联、有效时间损耗和主体连续性误判。
- 为后续 Source Card、变量表和图谱提供清晰入口。

更困难：

- 医学域数量继续增加，后续需要更严格的安全边界和交叉引用。
- 这些域容易被误用为个体诊断、急救、用药、预后或活动许可建议，必须保持禁止用途清晰。

必须关注：

- 不提供卒中/TBI/癫痫/谵妄/昏迷/自主神经/偏头痛的个体诊断、治疗、急救、用药、活动许可或预后判断。
- 不把可穿戴、影像、EEG、自测量表、症状描述或 AI 输出写成个人医疗结论。

## Safety And Evidence Boundary

本决策不提供任何临床建议，也不证明某个神经干预可以实现有效永生。新增域只说明：若 Human Infra 要研究主体持续性最大化，就必须审查急性和反复性神经失败如何改变意识、认知、行动、有效时间、照护需求和未来选择权。
