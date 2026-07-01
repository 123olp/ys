# Data Breach Notification Identity Recovery Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/data-breach-notification-identity-recovery-continuity` |
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

Data Breach Notification Identity Recovery Continuity 关注数据泄露通知、暴露数据类型、身份盗用恢复、信用冻结、账号恢复、医疗/金融/政府资料泄露和长期风险监测如何影响主体恢复能力。

## 对象

- Data breach notification、personal information exposure、identity theft recovery、credit freeze、fraud alert、account takeover 和 remediation。
- SSN、地址、生日、账号、医疗、保险、税务、学生、儿童、位置和生物特征等资料泄露后的长期风险。
- 企业、政府、医疗、教育、金融和平台泄露通知与主体恢复入口之间的断点。

## Human Infra 价值

```text
主体持续性需要泄露事件后仍能恢复身份和资源入口
-> 数据泄露会把身份、账号、信用、医疗、税务和家庭资料暴露给未知攻击面
-> 通知不足、资料类型不清或恢复入口不可达会让身份盗用和账号接管长期化
-> 泄露通知、身份恢复、冻结、监测和投诉入口把事件转成可处理的恢复链
-> 主体更可能保留金融、医疗、税务、教育、账号和公共服务连续性
```

## 边界

- 本域不提供法律建议、索赔建议、冻结/解冻操作指导、账号恢复代办、监测服务推荐或个案应对策略。
- 不提供利用泄露数据、撞库、社工、身份盗用、账号接管、数据购买或暗网搜索的方法。
- 不收集真实泄露资料、SSN、生日、账号、医疗记录、税务记录、未成年人资料或 breach notice。
- 只整理公开资料、通知变量、恢复路径、风险边界和禁止用途。

## 上下游

- 上游：`digital-identity-security/`、`health-data-privacy-governance/`、`software-supply-chain-dependency-provenance-continuity/`。
- 下游：`fraud-scams-consumer-protection/`、`credit-consumer-reporting-access-continuity/`、`banking-deposit-account-access-continuity/`、`email-account-recovery-continuity/`。

## Source Signals

- Federal Trade Commission IdentityTheft.gov and data breach guidance.
- NIST Cybersecurity Framework and Privacy Framework.
- HHS breach notification materials for health information as boundary context.
- CFPB consumer report freeze and fraud alert materials.
