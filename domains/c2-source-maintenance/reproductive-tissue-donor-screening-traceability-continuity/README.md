# Reproductive Tissue Donor Screening Traceability Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/reproductive-tissue-donor-screening-traceability-continuity` |
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

生殖组织供体筛查、检测、标签和可追溯连续性，关注 sperm、oocyte、embryo donation、HCT/P donor eligibility、communicable disease screening/testing、directed donor、anonymous/nonidentified donor、标签警示和记录保存如何影响安全、身份与未来权利。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 生殖技术把身体材料、亲缘关系、感染风险、身份信息和未来子代权利连接起来
  -> 供体筛查、检测、标签和记录决定材料能否被安全、可解释、可追溯地使用
  -> 如果追溯链断裂，主体和后代会面对感染、身份、法律、心理和医学信息风险
  -> 因此生殖组织供体可追溯性是 ART 安全与主体连续性的治理接口
```

## 关注对象

- FDA HCT/P、donor eligibility、donor screening/testing、reproductive cells and tissue、directed reproductive donor 和 donor summary records。
- sperm/oocyte/embryo donor evaluation、遗传/感染/心理筛查边界、标签、记录、样本身份和后代可识别性。
- 与 `fertility-preservation-gamete-embryo-cryostorage-continuity/` 的边界：冷冻域关注长期保存；本域关注供体资格、检测、标签和可追溯。

## Human Infra 模型链路

```text
供体筛查与追溯 T
  -> 改变感染风险识别、遗传资料、身份记录、标签警示、样本链和后代信息变量 X
  -> 改变主体使用生殖材料、信任诊所、管理亲缘/医学信息和保护后代权益状态 S
  -> 改变传播风险、样本错配、身份冲突、资料不可得和法律伦理争议风险 lambda(t)
  -> 影响生殖技术安全性、关系连续性和未来选择权的可治理性
```

## 非目标

- 不提供供体选择、筛查结果解释、遗传风险解释、感染风险判断、捐精捐卵、胚胎捐赠、法律或亲子关系建议。
- 不处理可执行实验室、采样、储存、运输或匿名识别操作。
- 不鼓励规避 FDA、CDC、ASRM、诊所、法律或伦理审查要求。

## Source Signals

- FDA What You Should Know - Reproductive Tissue Donation: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/what-you-should-know-reproductive-tissue-donation
- FDA Recommendations for Determining Eligibility of Donors of HCT/Ps: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/recommendations-determining-eligibility-donors-human-cells-tissues-and-cellular-and-tissue-based
- FDA Testing Donors of HCT/P Specific Requirements: https://www.fda.gov/vaccines-blood-biologics/safety-availability-biologics/testing-donors-human-cells-tissues-and-cellular-and-tissue-based-products-hctp-specific-requirements
- ASRM Gamete and embryo donation guidance: https://www.asrm.org/practice-guidance/practice-committee-documents/guidance-regarding-gamete-and-embryo-donation/

## 下一步

1. 建立 reproductive donor traceability card：donor type、eligibility、testing、labeling、records、identity boundary 和 offspring information rights。
2. 与 `third-party-reproduction-surrogacy-donor-legal-ethics-continuity/`、`health-data-privacy-governance/` 和 `biobanking-biospecimen-chain-of-custody/` 建立接口。
