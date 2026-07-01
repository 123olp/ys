# Shift Work Long Hours Fatigue Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/shift-work-long-hours-fatigue-continuity` |
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


`shift-work-long-hours-fatigue-continuity/` 研究夜班、轮班、长工时、连续值班、恢复窗口不足和组织排班如何影响睡眠、警觉性、安全和主体持续性。

> 核心问题：轮班和长工时不是个人时间管理问题，而是外部任务系统对睡眠-觉醒节律和恢复窗口的结构性占用。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要足够恢复窗口和稳定警觉性执行高质量任务
  -> 夜班、轮班和长工时会制造睡眠债、节律错位、警觉性下降和事故暴露
  -> 结果取决于组织排班、休息间隔、任务风险、交通暴露和疲劳风险管理
  -> 因此轮班长工时是外部时间制度侵蚀主体持续性的关键执行域
```

## 关注对象

- Shift work、night work、long work hours、extended shifts、sleep debt、fatigue risk management、commute safety、healthcare / transport / industrial / care work contexts。
- 与 `fatigue-risk-alertness-continuity/` 的边界：疲劳域是上位风险模型；本域专门处理轮班、夜班和长工时这类外部日程结构。
- 与 `circadian-rhythm-sleep-wake-disorder-continuity/` 的关系：节律障碍域关注个体生物钟失配；本域关注组织和制度时间安排造成的失配。

## Human Infra 模型链路

```text
轮班长工时与疲劳治理系统 T
  -> 改变工作时长、夜班暴露、轮班稳定性、休息间隔、通勤风险和恢复机会变量 X
  -> 改变睡眠债、警觉性、反应时间、错误率、情绪稳定和事故暴露 S
  -> 改变职业伤害、交通事故、慢病负担、离职和有效时间损失 λ(t)
  -> 影响主体长期行动能力、家庭时间和未来选择权
```

## 非目标

- 不提供个人排班法律建议、职业安全合规判断、驾驶许可、兴奋剂/药物建议、睡眠处方、雇佣争议或保险建议。
- 不生成个人班表优化、疲劳评分、雇主投诉、工伤索赔、法律信、请假材料或规避安全规则方案。
- 不收集个案班表、雇佣记录、睡眠数据、事故记录、健康资料、工号、位置或可识别工作资料。

## Source Signals

- CDC/NIOSH working hours and fatigue: https://www.cdc.gov/niosh/bulletin/2023/fatigue.html
- CDC/NIOSH sleep and work: https://www.cdc.gov/niosh/bulletin/2012/sleep-and-work.html
- NHLBI circadian rhythm disorders: https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders

## 下一步

- 建立 Shift Work Fatigue Card：hours, night exposure, rotation pattern, rest interval, commute exposure, task criticality, recovery opportunity。
- 与 `fatigue-risk-alertness-continuity/`、`circadian-rhythm-sleep-wake-disorder-continuity/` 和 `occupational-work-design/` 建立接口。
