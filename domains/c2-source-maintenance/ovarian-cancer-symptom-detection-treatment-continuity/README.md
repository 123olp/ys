# Ovarian Cancer Symptom Detection Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/ovarian-cancer-symptom-detection-treatment-continuity` |
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

`ovarian-cancer-symptom-detection-treatment-continuity/` 研究卵巢癌症状识别、诊断延迟、遗传风险入口、治疗负担、复发管理、家庭照护和生活质量如何影响主体持续性。

> 核心问题：卵巢癌常缺少普通人群有效筛查路径，连续性重点不是简单“早筛”，而是症状被认真对待、风险入口不失联、诊断延迟被压缩和复发负担被管理。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖高死亡风险但筛查困难的癌种被及时识别和持续支持
  -> 卵巢癌症状非特异、诊断延迟和复发负担改变死亡风险和家庭资源消耗
  -> 症状识别、风险入口、治疗可及、复发管理和照护支持决定主体是否保留行动能力
  -> 因此卵巢癌是癌症连续性中的症状-诊断延迟治理域
```

## 关注对象

- Ovarian cancer symptoms, diagnostic delay, genetic risk pathway, treatment burden, recurrence, caregiver load, quality of life, equity。
- 与 `cancer-screening-early-detection-continuity/` 的边界：本域不假定普通筛查可行，重点放在症状识别、风险通道和诊断延迟。
- 与 `reproductive-fertility-continuity/` 和 `caregiving-family-support-continuity/` 的关系：卵巢癌强烈影响生殖系统、家庭照护和长期心理负担。

## Human Infra 模型链路

```text
卵巢癌连续性系统 T
  -> 改变症状识别、风险入口、诊断延迟、治疗可及、复发管理和照护变量 X
  -> 改变癌症阶段、治疗毒性、复发负担、家庭资源和心理状态 S
  -> 改变死亡、失能、有效时间损失和照护资源消耗 λ(t)
  -> 影响主体健康寿命、家庭系统、行动能力和未来选择权
```

## 非目标

- 不提供症状诊断、CA-125/影像判读、遗传风险解释、筛查建议、病理分型、分期、治疗方案、用药、手术或个体建议。
- 不生成个人卵巢癌风险计算器、症状分诊、影像/标志物解释、治疗排序或商业检测推广。
- 不收集个案症状、CA-125、影像、病理、遗传检测、家族史或治疗资料。

## Source Signals

- NCI ovarian cancer: https://www.cancer.gov/types/ovarian
- NCI ovarian cancer screening: https://www.cancer.gov/types/ovarian/screening
- CDC ovarian cancer: https://www.cdc.gov/ovarian-cancer/

## 下一步

- 建立 Ovarian Cancer Continuity Card：symptom recognition, diagnostic delay, hereditary risk pathway, treatment burden, recurrence, caregiver load。
- 与 `cancer-control/`、`reproductive-fertility-continuity/` 和 `cancer-survivorship-late-effects-continuity/` 建立接口。
