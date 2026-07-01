# synthetic-biology-biosecurity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/synthetic-biology-biosecurity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


`domains/c2-source-maintenance/synthetic-biology-biosecurity/` 保存合成生物学与生物安全研究域。它关注未来生物技术修复能力与双重用途风险之间的治理边界。

## 目录结构

```text
synthetic-biology-biosecurity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责合成生物学、生物安全、生物安保、双重用途风险和治理边界。
- 本域可整理公开政策、风险分类、审查机制和非操作性安全原则。
- 本域不提供病原体工程、培养、传播、规避筛查、实验协议或湿实验步骤。

## 维护规则

- 任何生物技术主张必须说明收益路径、风险路径、审查边界、禁止用途和证据等级。
- 涉及高风险生物内容时只写治理、制度、风险分类和非操作性边界。
- 新增文件或子目录时，同步更新本文件。
