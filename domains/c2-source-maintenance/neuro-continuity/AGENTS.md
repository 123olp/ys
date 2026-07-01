# neuro-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/neuro-continuity` |
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


`domains/c2-source-maintenance/neuro-continuity/` 保存神经连续性研究域。它关注大脑、记忆、意识、人格、身份和行动能力的持续。

## 目录结构

```text
neuro-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责“延续的是否仍是同一个主体”的神经和身份条件。
- `memory-editing/` 处理记忆读写与修改，`disembodied-cns/` 处理去具身中枢架构，本域负责上位连续性框架。
- 本域不提供脑保存、神经刺激、药物、记忆操控或人体实验步骤。

## 维护规则

- 任何连续性主张必须区分数据连续、功能连续、心理连续、身体连续和主体权利连续。
- 涉及记忆、意识或人格时必须保留同意、退出、审计和不可逆风险。
- 新增文件或子目录时，同步更新本文件。
