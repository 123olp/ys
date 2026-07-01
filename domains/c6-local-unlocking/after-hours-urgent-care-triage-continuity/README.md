# After Hours Urgent Care Triage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/after-hours-urgent-care-triage-continuity` |
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

## 定位

本域研究夜间/周末服务、护士热线、urgent care、retail clinic、tele-triage、same-day advice、急诊替代边界和 closed-loop follow-up 如何在非急诊但不能等待时保护主体。

它不是急救分诊、症状判断、是否去急诊、urgent care 推荐或医疗建议入口。

## 先验问题

```text
问题发生在诊所关闭后何以不升级为危机？
  -> 主体必须有可信的非工作时间入口
  -> 入口必须区分可等待、需加急和需急救
  -> 记录和 follow-up 必须回到常规照护团队
  -> 否则时间断点会把小问题推向急诊和失控风险
```

## 研究对象

- After-hours care、nurse advice line、urgent care、retail clinic、telehealth triage 和 same-day advice。
- PCP on-call、portal message turnaround、weekend clinic 和 emergency department diversion。
- 服务范围、保险覆盖、地理可达、语言/无障碍、闭环回传和安全网说明。
- 误分诊、延误、重复就诊、网络外账单和缺少 follow-up。

## 关键变量

- 非工作时间入口覆盖率、响应时间、转急诊率和 next-day follow-up 闭环率。
- Urgent care 可达距离、营业时间、保险接受率、语言/无障碍支持和费用透明。
- 误分诊事件、重复就诊、网络外暴露和信息回传失败率。

## 证据入口

- Medicare urgent care coverage、CMS access standards、AHRQ care coordination 和 patient safety 资料。
- CDC emergency care and urgent care utilization、telehealth triage 和 primary care after-hours 研究。
- State health department、insurer nurse line 和 health system after-hours service materials。

## 非目标

- 不判断症状是否紧急、是否去急诊、去哪家 urgent care、是否等待或如何自我处理。
- 不提供急救、分诊脚本、诊断、治疗、药物、账单争议或保险规避。
- 不收集症状、位置、保险、医疗记录、通话内容、门户消息或个案健康资料。

## 上下游

- 上游：`primary-care-panel-appointment-access-continuity/`、`appointment-availability-wait-time-continuity/`、`telehealth-remote-monitoring-access/`。
- 下游：`emergency-medical-services-prehospital-care/`、`care-transitions-discharge-continuity/`、`patient-safety-organizational-learning/`。
