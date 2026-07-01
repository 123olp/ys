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
