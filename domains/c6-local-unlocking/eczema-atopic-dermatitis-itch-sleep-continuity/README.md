# Eczema, Atopic Dermatitis, Itch and Sleep Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/eczema-atopic-dermatitis-itch-sleep-continuity` |
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


`eczema-atopic-dermatitis-itch-sleep-continuity/` 研究湿疹/特应性皮炎、瘙痒、皮肤屏障、过敏炎症、睡眠中断、注意力消耗和生活质量如何影响主体有效时间。

> 核心问题：慢性瘙痒会把皮肤炎症转化为睡眠、注意力、情绪和学习执行的长期税收。

## 先验位置

```text
有效永生
  -> 主体持续性依赖睡眠、注意力和情绪稳定
  -> 湿疹/特应性皮炎会通过瘙痒和屏障失效持续打断恢复
  -> 恢复被打断会降低单位时间行动质量和学习轮次
  -> 因此湿疹是皮肤炎症影响有效时间的执行域
```

## 关注对象

- Eczema, atopic dermatitis, itch, barrier dysfunction, sleep disruption, allergy burden, flare, quality of life and care access。
- 与 `allergic-atopic-disease-immunologic-burden-continuity/` 的关系：后者关注过敏/特应性疾病总负担，本域关注皮肤、瘙痒和睡眠执行链。

## Human Infra 模型链路

```text
湿疹和瘙痒控制连续性 T
  -> 改变皮肤屏障、炎症、瘙痒、睡眠中断和护理可及 X
  -> 改变恢复质量、注意力、情绪稳定和生活执行 S
  -> 改变失眠、感染、心理负担和功能下降风险 lambda(t)
  -> 改变有效时间、学习能力和未来选择权
```

## 非目标

- 不提供诊断、处方、激素/免疫药物建议、皮肤护理产品推荐、过敏检测解释或个体治疗建议。
- 不根据皮疹照片、瘙痒描述或年龄输出疾病判断。

## Source Signals

- NIAMS atopic dermatitis materials.
- MedlinePlus eczema materials.
- AAD public eczema education materials as contextual sources.
