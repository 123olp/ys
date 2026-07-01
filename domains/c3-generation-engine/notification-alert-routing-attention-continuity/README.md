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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

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
