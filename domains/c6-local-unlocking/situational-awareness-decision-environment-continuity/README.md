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
