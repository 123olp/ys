# Bloodborne Pathogens Sharps Injury Worker Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/bloodborne-pathogens-sharps-injury-worker-continuity` |
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

`bloodborne-pathogens-sharps-injury-worker-continuity/` 研究血源性病原体、针刺/锐器伤、医疗和照护工作者暴露、报告、随访、污名和长期心理负担如何影响主体持续性。

核心问题：

> 照护别人时，主体可能通过血液、锐器和体液暴露承担感染和焦虑风险；安全系统必须保护照护者本身的身体、时间和尊严。

## 先验位置

```text
有效永生 / 主体持续性
  -> 医疗、照护、清洁和应急工作需要接触血液、锐器和体液
  -> 针刺或锐器伤可能暴露 HBV、HCV、HIV 等血源性病原体
  -> 暴露后报告、评估、随访和心理负担会影响工作者持续行动
  -> 因此血源性病原体与锐器伤治理是照护系统保护自身的条件
```

## 关注对象

- Bloodborne pathogens、needlestick injuries、sharps injury、HBV/HCV/HIV exposure context、exposure control plan、reporting and follow-up。
- 风险链：照护/清洁任务 -> 锐器/血液暴露 -> 报告/随访断裂 -> 感染风险/焦虑/污名 -> 工作退出或持续负担。
- 制度链：engineering controls、safer devices、training、vaccination context、post-exposure workflow、confidentiality。

## Human Infra 模型位置

```text
照护/医疗任务 T
  -> 改变血液和锐器暴露 X
  -> 改变感染风险、心理负担和工作状态 S
  -> 改变长期健康/工作退出风险 lambda(t)
  -> 改变照护人力、家庭资源和未来选择权
```

## 非目标

- 不提供暴露后处理、PEP、检测、疫苗、用药、针刺处置、感染判断、职业健康流程、报告表填写或个人医疗建议。
- 不判断个人风险、雇主责任、工伤、隐私投诉、OSHA 违规、复工或法律策略。
- 不帮助隐藏暴露、规避报告、重复使用锐器、绕开感染控制或收集可识别健康资料。

## Source Signals

- OSHA Bloodborne Pathogens: https://www.osha.gov/bloodborne-pathogens
- CDC/NIOSH Bloodborne Infectious Diseases: https://www.cdc.gov/niosh/topics/bbp/

## 下一步

- 建立 Sharps Exposure Continuity Card：task context、sharp type、exposure pathway、reporting latency、follow-up boundary、stigma/confidentiality。
- 与 `health-workforce-capacity/`、`sterilization-disinfection-infection-control/` 和 `occupational-exposure-industrial-hygiene/` 建立接口。
