# caregiver-health-burnout-screening-support-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/caregiver-health-burnout-screening-support-continuity` |
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


本目录维护照护者健康、burnout、负担筛查、支持服务和恢复资源资料。它把照护者作为独立主体处理，不把照护者当作无限资源。

## 目录结构

```text
caregiver-health-burnout-screening-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义照护者健康如何影响家庭照护系统、被照护者连续性和双主体持续性。
- 本目录只整理公开资料、机制链路、筛查/支持边界和研究变量。
- 不保存心理健康、家庭冲突、危机、收入、住址、病历或照护安排资料。

## 维护规则

- 新增资料必须区分 caregiver burden、burnout、心理健康、respite、社会支持和虐待/忽视风险。
- 不提供诊断、治疗、危机处置、家庭裁决、福利申请、雇佣或个体照护建议。
- 涉及危机或虐待风险时，必须保留专业服务、紧急服务和强制报告边界。
