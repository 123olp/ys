# Sleep Circadian And Recovery

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/sleep-circadian-recovery` |
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


Sleep Circadian And Recovery 负责整理睡眠、昼夜节律、恢复、疲劳、代谢修复和长期恢复能力。

核心问题：

> 主体持续行动依赖恢复系统；如果睡眠和昼夜节律崩坏，身体、认知、免疫和情绪都会退化。

## 先验位置

```text
主体持续性最大化
  -> 主体必须持续修复损伤、恢复能量和稳定认知
  -> 睡眠和昼夜节律是恢复系统的基础调度器
  -> 长期睡眠障碍会影响代谢、免疫、心血管、情绪和认知
  -> 因此睡眠、节律与恢复是有效时间的基础条件
```

## 关注对象

- 睡眠时长、睡眠质量、失眠、睡眠呼吸障碍和昼夜节律错位。
- 疲劳、恢复、轮班、时差、光照、压力和代谢节律。
- 睡眠与免疫、认知、心理健康、心血管和代谢的交叉影响。
- 与 `measurement-feedback/` 的关系：可穿戴和睡眠指标只能作为近似观测。

## Human Infra 模型链路

```text
睡眠 / 节律干预 T
  -> 改变恢复质量、认知稳定、免疫状态和代谢节律 X
  -> 改变主体恢复状态 S
  -> 降低疲劳、错误、慢病、心理失稳和事故风险
  -> 增加有效时间和长期行动密度
```

## 非目标

- 不提供个体睡眠诊断、处方、药物或医疗建议。
- 不把可穿戴睡眠分数当作真实恢复状态。
- 不把短期效率提升压过长期恢复。

## Source Signals

- CDC Sleep and Sleep Disorders: https://www.cdc.gov/sleep/
- NHLBI Sleep Deprivation and Deficiency: https://www.nhlbi.nih.gov/health/sleep-deprivation
