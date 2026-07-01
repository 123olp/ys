# Incontinence-Associated Dermatitis, Moisture and Skin Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/incontinence-associated-dermatitis-moisture-skin-continuity` |
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


`incontinence-associated-dermatitis-moisture-skin-continuity/` 研究尿失禁、粪失禁、潮湿暴露、摩擦、清洁用品、屏障产品和照护执行如何影响皮肤屏障、尊严、感染入口和长期照护质量。

> 核心问题：排泄失控不仅是泌尿或肠道问题，它会通过潮湿和刺激直接破坏皮肤边界与主体尊严。

## 先验位置

```text
有效永生
  -> 主体必须在排泄、清洁和皮肤保护之间保持稳定闭环
  -> 潮湿、尿液、粪便、摩擦和清洁失败会破坏屏障
  -> 屏障破坏增加疼痛、感染、压力损伤和照护羞耻负担
  -> 因此潮湿相关皮炎是排泄连续性与皮肤边界之间的接口域
```

## 关注对象

- Incontinence-associated dermatitis, moisture-associated skin damage, urine/stool exposure, cleansing, barrier products, friction and dignity。
- 与 `urogenital-continuity/` 的关系：后者关注排泄功能总框架，本域关注排泄暴露对皮肤边界的影响。

## Human Infra 模型链路

```text
潮湿暴露与皮肤保护连续性 T
  -> 改变尿/粪暴露、潮湿时间、摩擦、清洁和屏障用品可及 X
  -> 改变皮肤完整性、疼痛、感染入口和尊严状态 S
  -> 改变感染、压力损伤、照护负担和失能风险 lambda(t)
  -> 改变有效时间、照护质量和社会参与
```

## 非目标

- 不提供失禁用品选择、皮肤产品推荐、护理步骤、皮炎诊断、感染判断或个体照护建议。
- 不处理个人排泄、皮肤照片、长期照护机构或产品采购资料。

## Source Signals

- NCBI pressure injuries and skin integrity materials.
- CMS long-term-care quality and skin integrity materials.
- MedlinePlus urinary incontinence and skin care related materials.
