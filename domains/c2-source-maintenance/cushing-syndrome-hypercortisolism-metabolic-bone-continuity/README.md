# Cushing Syndrome Hypercortisolism Metabolic Bone Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cushing-syndrome-hypercortisolism-metabolic-bone-continuity` |
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


`cushing-syndrome-hypercortisolism-metabolic-bone-continuity/` 研究 Cushing's syndrome、长期高皮质醇、代谢风险、肌肉骨骼脆弱、情绪认知影响、感染风险和治疗后恢复连续性如何影响主体持续性。

> 核心问题：皮质醇过多不是单个症状，而是会同时改变体脂、血糖、血压、骨骼、肌力、睡眠、情绪、感染风险和外貌污名的系统性负荷。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要压力激素在合适窗口内工作，而不是长期过量
  -> 高皮质醇会改变代谢、骨骼、肌肉、免疫、睡眠、情绪和认知变量
  -> 结果取决于识别、病因定位、治疗通路、术后/治疗后恢复、复发监测和长期功能支持
  -> 因此库欣综合征是激素过量如何压缩健康寿命和有效时间的关键域
```

## 关注对象

- Cushing's syndrome、hypercortisolism、pituitary/adrenal/iatrogenic context、diabetes/hypertension risk、osteoporosis/fracture risk、muscle weakness、mood/cognition, recovery after treatment。
- 与 `adrenal-insufficiency-cortisol-stress-response-continuity/` 的关系：两者同属 HPA/cortisol axis，但一个关注不足和危象，一个关注过量和长期系统负荷。
- 与 `obesity-adiposity-metabolic-risk-continuity/`、`osteoporosis-fracture-prevention-bone-health-continuity/` 的关系：本域只聚焦高皮质醇机制。

## Human Infra 模型链路

```text
库欣综合征识别与恢复连续性 T
  -> 改变皮质醇暴露、血糖、血压、骨密度、肌力、睡眠、情绪和感染风险变量 X
  -> 改变代谢负荷、骨折脆弱性、工作能力、恢复速度、外貌污名和长期监测状态 S
  -> 改变心血管、骨折、感染、失能、复发和有效时间损耗风险 λ(t)
  -> 影响主体行动质量、恢复能力和长期健康寿命
```

## 非目标

- 不提供个人诊断、实验室判读、皮质醇/ACTH/地塞米松抑制试验解释、影像判断、病因定位、用药、手术、放疗、激素调整、减重、骨质疏松治疗或个体医疗建议。
- 不生成检查排序、治疗选择、术后计划、复发监测、保险申诉、工作/学校证明、外貌评估或心理处置脚本。
- 不收集个案化验、影像、处方、病理、手术记录、照片、体重、血压血糖、骨密度或保险资料。

## Source Signals

- NIDDK Cushing's syndrome: https://www.niddk.nih.gov/health-information/endocrine-diseases/cushings-syndrome
- MedlinePlus Cushing syndrome: https://medlineplus.gov/ency/article/000410.htm

## 下一步

- 建立 Hypercortisolism Burden Card：source context, metabolic load, bone/muscle effects, mood/cognition, recovery and recurrence boundary。
- 与 `endocrine-hormonal-regulation/`、`metabolic-energy-homeostasis/`、`musculoskeletal-integrity/` 和 `mental-health-affective-stability/` 建立接口。
