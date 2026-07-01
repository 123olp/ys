# Community Resilience Hub Shelter Center Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/community-resilience-hub-shelter-center-continuity` |
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


`community-resilience-hub-shelter-center-continuity` 研究社区韧性中心、避难所、冷却/取暖中心、清洁空气中心、充电点、物资分发点和灾害服务站如何在危机中维持主体生命线接入。

> 核心问题：灾害不是单一事件，而是生命线断裂；社区级中心把电力、通信、温控、水、信息、照护和社会服务重新接到主体身上。

## 关注对象

- 社区韧性中心、避难所、冷却中心、取暖中心、清洁空气中心、公共充电点、物资分发点和灾后服务中心。
- 开放触发条件、容量、无障碍、宠物/家庭/医疗需求支持、交通接入、语言服务、身份要求、数据隐私和恢复阶段退出。
- 与 FEMA Community Lifelines、Ready.gov、CISA、地方应急管理、公共卫生、能源、通信、图书馆、学校和宗教/社区组织的接口。

## Human Infra 链路

```text
社区韧性和避难中心可用
  -> 电力、温控、通信、水、信息和基础服务在灾害中重新接入
  -> 热/冷暴露、断电、孤立、信息失明和家庭照护崩溃风险下降
  -> 主体可以等待恢复、联系救援、维持治疗和重新组织行动
  -> 主体灾害生存窗口、恢复速度和未来选择权增强
```

## 非目标

- 不提供避难资格规避、安保绕过、物资骗领、骚扰弱势群体、中心拥挤实时跟踪、政治动员或个案救援指挥。
- 不替代 FEMA、地方应急管理、红十字、公共卫生、能源/通信公用事业、医疗机构或社会服务。
- 不收集避难者身份、家庭地址、医疗隐私、未成年人信息、实时容量、安防细节或救援行动敏感信息。

## Source Signals

- FEMA Community Lifelines: https://www.fema.gov/emergency-managers/practitioners/lifelines
- Ready.gov Shelters: https://www.ready.gov/shelter
- Ready.gov Power Outages: https://www.ready.gov/power-outages
- CISA Critical Infrastructure: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience

## 下一步

- 建立 `hub -> lifeline service -> trigger/capacity -> vulnerable need -> recovery continuity` 变量表。
- 区分日常社区韧性中心、冷却/取暖中心、清洁空气中心、灾害避难所、公共充电点和灾后服务站。
- 与 `emergency-preparedness-response`、`critical-infrastructure-lifeline-interdependency-resilience`、`energy-access-resilience`、`telecommunications-network-resilience-continuity` 和 `public-library-community-anchor-access-continuity` 建立边界。
