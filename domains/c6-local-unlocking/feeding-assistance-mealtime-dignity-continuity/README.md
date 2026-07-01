# Feeding Assistance Mealtime Dignity Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/feeding-assistance-mealtime-dignity-continuity` |
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


Feeding assistance mealtime dignity continuity studies how human help, timing, environment, adaptive tools, social context, and care quality determine whether people can eat safely, sufficiently, and with dignity.

核心问题：

> 进食不是把热量送入口中；它是时间、姿势、节奏、帮助、关系和尊严共同维护的日常主体活动。

## 先验位置

```text
主体持续性最大化
  -> 主体必须把营养摄入转化为可承受、可持续、可尊严的日常活动
  -> 吞咽困难、残障、衰弱或认知下降可能使独立进食失效
  -> 进食协助质量影响摄入量、误吸暴露、照护关系和主体尊严
  -> 因而进食协助是营养入口和人格尊严之间的照护基础设施
```

## 关注对象

- 喂食协助、用餐时间、姿势支持、辅助餐具、人员培训、长期照护、社交餐食、进食尊严和照护者负担。
- 与 `caregiving-long-term-care/` 的关系：照护域关注长期照护系统；本域关注用餐执行。
- 与 `dignity-personhood-respect-continuity/` 的关系：尊严域关注人格尊重；本域关注进食场景中的尊严。

## Human Infra 模型链路

```text
人员协助 / 用餐环境 / 辅助工具 / 时间安排 T
  -> 改变摄入量、进食速度、误吸暴露、关系体验和尊严变量 X
  -> 改变营养状态、情绪恢复、照护负担和社会参与状态 S
  -> 改变营养不足、脱水、误吸、孤立、拒食和照护崩溃风险 λ(t)
  -> 影响有效时间、生活质量和未来选择权
```

## 非目标

- 不提供喂食技巧、姿势、速度、饮食质地、人员培训方案、护理处置、机构合规判断或虐待判定。
- 不根据个体进食表现、照护环境或机构记录判断服务质量和责任。
- 不替代护理、营养、言语语言治疗、职业治疗、长期照护监管或法律服务。

## Source Signals

- CMS paid feeding assistant and long-term-care materials。
- ASHA adult dysphagia and pediatric feeding/swallowing materials。
- Person-centered care and dignity literature as research context。
