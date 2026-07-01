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
