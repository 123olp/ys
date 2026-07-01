# learning-skill-acquisition 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/learning-skill-acquisition` |
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


`domains/c3-generation-engine/learning-skill-acquisition/` 保存学习与技能获得研究域。它关注主体如何把时间、反馈和经验转化为可迁移能力。

## 目录结构

```text
learning-skill-acquisition/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责学习科学、技能形成、练习反馈、迁移能力、再训练和终身学习。
- 本域可整理公开教育、技能、训练、职业转换和 AI 学习工具资料。
- 本域不提供个体教育、考试、就业、移民、认证或职业处方。

## 维护规则

- 任何学习主张必须说明任务类型、学习者群体、证据边界、迁移范围和机会成本。
- 涉及教育资源、职业路径或技能证书时只写通用研究框架和非个体建议。
- 新增文件或子目录时，同步更新本文件。
