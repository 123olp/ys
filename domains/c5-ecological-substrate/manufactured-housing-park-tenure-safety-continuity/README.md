# Manufactured Housing Park Tenure Safety Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/manufactured-housing-park-tenure-safety-continuity` |
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

制造房屋、移动房屋园区与 tenure 安全连续性域研究“当住房本体、土地租赁、园区运营和基础设施分离时，主体是否仍能获得可负担、可维护、可迁移和可保留的住所”。

## Human Infra 价值

制造房屋常是可负担住房的重要来源，但其风险结构独特：居民可能拥有房屋却租赁土地，面对 lot rent、园区出售、基础设施失修、搬迁成本、融资限制和灾害暴露时，住房稳定性会被集中击穿。

```text
manufactured home + rented lot
  -> park rules / lot rent / infrastructure / relocation constraints
  -> tenure security or displacement
  -> housing continuity
```

## 关注对象

- manufactured housing、mobile home park、lot rent、park rules 和 resident notice。
- park sale、closure、relocation、infrastructure, utilities, flood/fire exposure 和 repair responsibility。
- resident ownership、financing、titling、consumer protection 和 affordability risk。
- disaster resilience、code standards、transportability limits 和 community governance。

## 不做什么

- 不提供购房、卖房、融资、租地、园区规则、搬迁、维修、产权、税务、法律或投资建议。
- 不提供规避园区规则、非法占用、拆迁对抗、维修施工、utility bypass 或虚假文件方法。
- 不判断任何制造房屋、园区、租约、产权或搬迁补偿是否合规。

## 证据与来源

- HUD manufactured housing program and standards.
- CFPB manufactured housing finance materials.
- State and local manufactured housing materials only as jurisdictional context.

## 上下游关系

- 上游：`housing-built-environment-stability`、`real-property-title-deed-record-continuity`、`water-wastewater-utility-service-continuity`。
- 下游：`rental-lease-tenancy-rights-continuity`、`housing-habitability-inspection-code-enforcement-continuity`、`disaster-recovery-relief-continuity`。
