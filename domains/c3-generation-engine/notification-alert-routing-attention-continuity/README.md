# Notification Alert Routing Attention Continuity

`notification-alert-routing-attention-continuity` 研究通知、警报、状态更新、推送、静音、优先级、渠道路由和注意力保护如何影响主体能否及时接收关键事件，同时避免被低价值信号持续消耗。

> 核心问题：通知是行动触发器，也是注意力攻击面；关键提醒漏掉会造成任务中断，过量通知会压垮判断和恢复。

## 关注对象

- Web、移动和桌面通知，push、email、SMS、in-app badge、状态页、系统警报和关键事件路由。
- 通知权限、订阅、退订、静音、勿扰模式、优先级、升级链、确认回执和失败重试。
- 医疗、金融、安全、灾害、学校、工作、照护、平台账号和项目协作中的关键事件通知。
- 通知疲劳、误报、漏报、暗黑模式、操纵性提醒、注意力碎片化和多渠道冲突。

## Human Infra 链路

```text
通知与警报路由连续
  -> 关键事件能按优先级到达正确主体和设备
  -> 漏接、误报、通知疲劳和注意力碎片化下降
  -> 主体更能及时响应风险、任务、关系和恢复需求
  -> 行动可靠性、注意力预算和安全窗口增强
```

## 非目标

- 不提供骚扰通知、垃圾推送、绕过系统权限、追踪用户、规避平台限制或增长黑客方案。
- 不替代医疗、灾害、安全、金融或法律通知的正式渠道和责任。
- 不收集个人通知内容、联系人、设备 token、位置、敏感提醒或私密事件。

## Source Signals

- W3C Notifications API: https://www.w3.org/TR/notifications/
- W3C Push API: https://www.w3.org/TR/push-api/
- W3C Permissions API: https://www.w3.org/TR/permissions/
- Human factors and notification-fatigue literature as evidence signals.

## 下一步

- 建立 `event severity -> channel -> permission -> delivery -> acknowledgement -> action` 变量表。
- 区分紧急安全警报、医疗/照护通知、工作协作通知、平台状态通知和低价值营销通知。
- 与 `attention-executive-control`、`emergency-alerts-communications`、`calendar-scheduling-appointment-continuity` 和 `reminder-alarm-routine-task-continuity` 建立边界。
