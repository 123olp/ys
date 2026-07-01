# research-metrics-incentives-assessment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/research-metrics-incentives-assessment-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录负责科研指标、评价激励和 Goodhart 风险连续性。

## 结构

```text
research-metrics-incentives-assessment-continuity/
├── AGENTS.md
└── README.md
```

## 边界

- 只维护指标激励、评价改革、证据生态风险和模型解释边界。
- 上游：`domains/c4-conversion-channel/research-portfolio-prioritization-funding-governance/`、`domains/c4-conversion-channel/citation-network-claim-propagation-continuity/`。
- 下游：科研组合治理、Source Card、证据等级和传播材料。
- 不提供刷指标、刷引用、期刊排名套利、基金包装、招聘晋升或机构排名建议。

## 维护规则

使用 DORA、Leiden Manifesto、CoARA 和 Metric Tide 作为锚点。任何指标只能作为上下文信号，不得替代研究质量评价。
