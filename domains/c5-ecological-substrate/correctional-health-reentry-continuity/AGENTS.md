# correctional-health-reentry-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/correctional-health-reentry-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录维护羁押健康与重返社会连续性域。它是 Human Infra 的“制度转换窗口健康不断线”层，负责羁押、释放和社区重返如何影响主体持续性。

## 目录结构

```text
correctional-health-reentry-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明羁押健康、药物连续性、慢病、心理健康、感染、身份、住房和重返服务如何影响主体持续性。
- 本域只做公开羁押健康、重返社会、公共卫生和服务连续性资料整理。
- 不提供法律策略、监管规避、设施安全弱点、违禁品、个体医疗、假释/缓刑或释放计划建议。

## 维护规则

- 新增材料必须区分羁押内健康服务、释放前计划、社区重返、身份文件、住房、保险和医疗连续性。
- 不把羁押或释放状态写成污名标签、风险定性或治安宣传。
- 涉及监狱、拘留和监管系统时，禁止写可操作安保规避、对抗、走私或逃避内容。
