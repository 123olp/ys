# Chronic Viral Hepatitis Screening Liver Protection Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-viral-hepatitis-screening-liver-protection-continuity` |
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

`chronic-viral-hepatitis-screening-liver-protection-continuity/` 研究乙肝、丙肝筛查、确认、治疗连接、肝纤维化/肝癌风险监测和公共卫生消除路径如何影响主体持续性。

> 核心问题：慢性病毒性肝炎常长期无症状，却可逐步改变肝硬化、肝癌、感染传播、治疗机会和寿命路径。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖肝脏代谢、解毒、凝血和免疫相关功能维持长期状态
  -> 慢性乙肝/丙肝可在无症状阶段推进纤维化、肝硬化和肝癌风险
  -> 结果取决于筛查、确认、分期、治疗连接、随访和风险监测连续性
  -> 因此慢性病毒性肝炎是感染、肝脏清除和癌症预防之间的关键域
```

## 关注对象

- Hepatitis B screening、hepatitis C screening、confirmatory testing、linkage to care、treatment access、fibrosis staging、cirrhosis and liver cancer surveillance, vaccination interface。
- 与 `renal-hepatic-clearance/` 的边界：该域关注肝肾清除总机制；本域关注病毒性肝炎筛查和长期风险控制执行链。
- 与 `cancer-screening-early-detection-continuity/` 的关系：慢性病毒性肝炎是肝癌风险管理的重要上游条件。

## Human Infra 模型链路

```text
慢性病毒性肝炎筛查与治疗连接系统 T
  -> 改变筛查覆盖、确认率、治疗连接、纤维化分期、随访和肝癌监测变量 X
  -> 改变肝脏储备、炎症/纤维化、感染传播和癌前风险状态 S
  -> 改变肝硬化、肝癌、急性失代偿、有效时间损失和死亡风险 λ(t)
  -> 影响主体长期身体储备、工作能力、照护负担和未来选择权
```

## 非目标

- 不提供个人肝炎检测判读、疫苗建议、抗病毒药物、剂量、监测周期、肝癌筛查安排或临床分诊。
- 不生成个人感染风险评分、化验解释、家庭传播处理、保险路径或治疗建议。
- 不收集个案检测、肝功能、病毒载量、影像、药物、性行为、注射暴露或身份资料。

## Source Signals

- CDC hepatitis B information: https://www.cdc.gov/hepatitis-b/
- CDC hepatitis C information: https://www.cdc.gov/hepatitis-c/
- CDC viral hepatitis screening and testing: https://www.cdc.gov/hepatitis/php/testing/index.html
- USPSTF hepatitis C screening: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/hepatitis-c-screening

## 下一步

- 建立 Viral Hepatitis Continuity Card：screening, confirmation, staging, linkage, treatment access, surveillance, prevention。
- 与 `renal-hepatic-clearance/`、`chronic-infectious-disease-care-continuity/` 和 `cancer-screening-early-detection-continuity/` 建立接口。
