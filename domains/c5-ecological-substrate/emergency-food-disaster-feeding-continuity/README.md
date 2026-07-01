# Emergency Food Disaster Feeding Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-food-disaster-feeding-continuity` |
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


`emergency-food-disaster-feeding-continuity` 研究灾害供餐、应急食品发放、D-SNAP、学校/社区紧急供餐、避难所餐食和供应链恢复如何在灾害中维持主体能量输入。

> 核心问题：灾害会同时切断厨房、商店、交通、电力、支付和常规福利；应急供餐把食物输入从日常系统切换到危机系统。

## 关注对象

- 灾害供餐、避难所餐食、应急食品包、D-SNAP、USDA disaster nutrition assistance、学校/社区紧急供餐和非营利组织供餐。
- 触发条件、资格、地点、交通、特殊饮食、食品安全、冷链、电力、配送、语言服务、残障可达和退出到常规系统。
- 与 USDA FNS disaster assistance、FEMA、Ready.gov、地方应急管理、学校、食品银行、社区韧性中心和供应链的接口。

## Human Infra 链路

```text
灾害供餐和应急食品发放可用
  -> 厨房、商店、支付、电力和交通中断时仍有能量输入
  -> 饥饿、恐慌采购、食品腐坏、慢病风险和照护崩溃下降
  -> 主体可以等待恢复、执行撤离/避难和重建日常食物路径
  -> 灾害生存窗口、恢复速度和未来选择权增强
```

## 非目标

- 不提供 D-SNAP 资格规避、骗领、物资抢占、发放点拥挤跟踪、救援路线跟踪、食品囤积套利、避难所规避或个案救援指挥。
- 不替代 USDA FNS、FEMA、地方应急管理、红十字、学校、食品银行、公共卫生或社会服务。
- 不收集受灾者身份、地址、家庭成员、福利材料、发放点实时库存、避难所容量、救援行动细节或医疗隐私。

## Source Signals

- USDA FNS Disaster Assistance: https://www.fns.usda.gov/disaster/disaster-assistance
- USDA FNS D-SNAP: https://www.fns.usda.gov/snap/disaster-snap
- FEMA Community Lifelines: https://www.fema.gov/emergency-managers/practitioners/lifelines
- Ready.gov Food: https://www.ready.gov/food

## 下一步

- 建立 `disaster trigger -> feeding channel -> access/capacity -> nutrition safety -> recovery transition` 变量表。
- 区分 D-SNAP、避难所供餐、应急食品包、学校紧急供餐、社区供餐和常规食品系统恢复。
- 与 `emergency-preparedness-response`、`community-resilience-hub-shelter-center-continuity`、`food-bank-pantry-community-food-distribution-continuity`、`grocery-retail-food-store-access-continuity` 和 `food-safety-contamination-control` 建立边界。
