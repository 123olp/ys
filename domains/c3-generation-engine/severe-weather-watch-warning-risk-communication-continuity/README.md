# Severe Weather Watch Warning Risk Communication Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/severe-weather-watch-warning-risk-communication-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

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


`severe-weather-watch-warning-risk-communication-continuity/` 研究 watch、warning、advisory、emergency、impact-based warning、警报渠道冗余和行动翻译如何影响主体持续性。

> 核心问题：预警不是信息本身，而是把不确定风险转化为可执行行动的接口；警报无法被理解或信任时，观测能力不会自动转化为生存能力。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体需要在不确定危险中及时改变行动
  -> 天气预警必须被接收、理解、相信并转化为避险、撤离或就地保护
  -> 若术语、渠道、语言、无障碍、误警和信任失败，风险信息会停留在系统内
  -> 因而强天气 watch/warning 风险沟通是所有天气 hazard 域的共同接口
```

## 关注对象

- Watch、warning、advisory、emergency、impact statements、WEA、NOAA Weather Radio、sirens、社交媒体和地方官方渠道。
- 多语言、无障碍、夜间警报、误警/漏警、风险感知、行动触发、社区信任和谣言控制。
- 与 `emergency-alerts-communications/` 的边界：该域关注公共警报基础设施；本域关注强天气警报语义、理解、信任和行动翻译。

## Human Infra 模型链路

```text
强天气风险沟通系统 T
  -> 改变警报触达、术语理解、可信度、行动阈值、语言可达和渠道冗余变量 X
  -> 改变主体在 hazard 到来前的决策状态 S
  -> 改变延迟撤离、错误庇护、风险暴露、恐慌和信息过载风险 λ(t)
  -> 影响急性生存、有效行动密度、恢复窗口和未来选择权
```

## 非目标

- 不发布实时预警、不解释个案警报、不替代官方渠道、不做恐慌传播、不做舆论操控或应急指挥。
- 不替代 NWS/NOAA、FEMA、地方应急管理、911/NG911、媒体或公共安全机构。
- 不收集个人位置、脆弱性档案、家庭撤离计划或实时灾情敏感数据。

## Source Signals

- NWS Weather Safety: https://www.weather.gov/safety/
- NWS Wireless Emergency Alerts: https://www.weather.gov/wrn/wea
- Ready.gov Alerts: https://www.ready.gov/alerts

## 下一步

- 建立 warning 术语、渠道冗余、影响式预警、多语言/无障碍、误警信任和行动触发 source card。
- 与 `emergency-alerts-communications/`、`language-access-plain-communication/` 和 `alert-fatigue-interruption-signal-management-continuity/` 对齐。
