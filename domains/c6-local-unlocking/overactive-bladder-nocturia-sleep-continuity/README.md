# Overactive Bladder, Nocturia and Sleep Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/overactive-bladder-nocturia-sleep-continuity` |
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


`overactive-bladder-nocturia-sleep-continuity/` 研究尿急、尿频、夜尿、睡眠中断、跌倒风险、工作疲劳和社交限制如何影响主体持续性。

> 核心问题：膀胱症状不只是局部问题，它会通过睡眠破坏、注意力下降、出行回避、跌倒风险和羞耻成本压缩有效时间。

## 先验位置

```text
有效永生
  -> 主体需要稳定睡眠和可预测行动半径
  -> 尿急尿频夜尿会打断恢复、工作和外出
  -> 因此 OAB / nocturia 是排泄节律影响有效时间的域
```

## 关注对象

- Overactive bladder, urgency, frequency, nocturia, sleep interruption, fall risk, social avoidance, workplace fatigue, continence access boundaries。
- 与 `pelvic-floor-continence-function-continuity/` 的关系：盆底域覆盖控尿控便和功能参与，本域聚焦膀胱节律、夜间恢复和行动半径。

## Human Infra 模型链路

```text
膀胱节律与夜间中断 T
  -> 改变夜醒、睡眠质量、疲劳、出行回避和跌倒暴露 X
  -> 改变恢复状态、注意力、工作可靠性和社交参与 S
  -> 改变失能、跌倒、抑郁、照护依赖和有效时间损失 lambda(t)
  -> 改变健康寿命和未来选择权
```

## 非目标

- 不提供 OAB 诊断、药物、盆底训练、饮水安排、夜尿处理、检查解释、设备或个体治疗建议。
- 不输出个人睡眠/跌倒风险、工作许可、驾驶许可或保险证明。

## Source Signals

- NIDDK bladder control problems.
- MedlinePlus overactive bladder and nocturia public materials.
- NIA falls / sleep public materials for downstream burden boundary.
