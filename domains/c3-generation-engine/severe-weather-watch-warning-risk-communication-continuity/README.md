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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
