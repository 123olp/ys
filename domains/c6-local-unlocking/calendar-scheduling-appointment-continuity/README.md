# Calendar Scheduling Appointment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/calendar-scheduling-appointment-continuity` |
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

`calendar-scheduling-appointment-continuity` 研究日历、时区、预约、改期、取消、邀请、可用性、提醒和跨平台同步如何影响主体是否能把未来时间承诺转化为真实行动。

> 核心问题：时间并不会自动变成有效行动；如果日程系统错配、时区错误、预约丢失或提醒失效，医疗、工作、学习、照护和协作机会会直接断线。

## 关注对象

- iCalendar、CalDAV、VTODO、VEVENT、VALARM、会议邀请、预约确认、改期、取消和重复事件。
- 时区数据库、夏令时、跨地区日程、可用性共享、冲突检测、候补名单和服务窗口。
- 医疗预约、面试、法庭日期、学校安排、公共服务预约、照护交班和长期项目里程碑。
- 日历导出、订阅、迁移、备份、权限、共享日历、委托管理和跨平台同步失败。

## Human Infra 链路

```text
日程与预约连续
  -> 时间承诺、地点、参与人、截止日期和提醒可被可靠记录
  -> 错过预约、时区错配、改期丢失和冲突成本下降
  -> 主体能把未来时间窗口稳定转化为医疗、工作、学习、照护和协作行动
  -> 有效时间、未来选择权和长期项目连续性增强
```

## 非目标

- 不提供绕过预约系统、抢号、自动刷号、批量占位、垃圾邀请或日历滥用方法。
- 不替代医疗、法律、移民、学校、就业或公共服务机构的正式预约规则。
- 不收集个人日历、位置、医疗预约、法庭日期、联系人或私密日程。

## Source Signals

- IETF RFC 5545 iCalendar: https://www.rfc-editor.org/rfc/rfc5545
- IETF RFC 4791 CalDAV: https://www.rfc-editor.org/rfc/rfc4791
- IANA Time Zone Database: https://www.iana.org/time-zones
- Unicode CLDR date/time data: https://cldr.unicode.org/

## 下一步

- 建立 `time commitment -> calendar object -> reminder -> attendance -> recovery` 变量表。
- 区分个人日历、家庭照护日历、医疗预约、教育日程、司法/行政日期和组织排班。
- 与 `time-allocation-effective-time`、`notification-alert-routing-attention-continuity`、`reminder-alarm-routine-task-continuity` 和 `collaborative-document-permission-version-continuity` 建立边界。
