# antimicrobial-resilience 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/antimicrobial-resilience` |
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


`domains/c2-source-maintenance/antimicrobial-resilience/` 保存抗微生物韧性研究域。它关注感染可治性、耐药性、感染控制和现代医学底座。

## 目录结构

```text
antimicrobial-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责抗微生物耐药、感染控制、抗菌药物治理和病原体威胁的高层研究框架。
- 本域与 `immune-maintenance/`、`cancer-control/` 和 `regenerative-medicine/` 交叉。
- 本域不提供个体用药、病原体操作、培养或规避感染控制建议。

## 维护规则

- 任何抗感染主张必须区分公共卫生、临床治疗、个人行为和药物研发证据。
- 涉及病原体和耐药性时只做防护、治理、监测和非操作性边界。
- 新增文件或子目录时，同步更新本文件。
