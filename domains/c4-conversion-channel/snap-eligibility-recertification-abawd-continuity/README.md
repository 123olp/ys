# SNAP Eligibility Recertification ABAWD Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/snap-eligibility-recertification-abawd-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 关键词显示该域主要处理研究、数据、模型、服务入口、身份记录、转化或治理接口。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何把潜在可能性转成真实可用路径，例如研究、医疗、数据、制度、身份、资金或转化接口？

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

- 界定转化瓶颈：研究发现、数据、临床、制度、身份、资金、可及性或操作接口。
- 说明接口机制：潜在可能性如何经过标准、流程、记录、组织或平台变成可用路径。
- 记录必要证据：登记系统、指南、监管材料、数据库、标准文档或真实世界部署资料。
- 识别摩擦指标：时间成本、资金成本、信息成本、合规成本、可及性和协作成本。
- 列出失败点：证据断裂、监管阻塞、制度排斥、隐私风险、责任不清或资源不可达。

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

`snap-eligibility-recertification-abawd-continuity` 研究 SNAP 从名义食物援助资格到持续可维护资格的行政链路：收入/家庭组成、认证期、recertification、通知、ABAWD 时间限制、工作要求、E&T 转介和错误恢复如何影响主体的食物输入、现金流缓冲、注意力预算和长期行动窗口。

## 核心问题

SNAP 的价值不只在于“是否有福利”，还在于主体能否持续满足、理解、维护和恢复资格。资格维护失败会把食物风险转化为行政负担、通知错过、证明摩擦、制裁、断粮和家庭预算冲击。

## 对象

- SNAP 资格、认证期、recertification、change reporting、notice 和 hearing 入口。
- ABAWD time limit、work requirement、豁免、Good Cause、SNAP E&T 和州级执行差异。
- 家庭组成、收入波动、地址/通信变化、语言可及、数字入口和行政错误。
- 与 `snap-ebt-redemption-retailer-payment-continuity` 的分工：本域关注资格维护，后者关注 EBT 支付兑换。

## Human Infra 价值

- 把食物援助从一次性资格判断改写为可续期、可通知、可纠错的主体持续性基础设施。
- 解释行政摩擦如何消耗时间、注意力、交通、文件管理和家庭恢复资源。
- 为“反稀缺工程”提供一个具体程序域：减少食物输入断点，保护学习、工作、照护和健康执行。

## 边界

- 不提供个人 SNAP 资格判断、申请、续期、听证、ABAWD 豁免、E&T 选择、材料准备或州级操作建议。
- 不生成规避工作要求、虚假家庭组成、收入隐瞒、身份冒用、福利欺诈、EBT 转售或听证策略内容。
- 不收集 SSN、收入、住址、家庭成员、移民身份、案件号、EBT 信息或州门户凭证。

## 上游与下游

- 上游：`social-protection-benefits-delivery`、`administrative-burden-procedural-friction`、`household-composition-dependent-eligibility-continuity`。
- 下游：`snap-ebt-redemption-retailer-payment-continuity`、`grocery-retail-food-store-access-continuity`、`food-bank-pantry-community-food-distribution-continuity`、`emergency-food-disaster-feeding-continuity`。

## 初始资料线索

- USDA FNS SNAP eligibility: https://www.fns.usda.gov/snap/recipient/eligibility
- USDA FNS SNAP work requirements: https://www.fns.usda.gov/snap/work-requirements
- USDA FNS SNAP Employment and Training: https://www.fns.usda.gov/snap/et
