# Chronic Wound, Venous, Diabetic and Pressure Ulcer Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-wound-venous-diabetic-pressure-ulcer-continuity` |
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


`chronic-wound-venous-diabetic-pressure-ulcer-continuity/` 研究静脉性溃疡、糖尿病相关溃疡、压力性损伤和其他慢性伤口如何把短期创伤转化为长期感染、疼痛、行动受限和照护依赖。

> 核心问题：慢性伤口意味着身体边界无法按预期闭合，主体持续暴露在感染、疼痛、资源消耗和功能下降中。

## 先验位置

```text
有效永生
  -> 主体必须能够修复边界破损
  -> 血流、代谢、压力、感染和护理失败会让伤口进入慢性化
  -> 慢性伤口消耗恢复资源并扩大感染和失能风险
  -> 因此慢性伤口是皮肤修复系统的长期失败域
```

## 关注对象

- Chronic wound, venous ulcer, diabetic ulcer, pressure ulcer, wound chronicity, pain, drainage, recurrence and care burden。
- 与 `pressure-injury-prevention-repositioning-support-surface-continuity/` 的关系：后者关注预防压力损伤，本域关注已慢性化伤口的高层证据和连续性边界。

## Human Infra 模型链路

```text
慢性伤口治理连续性 T
  -> 改变血流、代谢、压力、感染控制、护理可及和复发风险 X
  -> 改变伤口闭合能力、疼痛、行动限制和照护负担 S
  -> 改变感染、住院、截肢、失能和死亡风险 lambda(t)
  -> 改变有效寿命、独立性和资源消耗
```

## 非目标

- 不提供伤口清创、敷料、压迫治疗、抗生素、疼痛用药、图片判断或个体治疗建议。
- 不替代糖尿病足、压力损伤、烧伤、手术伤口和感染等下层域。

## Source Signals

- NCBI wound healing overview.
- MedlinePlus wounds and injuries materials.
- AHRQ / CMS pressure injury and long-term-care quality materials.
