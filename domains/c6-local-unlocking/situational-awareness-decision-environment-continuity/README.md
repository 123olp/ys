# Situational Awareness Decision Environment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/situational-awareness-decision-environment-continuity` |
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


Situational Awareness Decision Environment Continuity 研究主体如何形成对环境、任务状态、风险信号和下一步行动的共同理解，防止复杂系统中的误判和迟滞。

> 核心问题：人在复杂环境中不是缺少信息，而是需要正确感知、理解、预测和协同决策。

## 研究对象

- Situation awareness、sensemaking、decision environment、shared mental model、decision support 和 risk picture。
- 医疗、应急、航空、工业、软件运维、AI 协作和团队任务中的状态感知。
- 信息显示、告警、态势图、交接、训练、团队沟通和决策支持如何影响判断质量。

## 先验链路

```text
主体行动需要知道当前发生了什么、意味着什么、下一步可能发生什么
  -> 情境感知把信号、上下文、预测和团队理解组织成决策环境
  -> 感知缺失或理解错位会导致迟滞、误判、重复劳动和错误升级
  -> 决策质量和协作效率下降，风险窗口扩大
  -> 主体有效时间与系统恢复能力受损
  -> 因而情境感知是主体持续性的判断环境层
```

## 关键变量

- 信号可见性、信息延迟、上下文完整性、共享心智模型、预测能力、决策时间和升级路径。
- 状态看板、告警、日志、handoff、briefing、debriefing、团队沟通和 AI 决策支持。
- 过度可视化、错误态势图、虚假确定性、算法权威和敏感信息暴露风险。

## 证据入口

- AHRQ TeamSTEPPS situation monitoring and shared mental model materials。
- NASA / aviation human factors literature on situation awareness。
- NIST AI RMF and human-centered AI risk language。

## 非目标

- 本域不提供现场指挥、急救调度、军事/安全行动、个人风险评分或 AI 自动决策部署方案。
- 不提供绕过组织指挥链、监控员工、实时定位个人或敏感态势收集方法。
- 不收集现场位置、患者/员工/事故个案、组织内部日志、安防数据或敏感操作资料。

## 上下游

- 上游：`information-integrity-trust/`、`alert-fatigue-interruption-signal-management-continuity/`、`human-factors-ergonomics-task-system-continuity/`。
- 下游：`handoff-checklist-procedure-reliability-continuity/`、`automation-bias-mode-confusion-oversight-continuity/`、`emergency-alerts-communications/`。
