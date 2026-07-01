# Fatigue Risk Alertness Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/fatigue-risk-alertness-continuity` |
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


Fatigue Risk Alertness Continuity 研究疲劳、长工时、夜班、睡眠不足、轮班、恢复缺口和警觉性下降如何影响主体安全、判断和长期行动能力。

> 核心问题：疲劳不是个人硬扛问题，而是任务排布、组织资源、恢复窗口和安全边界共同决定的风险函数。

## 研究对象

- Fatigue risk management、alertness、sleep debt、shift work、long work hours、night work 和恢复窗口。
- 医疗、交通、工业、软件值班、照护、应急响应和高压知识工作中的疲劳风险。
- 疲劳如何改变注意力、反应时间、情绪稳定、错误率、事故风险和长期健康。

## 先验链路

```text
主体持续执行需要可恢复的警觉性
  -> 长工时、夜班、睡眠不足和恢复缺口积累疲劳
  -> 疲劳降低注意力、反应速度、判断质量和情绪调节
  -> 错误、事故、冲突、健康损耗和恢复时间增加
  -> 有效行动窗口被压缩，长期任务系统变得不可持续
  -> 因而疲劳风险是主体持续性的警觉性与恢复门槛
```

## 关键变量

- 睡眠时长、睡眠质量、工作时长、夜班、连续值班、休息间隔、轮班稳定性和恢复机会。
- 主观疲劳、警觉性、反应时、错误率、近失误、事故、情绪波动和健康损耗。
- 把疲劳管理转嫁给个人、用疲劳数据监控员工、合理化人手不足和无休止值班的风险。

## 证据入口

- NIOSH fatigue and work schedules resources。
- OSHA worker fatigue resources。
- FAA fatigue and human factors materials。
- Sleep and circadian recovery literature。

## 非目标

- 本域不提供睡眠医疗诊断、排班法律建议、个体药物/兴奋剂建议、驾驶/飞行/值班许可判断。
- 不提供规避工时、安全或职业健康要求的排班方案。
- 不收集睡眠追踪、雇佣记录、班表、事故个案、医疗诊断或员工监控资料。

## 上下游

- 上游：`sleep-circadian-recovery/`、`occupational-work-design/`、`light-exposure-circadian-environment-continuity/`。
- 下游：`human-error-just-culture-incident-learning-continuity/`、`handoff-checklist-procedure-reliability-continuity/`、`risk-engineering/`。
