# ADR 0067: Add Sixty-Third-Wave Human Factors Operational Reliability Domains

## Status

Accepted.

## Context

Human Infra 已经有患者安全、职业设计、注意力控制、通知路由、AI 代理安全和组织学习等域。但主体持续性还需要一个更通用的人因与操作可靠性层：人如何在复杂任务系统中持续感知、理解、交接、恢复、监督自动化并从错误中学习。

这些对象不能只归入 `patient-safety-organizational-learning`、`occupational-work-design`、`attention-executive-control`、`notification-alert-routing-attention-continuity`、`ai-agency-safety` 或 `risk-engineering`。那些域分别关注医疗安全、工作设计、注意力能力、通知递送、AI 代理和风险工程；本波关注跨场景的人-工具-流程适配、负荷、疲劳、情境感知、交接、事件学习、自动化误用和告警中断管理。

## Decision

新增第 63 波 8 个通用人因与操作可靠性连续性域：

- `human-factors-ergonomics-task-system-continuity`
- `cognitive-load-workload-measurement-continuity`
- `fatigue-risk-alertness-continuity`
- `situational-awareness-decision-environment-continuity`
- `handoff-checklist-procedure-reliability-continuity`
- `incident-reporting-just-culture-learning-continuity`
- `automation-bias-mode-confusion-oversight-continuity`
- `alert-fatigue-interruption-signal-management-continuity`

## Consequences

- Human Infra 能把“任务为什么失败”从个人能力、动机或意志问题，提升为人因适配、负荷边界、恢复窗口、情境感知、交接质量、事件学习和自动化监督问题。
- 这些域只做公开资料整理、机制建模、证据边界和禁止用途声明，不提供医疗/法律/安全个案建议、现场指挥、操作清单、排班规避、员工监控、事故调查代理或高风险系统部署方案。
- 后续若新增 NASA/NIST/FDA/FAA/NIOSH/OSHA/AHRQ/WHO 等人因、负荷、疲劳、交接、自动化、告警和组织学习资料，应先进入本波对应域，而不是混入宽泛注意力、患者安全或 AI 安全域中。
