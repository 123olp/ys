# calendar-scheduling-appointment-continuity 目录说明

本目录承载日历、排程与预约连续性研究域，关注未来时间承诺如何被记录、同步、提醒和恢复。

## 目录结构

```text
calendar-scheduling-appointment-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义日历、时区、预约、改期、提醒和跨平台同步如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 IETF iCalendar/CalDAV、IANA Time Zone Database、Unicode CLDR 和公开预约系统治理资料。
- 不写抢号、刷号、批量占位、垃圾邀请、规避预约规则或日历滥用方法。
- 涉及具体服务时只讨论公开流程、时间承诺变量、同步风险和恢复边界。
- 新增指标必须注明口径：预约到达率、提醒可达率、时区错配、改期恢复、冲突率、服务窗口或错过成本。
