# Fluid Electrolyte Acid Base Homeostasis

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/fluid-electrolyte-acid-base-homeostasis` |
| 分级 | `C2` - 可能性源体维护层 |
| 控制轴 | 生命载体维护 |
| 分级理由 | 直接维护身体、脑、器官、衰老、损伤或生命系统这些可能性源体。 |
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


Fluid Electrolyte Acid Base Homeostasis 负责整理水分、电解质、渗透压、酸碱平衡和内环境稳定如何支撑主体持续性。

核心问题：

> 主体持续行动依赖可稳定的内部化学环境；水、电解质和 pH 一旦失衡，认知、肌肉、心律、肾脏、神经和生命支持都会迅速失稳。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须维持内部环境稳定
  -> 水分、电解质、渗透压和酸碱状态决定细胞、神经、肌肉、循环和药物安全
  -> 脱水、水中毒、电解质紊乱或酸碱失衡会直接改变急性死亡风险和行动能力
  -> 因此体液电解质酸碱稳态是主体持续性的基础化学域
```

## 关注对象

- 水分平衡、钠、钾、钙、镁、氯、碳酸氢盐、渗透压和酸碱状态。
- 脱水、低钠/高钠、低钾/高钾、酸中毒、碱中毒、急慢性肾功能约束和药物安全。
- 热暴露、腹泻呕吐、出汗、肾脏、内分泌、心血管、神经和运动中的体液稳态问题。
- 内环境状态如何进入认知、行动、心律、治疗可用性、康复和极端环境模型。

## Human Infra 模型链路

```text
体液稳态相关因素 T
  -> 改变水分、电解质、渗透压、酸碱和肾脏调节变量 X
  -> 改变神经兴奋性、肌肉功能、心律稳定、认知清醒度和药物安全状态 S
  -> 改变急性失衡、跌倒、心律失常、住院、失能和死亡风险 λ(t)
  -> 影响健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供补液、盐分、电解质、酸碱、检查解释、药物调整、透析或急救建议。
- 不把单项实验室指标写成个体风险判断、处方或寿命结论。
- 不替代 `renal-hepatic-clearance/`、`endocrine-hormonal-regulation/` 或 `thermal-homeostasis-resilience/`，而是承载内环境化学主接口。

## Source Signals

- Merck Manual water balance: https://www.merckmanuals.com/home/hormonal-and-metabolic-disorders/electrolyte-balance/water-balance
- Merck Manual acid-base balance: https://www.merckmanuals.com/home/hormonal-and-metabolic-disorders/acid-base-balance/overview-of-acid-base-balance
- NCBI acid-base physiology: https://www.ncbi.nlm.nih.gov/books/NBK507807/

## 下一步

1. 建立体液稳态变量表：水分、钠钾钙镁、渗透压、酸碱、调节器官、急性失败模式。
2. 与 `renal-hepatic-clearance/`、`endocrine-hormonal-regulation/`、`thermal-homeostasis-resilience/` 和 `cardiovascular-resilience/` 建立交叉边界。
