# Food Pharmacy Clinic Pantry Integration Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/food-pharmacy-clinic-pantry-integration-continuity` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 关键词显示该域主要承载能源、水、食物、住房、治理、经济、通信、灾害或基础设施环境。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何承载主体展开未来的外部世界条件，例如能源、水、食物、住房、通信、治理、经济和基础设施？

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

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

该域研究 food pharmacy、clinic pantry、hospital pantry 和医疗场景内外食物支持如何与临床工作流、EHR 转介、社区伙伴和食物发放连接。它关注“医疗入口里的食物基础设施”。

## 核心问题

- food pharmacy / clinic pantry 如何嵌入筛查、转介、领取、随访和社区资源闭环。
- 现场发放、库存、营养教育、慢病照护、隐私、污名和人员角色如何影响主体真实获得食物。
- 临床场所食物支持与食品银行、MTM、MTG、produce prescription 和社会处方如何分工。
- 哪些执行断点会让 pantry 变成一次性发放，而不是持续照护接口。

## 对象

- Food pharmacy、clinic pantry、hospital pantry、onsite food distribution、community food partner。
- EHR referral、screening workflow、inventory、pickup/delivery、nutrition education、follow-up。
- 数据共享、同意、污名、空间设计、运营责任和社区组织协作。

## Human Infra 价值

当食物支持被放进医疗入口，主体不必在病情、交通、信息和多个机构之间反复切换。该域关注这种整合能否降低行动摩擦、改善慢病执行，并避免把食品发放变成医疗场景中的污名化附属物。

## 边界

- 只整理公开项目模型、执行变量、证据、风险和治理边界。
- 不推荐具体 pantry、医院、食品包、疾病饮食、领取路径、志愿者流程或个案资源。
- 不替代医疗、营养、福利、食品安全、隐私合规或机构运营建议。

## 上游与下游

- 上游：`nutrition-insecurity-screening-referral-continuity`、`social-prescribing-community-referral-continuity`、`patient-portal-account-message-continuity`、`healthcare-language-interpreter-effective-communication-continuity`。
- 下游：`food-bank-pantry-community-food-distribution-continuity`、`medically-tailored-groceries-food-benefit-continuity`、`produce-prescription-fruit-vegetable-benefit-continuity`。

## 初始资料线索

- HHS Food is Medicine.
- CMS Medicaid HRSN nutrition supports.
- Food pharmacy / clinic pantry implementation and evaluation literature.
- Community health center and hospital community benefit materials.
