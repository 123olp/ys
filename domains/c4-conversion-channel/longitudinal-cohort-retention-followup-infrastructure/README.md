# Longitudinal Cohort Retention Followup Infrastructure

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/longitudinal-cohort-retention-followup-infrastructure` |
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

`longitudinal-cohort-retention-followup-infrastructure/` 研究纵向队列、长期随访、参与者留存、失访、数据链接、生命历程观测和队列治理，如何支撑寿命、健康寿命和主体持续性模型。

> 核心问题：有效永生不是短期指标问题，而是生命路径问题。若没有长期队列、稳定随访和失访治理，就无法判断因素、技术和干预如何改变风险函数、生存曲线和未来选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要理解生命路径随时间如何变化
  -> 生命路径需要纵向队列、重复观测、随访、数据链接和失访控制
  -> 失访、选择偏差、随访断裂和队列老化会扭曲风险估计
  -> 因此纵向队列留存与随访基础设施是寿命模型的数据脊梁
```

## 关注对象

- 纵向队列、生命历程研究、随访设计、参与者留存、失访、再联系和数据链接。
- 队列代表性、选择偏差、幸存者偏差、迁移、死亡链接、健康记录链接和长期数据治理。
- 寿命、健康寿命、功能状态、暴露变化、干预采用、社会条件和未来选择权的长期观测。
- 与 `survival-analysis-healthspan-risk-modeling/` 的边界：生存分析域关注统计模型；本域关注支撑模型的长期观察基础设施。
- 与 `data-quality-missingness-representativeness/` 的边界：数据质量域关注一般缺失和代表性；本域聚焦队列随访、留存和生命历程观测。

## Human Infra 模型链路

```text
纵向队列留存与随访基础设施 T
  -> 改变随访频率、留存率、失访机制、数据链接、事件确认和代表性变量 X
  -> 改变生命路径数据、暴露变化和结局观测的系统状态 S
  -> 改变选择偏差、幸存者偏差、失访偏差和错误风险估计 λ(t)
  -> 影响寿命模型、健康寿命模型、干预评估和未来选择权预测可信度
```

## 非目标

- 不提供重新识别参与者、绕过同意、滥用数据链接、压迫参与者留存或规避伦理审查策略。
- 不把单个队列结果写成所有人群通用结论。
- 不替代统计建模、IRB、数据治理或参与者社区参与。

## Source Signals

- UK Biobank: https://www.ukbiobank.ac.uk/
- NIH All of Us Research Program: https://www.researchallofus.org/
- Framingham Heart Study: https://www.framinghamheartstudy.org/
- CDC National Health and Nutrition Examination Survey: https://www.cdc.gov/nchs/nhanes/
- NIA Health and Retirement Study: https://hrs.isr.umich.edu/

## 下一步

- 建立队列基础设施变量表：招募、留存、随访频率、失访机制、事件确认、数据链接和代表性。
- 与 `survival-analysis-healthspan-risk-modeling/`、`causal-inference-target-trial-emulation/`、`research-participant-consent-community-engagement/` 和 `registries-real-world-data-governance/` 建立接口。
