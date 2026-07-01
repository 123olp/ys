# ai-evaluation-benchmark-validity-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-evaluation-benchmark-validity-continuity` |
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
