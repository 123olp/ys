# Calendar Scheduling Appointment Continuity

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
