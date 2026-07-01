# Physical Activity Mobility

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/physical-activity-mobility` |
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


Physical Activity Mobility 负责整理身体活动、运动、久坐、心肺适能、肌肉力量、步态、移动能力和行动密度。

核心问题：

> 主体不是静态器官集合，而是持续行动的系统；身体活动维护心肺、代谢、肌肉、骨骼、情绪和认知，是有效时间的底层放大器。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能移动、工作、学习、照护自己并参与社会
  -> 身体活动是维持心肺、肌肉、骨骼、代谢和神经系统的常规输入
  -> 久坐和活动不足会提高慢病、失能和死亡风险
  -> 因此身体活动与移动能力是行动能力的基础条件
```

## 关注对象

- 身体活动量、久坐行为、心肺适能、力量、平衡、步态和移动能力。
- 活动不足与心血管、代谢、肌骨、心理、认知和跌倒风险的关系。
- 工作、城市、交通、环境和时间预算对活动机会的影响。
- 与 `rehabilitation-functioning/` 的关系：本域关注一般身体活动和移动能力，康复域关注损伤或疾病后的功能恢复。

## Human Infra 模型链路

```text
活动 / 移动干预 T
  -> 改变心肺适能、肌肉骨骼、代谢、情绪和认知变量 X
  -> 改变主体行动状态 S
  -> 改变慢病、失能、跌倒、疲劳和死亡风险
  -> 增加有效行动密度和长期任务能力
```

## 非目标

- 不提供个体训练计划、运动处方、康复方案或医学建议。
- 不把高强度表现主义等同于主体持续性。
- 不鼓励带伤训练或忽略恢复、睡眠、营养和医疗边界。

## Source Signals

- WHO Physical Activity: https://www.who.int/news-room/fact-sheets/detail/physical-activity
- WHO Guidelines on Physical Activity and Sedentary Behaviour: https://www.who.int/publications/i/item/9789240015128
