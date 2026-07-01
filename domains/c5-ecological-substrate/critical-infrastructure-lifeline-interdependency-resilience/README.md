# Critical Infrastructure Lifeline Interdependency Resilience

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/critical-infrastructure-lifeline-interdependency-resilience` |
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


`critical-infrastructure-lifeline-interdependency-resilience/` 研究能源、水务、通信、交通、医疗、食品、金融、政府和应急系统之间的互依赖、级联故障和生命线恢复如何支撑主体持续性。

> 核心问题：关键基础设施不是孤立部门。电网停电会影响通信和水务；通信中断会影响支付和救援；道路中断会影响药品和燃料；公共行政中断会影响身份、救济和协调。Human Infra 必须能描述这些级联关系。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体依赖多条生命线同时可用：能源、水、通信、交通、医疗、食品、金融、政府
  -> 各生命线之间存在能源、数据、人员、燃料、备件、道路、支付和授权依赖
  -> 单一部门故障可能通过互依赖变成级联故障和恢复阻塞
  -> 生命线互依赖失控会一次性击穿主体的医疗、资源、通信、移动和制度入口
```

## 关注对象

- Community Lifelines、National Critical Functions、关键基础设施部门、互依赖、级联故障、恢复优先级、跨部门协调、关键节点、冗余、演练和情景分析。
- 与单部门域的边界：电网、水务、通信、交通、医疗、食品和金融域各自研究本部门连续性；本域研究跨部门依赖如何放大或缓解失败。
- 与 `risk-engineering/` 的边界：风险工程关注通用风险建模；本域关注关键基础设施生命线互依赖和恢复协调。

## Human Infra 模型链路

```text
关键基础设施生命线互依赖
  -> 能源、水、通信、交通、医疗、食品、金融和政府依赖关系可被识别
  -> 级联故障、单点瓶颈、恢复优先级和跨部门协调进入模型
  -> 多系统同时中断、恢复阻塞和脆弱人群暴露下降
  -> 主体获得不被单一基础设施故障连锁清零的社会运行底座
```

## 非目标

- 不提供敏感关键设施清单、漏洞、攻击路径、破坏方法、绕行策略、安保规避、恢复优先级操控或实时事故指挥。
- 不提供政府、企业、公用事业或应急机构内部计划替代品。
- 不把跨部门韧性写成监控、强制控制、资源剥夺或群体排除的理由。

## Source Signals

- FEMA Community Lifelines: https://www.fema.gov/emergency-managers/practitioners/lifelines
- CISA National Critical Functions: https://www.cisa.gov/resources-tools/resources/national-critical-functions-set
- CISA Critical Infrastructure Sectors: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors
- CISA Infrastructure Resilience Planning Framework: https://www.cisa.gov/resources-tools/resources/infrastructure-resilience-planning-framework-irpf

## 下一步

- 建立生命线互依赖变量表：能源依赖、通信依赖、水务依赖、交通依赖、人员依赖、金融依赖、恢复时间和级联风险。
- 整理 FEMA、CISA、NIST、NRC、OECD、World Bank 和地方应急管理公开资料卡片。
- 与电网、水务、电信、交通、物流、公共行政、应急响应和灾后恢复域建立接口。
