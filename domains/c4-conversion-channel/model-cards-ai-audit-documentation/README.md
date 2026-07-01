# Model Cards AI Audit Documentation

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/model-cards-ai-audit-documentation` |
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

## 定位

本域研究模型卡、数据集说明、系统卡、AI 审计文档、评估报告和可追溯模型治理，如何让 Human Infra 的预测模型、可视化、仿真和 AI 辅助研究输出可解释、可复核、可限制和可追责。

Human Infra 会持续产生模型、图表、论文页、推导框架和技术评估。如果没有统一文档契约，模型很容易从“研究解释工具”滑向“不可审查的权威判断”。本域负责让每个模型知道自己从哪里来、适用于什么、不适用于什么、失败时如何被发现。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要模型、图表和 AI 系统辅助判断技术路径
  -> 模型输出若不可解释、不可审计或边界不明，会制造虚假确定性
  -> 需要模型卡、数据说明、审计报告和用途限制
  -> model-cards-ai-audit-documentation
```

## 关注对象

- Model Cards、Datasheets for Datasets、System Cards、FactSheets 和模型治理文档。
- 训练数据、适用对象、任务定义、评估集、性能、校准、偏差、漂移和失效模式。
- 预测模型、D3 可视化、论文页、Scenario Evaluator 和 Human Infra Web 展示的审计记录。
- NIST AI RMF 的 govern、map、measure、manage 风险语言。
- 模型文档如何连接 Source Card、Data Card、Scenario Card 和伦理边界。

## Human Infra 模型链路

```text
模型 / 图表 / AI 系统
  -> 模型卡和审计文档
  -> 声明数据、任务、评估、边界、风险和禁止用途
  -> 支撑读者复核、版本追踪、错误纠正和治理门禁
  -> 防止模型输出被误读为医学建议、寿命承诺或自动化评分
```

## 非目标

- 不把模型卡写成营销材料、合规豁免或可信背书。
- 不输出个人寿命预测、死亡日期、诊断、治疗建议、保险评分、招聘评分或资格判断。
- 不掩盖模型失败、数据缺陷、不确定性、适用边界或人群差异。
- 不替代 `uncertainty-quantification-model-calibration/`；本域负责文档和审计契约，校准方法由模型校准域负责。

## Source Signals

- Model Cards for Model Reporting: https://arxiv.org/abs/1810.03993
- Datasheets for Datasets: https://arxiv.org/abs/1803.09010
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence
- OECD AI Principles: https://oecd.ai/en/ai-principles

## 下一步

- 为 Human Infra 建立 `MODEL_CARD.md` 模板：purpose、data、population、evaluation、calibration、limitations、forbidden uses、review status。
- 给 `/paper/` 和新增论文页建立模型/图表审计清单，避免图表被误读为事实预测。
- 与 `knowledge-graph-ontology-semantic-interoperability/` 对接，把模型卡字段纳入可查询知识结构。
