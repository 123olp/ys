# Life Insurance Beneficiary Claim Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/life-insurance-beneficiary-claim-continuity` |
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

Life Insurance Beneficiary Claim Continuity 研究寿险保单、受益人指定、保单定位、死亡理赔、未领取权益和争议边界如何把死亡风险池转化为幸存者可获得资源。

> 核心问题：寿险的价值不在保单存在，而在死亡后受益人能否知道、证明、申请并实际获得给付；保单失联会把风险转移工具变成沉没文件。

## 研究对象

- Life insurance policy、beneficiary designation、claim、policy locator、unclaimed benefits 和 group life insurance。
- 受益人记录更新、保单查找、死亡证明、理赔文件、雇主团体寿险和州监管/未领取财产。
- 受益人冲突、离婚/再婚、未成年受益人、信托受益人、诈骗和身份核验。

## 先验链路

```text
主体生前可能通过寿险把死亡风险转移给保险池
  -> 死亡后受益人必须知道保单存在并完成身份、死亡和受益权证明
  -> 保单、受益人或理赔入口若失联，风险转移无法兑现
  -> 幸存者失去偿债、丧葬、住房、教育和恢复所需资源
  -> 家庭未来选择权和财务韧性下降
  -> 因而寿险受益人与理赔链是死亡后风险转移兑现层
```

## 关键变量

- 保单可发现性、受益人记录准确性、理赔入口、证明材料、理赔延迟和未领取权益。
- 个人寿险、团体寿险、雇主福利、州保单定位器、未领取财产和监管投诉路径。
- 受益人争议、未成年/失能受益人、家庭暴力、诈骗、身份盗用和隐私风险。

## 证据入口

- NAIC Life Insurance Policy Locator and consumer materials。
- State insurance department consumer materials。
- Employer group life and unclaimed property public materials。

## 非目标

- 本域不推荐寿险、计算保额、解释保单、判断受益人、代写理赔或争议材料。
- 不提供法律、税务、保险、投资、遗产规划或个案财务建议。
- 不收集保单号、死亡证明、受益人信息、身份证件、银行账户或理赔资料。

## 上下游

- 上游：`death-certificate-registration-cause-of-death-record-continuity/`、`insurance-risk-transfer/`、`retirement-pension-savings-plan-continuity/`。
- 下游：`survivor-benefits-death-notification-continuity/`、`estate-inventory-asset-liability-handoff-continuity/`、`financial-resilience-access/`。
