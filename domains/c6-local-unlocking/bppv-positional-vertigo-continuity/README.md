# BPPV Positional Vertigo Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/bppv-positional-vertigo-continuity` |
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


BPPV positional vertigo continuity studies benign paroxysmal positional vertigo as a high-frequency vestibular failure mode where specific head positions can trigger brief vertigo, instability, activity avoidance, and fall exposure.

核心问题：

> 主体不是只需要“有移动能力”，还需要转头、躺下、起身、弯腰和转身这些日常姿势切换不触发空间错觉；BPPV 会把普通动作变成不可预测的眩晕触发器。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能安全完成姿势切换和方向调整
  -> 内耳前庭信号必须与重力和头部位置保持可解释关系
  -> BPPV 使特定头位触发短暂眩晕、失衡和行动回避
  -> 因而 BPPV 是空间行动基础设施中的位置触发型失效模式
```

## 关注对象

- 位置性眩晕、头位触发、翻身、低头、仰头、起卧和转身。
- 眩晕发作对跌倒风险、驾驶/通勤担忧、睡眠姿势、工作任务和活动回避的影响。
- 与 `vestibular-balance-spatial-orientation/` 的关系：父域关注前庭平衡总框架；本域只关注 BPPV 这种位置触发型眩晕。
- 与 `fall-risk-prevention-home-safety-continuity/` 的关系：后者关注家庭防跌倒系统；本域关注头位-前庭信号失配。

## Human Infra 模型链路

```text
识别 / 转诊 / 前庭评估 / 康复路径 T
  -> 改变位置性眩晕触发、姿势切换信心和回避行为 X
  -> 改变移动半径、睡眠姿势、工作动作和跌倒暴露状态 S
  -> 改变跌倒、活动减少、孤立和有效时间损耗风险 λ(t)
  -> 影响行动密度、独立生活、任务完成和未来选择权
```

## 非目标

- 不提供 BPPV 诊断、体位试验解释、复位手法、康复动作、药物或急诊判断。
- 不根据个人眩晕描述判断是否 BPPV、是否可开车、是否需要影像或是否需要急诊。
- 不替代耳鼻喉、神经、前庭康复、物理治疗或急诊专业服务。

## Source Signals

- NIDCD balance disorders resources。
- Mayo Clinic BPPV overview as clinical education context。
- CDC STEADI fall prevention resources as downstream risk context。
