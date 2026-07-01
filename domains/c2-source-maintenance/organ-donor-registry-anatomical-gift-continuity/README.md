# Organ Donor Registry Anatomical Gift Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/organ-donor-registry-anatomical-gift-continuity` |
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

Organ Donor Registry Anatomical Gift Continuity 研究器官捐赠登记、anatomical gift、授权状态、家庭沟通、驾驶证/州登记和医疗系统识别如何影响主体死亡边界后的意愿执行与他人生命连续性。

> 核心问题：主体持续性研究不能只看死亡前；死亡边界后的捐赠意愿、登记识别和家庭沟通，会把一个主体的终局转化为其他主体的生存机会。

## 研究对象

- Organ donor registry、anatomical gift law、驾驶证/州登记、撤销/更新、家庭沟通和医院识别流程。
- 器官、眼、组织捐赠与 transplant system、biovigilance 和隐私边界的关系。
- 意愿记录、身份匹配、错误登记、家庭冲突、宗教文化和公平分配问题。

## 先验链路

```text
死亡边界并不结束身体资源的社会影响
  -> 器官、眼和组织可能成为其他主体的生命维持资源
  -> 捐赠意愿必须在登记、识别、授权和家庭沟通中被保留
  -> 记录缺失、错误、不可见或冲突会导致意愿无法执行或信任受损
  -> 因而器官捐赠登记是主体意愿、身体资源和他人持续性的跨边界接口
```

## 关键变量

- 登记状态、更新/撤销、身份匹配、州系统、驾驶证标记和医院识别。
- 家庭沟通、文化信任、授权边界、分配公平、组织安全和数据隐私。
- 错误登记、身份盗用、强迫、误解、商业化和谣言风险。

## 证据入口

- OrganDonor.gov and state donor registry materials.
- HRSA organ donation and transplantation materials.
- OPTN / transplant system public materials.
- Biovigilance and anatomical gift law overview materials.

## 非目标

- 本域不建议是否登记捐赠、如何登记、如何撤销、捐赠范围、家庭沟通策略或法律选择。
- 不提供医学、法律、宗教、伦理个案判断、移植等待名单建议或死亡判定解释。
- 不收集捐赠登记、身份文件、驾驶证、病历、家庭信息或宗教/文化资料。

## 上下游

- 上游：`blood-organ-tissue-biovigilance-transplantation/`、`vital-records-life-event-continuity/`、`driver-license-vehicle-registration-continuity/`。
- 下游：`trust-estate-affairs-succession-continuity/`、`governance-rights/`、`healthcare-civil-rights-nondiscrimination-continuity/`。
