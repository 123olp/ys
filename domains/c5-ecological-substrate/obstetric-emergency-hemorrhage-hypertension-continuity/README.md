# Obstetric Emergency Hemorrhage Hypertension Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/obstetric-emergency-hemorrhage-hypertension-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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


`obstetric-emergency-hemorrhage-hypertension-continuity/` 研究产科出血、子痫前期/子痫、妊娠高血压、产后危险窗口、转运/产科团队能力和母体恢复如何影响主体持续性。

> 核心问题：妊娠和产后阶段会把一个主体的循环、凝血、血压、肾脏、神经和社会支持同时推入高负荷状态。产科出血和高血压急症是可预防孕产妇死亡的重要急性边界。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体在妊娠、分娩和产后阶段承受特殊循环、凝血和血压负荷
  -> 出血、高血压和子痫可快速改变死亡、脑损伤、肾损伤和家庭连续性
  -> 结果取决于识别、转运、产科团队、血液系统、ICU 接口和产后随访
  -> 因此产科急症是生命历程中高负荷阶段的急性主体持续性域
```

## 关注对象

- Obstetric hemorrhage、postpartum hemorrhage、preeclampsia/eclampsia、severe maternal morbidity、maternal mortality review, transport, blood availability, postpartum follow-up。
- 与 `maternal-newborn-child-development/` 的边界：该域关注母婴儿童发展；本域关注孕产妇急性死亡和严重并发症窗口。
- 与 `transfusion-blood-management-hemorrhage-continuity/` 和 `hypertensive-crisis-end-organ-risk-continuity/` 的关系：产科出血与高血压急症分别连接血液系统和血管靶器官风险。

## Human Infra 模型链路

```text
产科急症系统 T
  -> 改变识别、转运、产科团队、血液可得、ICU 接口和产后随访变量 X
  -> 改变出血、血压、神经/肾脏损伤、住院、母体恢复和家庭连续性状态 S
  -> 改变孕产妇死亡、严重并发症、长期失能和照护断裂风险 λ(t)
  -> 影响主体存活、家庭系统和未来选择权
```

## 非目标

- 不提供妊娠/产后症状判断、血压判断、出血判断、用药、分娩方式、医院选择、转运、母乳、产后恢复或个体医疗建议。
- 不生成产科 emergency plan、风险评分、家庭处理、药物路径、分娩决策或产后预警工具。
- 不收集个案妊娠状态、血压、出血量、胎儿信息、病历、位置、家庭或法律资料。

## Source Signals

- ACOG obstetric hemorrhage and hypertension materials: https://www.acog.org/
- WHO postpartum haemorrhage and maternal health materials: https://www.who.int/
- CDC maternal mortality / severe maternal morbidity materials: https://www.cdc.gov/maternal-mortality/

## 下一步

- 建立 Obstetric Emergency Card：hemorrhage, hypertension/eclampsia, transport, blood interface, ICU interface, postpartum follow-up。
- 与 `maternal-newborn-child-development/`、`transfusion-blood-management-hemorrhage-continuity/` 和 `hypertensive-crisis-end-organ-risk-continuity/` 建立接口。
