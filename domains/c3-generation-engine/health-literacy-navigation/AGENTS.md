# health-literacy-navigation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/health-literacy-navigation` |
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


`domains/c3-generation-engine/health-literacy-navigation/` 保存健康素养与服务导航研究域。它关注外部医疗和社会资源如何被主体理解、进入、使用和复核。

## 目录结构

```text
health-literacy-navigation/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责健康素养、plain language、风险沟通、服务导航和共同决策的研究整理。
- 本域可整理公共健康资料、服务入口、行政负担和导航变量。
- 本域不提供医学、法律、保险、福利申请或规避制度建议。

## 维护规则

- 任何导航主张必须区分信息解释、决策支持、专业建议和制度申请。
- 与资源基础设施、治理权利、医疗数据和患者访问交叉时必须标注主拥有域。
- 新增文件或子目录时，同步更新本文件。
