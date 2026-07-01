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
