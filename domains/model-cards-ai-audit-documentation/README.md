# Model Cards AI Audit Documentation

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
