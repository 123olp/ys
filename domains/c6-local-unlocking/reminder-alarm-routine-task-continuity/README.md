# Reminder Alarm Routine Task Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/reminder-alarm-routine-task-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->


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
