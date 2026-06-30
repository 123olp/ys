# 0036 Add Thirty Second Wave Research Evidence Infrastructure Domains

## Status

Accepted

## Context

Human Infra 已经补齐定量方法学、知识治理、技术预见和技术扩散域，但仍缺少一层更底部的科研证据基础设施：研究结论进入模型之前，必须先经过可信传播、参与者同意、样本质量、纵向随访、登记系统和仪器校准。

如果缺少这些域，项目容易把“统计模型”“知识图谱”或“AI 审计”建在不稳定的证据输入上。有效永生和主体持续性研究需要的不只是更多资料，而是能解释资料何以可靠、何以可追踪、何以能长期观察和纠错的基础设施。

## Decision

新增第三十二波 6 个正式研究域：

- `domains/trustworthy-scientific-communication-peer-review/`
- `domains/research-participant-consent-community-engagement/`
- `domains/biobanking-biospecimen-quality-chain-of-custody/`
- `domains/longitudinal-cohort-retention-followup-infrastructure/`
- `domains/registries-real-world-data-governance/`
- `domains/scientific-instrumentation-sensor-calibration-maintenance/`

同步更新根 README、AGENTS、`domains/` 索引、`docs/` 索引、域地图、研究域图谱、潜在域雷达、伦理边界、真实应用与文献索引，以及仓库结构检查脚本。

## Alternatives Considered

- Option A: 把它们全部放进 `research-infrastructure-open-science-translation/`。拒绝，因为该域过宽，无法单独承载出版纠错、参与者同意、样本保管链、队列留存、登记治理和仪器校准的不同失败模式。
- Option B: 放进 `data-quality-missingness-representativeness/`。拒绝，因为这些域不只是数据质量问题，还包括人体研究伦理、物质样本、测量硬件、真实世界治理和科研传播。
- Option C: 暂留 radar。拒绝，因为这些方向已经有稳定对象、独立来源、独立伦理边界和长期维护价值。

## Consequences

更容易：

- 把 Human Infra 的证据链从“资料堆”推进到“可采样、可保管、可随访、可登记、可校准、可传播纠错”的基础设施。
- 为后续 Source Card、Data Card、Scenario Card、Model Card 增加更具体的证据状态字段。
- 防止论文页、README 或 Web 展示把传播性材料、低质量样本、失访队列、登记偏差或未校准测量写成可靠结论。

更困难：

- 索引维护成本继续上升。
- 后续每个域需要独立的 Source Card 和证据模板，否则目录会停留在骨架状态。

必须关注：

- 不把研究治理资料写成合规建议、IRB 替代、医疗建议或设备操作指南。
- 不处理个人数据、样本数据、参与者身份、设备原始读数或未授权论文全文。

## Safety And Evidence Boundary

本决策不证明任何具体技术能延寿、逆龄或实现有效永生。新增域只说明：若 Human Infra 要判断技术、干预和研究结论对主体持续性的影响，就必须审查科研传播、研究同意、样本保管、长期随访、真实世界登记和仪器校准这些前置条件。
