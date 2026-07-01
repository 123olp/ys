# Transfusion Blood Management Hemorrhage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/transfusion-blood-management-hemorrhage-continuity` |
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

`transfusion-blood-management-hemorrhage-continuity/` 研究输血、血液可得性、患者血液管理、大出血方案、凝血支持、血液安全和 hemovigilance 如何影响创伤、手术和危重病中的主体持续性。

> 核心问题：失血和凝血失败会迅速终止灌注。血液管理不是后勤细节，而是把创伤、手术和产科等急性风险转化为可救治窗口的基础设施。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体持续性依赖循环容量、携氧能力和凝血稳定
  -> 创伤、手术、产科和危重病可造成大出血或凝血障碍
  -> 输血和血液管理可恢复灌注，但受库存、匹配、安全和不良反应约束
  -> 因此输血与血液管理是出血性死亡边界的修复域
```

## 关注对象

- Blood availability、patient blood management、massive transfusion protocol、hemorrhage control、coagulation, transfusion safety, adverse events, hemovigilance。
- 与 `blood-organ-tissue-biovigilance-transplantation/` 的边界：该域关注血液/器官/组织系统整体；本域聚焦输血和出血性急救。
- 与 `trauma-system-hemorrhage-control-continuity/` 的关系：创伤系统常依赖大出血管理和血液可得。

## Human Infra 模型链路

```text
输血与血液管理 T
  -> 改变血液可得、匹配、安全、凝血、库存和不良事件变量 X
  -> 改变灌注、携氧、止血、手术/创伤结局和恢复状态 S
  -> 改变出血死亡、输血反应、感染、凝血失败和长期失能风险 λ(t)
  -> 影响主体急性存活、器官保护和恢复窗口
```

## 非目标

- 不提供输血阈值、血型匹配、输血方案、止血药、凝血处理、手术/产科/创伤个案建议。
- 不生成血液产品采购、献血资格、库存调度、医院协议或替代血库/医生的内容。
- 不收集血型、输血记录、化验、病历、献血者资料、供应合同或敏感医疗数据。

## Source Signals

- AABB Guidelines: https://www.aabb.org/news-resources/resources/clinical-practice-guidelines
- WHO Blood Safety and Availability: https://www.who.int/news-room/fact-sheets/detail/blood-safety-and-availability
- CDC Blood Safety: https://www.cdc.gov/blood-safety/

## 下一步

- 建立 Hemorrhage Blood Support Card：bleeding context, blood availability, protocol, matching, safety, adverse event, recovery。
- 与 `blood-organ-tissue-biovigilance-transplantation/`、`trauma-system-hemorrhage-control-continuity/` 和 `surgical-anesthesia-perioperative-safety/` 建立接口。
