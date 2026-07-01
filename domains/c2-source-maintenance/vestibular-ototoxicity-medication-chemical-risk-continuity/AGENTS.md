# vestibular-ototoxicity-medication-chemical-risk-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-ototoxicity-medication-chemical-risk-continuity` |
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


## 职责

- 维护耳毒性、药物/化学暴露、噪声协同、听觉前庭副作用和监测边界。
- 将干预副作用、职业暴露、听觉/平衡终点和风险权衡资料整理为 Source Card。
- 与 `medicine-access-treatment-continuity/`、`occupational-exposure-industrial-hygiene/`、`noise-induced-hearing-loss-prevention-continuity/` 保持边界清晰。

## 非目标

- 不提供用药、停药、剂量、暴露限值、监测计划、诊断、职业法律或监管判断。
- 不替代医生、药师、职业卫生、毒理、听力学、耳鼻喉或监管服务。

## 上游

- `vestibular-balance-spatial-orientation/`：前庭和平衡总框架。
- `medicine-access-treatment-continuity/`：用药和治疗连续性。
- `occupational-exposure-industrial-hygiene/`：职业暴露治理。

## 下游

- `hearing-auditory-communication-continuity/`：听觉沟通后果。
- `risk-engineering/`：副作用和尾部风险建模。
