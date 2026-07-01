# regenerative-medicine 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/regenerative-medicine` |
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


`domains/c2-source-maintenance/regenerative-medicine/` 保存再生医学与组织修复谱系。它关注身体部件是否可修复、替换、再生或长期整合。

## 目录结构

```text
regenerative-medicine/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责干细胞、组织工程、器官修复、类器官、移植、支架和生物制造的高层研究框架。
- 临床证据账本可引用 `domains/c1-boundary-rewriting/longevity-evidence/`，机制交叉可引用 `domains/c2-source-maintenance/cellular-reprogramming/`。
- 本域不承载实验操作、细胞培养、手术、移植或人体应用步骤。

## 维护规则

- 任何“修复”主张必须区分结构修复、功能恢复、长期整合和临床终点。
- 任何器官替代主张必须标注免疫、血管化、神经接入、长期安全和失败模式。
- 新增文件或子目录时，同步更新本文件。
