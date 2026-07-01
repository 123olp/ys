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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定生命载体变量：细胞、组织、器官、脑、免疫、代谢、急性风险或衰老损伤。
- 说明影响机制：修复、替换、再生、控制、筛查、预防、维持或风险降低。
- 列出可观察状态：功能指标、生物标志物、疾病终点、失能时间、恢复能力或死亡风险。
- 记录副作用、过度干预、癌变、免疫、长期安全性和尾部风险。
- 区分机制合理性、体外证据、动物证据、人体早期数据、临床终点和长期安全性。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
