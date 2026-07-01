# Functioning Quality Of Life Outcomes

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/functioning-quality-of-life-outcomes` |
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

`functioning-quality-of-life-outcomes/` 研究功能状态、生活质量、症状负担、患者报告结局和主体中心结果。

> 核心问题：Human Infra 不能只问指标是否变好，还必须问主体是否更能行动、沟通、参与、恢复、承受生活并保持选择权。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 主体不只是活着，还必须可行动、可感知、可沟通、可参与、可恢复
  -> 干预价值必须能回到功能、症状、生活质量和主体体验
  -> 结果测量决定项目是否优化真实主体，而不是优化替代指标
```

## 关注对象

- 功能状态、活动能力、参与能力、生活质量、健康相关生活质量、症状负担和患者报告结局。
- PROMIS、WHO ICF、EQ-5D、ICHOM、PRO-CTCAE、WHOQOL、CDC Healthy Days、SF-36 等测量语言。
- 与 `rehabilitation-functioning/` 的关系：康复功能域关注恢复服务和失能路径；本域关注跨域结局语言和价值判断终点。
- 与 `measurement-feedback/`、`pain-suffering-control/`、`health-economics-value-assessment/` 和 `healthcare-access-continuity/` 的接口。

## Human Infra 模型链路

```text
功能与生活质量结局基础设施
  -> 改变功能、症状、生活质量、参与和主体体验的观测能力
  -> 改变技术、医疗、照护和社会服务的真实价值判断
  -> 降低替代指标崇拜、无效延寿、痛苦延长和主体体验被忽略的风险
  -> 增强有效时间、可承受持续性、生活质量和未来选择权
```

## 非目标

- 不解释个人量表分数、诊断状态、残障资格、保险待遇或个体生活质量结论。
- 不把任何量表写成单一价值函数，也不把人压缩成一个分数。
- 不替代临床评估、康复评估、心理评估、社会服务评估或共同决策。

## Source Signals

- PROMIS: https://www.healthmeasures.net/explore-measurement-systems/promis
- WHO ICF: https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health
- EQ-5D: https://euroqol.org/information-and-support/euroqol-instruments/
- ICHOM Patient-Centered Outcome Measures: https://www.ichom.org/patient-centered-outcome-measures/
- PRO-CTCAE: https://healthcaredelivery.cancer.gov/pro-ctcae/
- WHOQOL: https://www.who.int/tools/whoqol

## 下一步

- 建立结局变量表：功能、活动、参与、疼痛、疲劳、情绪、社会功能、症状负担、生活质量和主体体验。
- 与 `measurement-feedback/` 拆清测量管道和价值终点边界。
- 整理 PROMIS、WHO ICF、EQ-5D、ICHOM、PRO-CTCAE 和 WHOQOL 的 Source Cards。
