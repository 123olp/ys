# Medically Tailored Groceries Food Benefit Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/medically-tailored-groceries-food-benefit-continuity` |
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

该域研究 medically tailored groceries（MTG）和健康导向食品福利如何把慢病、营养风险和食物不安全转化为可购买、可领取、可烹饪、可持续的食材支持。它关注的是食材福利执行链，不是个人购物清单。

## 核心问题

- 医学定制食材如何在临床需求、营养教育、处方、福利、零售/pantry、配送和家庭烹饪能力之间衔接。
- 食材包、健康食品福利、grocery box、voucher 和数字支付如何影响饮食质量、慢病控制和家庭预算。
- 哪些断点会让“有食材福利”无法转化为可吃、可做、可接受、可持续的餐食。
- 如何处理文化适配、厨房条件、时间、交通、数字支付、家庭成员共享和食品安全。

## 对象

- Medically tailored groceries、healthy food benefit、grocery box、pantry prescription、food benefit card。
- 食材选择、营养教育、recipe support、零售兑换、pantry 发放、配送和家庭端存储烹饪。
- 慢病状态、营养风险、食物不安全、支付接口和 redemption data。

## Human Infra 价值

食材支持比餐食配送更依赖主体的时间、厨房、认知、文化偏好和家庭结构。该域用于识别医学化食材福利何时能增加主体行动能力，何时只是把照护负担转移回家庭。

## 边界

- 只整理公开项目模型、证据、变量和执行边界。
- 不提供个人购物清单、膳食计划、疾病饮食、福利选择、资格判断、零售商推荐或优惠策略。
- 不处理个人健康、收入、住址、购买记录、厨房条件或家庭成员敏感信息。

## 上游与下游

- 上游：`nutrition-insecurity-screening-referral-continuity`、`grocery-retail-food-store-access-continuity`、`snap-ebt-redemption-retailer-payment-continuity`、`food-bank-pantry-community-food-distribution-continuity`。
- 下游：`cooking-meal-preparation-kitchen-safety-continuity`、`home-refrigeration-food-storage-continuity`、`produce-prescription-fruit-vegetable-benefit-continuity`。

## 初始资料线索

- HHS Food is Medicine.
- NIH Food is Medicine research opportunities.
- CMS Medicaid HRSN nutrition supports.
- USDA SNAP-Ed and food access materials.
