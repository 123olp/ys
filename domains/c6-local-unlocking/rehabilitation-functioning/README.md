# Rehabilitation And Functioning

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rehabilitation-functioning` |
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


Rehabilitation And Functioning 负责整理康复、功能恢复、失能预防、活动能力、日常生活能力和长期参与能力。

核心问题：

> 有效永生不是只延长生物存活，而是让主体在损伤、疾病和衰退后仍能恢复功能、继续行动和参与生活。

## 先验位置

```text
主体持续性最大化
  -> 主体必须能行动、沟通、自理、工作和参与关系
  -> 疾病、损伤、衰老和残障会降低功能而不一定立即致死
  -> 如果功能无法恢复，延寿会变成低行动能力的被动持续
  -> 因此康复与功能是健康寿命转化为有效时间的必要条件
```

## 关注对象

- 康复医学、物理治疗、作业治疗、语言治疗和认知康复。
- 失能预防、衰弱、跌倒、移动能力、日常生活能力和社会参与。
- 康复服务可及性、长期康复、远程康复和社区康复。
- 与 `assistive-technology-access/` 的关系：康复恢复功能，辅助技术补偿或放大功能。

## Human Infra 模型链路

```text
康复干预 T
  -> 改变功能状态、活动能力、自理能力和参与能力 X
  -> 改变主体行动状态 S
  -> 降低失能、跌倒、依赖和社会退出风险 λ(t)
  -> 增加健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供个人康复处方、训练计划、医疗诊断或治疗建议。
- 不把寿命延长等同于功能延长。
- 不把单一功能评分改善外推为完整主体持续性收益。

## Source Signals

- WHO Rehabilitation: https://www.who.int/news-room/fact-sheets/detail/rehabilitation
- WHO Rehabilitation 2030: https://www.who.int/initiatives/rehabilitation-2030
