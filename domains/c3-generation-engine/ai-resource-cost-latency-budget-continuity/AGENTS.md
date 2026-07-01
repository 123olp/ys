# ai-resource-cost-latency-budget-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-resource-cost-latency-budget-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
| 路径真相源 | `domains/_possibility-space-control/classification.tsv` |
| 复核状态 | `heuristic-v0.1` |

### 文件职责

- `README.md` 面向读者，说明研究对象、Human Infra 价值链路、证据边界、非目标和下一步资料入口。
- `AGENTS.md` 面向维护者和代理，说明目录结构、上下游依赖、禁止事项、更新规则和验证要求。

### 更新规则

- 修改本域对象、边界或上下游关系时，必须同步检查 README、AGENTS 和分类表中的 `physical_path`。
- 新增资料优先沉淀为 Source Signals、Source Cards、Claim-Evidence Matrix 或明确的证据段落，不把未经核验的摘要写成稳定结论。
- 若发现当前层级不符合“可能性空间控制力”标尺，先修改 `_possibility-space-control/rubric.md` 或 `classification.tsv`，再移动目录。

### 禁止事项

- 不把研究域写成个体行动处方、临床建议、法律建议、投资建议、工程操作手册或规避规则指南。
- 不在本目录保存无来源、无边界、无证据等级的断言。
- 不绕过父级 C1-C6 物理目录直接在 `domains/` 根目录新增正式研究域。
<!-- domain-agent-contract:end -->


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
