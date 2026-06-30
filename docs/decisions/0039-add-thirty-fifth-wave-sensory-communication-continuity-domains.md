# 0039 Add Thirty Fifth Wave Sensory Communication Continuity Domains

## Status

Accepted.

## Context

`sensory-continuity/` 已经覆盖视觉、听觉、平衡、触觉等跨感官反馈，但 Human Infra 的先验追问继续向下拆解后发现：外部输入、主体表达、空间定向、安全摄食、危险化学信号和身体边界反馈具有不同机制、证据体系、失败模式和禁止用途。

这些对象不能长期只放在上位感官域或辅助技术域中，否则会混淆眼科、听力、前庭、言语语言、吞咽、嗅味觉和周围神经的专业边界。

## Decision

新增第三十五波感官、沟通与具身反馈连续性研究域：

- `vision-eye-health-continuity/`
- `hearing-auditory-communication-continuity/`
- `vestibular-balance-spatial-orientation/`
- `speech-language-communication-continuity/`
- `swallowing-dysphagia-aspiration-nutrition/`
- `smell-taste-chemosensory-continuity/`
- `peripheral-neuropathy-somatosensory-continuity/`

这些域分别承担视觉输入、听觉沟通、空间平衡、语言表达、吞咽摄食、化学感知和躯体感觉反馈的研究边界。

## Alternatives

- 继续全部放入 `sensory-continuity/`：拒绝。该域会变成过宽的感官桶，无法维护专业风险和禁止用途。
- 放入 `assistive-technology-access/`：拒绝。辅助技术只处理工具可及与维护，不处理感官系统本身的机制和失效。
- 放入 `rehabilitation-functioning/`：拒绝。康复功能是下游恢复和参与框架，不应吞并所有输入/表达/吞咽/感觉机制。
- 放入 `oral-health-continuity/` 或 `neuro-continuity/`：拒绝。吞咽、言语、前庭、周围神经和感官损失与这些域有交叉，但需要独立证据和边界。

## Consequences

- `docs/reference/research-domain-atlas.md` 与 `research-domain-radar.md` 必须把这些域标为已晋升研究域。
- `docs/reference/domain-map.md` 必须说明这些域与上位感官、辅助技术、康复、神经和口腔域的边界。
- `docs/reference/ethics-and-safety-boundaries.md` 必须新增感官、沟通与具身反馈连续性禁止用途。
- `tools/check_repository.py` 必须把新增域和本 ADR 纳入必需文件检查。

## Safety and Evidence Boundary

这些域只整理公共资料、机制链路、变量、证据等级和模型边界；不得提供个体诊断、治疗、设备处方、检查解释、康复训练、饮食质地调整、误吸处置、跌倒训练、驾驶/工作/活动许可或 AI 个人医疗结论。
