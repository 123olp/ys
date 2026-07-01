# Medicine Access Treatment Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/medicine-access-treatment-continuity` |
| 分级 | `C4` - 可能性转换通道层 |
| 控制轴 | 路径转换接口 |
| 分级理由 | 主要把科学、医疗、数据、制度或技术从潜在能力转成真实可用路径。 |
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

`medicine-access-treatment-continuity/` 研究药品可及、用药安全、药品信息、短缺、支付覆盖和治疗连续性，负责把“处方能否变成持续、可理解、可负担、不断供的治疗路径”纳入 Human Infra。

> 核心问题：主体即使获得医疗建议，也可能因为药品短缺、费用、标签不可理解、药房断点、用药错误或覆盖失败而无法持续治疗。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 可修复风险需要持续干预和治疗执行
  -> 关键药物必须可得、可负担、可理解且供应不断
  -> 治疗连续性决定医疗建议能否转化为真实恢复和风险下降
```

## 关注对象

- 基本药物、药品短缺、药品目录、标签说明、患者药品信息和用药安全。
- 处方覆盖、费用负担、药房可及、供应连续、替代路径和用药错误防护。
- 药品作为医疗系统、供应链、支付系统和患者理解能力之间的接口。
- 与 `healthcare-access-continuity/`、`supply-chain-continuity/`、`health-literacy-navigation/` 和 `financial-resilience-access/` 的交叉。

## Human Infra 模型链路

```text
药品与治疗连续性基础设施
  -> 改变关键药物可得性、可负担性、标签理解、供应稳定和用药安全
  -> 改变治疗执行状态和可修复风险控制能力
  -> 降低治疗中断、用药错误、疾病进展和恢复失败风险
  -> 增强健康寿命、有效时间和未来选择权
```

## 非目标

- 不提供用药建议、剂量、替代药物、停药建议、购药建议或处方解释。
- 不替代医生、药师、保险计划、监管机构或急救服务。
- 不把药品目录、短缺信息或标签资料写成个体可用性、保险覆盖或治疗适用性结论。

## Source Signals

- WHO Essential Medicines Lists: https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
- WHO Medication Without Harm: https://www.who.int/initiatives/medication-without-harm
- FDA Drug Shortages: https://www.fda.gov/drugs/drug-safety-and-availability/drug-shortages
- DailyMed: https://dailymed.nlm.nih.gov/dailymed/
- CDC Medication Safety Program: https://www.cdc.gov/medication-safety/

## 下一步

- 建立治疗连续性变量表：可得性、短缺、费用、覆盖、标签、理解、药房接入、错误防护和供应恢复。
- 将药品供应与 `supply-chain-continuity/` 的通用供应链问题拆清。
- 整理基本药物、用药安全、药品短缺和患者药品信息的 Source Cards。
