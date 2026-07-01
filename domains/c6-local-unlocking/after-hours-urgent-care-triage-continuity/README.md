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
