# ai-agency-safety 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-agency-safety` |
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


`domains/c3-generation-engine/ai-agency-safety/` 保存 AI 代理安全研究域。它关注 AI 代表主体行动时的权限、监督、审计、可撤销性和失败隔离。

## 目录结构

```text
ai-agency-safety/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责 AI 代理授权、工具调用、监督、回滚、审计和事故治理。
- 本域可整理生成式 AI、代理系统和人机协作风险的高层研究框架。
- 本域不提供越狱、提示注入攻击、恶意自动化、数据窃取或绕过安全控制的方法。

## 维护规则

- 任何 AI 代理主张必须说明权限边界、监督机制、失败模式、回滚路径和主体权利。
- 涉及安全风险时只写防护、治理、评估和非操作性边界。
- 新增文件或子目录时，同步更新本文件。
