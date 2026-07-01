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
