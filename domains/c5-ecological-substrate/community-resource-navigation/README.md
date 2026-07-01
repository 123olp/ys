# Community Resource Navigation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/community-resource-navigation` |
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

`community-resource-navigation/` 研究 211、社区资源目录、社会需求筛查、转介、闭环回访和本地服务导航。

> 核心问题：资源存在不等于主体能够找到、理解、申请、抵达和持续使用；社区资源导航是把分散服务转化为实际支持的接口。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 资源、服务和支持必须能被发现、匹配、转介和确认到达
  -> 本地服务网络必须降低搜索成本、行政摩擦和断点
  -> 社区资源才能从名义存在转化为主体恢复与持续行动能力
```

## 关注对象

- 211、本地资源目录、Open Referral HSDS、社会需求筛查、闭环转介和服务导航。
- 食物、住房、交通、医疗、心理健康、照护、法律援助和危机服务入口的连接逻辑。
- 资源目录新鲜度、服务资格不确定、转介失败、回访缺失、人工帮助和跨机构协作。
- 与 `social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`health-literacy-navigation/` 和 `resource-social-infra/` 的接口。

## Human Infra 模型链路

```text
社区资源导航基础设施
  -> 改变资源发现、匹配、转介、回访和人工协助能力
  -> 改变主体获得食物、住房、医疗、交通、照护和危机支持的状态
  -> 降低服务碎片化、申请放弃、资源错配和恢复路径中断风险
  -> 增强抗冲击能力、有效时间和未来选择权
```

## 非目标

- 不判断个人资格、申请策略、福利结果、机构质量或资源实时可用性。
- 不替代 911、988、危机热线、社工、法律援助、医疗或福利机构。
- 不收集、交换或公开敏感个人需求数据。

## Source Signals

- 211: https://www.211.org/
- Open Referral: https://openreferral.org/
- Human Services Data Specification: https://docs.openreferral.org/en/latest/hsds/
- The Gravity Project: https://thegravityproject.net/
- CMS Accountable Health Communities Model: https://www.cms.gov/priorities/innovation/innovation-models/ahcm

## 下一步

- 建立社区资源导航变量表：资源发现、目录更新、资格不确定、转介完成、闭环回访、人工协助和隐私边界。
- 与 `social-protection-benefits-delivery/` 拆分福利制度递送边界，与 `resource-social-infra/` 拆分资源供给边界。
- 整理 211、Open Referral、Gravity Project 和 AHC 的 Source Cards。
