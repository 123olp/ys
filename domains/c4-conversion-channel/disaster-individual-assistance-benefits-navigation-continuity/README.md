# Disaster Individual Assistance Benefits Navigation Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/disaster-individual-assistance-benefits-navigation-continuity` |
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

`disaster-individual-assistance-benefits-navigation-continuity/` 研究灾后个人援助、灾害救助申请、资格导航、材料补正、申诉和重复给付治理如何影响主体从灾害冲击中恢复基本行动能力。

> 核心问题：灾害后的主体不仅需要“活下来”，还需要把损失转化为可申请、可审核、可补正、可兑现的恢复资源；援助导航失败会把短期灾害变成长尾贫困、住房不稳和医疗中断。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体会遭遇灾害导致住房、收入、医疗、交通、文件和通信断裂
  -> 灾后恢复需要把损失映射为公共援助、保险、社区资源和补充材料
  -> 若援助入口、资格解释、材料补正或申诉失败，恢复窗口被压缩
  -> 因此灾后个人援助导航是主体灾后恢复连续性的执行域
```

## 关注对象

- FEMA Individual Assistance、DisasterAssistance.gov、Small Business Administration disaster loans、地方/州补充援助和非营利救助入口。
- 申请入口、身份验证、损失证明、重复给付、申诉、转介、语言可达、数字可达和隐私保护。
- 与 `emergency-financial-document-cash-readiness-continuity/` 的边界：该域关注灾前金融文件准备；本域关注灾后援助申请链。

## Human Infra 模型链路

```text
灾后个人援助导航系统 T
  -> 改变申请入口、材料完整性、资格解释、补正、申诉和转介变量 X
  -> 改变主体灾后资源恢复状态 S
  -> 改变住房不稳、治疗中断、债务累积和长期失能风险 λ(t)
  -> 影响有效时间、恢复速度、家庭稳定和未来选择权
```

## 非目标

- 不提供个案救助承诺、资格判断、申请代办、欺诈规避、文件伪造、补助最大化策略或法律/财务建议。
- 不收集身份证件、家庭住址、银行账户、保险材料、灾害损失证明或其他敏感恢复资料。
- 不替代 FEMA、SBA、州/地方应急管理、保险机构、法律援助或社区组织。

## Source Signals

- DisasterAssistance.gov: https://www.disasterassistance.gov/
- FEMA Individual Assistance: https://www.fema.gov/assistance/individual
- FEMA Help After a Disaster: https://www.fema.gov/assistance/individual/program
- SBA Disaster Assistance: https://www.sba.gov/funding-programs/disaster-assistance
