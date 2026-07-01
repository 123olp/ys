# Reminder Alarm Routine Task Continuity

`reminder-alarm-routine-task-continuity` 研究提醒、闹钟、重复任务、习惯、例行维护、服药提醒、复查提醒、账单到期和照护例程如何影响主体是否能稳定完成低显著但高累积价值的任务。

> 核心问题：许多主体持续性风险不是一次灾难，而是由无数小任务遗忘、延迟和中断累积而成。

## 关注对象

- 闹钟、提醒、重复任务、清单、到期日、snooze、确认、失败重试和补救任务。
- 服药提醒、复查、饮水/进食、设备维护、账单、证件续期、照护交接、运动康复和家庭事务。
- VTODO、VALARM、任务管理器、家庭共享提醒、可穿戴提醒、智能音箱和低技术纸面备份。
- 提醒依赖、过载、误设、设备故障、时区错配、通知权限变化和例程断裂。

## Human Infra 链路

```text
提醒与例行任务连续
  -> 重复任务、到期任务和维护任务可被触发、确认和补救
  -> 遗忘、延迟、例程断裂和小故障累积下降
  -> 主体把长期维护需求转化为可执行的日常行动
  -> 健康、资源、设备、关系和长期项目连续性增强
```

## 非目标

- 不提供具体医疗、用药、剂量、治疗、账单、法律期限或财务操作建议。
- 不提供绕过应用限制、监控家庭成员、强迫执行、操纵提醒或行为控制方案。
- 不收集个人提醒、药物清单、账单、照护任务、家庭成员或设备数据。

## Source Signals

- IETF RFC 5545 VTODO / VALARM components: https://www.rfc-editor.org/rfc/rfc5545
- AHRQ medication management and patient safety materials as healthcare-context signals.
- CDC and NIH public materials for adherence, chronic care and reminder evidence boundaries.
- Human-computer interaction literature on habit, reminders and task resumption.

## 下一步

- 建立 `routine task -> trigger -> acknowledgement -> completion -> missed-task recovery` 变量表。
- 区分健康例程、照护例程、设备维护、行政续期、账单到期和长期项目维护。
- 与 `calendar-scheduling-appointment-continuity`、`notification-alert-routing-attention-continuity`、`multimorbidity-polypharmacy-care-coordination` 和 `contract-subscription-billing-consent-continuity` 建立边界。
