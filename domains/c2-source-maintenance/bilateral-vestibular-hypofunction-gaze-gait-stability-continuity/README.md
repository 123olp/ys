# Bilateral Vestibular Hypofunction Gaze Gait Stability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/bilateral-vestibular-hypofunction-gaze-gait-stability-continuity` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 关键词显示该域主要维护身体、脑、器官、细胞、急性生命风险或衰老损伤控制。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何维护产生可能性的生命载体，例如身体、脑、器官、细胞、急性生命风险或衰老损伤控制？

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


Bilateral vestibular hypofunction gaze and gait stability continuity studies chronic loss of vestibular function on both sides as a failure of stable vision during movement, gait confidence, night walking, and spatial navigation.

核心问题：

> 主体移动时不仅要腿能走，还要眼睛能在头部运动中稳定看见世界；双侧前庭功能下降会让走路、转头、夜间移动和复杂地面变成高负荷任务。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能在头动和行走中保持视觉稳定
  -> 双侧前庭输入不足削弱凝视稳定、步态反馈和空间安全感
  -> 夜间、崎岖地面和复杂环境中的移动风险上升
  -> 因而双侧前庭功能下降是移动中的视觉-步态稳定基础设施失效
```

## 关注对象

- 双侧前庭功能下降、凝视稳定、振动幻视、步态不稳、夜间行走和复杂地面。
- 行动半径、户外移动、楼梯、交通换乘、跌倒暴露和辅助补偿。
- 与 `low-vision-rehabilitation-assistive-technology-continuity/` 的关系：低视力域关注视觉输入补偿；本域关注头动时视觉稳定。
- 与 `peripheral-neuropathy-somatosensory-continuity/` 的关系：周围神经域关注本体/触觉反馈；本域关注前庭反馈。

## Human Infra 模型链路

```text
前庭评估 / 康复 / 辅助补偿 / 环境适配 T
  -> 改变凝视稳定、步态信心、夜间移动和复杂地面耐受 X
  -> 改变行动半径、外出频率、跌倒暴露和任务参与状态 S
  -> 改变跌倒、隔离、依赖和有效时间损耗风险 λ(t)
  -> 影响独立生活、移动自由和未来选择权
```

## 非目标

- 不提供前庭测试解释、诊断、康复训练、助行器建议、用药建议或个人跌倒风险判断。
- 不根据个人步态或眩晕描述判断病因、外出许可或驾驶许可。
- 不替代耳鼻喉、神经、前庭康复、物理治疗或老年医学服务。

## Source Signals

- Vestibular rehabilitation clinical practice guideline for peripheral vestibular hypofunction。
- NIDCD balance disorders resources。
- CDC STEADI fall prevention resources as downstream risk context。
