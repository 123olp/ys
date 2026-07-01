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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
