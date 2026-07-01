# CPAP PAP Device Mask Supply Power Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/cpap-pap-device-mask-supply-power-continuity` |
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

`cpap-pap-device-mask-supply-power-continuity` 研究 CPAP/BiPAP/PAP 设备、面罩、管路、滤芯、清洁、供电、旅行、召回、供应商和依从支持如何影响睡眠、日间警觉、心血管风险、驾驶安全和恢复能力。

> 核心问题：PAP 治疗的收益依赖设备每天晚上可用；面罩漏气、耗材断供、停电、旅行断点或供应商摩擦会把可治疗睡眠风险重新变成恢复失败。

## 关注对象

- CPAP、BiPAP、PAP 设备、面罩、管路、滤芯、加湿器、清洁维护、供电、旅行电源、召回和耗材替换。
- 睡眠呼吸暂停、日间嗜睡、疲劳、驾驶/工作安全、心血管风险和照护者观察。
- 供应商、医保合规、依从记录、设备数据、隐私和远程监测接口。
- 与睡眠、呼吸、家庭医疗设备、备用电、召回和医疗服务连续性的接口。

## Human Infra 链路

```text
PAP 设备运行连续
  -> 主体夜间呼吸支持和睡眠恢复更稳定
  -> 面罩、耗材、供电、召回和供应商断点造成的治疗中断下降
  -> 日间警觉、认知、驾驶/工作安全和长期恢复能力增强
  -> 有效时间、风险控制和未来选择权提高
```

## 非目标

- 不提供睡眠呼吸暂停诊断、PAP 处方、压力参数、面罩选择、清洁步骤、设备购买、维修、召回个案或保险申诉建议。
- 不替代睡眠医生、呼吸治疗师、DME 供应商、NHLBI、CMS、FDA 或设备说明。
- 不把设备依从性简化为意志问题；面罩适配、费用、供电、隐私、召回和供应商接口必须纳入。

## Source Signals

- Medicare CPAP Devices: https://www.medicare.gov/coverage/continuous-positive-airway-pressure-devices
- CMS CPAP Devices and Accessories: https://www.cms.gov/training-education/medicare-learning-networkr-mln/compliance/medicare-provider-compliance-tips/cpap-devices-accessories

## 下一步

- 建立 `PAP device state -> mask/supply/power/provider dependency -> sleep recovery -> daytime function` 变量表。
- 区分居家、旅行、停电、召回、依从记录、隐私和长期供应商维护场景。
- 与 `sleep-disordered-breathing-screening-treatment-continuity`、`home-oxygen-respiratory-equipment-supply-continuity` 和 `refrigerated-medication-medical-device-power-outage-continuity` 建立边界。
