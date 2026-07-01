# Emergency Alerts Communications

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/emergency-alerts-communications` |
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

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定外部承载条件：能源、水、食物、住房、通信、交通、治理、经济或公共基础设施。
- 说明它如何改变主体展开未来所需的稳定性、冗余、可获得性和安全边界。
- 记录基础设施依赖：供应链、地理环境、制度、资金、维护能力和公共服务。
- 识别冲击场景：灾害、战争、断供、污染、气候、系统失灵或社会支持崩溃。
- 建立韧性指标：可用率、恢复时间、冗余、成本、覆盖范围、可负担性和风险暴露。

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

`emergency-alerts-communications/` 研究公共预警、应急通信、911/NG911、天气广播、移动警报和第一响应通信如何保护主体免于低频高冲击事件。

> 核心问题：灾害和急症发生时，主体首先需要收到可信警报、理解风险、联系求助入口，并让响应系统找到自己；通信断裂会把可响应风险变成不可逆伤害。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体必须能在灾害、事故、暴力、疾病和环境极端中收到预警并求助
  -> 预警、911、NG911、天气广播和第一响应通信构成危机时的行动接口
  -> 警报失败、通信失败、位置失败或误报会放大生命风险和恢复成本
  -> 因此应急预警与通信是主体持续性的危机入口域
```

## 关注对象

- FEMA IPAWS、Wireless Emergency Alerts、Emergency Alert System、NOAA Weather Radio、911、NG911 和 FirstNet。
- 警报到达率、可理解性、定位、冗余通信、无障碍、语言可达和误报/漏报治理。
- 与 `emergency-preparedness-response/` 的边界：本域专注预警与通信入口；应急准备与响应覆盖更广泛的准备、医疗、安置和恢复。

## Human Infra 模型链路

```text
应急预警通信系统 T
  -> 改变警报到达、理解、定位、求助、冗余通信和响应协调变量 X
  -> 改变主体在危机中的可响应状态 S
  -> 改变伤害、延误、失联、撤离失败和救援失败风险 λ(t)
  -> 影响生存概率、恢复窗口、家庭连续性和未来选择权
```

## 非目标

- 不提供实时应急指挥、撤离路线、急救操作、无线电操作、调度替代或公共警报发布方法。
- 不支持伪造警报、干扰通信、冒充响应人员、滥用 911 或绕过官方系统。
- 不把本域资料当作官方警报或现场安全判断。

## Source Signals

- FEMA IPAWS: https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system
- FCC Wireless Emergency Alerts: https://www.fcc.gov/consumers/guides/wireless-emergency-alerts-wea
- FCC Emergency Alert System: https://www.fcc.gov/emergency-alert-system
- NOAA Weather Radio: https://www.weather.gov/nwr/
- 911.gov: https://www.911.gov/
- NG911: https://www.911.gov/issues/ng911/
- FirstNet: https://www.firstnet.gov/

## 下一步

- 建立变量表：警报渠道、覆盖、理解、定位、冗余、响应互操作、误报、漏报和无障碍。
- 与 `emergency-preparedness-response/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/` 和 `risk-engineering/` 拆分边界。
