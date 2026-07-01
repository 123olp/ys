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
