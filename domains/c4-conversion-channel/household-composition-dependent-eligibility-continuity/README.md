# 家庭组成、受扶养人与资格关系连续性

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/household-composition-dependent-eligibility-continuity` |
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

本域研究 household、受扶养人、共同居住、照护关系、亲属关系和申报单位如何影响税务、健康保险、福利、学校、住房、托育和社会服务资格。它关注家庭事实如何被制度建模，不提供个人报税、福利、保险或家庭法建议。

## 研究对象

- household composition、tax dependents、coverage household、benefit household 和服务资格单位。
- 共同居住、主要照护者、受扶养人、监护安排、共享费用和家庭收入计算。
- IRS、HealthCare.gov、Medicaid/SNAP/TANF、学校、住房、保险和托育系统中的 household 定义差异。
- 家庭变化、分居、离婚、再婚、监护变化、寄养、大学生、老年照护和多代同堂场景。

## 价值链路

```text
资源资格不是只由个人决定
  -> 许多制度先把人放进 household、受扶养人或照护关系模型
  -> 家庭组成决定收入计算、责任归属、保险覆盖、福利资格和服务入口
  -> 家庭事实变化或系统定义不一致会导致错误拒绝、错误支付、覆盖断裂或追缴风险
  -> 家庭组成连续性把关系事实转化为可审查的资源资格底座
```

## 关键问题

- 不同制度如何定义 household、dependent、coverage family 和 benefit unit？
- 家庭组成变化如何影响医疗覆盖、税务抵免、公共福利、学校和住房资格？
- household 变量如何连接资源分配、责任归属、照护角色和行政负担？
- 如何避免把家庭关系建模简化为个体失败、福利欺诈假设或家庭监控？

## 上游与下游

- 上游：`vital-records-life-event-continuity/`、`family-law-custody-child-support-continuity/`、`kinship-foster-adoption-care-continuity/`、`childcare-family-continuity/`。
- 下游：`tax-administration-filing-record-continuity/`、`social-protection-benefits-delivery/`、`healthcare-access-continuity/`、`insurance-risk-transfer/`、`public-benefits-eligibility-automated-decision-continuity/`。

## 非目标

- 不提供个人税务申报、dependent claim、健康保险 household、Medicaid/SNAP/TANF、住房、学校或托育资格判断。
- 不判断谁能申报谁、谁应计入 household、谁有监护权、谁应支付费用或谁应取得福利。
- 不协助福利欺诈、虚假申报、规避追缴、隐瞒家庭成员、逃避抚养责任或操纵资格规则。

## 初始资料入口

- IRS: Dependents
- HealthCare.gov: Household size and income
- Medicaid, SNAP, TANF, school and housing program official rules
- State/local benefits eligibility official resources
