# Circadian Rhythm Sleep Wake Disorder Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/circadian-rhythm-sleep-wake-disorder-continuity` |
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

`circadian-rhythm-sleep-wake-disorder-continuity/` 研究昼夜节律睡眠-觉醒障碍、睡眠时相错位、光照/社会时间线、上学上班冲突和长期恢复调度如何影响主体持续性。

> 核心问题：昼夜节律障碍不是意志力问题，而是内部生物钟与外部制度时间错位，可能让主体在正确地点、错误时间、错误清醒状态下执行任务。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要内部生物钟与外部任务时间基本同步
  -> 昼夜节律错位会造成入睡/醒来时间偏移、日间功能下降和恢复质量下降
  -> 结果取决于识别、光暗环境、学校/工作时间、社会支持和睡眠医学可及
  -> 因此昼夜节律障碍是恢复调度与制度时间匹配的关键研究域
```

## 关注对象

- Circadian rhythm sleep-wake disorders、delayed / advanced sleep-wake phase、irregular sleep-wake rhythm、non-24-hour sleep-wake rhythm、light exposure、social schedule conflict。
- 与 `sleep-circadian-recovery/` 的边界：该域关注睡眠和节律总机制；本域关注正式睡眠-觉醒节律障碍和制度时间错位。
- 与 `light-exposure-circadian-environment-continuity/` 的关系：光照域关注环境输入；本域关注睡眠-觉醒调度结果。

## Human Infra 模型链路

```text
节律障碍识别与时间环境支持系统 T
  -> 改变生物钟相位、光暗暴露、社会时间冲突、入睡/醒来时间和支持可及变量 X
  -> 改变睡眠稳定、日间警觉、学校/工作参与、情绪和代谢状态 S
  -> 改变有效时间损失、学习/就业损耗、事故暴露和长期恢复失败 λ(t)
  -> 影响主体行动密度、关系参与和未来选择权
```

## 非目标

- 不提供个人昼夜节律诊断、光照方案、褪黑素/药物建议、剂量、作息处方、学校/工作时间安排或治疗建议。
- 不生成个人睡眠相位判断、光照计划、时差恢复方案、设备购买建议、便利申请或职业安排。
- 不收集个案睡眠日志、光照数据、可穿戴数据、学校/工作记录、用药、病史或可识别医疗资料。

## Source Signals

- NHLBI circadian rhythm disorders: https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders
- NHLBI circadian rhythm disorder types: https://www.nhlbi.nih.gov/health/circadian-rhythm-disorders/types
- MedlinePlus sleep disorders: https://medlineplus.gov/ency/article/000800.htm

## 下一步

- 建立 Circadian Alignment Card：phase pattern, light-dark environment, social schedule conflict, sleep timing, daytime impairment, support access。
- 与 `sleep-circadian-recovery/`、`light-exposure-circadian-environment-continuity/` 和 `fatigue-risk-alertness-continuity/` 建立接口。
