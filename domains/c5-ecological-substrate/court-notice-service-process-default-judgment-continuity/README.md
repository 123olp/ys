# Court Notice Service Process Default Judgment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/court-notice-service-process-default-judgment-continuity` |
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

本域研究法律通知、送达、开庭信息、语言/无障碍可达、回应期限、缺席判决和执行后果如何影响主体是否真正拥有程序参与机会。

> 核心问题：权利常常不是在实体规则中丢失，而是在没有收到通知、看不懂程序、错过期限或缺席判决后丢失；程序通知连续性是主体避免资源、住房、收入和身份被静默剥夺的基础设施。

## 关注对象

- 法律通知、service of process、法院传票、听证通知、电子通知、邮寄失败、地址错误和语言可达。
- 回应期限、缺席判决、工资扣押、驱逐、债务执行、家庭法院命令、保护令和行政听证。
- 与 `address-residency-mail-service-continuity/`、`access-to-justice-legal-aid/`、`debt-obligation-collection-relief-continuity/` 和 `tenant-screening-rental-access-continuity/` 的接口。
- 通知质量、可理解性、无障碍、身份匹配、记录校验、复议/撤销路径和程序性排除风险。

## Human Infra 链路

```text
法院通知 / 送达 / 缺席判决风险可控
  -> 主体能够及时知道程序、理解要求并获得回应机会
  -> 资源、住房、收入、家庭权利和信用不因静默程序失败被剥夺
  -> 法律救济、复议、撤销和执行监督路径仍可进入
  -> 名义权利转化为真实可用的程序参与能力
```

## 非目标

- 不提供个人案件、送达有效性、答辩、撤销缺席判决、驱逐、债务、家庭法院、保护令或法律建议。
- 不指导躲避送达、伪造通知、隐藏地址、滥用程序、规避执行或骚扰当事人。
- 不替代律师、法院自助中心、法律援助、书记员、调解员或官方通知系统。

## Source Signals

- U.S. Courts Civil Cases: https://www.uscourts.gov/about-federal-courts/types-cases/civil-cases
- Federal Rules of Civil Procedure: https://www.uscourts.gov/rules-policies/current-rules-practice-procedure/federal-rules-civil-procedure
- National Center for State Courts Access to Justice: https://www.ncsc.org/consulting-and-research/areas-of-expertise/access-to-justice

## 下一步

- 建立程序通知变量表：送达方式、地址质量、语言、无障碍、期限、回应入口、缺席后果、执行路径和救济机制。
- 整理 U.S. Courts、FRCP、NCSC、Legal Services Corporation 和 state court self-help Source Cards。
- 与 `access-to-justice-legal-aid/` 明确分工：司法可及域关注法律服务入口，本域关注程序通知和缺席风险链。
