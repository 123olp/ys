# Memory Editing 架构说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c1-boundary-rewriting/memory-editing` |
| 所属层级 | `C1` - 可能性边界改写层 |
| 父级容器 | `domains/c1-boundary-rewriting` |
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


`memory-editing/` 是记忆编辑与人格连续性研究域。它处理记忆痕迹读写、删除、写入、重构、验证和治理的高层模型，不提供可执行神经操控步骤。

## 目录结构

```text
memory-editing/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义记忆编辑的核心对象、研究问题、安全边界和与 Human Infra 的关系。

## 上下游关系

- 上游依赖 `docs/reference/ethics-and-safety-boundaries.md` 的神经安全、同意、退出和审计原则。
- 与 `disembodied-cns/` 共享主体连续性和尊严原则。
- 不与 `longevity-evidence/` 共享数据模型；记忆编辑不是普通健康干预证据页。

## 维护规则

- 新增内容必须明确区分治疗性干预、增强性干预和控制性操控。
- 禁止写入可执行的记忆读取、删除、写入、重构或人体实验步骤。
- 技术路线只能作为公开证据的高层整理，并必须保留不确定性、失败模式和滥用风险。
