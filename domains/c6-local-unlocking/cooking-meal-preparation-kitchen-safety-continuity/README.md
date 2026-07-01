# Cooking Meal Preparation Kitchen Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/cooking-meal-preparation-kitchen-safety-continuity` |
| 分级 | `C6` - 局部可能性解锁层 |
| 控制轴 | 局部阻塞解除 |
| 分级理由 | 未命中更高层边界、载体、能力、转换或生态规则，暂归为具体场景的局部可能性解锁。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域解除的是哪一个具体疾病、流程、服务、职业、家庭、社区或专项风险中的局部阻塞？

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

- 界定局部阻塞：某一疾病、流程、服务、职业、家庭、社区或专项风险中的具体失败点。
- 说明受影响任务：它阻碍了主体完成什么行动、服务、照护、转换或恢复过程。
- 记录可测改善：等待时间、错误率、成本、可及性、完成率、伤害率或恢复速度。
- 明确升级边界：何时应转交 C2-C5 的上层生命、能力、转化或基础设施域。
- 避免把局部改良包装成根本性解决方案，必须标注适用范围和外部依赖。

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

`cooking-meal-preparation-kitchen-safety-continuity` 研究家庭烹饪、备餐、厨房设备、食品处理、火灾/烫伤/中毒风险和餐食计划如何影响营养、时间、健康和家庭安全连续性。

> 核心问题：吃饭不是单一营养摄入，而是采购、储存、清洗、烹饪、清理和安全控制组成的任务链；任一环节失效，都可能把日常恢复输入变成火灾、感染、伤害或时间成本。

## 关注对象

- 家庭烹饪设备、备餐流程、食材处理、交叉污染、温度、剩菜、餐具清洁和厨房布局。
- 厨房火灾、油烟、烫伤、刀具伤害、燃气/一氧化碳、儿童厨房安全和照护场景餐食。
- 餐食计划、批量备餐、特殊饮食需求、能源中断和灾害/失能状态下的餐食连续性。
- 与食品安全、能源、空气质量、家庭设备、消防生命安全和照护连续性的接口。

## Human Infra 链路

```text
烹饪备餐安全连续
  -> 食物被稳定转化为营养、恢复和家庭协作输入
  -> 火灾、烫伤、交叉污染、燃气风险和备餐摩擦下降
  -> 主体用更低时间成本获得更可靠的能量与生活节律
  -> 健康寿命、有效时间、家庭安全和照护连续性增强
```

## 非目标

- 不提供具体食谱、饮食处方、食品温度判断、燃气/电气维修、厨房改造或个体安全操作指南。
- 不替代 USDA/FDA/CDC、NFPA、CPSC、本地消防、医疗或建筑规范。
- 不鼓励危险烹饪、燃气规避、食品召回规避、极端节食或无证食品经营。

## Source Signals

- USDA Food Safety Basics: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation
- CDC Food Safety: https://www.cdc.gov/food-safety/
- NFPA Home Cooking Fires: https://www.nfpa.org/education-and-research/home-fire-safety/cooking
- CPSC Recalls: https://www.cpsc.gov/Recalls

## 下一步

- 建立 `meal task -> food safety control -> equipment dependency -> injury/fire risk -> time/recovery value` 变量表。
- 区分日常烹饪、照护备餐、儿童/老年厨房风险、灾害能源中断和共享厨房场景。
- 与 `food-safety-contamination-control`、`nutrition-metabolic-health`、`building-fire-life-safety-codes` 和 `home-refrigeration-food-storage-continuity` 建立边界。
