# Cancer Survivorship Late Effects Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cancer-survivorship-late-effects-continuity` |
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

`cancer-survivorship-late-effects-continuity/` 研究癌症幸存者的复发恐惧、晚期效应、二次肿瘤、器官毒性、疲劳、心理健康、工作/保险、家庭角色和长期照护转接如何影响主体持续性。

> 核心问题：癌症治疗结束不是连续性的结束；幸存者阶段常把复发风险、晚期毒性、财务压力、工作身份、照护角色和长期不确定性带入主体系统。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体在重大疾病后需要恢复可行动、可学习、可工作、可关系化的存在状态
  -> 癌症幸存者晚期效应和复发恐惧改变有效时间、身体储备、心理安全和资源结构
  -> 长期随访、二次预防、工作/保险支持和照护转接决定治疗后主体是否真正回到未来路径
  -> 因此癌症幸存者晚期效应是癌症连续性的恢复与长期治理域
```

## 关注对象

- Cancer survivorship, late effects, recurrence fear, second cancers, organ toxicity, fatigue, mental health, work / insurance, care transition, quality of life。
- 与各器官癌症域的关系：本域提供跨癌种幸存者和晚期效应框架，各器官域保留自身治疗和复发路径。
- 与 `mental-health-continuity/`、`workplace-safety-labor-rights` 和 `social-protection-benefits-delivery/` 的关系：癌症后连续性常取决于心理、劳动和社会保护系统。

## Human Infra 模型链路

```text
癌症幸存者连续性系统 T
  -> 改变晚期效应监测、复发恐惧、二次肿瘤、器官毒性、疲劳、工作/保险和照护转接变量 X
  -> 改变身体储备、心理安全、劳动参与、家庭角色和资源状态 S
  -> 改变复发/二次癌症、长期失能、有效时间损失和资源耗竭 λ(t)
  -> 影响主体健康寿命、可持续创造、关系稳定和未来选择权
```

## 非目标

- 不提供个人随访计划、复发判断、症状诊断、晚期效应诊断、用药、康复方案、保险/工作证明、预后判断或个体建议。
- 不生成个人癌症幸存者风险预测器、复发恐惧治疗器、保险申诉、工作能力证明或商业康复推广。
- 不收集个案治疗史、病理、随访、症状、工作、保险、财务或心理资料。

## Source Signals

- NCI survivorship: https://www.cancer.gov/about-cancer/coping/survivorship
- NCI follow-up medical care: https://www.cancer.gov/about-cancer/coping/survivorship/follow-up-care
- CDC cancer survivors: https://www.cdc.gov/cancer-survivors/

## 下一步

- 建立 Survivorship Continuity Card：late effects, recurrence fear, secondary cancers, organ toxicity, fatigue, mental health, work / insurance, care transition。
- 与所有器官特异癌症域、`mental-health-continuity/` 和 `social-protection-benefits-delivery/` 建立接口。
