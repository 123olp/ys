# Alert Fatigue Interruption Signal Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/alert-fatigue-interruption-signal-management-continuity` |
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


Alert Fatigue Interruption Signal Management Continuity 研究告警、通知、中断、提示、报警疲劳和信号优先级如何影响注意力、情境感知和任务连续性。

> 核心问题：信号太少会漏掉风险，信号太多会摧毁注意力；主体需要可校准的信号环境。

## 研究对象

- Alert fatigue、alarm fatigue、notification fatigue、interruption management、signal prioritization、quiet hours 和 escalation routing。
- 医疗警报、运维告警、个人通知、AI 提示、应急消息、任务提醒和团队协作消息。
- 信号过载如何影响注意力、疲劳、响应率、错误恢复、睡眠和有效时间。

## 先验链路

```text
主体需要及时接收重要信号以避免风险和推进任务
  -> 告警和中断把外部事件竞争性地插入注意力系统
  -> 信号过载会造成忽略、麻木、错误响应、睡眠破坏和注意力碎片化
  -> 重要风险被淹没，普通任务也被频繁打断
  -> 有效时间、情境感知和恢复能力下降
  -> 因而告警中断管理是主体持续性的注意力环境层
```

## 关键变量

- 告警数量、优先级、假阳性、假阴性、响应时间、升级路径、静默窗口、确认机制和撤销机制。
- 频率、渠道、上下文、可操作性、重复通知、夜间打扰、值班负荷和恢复影响。
- 以“通知即责任转移”、把所有风险推给用户、用中断操控注意力或制造成瘾的风险。

## 证据入口

- Joint Commission / AHRQ alarm fatigue and patient safety materials。
- Notification fatigue and human factors literature。
- `notification-alert-routing-attention-continuity/` existing domain materials。
- NIST / human-centered design signal and warning design materials。

## 非目标

- 本域不提供医疗告警配置、生产运维阈值、应急通知策略、个人治疗提醒或高风险系统部署方案。
- 不提供绕过安全告警、降低监管要求、隐藏风险信号、操控用户注意力或增长黑客方案。
- 不收集个人通知记录、医疗告警、生产告警、位置、睡眠数据、值班记录或内部事件日志。

## 上下游

- 上游：`notification-alert-routing-attention-continuity/`、`attention-executive-control/`、`situational-awareness-decision-environment-continuity/`。
- 下游：`fatigue-risk-alertness-continuity/`、`automation-bias-mode-confusion-oversight-continuity/`、`emergency-alerts-communications/`。
