# Obesity Adiposity Metabolic Risk Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/obesity-adiposity-metabolic-risk-continuity` |
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

`obesity-adiposity-metabolic-risk-continuity/` 研究肥胖、脂肪分布、代谢风险、结构性环境、体重管理服务、污名风险和长期功能结局如何影响主体持续性。

> 核心问题：肥胖和脂肪分布不是单一意志问题，而是生物、药物、食物环境、睡眠、压力、城市设计、收入和照护系统共同作用的长期风险状态。有效永生需要把它建模为代谢、心血管、肌骨、癌症和有效时间的多路径变量。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖可持续能量平衡、行动能力和低炎症代谢环境
  -> 肥胖和脂肪分布会改变多疾病风险、治疗负担和社会参与
  -> 结果取决于环境、服务可及、抗污名沟通、长期支持和复发预防
  -> 因此肥胖/脂肪代谢风险是多系统慢病上游执行域
```

## 关注对象

- Adult obesity interventions, adiposity measures, cardiometabolic risk, access to obesity care, stigma, weight cycling, built / food environment, long-term maintenance。
- 与 `nutrition-metabolic-health/` 的边界：该域关注营养代谢机制；本域关注肥胖/脂肪风险的系统执行、服务可及和污名边界。
- 与 `physical-activity-mobility/` 的关系：行动和活动环境是输入之一，但本域不提供训练计划。

## Human Infra 模型链路

```text
肥胖与脂肪代谢风险治理 T
  -> 改变食物环境、活动环境、服务可及、污名、坚持和复发变量 X
  -> 改变代谢状态、炎症、行动负荷、心血管/癌症/关节风险 S
  -> 改变慢病发生、急症进入、失能和有效时间损失 λ(t)
  -> 影响主体健康寿命、行动半径和未来选择权
```

## 非目标

- 不提供个人 BMI/体脂解读、减重目标、饮食、运动、药物、手术、补剂、热量、餐单或个体医疗建议。
- 不生成羞辱性、道德化、审美化、体型歧视或商业减肥推荐内容。
- 不收集个案体重、体型、饮食、照片、病史、用药或行为数据。

## Source Signals

- CDC obesity: https://www.cdc.gov/obesity/
- USPSTF behavioral weight loss interventions: https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/obesity-in-adults-interventions
- WHO obesity: https://www.who.int/health-topics/obesity

## 下一步

- 建立 Metabolic Risk Card：adiposity, environment, access, stigma, intervention retention, comorbidity, function。
- 与 `nutrition-metabolic-health/`、`physical-activity-mobility/` 和 `prediabetes-diabetes-prevention-continuity/` 建立接口。
