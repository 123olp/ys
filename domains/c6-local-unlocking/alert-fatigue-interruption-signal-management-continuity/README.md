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
