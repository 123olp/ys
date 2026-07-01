# Home Utility Shutoff Location Labeling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/home-utility-shutoff-location-labeling-continuity` |
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

`home-utility-shutoff-location-labeling-continuity` 研究家庭水、电、燃气等关键公用设施的关断位置、责任边界、标签、地图和交接资料如何影响事故响应、灾害恢复、维修协作和照护连续性。

> 核心问题：家庭基础设施在正常状态下经常“隐形”；一旦漏水、燃气风险、停电、维修或灾后返家发生，家庭成员、照护者、房东、维修人员和应急人员是否能知道关键位置在哪里，会直接改变损失扩大、响应延误和恢复失败风险。

## 关注对象

- 水、电、燃气、供暖、网络和其他家庭关键服务的入口位置、标识、访问状态、权限边界和资料备份。
- 租房、合租、老年照护、残障支持、短租、房屋托管、灾害返家、维修交接和临时照护场景。
- 标签、家庭地图、照片索引、责任说明、联系人和更新周期如何降低家庭系统不可读性。
- 与燃气泄漏边界、电气安全、水管维护、物业责任、应急文件和家庭通信计划的接口。

## Human Infra 链路

```text
家庭关键服务位置可读
  -> 关键信息不再只存在于单个家庭成员记忆中
  -> 照护者、维修人员、房东或应急响应者能更快理解家庭系统边界
  -> 漏水、燃气风险、停电、维修延误和灾后返家摩擦下降
  -> 居住、照护、卫生、通信和恢复任务连续性提高
```

## 非目标

- 不提供关断操作教程、电气面板操作、燃气阀门操作、管线维修、现场判断、灾后返家许可、房屋改造或个案安全建议。
- 不替代公用事业公司、消防部门、持证电工、持证 plumber/HVAC、房东/物业、本地规范或应急服务。
- 不收集住址、设施照片、阀门位置、面板位置、门禁、账户、住户身份或其他可被滥用的家庭基础设施细节。

## Source Signals

- Ready.gov Make a Plan: https://www.ready.gov/plan
- Ready.gov Document and Insure Your Property: https://www.ready.gov/sites/default/files/2020-03/ready_document-and-insure-your-property.pdf
- USFA Appliance and Electrical Fire Safety: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/appliance-and-electrical/

## 下一步

- 建立 `utility location knowledge -> label/map state -> emergency/repair handoff -> continuity outcome` 变量表。
- 区分业主、租客、照护者、短期访客、物业和专业维修人员的权限边界。
- 与 `natural-gas-propane-leak-shutoff-continuity`、`residential-electrical-wiring-outlet-safety-continuity` 和 `premise-plumbing-backflow-cross-connection-continuity` 建立边界。
