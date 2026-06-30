# Home Refrigeration Food Storage Continuity

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
