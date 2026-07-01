# attention-executive-control 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/attention-executive-control` |
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


`domains/c3-generation-engine/attention-executive-control/` 保存注意力与执行控制研究域。它关注注意力、工作记忆、抑制控制、任务切换和分心环境如何影响主体有效行动密度。

## 目录结构

```text
attention-executive-control/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责注意力稳定、执行功能、冲动控制、分心风险、任务切换成本和计划执行变量。
- 本域可整理公开心理学、神经科学、工作流和信息环境资料。
- 本域不提供 ADHD、心理、神经疾病诊断治疗，也不提供药物、补剂或神经刺激建议。

## 维护规则

- 任何注意力主张必须说明变量、证据等级、适用对象、任务场景和恢复代价。
- 涉及诊断、药物、成瘾、神经刺激或个体心理危机时只写安全边界。
- 新增文件或子目录时，同步更新本文件。
