# Skin Cancer UV Protection Early Detection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/skin-cancer-uv-protection-early-detection-continuity` |
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

`skin-cancer-uv-protection-early-detection-continuity/` 研究 UV 暴露、皮肤癌预防、日晒防护、风险沟通、早期识别、转诊可及和职业/户外环境如何影响主体持续性。

> 核心问题：皮肤癌风险是环境暴露、行为、职业、肤色不平等、早期识别和医疗可及共同决定的长期风险。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体皮肤屏障和户外行动暴露于长期 UV 风险
  -> UV 暴露可改变皮肤癌、眼部损伤、职业风险和未来治疗负担
  -> 结果取决于防晒环境、行为支持、风险沟通、早期识别、转诊和公平可及
  -> 因此皮肤癌与 UV 防护是环境暴露控制和癌症早期检测之间的执行域
```

## 关注对象

- UV exposure、sun protection counseling、shade and occupational exposure, skin cancer prevention, early detection access, suspicious lesion referral, skin tone equity, indoor tanning risk。
- 与 `cancer-screening-early-detection-continuity/` 的边界：该域关注癌症筛查总执行；本域关注皮肤癌、UV 暴露和早期识别。
- 与 `skin-barrier-wound-healing/` 的关系：皮肤屏障域关注组织完整性，本域关注 UV/癌症风险。

## Human Infra 模型链路

```text
UV 防护与皮肤癌早识别系统 T
  -> 改变 UV 暴露、防晒环境、风险沟通、早期识别、转诊可及和肤色公平变量 X
  -> 改变皮肤损伤、癌前风险、治疗时机、职业暴露和心理负荷 S
  -> 改变皮肤癌进展、治疗负担、有效时间损失和死亡风险 λ(t)
  -> 影响主体户外行动、工作可持续性、身体完整性和未来选择权
```

## 非目标

- 不提供个人痣/皮损判断、照片诊断、防晒产品选择、筛查周期、治疗、活检、用药或转诊建议。
- 不生成个人皮肤癌风险评分、职业暴露合规判定、保险路径或医疗分诊。
- 不收集个案皮肤照片、病史、肤色、职业、定位、基因或身份敏感资料。

## Source Signals

- CDC skin cancer prevention: https://www.cdc.gov/skin-cancer/prevention/
- USPSTF skin cancer prevention counseling: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/skin-cancer-counseling
- NCI skin cancer prevention: https://www.cancer.gov/types/skin/patient/skin-prevention-pdq

## 下一步

- 建立 Skin UV Continuity Card：exposure, protection environment, counseling, early recognition, referral, equity, occupational risk。
- 与 `cancer-screening-early-detection-continuity/`、`skin-barrier-wound-healing/` 和 `occupational-exposure-industrial-hygiene/` 建立接口。
