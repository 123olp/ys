# space-extreme-habitation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/space-extreme-habitation` |
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


`domains/c6-local-unlocking/space-extreme-habitation/` 保存空间与极端栖居研究域。它关注极端环境中的身体、认知、资源闭环、生命支持和协作风险。

## 目录结构

```text
space-extreme-habitation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责空间飞行、极端环境、闭环资源、远程医疗、人因和长期栖居风险建模。
- 本域可整理 NASA HRP、类比环境和极端栖居系统的高层证据与风险边界。
- 本域不提供太空任务、危险环境进入、生命支持建造、生存操作或规避安全程序建议。

## 维护规则

- 任何极端栖居主张必须说明环境压力、系统依赖、失败模式、恢复路径和证据边界。
- 涉及危险环境时只写研究框架、治理和非操作性安全边界。
- 新增文件或子目录时，同步更新本文件。
