# ai-evaluation-benchmark-validity-continuity 目录说明

本目录维护 AI 评测、基准有效性和能力校准资料。它是 AI 工具进入 Human Infra 主体增强系统前的评测可信度过滤层。

## 目录结构

```text
ai-evaluation-benchmark-validity-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI benchmark、评测任务、污染风险、覆盖率和指标解释如何影响主体持续性。
- 本目录只维护评测方法、证据边界和失败模式，不保存模型权重、测试集泄露材料或私有 benchmark。
- 资料进入本域时必须保留评测任务、指标、数据来源、污染风险、适用场景和不可推广边界。

## 上下游关系

- 上游来自 NIST AI RMF、HELM、MLCommons、Dioptra 和模型评测文献。
- 下游服务 `model-cards-ai-audit-documentation/`、`ai-agent-tool-permission-sandbox-continuity/` 和 Web 论文页。
- 不替代 `uncertainty-quantification-model-calibration/`；该域关注一般模型校准，本目录关注 AI benchmark 有效性。

## 维护规则

- 不记录刷榜、测试集污染、规避评测或隐藏失败样本方法。
- 不把单一分数升级为生产可用结论。
- 若新增评测字段影响模型卡、Source Card 或论文页契约，必须同步更新对应索引。
