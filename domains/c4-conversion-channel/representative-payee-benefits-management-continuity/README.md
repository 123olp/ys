# Representative Payee Benefits Management Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/representative-payee-benefits-management-continuity` |
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

Representative Payee Benefits Management Continuity 关注 Social Security representative payee、VA fiduciary、公共福利代收代管、记录责任和防滥用机制如何在主体无法管理福利时保持收入和基本生活连续性。

## 对象

- Representative payee、VA fiduciary、benefits management、收入支付、账单、住房、食物、医疗和照护费用。
- 主体无法管理福利、认知下降、严重疾病、儿童、残障、无家可归或机构照护中的收入断点。
- 报告义务、资金用途、记录保存、滥用、监督、变更代理和受益人保护。

## Human Infra 价值

```text
主体持续性需要公共收入在能力下降时仍用于主体本身
-> 福利支付常常承担住房、食物、药物和照护的底线输入
-> 若主体无法管理资金，收入可能被浪费、挪用、断供或被他人控制
-> 代表收款人和受托项目把代管、用途限制、报告和监督纳入制度
-> 福利更可能稳定转化为主体基本生活和照护连续性
```

## 边界

- 本域不提供福利申请、代表收款人申请、资格判断、支付金额、申诉、账户设置、资金使用或个案举报建议。
- 不判断某人是否需要代表收款人、某代理是否合格或某支出是否合规。
- 不替代 SSA、VA、福利机构、律师、保护服务、法院或个案管理人员。
- 只整理公开资料、角色义务、监督结构、风险边界和禁止用途。

## 上游与下游

- 上游：`social-protection-benefits-delivery/`、`financial-inclusion-payment-systems/`、`disability-services-independent-living/`、`homelessness-unsheltered-health-continuity/`。
- 下游：`financial-fiduciary-power-of-attorney-continuity/`、`elder-justice-adult-protective-services/`、`community-resource-navigation/`。

## 初始资料线索

- Social Security Administration Representative Payee Program.
- Social Security Administration Advance Designation.
- VA Fiduciary Program public materials.
