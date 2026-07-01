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
