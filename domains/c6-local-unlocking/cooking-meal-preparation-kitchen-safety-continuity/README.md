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
