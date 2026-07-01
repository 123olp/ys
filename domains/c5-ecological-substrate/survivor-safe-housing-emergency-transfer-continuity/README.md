# survivor-safe-housing-emergency-transfer-continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/survivor-safe-housing-emergency-transfer-continuity` |
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

`survivor-safe-housing-emergency-transfer-continuity` 研究家庭暴力、性暴力、dating violence、stalking、人身安全威胁和犯罪伤害后，安全住所、confidentiality、emergency transfer、VAWA housing protections、transitional housing 和 shelter referral 如何影响主体逃离危险、保持住房、连接服务和恢复行动。

## Scope

- VAWA housing protections、emergency transfer、confidentiality、lease bifurcation、survivor housing stability、transitional housing 和 shelter referral。
- 地址保密、学校/工作/医疗通信风险、儿童与宠物照护、残障可达、语言可达、移民身份风险。
- 与 homelessness、灾害避难、家庭法、保护令和受害者服务交叉的公开制度资料。

## Continuity Logic

```text
安全威胁与住所暴露重叠
-> 留在原住所可能危险，离开原住所又可能造成无家可归和服务断裂
-> emergency transfer、保密、住房保护和 transitional housing 成为恢复接口
-> 住房链失败会把安全事件放大为长期居住、工作、学校和照护断裂
```

## Source Spine

- HUD VAWA housing protections and emergency transfer plan materials.
- DOJ OVW transitional housing and victim services materials.
- OVC victim assistance resources.
- Homelessness and housing stability public materials where survivor housing is in scope.

## Evidence Boundary

本域只整理公开 survivor housing、VAWA housing protections、emergency transfer 和 transitional housing 资料。

Do not include:

- 个案逃离路线、庇护所定位、转移申请策略、租约法律建议、保护令策略或安全计划。
- 可识别住址、庇护所、受害者、儿童、服务人员、施暴者或实时移动的信息。
- 规避资格、骗取住房服务、骚扰房东/机构、跟踪、定位或报复方法。

## Upstream / Downstream

- Upstream: `domestic-violence-coercive-control-safety-continuity/`, `stalking-harassment-protection-order-continuity/`, `housing-built-environment-stability/`.
- Downstream: `homelessness-unsheltered-health-continuity/`, `address-residency-mail-service-continuity/`, `family-law-custody-child-support-continuity/`, `pet-disaster-evacuation-sheltering-continuity/`.
