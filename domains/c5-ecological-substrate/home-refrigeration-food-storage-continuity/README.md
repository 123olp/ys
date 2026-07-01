# Home Refrigeration Food Storage Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-refrigeration-food-storage-continuity` |
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

`home-refrigeration-food-storage-continuity` 研究家庭冷藏、冷冻、食品保存、停电、温度控制和食品安全如何影响营养输入、感染风险、经济损失和日常恢复能力。

> 核心问题：食物买得到不等于能安全保存；冷藏冷冻链一旦在家中断裂，营养资源会转化为浪费、食源性风险、账单压力和行动恢复断点。

## 关注对象

- 冰箱、冷冻柜、温度控制、储存时间、停电、门封、设备故障和食物丢弃决策边界。
- 易腐食品、冷冻食品、婴幼儿/老年/免疫低下相关食品安全风险、药品/生物材料冷藏接口。
- 食品标签、召回通知、家庭库存、备餐、餐食计划、能源中断和灾害恢复。
- 与食品安全、能源连续性、家庭设备、电网可靠性和家庭应急准备的接口。

## Human Infra 链路

```text
家庭冷藏保存连续
  -> 营养输入、食品安全、家庭预算和备餐计划保持可用
  -> 停电、设备故障、温度失控和召回造成的浪费与感染风险下降
  -> 食物从易腐资源转化为可调度的恢复输入
  -> 健康寿命、有效时间、经济韧性和家庭应急能力增强
```

## 非目标

- 不提供具体食物能否继续食用、疾病判断、食品处置、冷链设备购买或个体食品安全建议。
- 不替代 USDA/FDA/CDC、本地公共卫生、食品召回、医疗或紧急管理指导。
- 不鼓励恐慌囤积、黑市采购、隐瞒污染、标签篡改或食品召回规避。

## Source Signals

- USDA FSIS Refrigeration and Food Safety: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/refrigeration
- USDA FSIS Food Safety During Power Outage: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/emergencies/food-safety-power-outage
- FDA Food Safety and Recalls: https://www.fda.gov/food
- CDC Food Safety: https://www.cdc.gov/food-safety/

## 下一步

- 建立 `food item -> storage requirement -> temperature exposure -> discard/retain boundary -> health/economic cost` 变量表。
- 区分日常保鲜、灾害停电、食品召回、特殊人群食品风险和药品冷藏接口。
- 与 `food-safety-contamination-control`、`food-security-nutrition-access`、`energy-access-resilience` 和 `household-appliance-maintenance-repair-continuity` 建立边界。
