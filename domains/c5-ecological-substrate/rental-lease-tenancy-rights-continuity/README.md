# Rental Lease Tenancy Rights Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/rental-lease-tenancy-rights-continuity` |
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

租赁、租约与居住权连续性域研究“一个人是否能在租赁住房中稳定居住、理解义务、获得通知、保有基本权利并在争议中不被程序性排除”。

## Human Infra 价值

租赁住房不是单纯消费品，而是睡眠、恢复、工作、学习、照护、身份邮件、医疗随访和社会关系的运行基座。租约条款、租金支付、通知、维修责任、续租、押金、占有权和程序可理解性都会影响主体是否能持续执行长期任务。

该域把租赁关系建模为：

```text
rental housing
  -> lease terms / rent / notices / habitability / renewal
  -> housing stability
  -> sleep, recovery, work, school, care, records
  -> subject continuity
```

## 关注对象

- 租赁协议、month-to-month tenancy、续租和终止通知。
- 租金、押金、费用、late fees、utilities pass-through 和收据记录。
- habitability、repair request、access notice 和 landlord-tenant communication。
- 租客权利、责任、通知可理解性和语言/残障可达性。
- 租赁事实如何影响身份、学校、医疗、福利、信用和就业入口。

## 不做什么

- 不提供个案法律意见、租约解释、驱逐抗辩、押金争议、维修策略、谈判话术或文书代写。
- 不提供绕过租约、逃租、伪造记录、非法占有、报复房东/租客、骚扰、威胁或规避执法方法。
- 不判断任何个人租赁关系、通知、期限、费用、权利或责任是否有效。

## 证据与来源

- USA.gov tenant rights and renting resources.
- HUD renter resources and fair housing materials.
- 地方和州 landlord-tenant law 只能作为管辖区差异背景，不作为本项目个案建议来源。

## 上下游关系

- 上游：`housing-built-environment-stability`、`tenant-screening-rental-access-continuity`、`address-residency-mail-service-continuity`。
- 下游：`eviction-prevention-court-diversion-continuity`、`housing-habitability-inspection-code-enforcement-continuity`、`fair-housing-discrimination-reasonable-accommodation-continuity`。
