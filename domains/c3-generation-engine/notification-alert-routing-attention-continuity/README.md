# Notification Alert Routing Attention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/notification-alert-routing-attention-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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
