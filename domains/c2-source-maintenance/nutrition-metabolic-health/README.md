# Nutrition Metabolic Health

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/nutrition-metabolic-health` |
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


Nutrition Metabolic Health 负责整理营养、饮食质量、代谢健康、体重、糖尿病风险、微量营养和食物环境。

核心问题：

> 主体持续行动需要稳定的能量、代谢和修复材料；营养与代谢失衡会通过慢病、疲劳、炎症和失能压缩有效时间。

## 先验位置

```text
主体持续性最大化
  -> 身体必须持续获得能量、结构材料和代谢稳定性
  -> 饮食质量、食物环境和代谢状态决定长期慢病风险
  -> 代谢失衡会影响心血管、免疫、肾脏、神经、行动和恢复
  -> 因此营养与代谢健康是主体有效时间的基础变量
```

## 关注对象

- 饮食模式、营养质量、能量平衡、蛋白质、纤维、微量营养和超加工食品暴露。
- 肥胖、糖尿病、胰岛素抵抗、脂代谢、营养不良和肌少症交叉风险。
- 食物可及性、价格、文化、工作节奏和社会环境对营养选择的影响。
- 与 `measurement-feedback/` 的关系：体重、血糖、血脂和代谢指标只能作为状态观测，不等于完整健康结论。

## Human Infra 模型链路

```text
营养 / 代谢干预 T
  -> 改变能量供给、代谢稳定、炎症、体重和修复材料 X
  -> 改变身体状态 S
  -> 改变心血管、糖尿病、肾脏、免疫、行动和恢复风险
  -> 改变健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供个体饮食处方、减重方案、补剂方案或医学建议。
- 不把单一营养素写成延寿变量。
- 不用热量、体重或血糖单指标替代主体持续性模型。

## Source Signals

- WHO Healthy Diet: https://www.who.int/news-room/fact-sheets/detail/healthy-diet
- WHO Obesity and Overweight: https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight
