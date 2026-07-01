# trust-estate-affairs-succession-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/trust-estate-affairs-succession-continuity` |
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


本目录承载事务整理、信托/遗产角色和继承连续性资料。它研究失能或死亡边界附近，资源、文件、账户、责任和长期项目如何避免冻结、丢失或冲突化。

## 目录结构

```text
trust-estate-affairs-succession-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应记录文件类型、角色类型、交接断点、平台边界、司法边界和禁止用途。
- 本域不保存个人遗产资料，不解释文件效力，也不输出法律、税务、继承、保险或投资建议。

## 维护规则

- 引用资料优先来自 NIA、CFPB、法院/公共法律教育机构、消费者保护机构和平台公开政策。
- 必须区分资料整理、角色说明和个案法律行动。
- 不把继承连续性写成绕过主体同意、隐私或平台规则的工具。
