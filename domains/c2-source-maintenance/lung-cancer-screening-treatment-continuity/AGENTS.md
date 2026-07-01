# lung-cancer-screening-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/lung-cancer-screening-treatment-continuity` |
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


本目录维护肺癌筛查、影像异常追踪、烟草风险、治疗负担和呼吸功能连续性资料。它是癌症控制在高死亡风险和呼吸功能交叉处的器官特异域。

## 目录结构

```text
lung-cancer-screening-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义肺癌筛查、异常影像、诊断延迟、治疗负担和呼吸功能如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案 CT、结节、病理、吸烟史、症状、氧疗或治疗资料。
- 资料进入本域时必须保留筛查对象、影像异常追踪、烟草污名、呼吸功能、治疗负担和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和肺癌公开资料。
- 下游服务 `cancer-control/`、`tobacco-nicotine-cessation-continuity/`、影像、呼吸功能和幸存者建模。
- 不替代医生、肺科、肿瘤科、影像科、戒烟服务、氧疗服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人筛查资格、影像判读、结节风险、戒烟处方、分期、治疗、氧疗、手术或个体建议。
- 不把系统级肺癌研究写成影像第二意见、筛查推荐器、结节风险评估或商业检测推广。
- 新增变量必须区分筛查覆盖、LDCT 可及、异常追踪、诊断延迟、烟草污名、治疗负担和呼吸功能。
