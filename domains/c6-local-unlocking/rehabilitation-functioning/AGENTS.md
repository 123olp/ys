# rehabilitation-functioning 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/rehabilitation-functioning` |
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


`domains/c6-local-unlocking/rehabilitation-functioning/` 保存康复与功能恢复研究域。它关注主体在疾病、损伤、衰老和残障后能否恢复行动、自理、沟通和社会参与。

## 目录结构

```text
rehabilitation-functioning/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责康复、功能恢复、失能预防、衰弱、活动能力和参与能力。
- 本域可引用 WHO ICF、WHO Rehabilitation 2030 和康复服务资料。
- 本域不提供个人康复处方、训练计划、诊断或治疗建议。

## 维护规则

- 任何功能改善主张必须区分身体结构、活动能力、参与能力和生活质量。
- 涉及残障和康复时，必须保留可及性、辅助技术和社会支持维度。
- 新增文件或子目录时，同步更新本文件。
