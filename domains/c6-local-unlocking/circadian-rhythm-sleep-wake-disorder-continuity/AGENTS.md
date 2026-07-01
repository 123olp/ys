# circadian-rhythm-sleep-wake-disorder-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/circadian-rhythm-sleep-wake-disorder-continuity` |
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


本目录维护昼夜节律睡眠-觉醒障碍、睡眠时相错位和制度时间冲突资料。它关注生物钟与外部任务时间错位如何损耗有效时间。

## 目录结构

```text
circadian-rhythm-sleep-wake-disorder-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义昼夜节律障碍如何通过睡眠时间错位、日间功能下降和社会时间冲突影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠、光照、可穿戴、学校、工作或医疗资料。
- 资料进入本域时必须保留节律类型、时间环境、支持接口、功能影响和禁止用途。

## 上下游关系

- 上游来自 NHLBI、MedlinePlus 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`light-exposure-circadian-environment-continuity/` 和疲劳风险模型。
- 不替代睡眠医学、精神健康、药学、学校/雇主、职业安全或个体医疗建议。

## 维护规则

- 不写个人诊断、光照方案、药物/褪黑素、剂量、作息处方、便利申请或职业安排。
- 不把节律教育资料写成个人相位判断。
- 新增资料必须区分节律类型、外部时间约束、光暗输入、日间损害和支持可及。
