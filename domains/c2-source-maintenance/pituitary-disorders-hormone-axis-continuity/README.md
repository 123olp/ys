# Pituitary Disorders Hormone Axis Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pituitary-disorders-hormone-axis-continuity` |
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

`pituitary-disorders-hormone-axis-continuity/` 研究垂体疾病、垂体腺瘤、激素轴调度、头痛/视野影响、催乳素/ACTH/GH/TSH/性腺轴异常、下丘脑-垂体接口和长期监测连续性如何影响主体持续性。

> 核心问题：垂体是多个内分泌轴的调度节点；它的问题常常不是单一激素，而是能量、生殖、压力、成长、视野、情绪和认知的多轴耦合失败。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要多个激素轴按时间和情境协调工作
  -> 垂体疾病会影响甲状腺、肾上腺、性腺、生长激素、催乳素和水盐调节等多条轴
  -> 结果取决于识别、影像与实验室边界、视觉/神经风险、长期监测、治疗后替代和复发风险
  -> 因此垂体疾病是内分泌调度层和多轴连续性的关键域
```

## 关注对象

- Pituitary disorders、pituitary tumors/adenomas、hypopituitarism context、hyperprolactinemia/prolactinoma context、headache/vision context、multi-axis hormone monitoring, long-term follow-up。
- 与 `thyroid-disease-endocrine-function-continuity/`、`adrenal-insufficiency-cortisol-stress-response-continuity/`、`hypogonadism-testosterone-sex-hormone-continuity/` 的关系：本域关注垂体调度层，不替代各靶腺域。
- 与 `vision-eye-health-continuity/` 的关系：视野压迫风险只作为功能接口，不提供眼科判断。

## Human Infra 模型链路

```text
垂体轴识别与监测系统 T
  -> 改变多激素轴、视野、头痛、疲劳、生殖、压力响应和长期替代治疗变量 X
  -> 改变能量、情绪、认知速度、视觉功能、生殖窗口和急性风险承载状态 S
  -> 改变失能、危象、视觉损害、治疗中断、复发和有效时间损耗风险 λ(t)
  -> 影响主体跨系统调节、行动质量和未来选择权
```

## 非目标

- 不提供个人垂体诊断、MRI/CT 判读、视野判读、激素化验解释、催乳素/ACTH/GH/TSH/性腺轴解释、用药、手术、放疗、妊娠、生育、急救或个体医疗建议。
- 不生成检查排序、病因定位、垂体腺瘤大小判断、药物调整、术后监测、保险申诉、工作/学校证明或视觉功能许可材料。
- 不收集个案化验、影像、视野报告、处方、病理、手术、妊娠、生育、照片、保险或身份资料。

## Source Signals

- MedlinePlus pituitary disorders: https://medlineplus.gov/pituitarydisorders.html
- MedlinePlus prolactin levels test: https://medlineplus.gov/lab-tests/prolactin-levels/

## 下一步

- 建立 Pituitary Axis Card：multi-axis state, mass-effect context, prolactin/GH/ACTH/TSH/gonadal interfaces, replacement continuity, recurrence boundary。
- 与 `endocrine-hormonal-regulation/`、`vision-eye-health-continuity/`、`neuro-continuity/` 和各靶腺域建立接口。
