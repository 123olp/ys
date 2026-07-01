# shift-work-long-hours-fatigue-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/shift-work-long-hours-fatigue-continuity` |
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


本目录维护轮班、夜班、长工时、连续值班和恢复窗口不足资料。它关注外部工作制度如何占用睡眠、节律和警觉性。

## 目录结构

```text
shift-work-long-hours-fatigue-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义轮班长工时如何通过睡眠债、节律错位、警觉性下降和事故暴露影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案班表、雇佣、睡眠、事故、健康或位置资料。
- 资料进入本域时必须保留工时结构、夜班暴露、任务风险、恢复窗口和禁止用途。

## 上下游关系

- 上游来自 CDC/NIOSH、NHLBI 和职业健康资料。
- 下游服务 `fatigue-risk-alertness-continuity/`、`sleep-circadian-recovery/`、`occupational-work-design/` 和安全工程模型。
- 不替代雇主、职业安全、劳动法律、睡眠医学、药学、保险、工伤或个体医疗建议。

## 维护规则

- 不写个人排班优化、法律建议、驾驶/值班许可、兴奋剂、药物、请假、投诉或索赔策略。
- 不把疲劳风险资料写成规避工时、安全或职业健康要求的方案。
- 新增资料必须区分工时、夜班、轮班稳定性、休息间隔、通勤暴露和任务关键性。
