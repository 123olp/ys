# Handoff Checklist Procedure Reliability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/handoff-checklist-procedure-reliability-continuity` |
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

Handoff Checklist Procedure Reliability Continuity 研究交接、清单、SOP、标准工作、briefing/debriefing 和过程可靠性如何降低遗漏、断点和重复失败。

> 核心问题：主体持续性经常死在交接处；经验、责任、上下文和下一步动作必须能被可靠传递。

## 研究对象

- Handoff、checklist、standard work、SOP、briefing、debriefing、read-back、closed-loop communication 和任务转交。
- 医疗交接、手术安全、航空检查单、应急交接、软件 on-call、项目移交和照护交接。
- 过程外部化如何降低记忆负担、遗漏、沟通错位、责任模糊和恢复成本。

## 先验链路

```text
主体任务通常跨人、跨时间、跨工具和跨场景
  -> 交接和清单把上下文、责任、风险和下一步动作外部化
  -> 交接失败会造成遗漏、重复、误解、失访、事故和责任真空
  -> 恢复成本上升，长期项目和照护链断裂
  -> 主体有效时间、信任和系统韧性下降
  -> 因而交接清单是主体持续性的过程记忆层
```

## 关键变量

- 交接完整性、关键信息字段、read-back、确认机制、责任人、截止时间、异常升级和记录可追溯性。
- 清单质量、执行负担、流程适配、培训、更新频率和对真实工作流的贴合度。
- 清单形式主义、过度文档、伪合规、责任外包和把复杂判断机械化的风险。

## 证据入口

- WHO Surgical Safety Checklist and safe surgery materials。
- AHRQ TeamSTEPPS handoff / communication materials。
- Care transitions, discharge and high-reliability organization literature。

## 非目标

- 本域不提供临床、航空、应急、工程或法律场景的可执行操作清单。
- 不提供绕过专业培训、监管流程、责任链或安全审查的 SOP。
- 不收集患者、员工、事故、项目秘密、系统凭据、内部流程或敏感交接资料。

## 上下游

- 上游：`situational-awareness-decision-environment-continuity/`、`patient-safety-organizational-learning/`、`collaborative-document-permission-version-continuity/`。
- 下游：`incident-reporting-just-culture-learning-continuity/`、`care-transitions-discharge-continuity/`、`personal-automation-integration-workflow-continuity/`。
