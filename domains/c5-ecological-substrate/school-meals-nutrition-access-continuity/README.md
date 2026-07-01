# School Meals Nutrition Access Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/school-meals-nutrition-access-continuity` |
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

`school-meals-nutrition-access-continuity` 研究校餐、早餐、午餐、免费/减价资格、Community Eligibility Provision、暑期餐食和特殊饮食安排如何影响儿童营养、学习准备和家庭资源压力。

> 核心问题：学校餐食是儿童每日能量、注意力、健康公平和家庭预算缓冲的基础设施，不只是学校附属服务。

## 关注对象

- National School Lunch Program、School Breakfast Program、CEP、暑期餐食和 EBT 类食物支持。
- 免费/减价资格、申请摩擦、污名、账户欠费、膳食债务、转学和假期断点。
- 食物不安全、营养质量、特殊饮食需求、过敏、文化语言可达和家庭收入冲击。
- 校餐与出勤、学习注意力、慢病管理、学校健康服务、家庭照护和社会保护的交叉。

## Human Infra 链路

```text
校餐与营养可及连续
  -> 儿童每日能量、微量营养和餐食可靠性提高
  -> 饥饿、注意力波动、家庭现金压力和学习日损耗下降
  -> 学习参与、健康恢复、情绪稳定和家庭资源韧性增强
  -> 长期能力积累、健康寿命基础和未来选择权扩大
```

## 非目标

- 不提供个人营养处方、校餐申请、家庭福利申请、饮食治疗、过敏管理、食品安全处置或医疗建议。
- 不替代学校营养部门、USDA FNS、州机构、医生、营养师或社会服务。
- 不收集儿童餐食账户、收入、过敏、健康、移民身份或家庭资格信息。

## Source Signals

- USDA Food and Nutrition Service National School Lunch Program.
- USDA School Breakfast Program.
- USDA Community Eligibility Provision.
- CDC and school nutrition/public health guidance where relevant.

## 下一步

- 建立 `meal access -> nutrition reliability -> learning readiness -> family resource buffer` 变量表。
- 区分校内餐食、暑期餐食、家庭食物安全、食品安全和个体营养治疗。
- 与 `food-security-nutrition-access`、`nutrition-metabolic-health`、`school-health-services-chronic-condition-continuity` 和 `social-protection-benefits-delivery` 建立边界。
