# Diabetic Therapeutic Footwear Offloading Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/diabetic-therapeutic-footwear-offloading-continuity` |
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

`diabetic-therapeutic-footwear-offloading-continuity` 研究糖尿病治疗鞋、鞋垫、卸载设备、足部检查、适配、覆盖、替换和日常穿着依从如何影响足溃疡、截肢风险、移动能力和工作生活连续性。

> 核心问题：糖尿病足风险不是只在伤口出现后才开始；合适鞋履、卸载和足部保护把感觉丧失、血供不足、压力点和移动需求接入同一个预防系统。

## 关注对象

- 治疗鞋、定制鞋垫、卸载靴、足部压力点、鞋内异物、袜子、穿着时间和替换周期。
- 神经病变、足畸形、既往溃疡、截肢史、覆盖资格、供应商、适配失败和随访断点。
- 工作站立、通勤、住房不稳、运动、旅行、农村地区和低收入场景。
- 与糖尿病足溃疡、慢性伤口、DME、皮肤耗材、交通和职业设计的接口。

## Human Infra 链路

```text
糖尿病治疗鞋与卸载连续
  -> 高风险足部获得压力再分配、保护和日常移动支撑
  -> 小创口、压力点、适配失败和供应延迟进入溃疡/感染链条的概率下降
  -> 行走、工作、照护、通勤和自理能力更不容易被足部失效截断
  -> 有效时间、行动半径和未来选择权增强
```

## 非目标

- 不提供糖尿病足诊断、伤口处理、鞋垫处方、卸载设备使用、足部护理操作、覆盖资格判断或产品推荐。
- 不替代足病医生、内分泌/初级照护、伤口团队、CMS/Medicare、DME 供应商或临床指南。
- 不把治疗鞋履写成足溃疡治疗替代或忽视感染、疼痛、红肿、伤口等转诊信号。

## Source Signals

- NIDDK Diabetes and Foot Problems: https://www.niddk.nih.gov/health-information/diabetes/overview/preventing-problems/foot-problems
- Medicare Therapeutic Shoes and Inserts: https://www.medicare.gov/coverage/therapeutic-shoes-inserts
- CDC Diabetes and Your Feet: https://www.cdc.gov/diabetes/diabetes-complications/diabetes-and-your-feet.html

## 下一步

- 建立 `foot risk -> footwear/offloading function -> supply/adherence -> mobility/amputation impact` 变量表。
- 区分预防、溃疡后卸载、既往截肢、工作站立、低收入覆盖、农村供应和灾害断供场景。
- 与 `diabetic-foot-ulcer-amputation-prevention-continuity`、`chronic-wound-venous-diabetic-pressure-ulcer-continuity` 和 `durable-medical-equipment-supplier-repair-continuity` 建立边界。
