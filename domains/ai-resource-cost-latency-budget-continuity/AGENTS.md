# ai-resource-cost-latency-budget-continuity 目录说明

本目录维护 AI 资源、成本和延迟预算资料。它是 AI 增强从一次性使用走向长期可持续运行的运营约束层。

## 目录结构

```text
ai-resource-cost-latency-budget-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 token、算力、延迟、费用、配额、缓存和降级策略如何影响主体持续性。
- 本目录只维护预算和运行约束框架，不保存云账单、API key、私有用量日志或采购合同。
- 资料进入本域时必须保留任务类型、预算边界、延迟目标、费用上限、降级策略和不可绕过边界。

## 上下游关系

- 上游来自 NIST AI RMF、FinOps、绿色软件、MLCommons 和云资源治理资料。
- 下游服务 `ai-agent-tool-permission-sandbox-continuity/`、`compute-data-center-ai-infrastructure/` 和 AI 工具运行策略。
- 不替代 `compute-data-center-ai-infrastructure/`；该域关注基础设施供给，本目录关注使用侧预算治理。

## 维护规则

- 不记录绕过计费、盗用算力、规避速率限制或云服务滥用方法。
- 不把更高成本写成更高价值。
- 若新增预算字段影响工具链或 Web 运行说明，必须同步更新索引。
