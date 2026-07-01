# Prediabetes Diabetes Prevention Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/prediabetes-diabetes-prevention-continuity` |
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


`prediabetes-diabetes-prevention-continuity/` 研究糖尿病前期筛查、2 型糖尿病预防项目、生活方式支持、体重/活动环境、随访和转化为长期照护的过程如何影响主体持续性。

> 核心问题：糖尿病风险常在多年无症状状态中累积，最终改变血管、肾脏、神经、视网膜和急性代谢危象风险。有效永生需要把糖尿病预防建模为急性危象和慢性并发症之前的概率分布调整器。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖稳定葡萄糖和胰岛素系统维持能量、血管和神经功能
  -> 糖尿病前期会提高未来糖尿病及并发症风险
  -> 结果取决于筛查、转介、预防项目、可持续行为环境和随访
  -> 因此糖尿病预防是代谢危象和慢性并发症的上游执行域
```

## 关注对象

- Prediabetes screening、Diabetes Prevention Program、referral, retention, weight/activity support, social barriers, conversion to chronic diabetes care。
- 与 `nutrition-metabolic-health/` 的边界：该域关注营养代谢机制；本域关注糖尿病前期识别和预防项目执行。
- 与 `diabetic-hyperglycemic-hypoglycemic-crisis-continuity/` 的关系：本域处理急性危象之前的长期风险转移，后者处理 DKA/HHS/严重低血糖。

## Human Infra 模型链路

```text
糖尿病预防系统 T
  -> 改变筛查、转介、项目保留、体重/活动支持和随访变量 X
  -> 改变胰岛素抵抗、糖代谢、血管/神经/肾脏风险状态 S
  -> 改变糖尿病发病、并发症、急性危象和有效时间损失 λ(t)
  -> 影响主体健康寿命、行动能力和未来选择权
```

## 非目标

- 不提供个人血糖/A1c 解读、诊断、饮食、运动、药物、补剂、减重、设备或个体预防建议。
- 不生成个人糖尿病风险评分、项目选择、保险申诉、CGM/胰岛素设置或治疗建议。
- 不收集个案血糖、体重、饮食、活动、用药、病史或诊疗资料。

## Source Signals

- USPSTF prediabetes and type 2 diabetes screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/screening-for-prediabetes-and-type-2-diabetes
- CDC National Diabetes Prevention Program: https://www.cdc.gov/diabetes/prevention/
- NIDDK diabetes information: https://www.niddk.nih.gov/health-information/diabetes

## 下一步

- 建立 Diabetes Prevention Card：screening, referral, retention, access, behavior support, conversion, complications prevention。
- 与 `nutrition-metabolic-health/`、`diabetes-insulin-glucose-monitoring-supplies-continuity/` 和 `diabetic-hyperglycemic-hypoglycemic-crisis-continuity/` 建立接口。
