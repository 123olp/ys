# Food Bank Pantry Community Food Distribution Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/food-bank-pantry-community-food-distribution-continuity` |
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


`food-bank-pantry-community-food-distribution-continuity` 研究食品银行、食品 pantry、社区发放点、TEFAP、捐赠物流、资格摩擦、开放时段和尊严保护如何在收入、灾害或服务断点中维持食物输入。

> 核心问题：社区食物发放是最后缓冲层；当正式收入、福利或零售购买失败时，它决定主体是否仍有食物恢复窗口。

## 关注对象

- 食品银行、食品 pantry、社区餐食、TEFAP、捐赠食品、移动发放、drive-through 发放、宗教/社区组织发放点。
- 开放时段、资格要求、排队、交通、语言、隐私、食品安全、特殊饮食、库存波动、志愿者能力和灾害扩容。
- 与 USDA FNS TEFAP、Feeding America 网络、地方社会服务、食品安全、灾害响应和社区资源导航的接口。

## Human Infra 链路

```text
社区食品发放可持续
  -> 收入、福利、零售或灾害冲击下仍有食物缓冲
  -> 饥饿、羞辱、排队失败、库存断裂和食品安全风险下降
  -> 主体可以把危机时间转化为恢复和重新组织资源
  -> 家庭韧性、健康维护和未来选择权增强
```

## 非目标

- 不提供资格规避、重复领取、转售捐赠食品、排队插队、库存操纵、食品处置决策、个案福利申请或组织运营合规建议。
- 不替代 USDA FNS、食品银行、pantry、地方社会服务、营养师、食品安全机构或法律服务。
- 不收集领取者身份、收入材料、地址、家庭组成、排队位置、机构库存漏洞、捐赠者身份或敏感服务记录。

## Source Signals

- USDA FNS TEFAP: https://www.fns.usda.gov/tefap/emergency-food-assistance-program
- USDA FNS Food Distribution Programs: https://www.fns.usda.gov/fdd
- Feeding America Hunger and Food Bank Network: https://www.feedingamerica.org/
- USDA Food Safety and Inspection Service: https://www.fsis.usda.gov/food-safety

## 下一步

- 建立 `distribution node -> eligibility friction -> inventory/service window -> dignity/safety -> food continuity` 变量表。
- 区分食品银行、pantry、TEFAP、社区餐食、移动发放、灾害扩容和特殊饮食支持。
- 与 `food-security-nutrition-access`、`social-protection-benefits-delivery`、`emergency-food-disaster-feeding-continuity`、`community-resource-navigation` 和 `food-safety-contamination-control` 建立边界。
