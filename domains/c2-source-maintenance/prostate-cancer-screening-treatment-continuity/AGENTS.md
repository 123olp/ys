# prostate-cancer-screening-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/prostate-cancer-screening-treatment-continuity` |
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


本目录维护前列腺癌筛查、风险分层、主动监测、治疗副作用和生活质量连续性资料。它是癌症控制中收益伤害权衡最明显的器官特异域之一。

## 目录结构

```text
prostate-cancer-screening-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义前列腺癌筛查争议、风险分层、主动监测和治疗副作用如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案 PSA、影像、病理、尿控、性功能、症状或治疗资料。
- 资料进入本域时必须保留收益伤害权衡、过度诊断、主动监测、治疗副作用、共享决策和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和前列腺癌公开资料。
- 下游服务 `cancer-control/`、`cancer-screening-early-detection-continuity/`、泌尿功能、性健康和幸存者建模。
- 不替代医生、泌尿科、肿瘤科、病理科、放疗团队、性健康服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人 PSA 判读、筛查决策、活检、影像/病理解释、主动监测、治疗、用药、手术、放疗或个体建议。
- 不把系统级前列腺癌研究写成 PSA 解释器、治疗推荐器、性功能方案或商业检测推广。
- 新增变量必须区分筛查争议、风险分层、主动监测、过度诊断、治疗副作用、尿控/性功能和公平性。
