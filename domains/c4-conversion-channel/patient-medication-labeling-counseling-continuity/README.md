# Patient Medication Labeling Counseling Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/patient-medication-labeling-counseling-continuity` |
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

## 定位

本域研究药品标签、Medication Guide、Patient Medication Information、处方标签、说明书、药师咨询、语言可及和健康素养如何影响主体理解药物用途、风险、执行要求和求助信号。

它不是药品说明书解释器、诊断建议或个案用药咨询入口。

## 先验问题

```text
药物何以被安全使用？
  -> 风险和执行要求必须以主体能理解的形式出现
  -> 标签、说明、咨询和语言服务必须可达
  -> 主体必须知道何时求助而不是自行猜测
  -> 否则药物信息会成为新的行动摩擦和安全风险
```

## 研究对象

- FDA labeling、Medication Guides、Patient Medication Information。
- 处方瓶标签、辅助标签、用药说明、风险沟通和药师咨询。
- 语言可及、plain language、低健康素养、视觉/认知可访问性。
- OTC 与处方药信息差异、警示疲劳和风险理解。

## 关键变量

- 标签理解度、回忆率、用法错误、风险识别和咨询可达性。
- 语言服务覆盖、字体/版式可读性、认知负担和信息一致性。
- Medication Guide 提供率、咨询率和高风险药物信息完整性。

## 证据入口

- FDA drug labeling、Medication Guides、Patient Medication Information 资料。
- AHRQ health literacy、plain language 和 patient safety 资料。
- 药学、HCI、健康传播和用药安全研究。

## 非目标

- 不解释某个药品对某个人是否适用、如何服用、是否停药或如何处理副作用。
- 不生成个体药品说明、风险判断、患者教育材料或药师咨询替代文本。
- 不收集药名、处方、诊断、药品照片、过敏史或副作用个案。

## 上下游

- 上游：`medicine-access-treatment-continuity/`、`language-access-plain-communication/`、`health-literacy-navigation/`。
- 下游：`medication-reconciliation-regimen-adherence-continuity/`、`pharmacovigilance-drug-safety-monitoring/`。
