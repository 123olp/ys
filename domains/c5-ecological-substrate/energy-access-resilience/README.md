# Energy Access Resilience

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/energy-access-resilience` |
| 分级 | `C5` - 可能性生态承载层 |
| 控制轴 | 外部生态承载 |
| 分级理由 | 主要提供主体展开未来所需的基础环境、资源、治理或基础设施。 |
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


`energy-access-resilience/` 研究电力、清洁烹饪、供暖/制冷、通信供能和家庭能源服务能否稳定支撑主体生活、恢复、照护和技术使用。

> 核心问题：能源不是抽象资源，而是照明、温控、烹饪、通信、医疗设备、数字服务和应急恢复的运行底座；能源断裂会把多个系统同时打断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖照明、烹饪、温控、通信、医疗设备和数字工具
  -> 能源服务必须可得、可负担、可靠、清洁且具备韧性
  -> 恢复、照护、学习、工作、医疗和应急响应才不会因能源断裂而停摆
```

## 关注对象

- 电力可及、清洁烹饪、能源负担、停电、备用电源、家庭能源、能源贫困和能源韧性。
- 室内空气污染、热/冷风险、医疗设备供电、通信供电、灾害下能源恢复。
- 与住房、热稳态、数字身份、医疗连续性、应急响应和供应链的接口。

## Human Infra 模型链路

```text
能源可及与韧性
  -> 照明、烹饪、温控、通信、医疗设备和数字工具持续运行
  -> 室内污染、温度风险、服务中断和应急失联减少
  -> 健康、恢复、照护、学习、工作和技术采用能力提高
  -> 主体持续性获得可运行的基础能源层
```

## 非目标

- 不提供个体电气施工、发电设备购买、燃料储存、危险接线、规避监管或应急供电操作建议。
- 不提供能源投资、补贴申请、账单处理或个体能源方案。
- 不把能源韧性写成个人囤积和高风险 DIY。

## Source Signals

- Tracking SDG7: https://trackingsdg7.esmap.org/
- IEA Energy Access: https://www.iea.org/topics/energy-access
- WHO Household Air Pollution: https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health

## 下一步

- 建立能源连续性变量表：电力可及、可靠性、能源负担、清洁烹饪、停电时长、医疗设备供电和通信供电。
- 整理 Tracking SDG7、IEA energy access、WHO household air pollution 和能源贫困资料卡片。
- 与 `thermal-homeostasis-resilience/` 明确分工：本域研究外部能源服务，后者研究体温生理边界。
