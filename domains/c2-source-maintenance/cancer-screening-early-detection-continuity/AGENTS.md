# cancer-screening-early-detection-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cancer-screening-early-detection-continuity` |
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


本目录维护癌症筛查、早期发现、异常结果追踪、过度诊断和筛查公平资料。它是主体在癌症进入晚期治疗负担之前的前端证据执行域。

## 目录结构

```text
cancer-screening-early-detection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义癌症筛查、异常结果闭环、早诊、假阳性/假阴性和公平可及如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案筛查结果、家族史、遗传信息、影像、病理、症状或诊疗资料。
- 资料进入本域时必须保留筛查对象、收益伤害权衡、异常追踪、过度诊断和禁止用途。

## 上下游关系

- 上游来自 USPSTF、NCI、CDC 和癌症筛查资料。
- 下游服务 `cancer-control/`、实验室、影像和真实世界随访建模。
- 不替代医生、肿瘤科、遗传咨询、筛查项目、保险服务或个体医疗建议。

## 维护规则

- 不写个人筛查年龄、频率、检查选择、结果解读、遗传风险、治疗或个体建议。
- 不把系统级癌筛研究写成个人筛查推荐器或商业检测推广。
- 新增变量必须区分覆盖、质量、异常追踪、收益伤害、过度诊断和公平性。
