# Public Works Civil Infrastructure Asset Management

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/public-works-civil-infrastructure-asset-management` |
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


`public-works-civil-infrastructure-asset-management/` 研究道路、桥梁、隧道、排水、公用设施、公共设施和土木基础设施资产如何通过生命周期维护支撑主体持续性。

> 核心问题：基础设施不是建成一次就完成，而是持续退化、维护、更新和失效的资产组合。公共工程资产管理失败会把医疗、就业、教育、物流、应急、住房和城市运行同时拖入高摩擦状态。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖道路、桥梁、排水、公共设施和城市资产长期可用
  -> 这些资产会随时间老化，并需要检查、维护、更新、预算和优先级排序
  -> 资产管理失败会增加中断、事故、拥堵、服务成本、灾害脆弱性和恢复时间
  -> 公共工程资产失修会在交通、住房、医疗和物流之前击穿主体持续性
```

## 关注对象

- 道路、桥梁、隧道、排水、公共设施、路面、交通资产、公共建筑外部系统和城市维护资产。
- 生命周期成本、状态评估、资产登记、维护优先级、韧性投资、资本计划、维修积压和服务水平。
- 与 `transportation-access-mobility/` 的边界：交通域关注人能否到达资源；本域关注支撑交通和公共服务的实体资产是否可维护。
- 与 `building-fire-life-safety-codes/` 的边界：建筑域关注单体建筑生命安全；本域关注公共工程资产组合和维护治理。

## Human Infra 模型链路

```text
公共工程资产管理
  -> 道路、桥梁、排水、公共设施和城市资产状态可被登记、检查和维护
  -> 服务水平、维修优先级、预算缺口和灾害脆弱性进入决策
  -> 中断、事故、拥堵、维护债务和恢复时间下降
  -> 主体获得低摩擦、可预测、可恢复的公共物理底座
```

## 非目标

- 不提供桥梁、道路、隧道、排水、公用设施或公共建筑的工程设计、施工、检查、维修或采购建议。
- 不提供敏感基础设施弱点、绕行策略、破坏方法、招投标策略、成本估算或法律/索赔建议。
- 不替代交通、公共工程、工程咨询、设施管理、采购或监管机构的官方信息。

## Source Signals

- FHWA Asset Management: https://www.fhwa.dot.gov/asset/
- OECD Infrastructure: https://www.oecd.org/en/topics/infrastructure.html
- World Bank Infrastructure: https://www.worldbank.org/en/topic/infrastructure

## 下一步

- 建立公共工程资产变量表：资产状态、寿命、维护、维修积压、服务水平、预算、韧性和失效影响。
- 整理 FHWA、OECD、World Bank、ASCE、ISO 55000 和地方公共工程资料卡片。
- 与交通、物流、住房、灾害恢复、城市规划和采购合同能力域建立接口。
