# 证据模型

Longevity Evidence 的核心不是长寿百科，而是围绕“主张”组织证据。

## 核心实体

### Intervention

干预方法，例如 rapamycin、metformin、运动、限食、NAD+ 前体、senolytics。

关键字段：

- `name`
- `category`
- `mechanism_summary`
- `known_risks`
- `status`

### Claim

关于干预的具体主张，例如“rapamycin 可能延长健康寿命”。

关键字段：

- `intervention_id`
- `claim_text`
- `population`
- `outcome`
- `confidence_level`
- `last_reviewed_at`

### Evidence

支持或反驳主张的证据。

关键字段：

- `source_type`
- `source_id`
- `title`
- `year`
- `study_type`
- `species`
- `population`
- `sample_size`
- `outcome`
- `effect_summary`
- `limitations`

### Trial

临床试验信息。

关键字段：

- `nct_id`
- `status`
- `phase`
- `intervention`
- `condition`
- `primary_outcome`
- `results_available`

## 初始证据等级

| 等级 | 含义 |
| --- | --- |
| 0 | 营销说法或机制猜想，缺少直接证据 |
| 1 | 体外或机制实验 |
| 2 | 动物实验 |
| 3 | 人体观察研究 |
| 4 | 小型人体 RCT 或明确临床试验 |
| 5 | 多项高质量人体 RCT、系统综述或指南级证据 |

## 评分原则

- 人体证据和动物证据分开标注。
- 效果大小和证据确定性分开标注。
- 安全风险独立于有效性评分。
- 不确定性必须显式展示。
