# Electric Grid Reliability Resilience Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/electric-grid-reliability-resilience-continuity` |
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


`electric-grid-reliability-resilience-continuity/` 研究发电、输电、配电、调度、停电恢复、备用能力和电网韧性如何支撑主体持续性。

> 核心问题：现代主体的医疗设备、通信、制冷制热、支付、照明、交通、水务、食品冷链和 AI 工具都依赖电力。电网不是“有电/没电”的背景变量，而是多部门连续运行的上游生命线。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖电力维持通信、温控、医疗、食品、水务、支付、照明和数字工具
  -> 电网由发电、输电、配电、调度、保护、燃料、备件和恢复队伍共同支撑
  -> 极端天气、燃料短缺、网络攻击、设备老化、负荷峰值和互依赖故障会造成停电
  -> 电网失效会把多个下游基础设施同时推入中断状态
```

## 关注对象

- 电力可靠性、资源充足性、输配电资产、调度、停电恢复、微电网、备用电源、关键负荷、黑启动、互联互通和韧性投资。
- 与 `energy-access-resilience/` 的边界：能源可及域关注家庭和社区能否获得可负担能源服务；本域关注电网作为公共生命线系统的可靠运行和恢复。
- 与 `telecommunications-network-resilience-continuity/`、`water-wastewater-utility-service-continuity/`、`compute-data-center-ai-infrastructure/` 的接口：电网是通信、水务、算力和医疗服务的上游供能条件。

## Human Infra 模型链路

```text
电网可靠性与韧性
  -> 发电、输电、配电和调度能力维持关键负荷
  -> 停电频率、持续时间、恢复时间和脆弱用户暴露下降
  -> 医疗、通信、水务、冷链、温控、支付和数字工具连续性提升
  -> 主体获得可预测、可恢复、可扩展的电力生命线
```

## 非目标

- 不提供电网调度、变电站、线路、保护系统、控制系统、黑启动、绕供、攻击、破坏、入侵或敏感设施信息。
- 不提供电力交易、投资、采购、发电并网、工程设计、施工、维修或监管规避建议。
- 不替代公用事业公司、监管机构、应急管理机构、NERC、DOE、EIA、CISA 或地方官方公告。

## Source Signals

- DOE Grid Resilience: https://www.energy.gov/gdo/grid-resilience
- NERC Reliability: https://www.nerc.com/pa/Pages/default.aspx
- EIA Electricity: https://www.eia.gov/electricity/
- CISA Energy Sector: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/energy-sector

## 下一步

- 建立电网连续性变量表：可靠性、停电持续时间、恢复时间、资源充足性、关键负荷、备用能力、脆弱用户和互依赖风险。
- 整理 DOE、NERC、EIA、CISA、FERC 和地方公用事业公开资料卡片。
- 与水务、通信、医疗设备、温控、交通、食品冷链和关键基础设施互依赖域建立接口。
