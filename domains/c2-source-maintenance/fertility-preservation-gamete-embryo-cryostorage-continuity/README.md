# Fertility Preservation Gamete Embryo Cryostorage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/fertility-preservation-gamete-embryo-cryostorage-continuity` |
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

生育保存、配子/胚胎冷冻储存连续性，关注 medical fertility preservation、planned oocyte cryopreservation、egg/sperm/embryo cryostorage、储存同意、样本身份、长期费用、处置授权、灾害停电和未来使用权如何影响主体长期选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 长期主体需要保留未来行动和关系路径
  -> 癌症治疗、性腺毒性治疗、年龄、生殖疾病和社会时间表会压缩生育窗口
  -> 配子/胚胎冷冻把当前生殖材料转化为未来可选资源
  -> 因此生育保存是把未来选择权从身体时间窗口中部分解耦的基础设施
```

## 关注对象

- 医疗适应证生育保存、planned oocyte cryopreservation、精子/卵母细胞/胚胎冷冻、卵巢组织保存和儿童/青少年边界。
- 样本身份、chain of custody、储存温度、灾害停电、库存记录、费用续缴、知情同意、处置指令和死亡/失能后的授权。
- 与 `reproductive-fertility-continuity/` 的边界：上位域关注生殖未来选择权；本域关注生殖材料保存和长期可用性。

## Human Infra 模型链路

```text
生育保存 T
  -> 改变配子/胚胎可用性、储存可靠性、身份追踪、费用续缴和未来使用授权变量 X
  -> 改变主体未来生殖选择权、疾病治疗决策、心理负担和长期计划状态 S
  -> 改变生育窗口丧失、样本丢失、同意冲突、费用中断和未来不可用风险 lambda(t)
  -> 影响主体长期选择权、关系路径和跨时间资源保全能力
```

## 非目标

- 不提供是否冷冻、何时冷冻、促排取精取卵、胚胎处置、成功率、诊所、费用、保险或法律建议。
- 不把冷冻保存写成保证未来生育或保证亲缘结果。
- 不处理可执行实验室操作、样本运输协议、温控工程设计或具体灾害应急操作。

## Source Signals

- ASRM Fertility preservation in patients with medical indications: https://www.asrm.org/practice-guidance/practice-committee-documents/fertility-preservation-in-patients-with-medical-indications-a-committee-opinion-2026/
- ASRM Planned oocyte cryopreservation: https://www.asrm.org/practice-guidance/ethics-opinions/planned-oocyte-cryopreservation/
- CDC About ART: https://www.cdc.gov/art/about/index.html
- FDA Tissue & Tissue Products: https://www.fda.gov/vaccines-blood-biologics/tissue-tissue-products

## 下一步

1. 建立 cryostorage continuity card：specimen identity、storage status、fee continuity、consent, disposition, disaster boundary 和 future-use authorization。
2. 与 `reproductive-tissue-donor-screening-traceability-continuity/`、`trust-estate-affairs-succession-continuity/` 和 `refrigerated-medication-medical-device-power-outage-continuity/` 建立接口。
