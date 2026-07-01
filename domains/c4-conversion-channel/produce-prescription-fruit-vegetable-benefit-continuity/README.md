# Produce Prescription Fruit Vegetable Benefit Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/produce-prescription-fruit-vegetable-benefit-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

该域研究 produce prescription、fruit and vegetable prescription、蔬果 voucher 和营养激励如何把临床/社区健康目标转成可兑换的新鲜农产品购买力。它关注处方到兑换到食用的连续性。

## 核心问题

- 蔬果处方如何从临床转介、社区项目、零售/农贸市场、福利卡和兑换数据中形成闭环。
- 兑换金额、地点、频率、限制、交通、季节性、文化适配和食品保存如何影响真实摄入。
- produce prescription 对食物安全、饮食质量、慢病指标、医疗利用和家庭预算可能产生什么证据。
- 哪些断点会让“处方”停留在纸面，无法变成主体可用的食物输入。

## 对象

- Produce prescriptions、fruit and vegetable prescriptions、nutrition incentives、voucher / debit card / coupon。
- 医疗转介、community partner、farmers market、grocery retailer、redemption platform 和 outcome tracking。
- 食物安全、慢病风险、饮食质量、支付系统和地理可达。

## Human Infra 价值

蔬果处方把“健康食物”从道德建议改写为可支付、可追踪、可兑换的行动条件。该域用于判断这种购买力是否能真正扩大主体恢复、慢病控制和未来选择权，而不是只制造短期项目指标。

## 边界

- 只整理公开项目资料、研究证据、兑换变量、执行风险和治理边界。
- 不提供个人处方、疾病饮食、农产品选择、店铺推荐、福利申请、平台使用或医疗建议。
- 不收集个人位置、购买记录、健康指标、收入或家庭饮食资料。

## 上游与下游

- 上游：`nutrition-insecurity-screening-referral-continuity`、`grocery-retail-food-store-access-continuity`、`food-bank-pantry-community-food-distribution-continuity`。
- 下游：`nutrition-metabolic-health`、`cardiovascular-resilience`、`diabetes-insulin-glucose-monitoring-supplies-continuity`、`cooking-meal-preparation-kitchen-safety-continuity`。

## 初始资料线索

- NIH Food is Medicine research opportunities.
- HHS Food is Medicine.
- USDA nutrition incentive and SNAP-Ed context.
- Peer-reviewed produce prescription evaluations.
