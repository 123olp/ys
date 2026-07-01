# Clinical Results Notification Followup Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/clinical-results-notification-followup-continuity` |
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

本域研究临床结果、异常结果、关键值、诊断报告、患者通知、责任分配和 follow-up tracking 如何影响主体能否把检测和诊断信号转化为行动。

它不是结果解释、诊断建议、随访建议、急救分诊或医疗消息代写工具。

## 先验问题

```text
检测结果何以成为行动？
  -> 结果必须到达负责团队和主体可见入口
  -> 异常、关键值和待随访结果必须有责任人和闭环
  -> 通知必须可理解、可追踪、可升级
  -> 否则诊断信号会变成未读、误读、漏随访或延误
```

## 研究对象

- Result notification、critical values、abnormal findings、incidental findings 和 follow-up tracking。
- 患者可见结果、clinician inbox、closed-loop communication、责任分配和 escalation。
- 检验、影像、病理、筛查、诊断报告和跨机构结果回传。

## 关键变量

- 结果回传时间、未读率、异常结果 follow-up 完成率和责任归属清晰度。
- 结果语言可理解性、通知渠道、alert fatigue、clinician inbox burden 和失访。
- 关键值升级、closed-loop tracking、患者查看和跨机构结果丢失。

## 证据入口

- AHRQ diagnostic safety、closed-loop communication 和 patient safety 资料。
- ONC patient access、21st Century Cures Act patient-facing result release 语境。
- 临床结果通知、异常结果随访、diagnostic error 和 EHR inbox 研究。

## 非目标

- 不解释化验、影像、病理、筛查、诊断、风险、治疗或是否需要急诊。
- 不提供结果跟进话术、医生消息、加急策略、第二意见、诊断路径或法律建议。
- 不收集报告、数值、影像、PHI、portal 凭证、联系方式或定位资料。

## 上下游

- 上游：`outpatient-laboratory-specimen-result-routing-continuity/`、`diagnostic-imaging-order-scheduling-report-continuity/`。
- 下游：`patient-portal-account-message-continuity/`、`patient-safety-organizational-learning/`。
