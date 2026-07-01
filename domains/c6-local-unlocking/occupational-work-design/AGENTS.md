# occupational-work-design 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/occupational-work-design` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


`domains/c6-local-unlocking/occupational-work-design/` 保存职业与工作设计研究域。它关注工作结构如何影响资源、健康、注意力、恢复、学习和长期行动能力。

## 目录结构

```text
occupational-work-design/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责职业安全、人体工学、工作组织、工时、职业暴露、压力、倦怠、技能转型和工作可持续性。
- 本域可整理公开职业健康、工作设计、劳动安全和就业质量资料。
- 本域不提供个体职业、劳动争议、法律、工伤、薪酬、移民或雇佣建议。

## 维护规则

- 任何工作设计主张必须说明工作类型、暴露对象、证据等级、恢复代价和权利边界。
- 涉及劳动关系、监管、薪酬、工伤或员工监控时只写公共资料和禁止用途。
- 新增文件或子目录时，同步更新本文件。
