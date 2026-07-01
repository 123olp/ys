# chronic-kidney-disease-screening-progression-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-kidney-disease-screening-progression-continuity` |
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


本目录维护慢性肾病筛查、进展风险、心肾代谢交互、保护治疗可及和透析前准备资料。它是主体在急性肾衰、心衰和长期肾替代治疗之前的上游储备域。

## 目录结构

```text
chronic-kidney-disease-screening-progression-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 CKD 观测、分层、进展延缓、转诊和替代治疗准备如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案实验室、尿检、血压、糖尿病、用药、影像或诊疗资料。
- 资料进入本域时必须保留观测指标、进展阶段、转诊边界、治疗负担和禁止用途。

## 上下游关系

- 上游来自 KDIGO、NIDDK、NKF 和 CKD 进展管理资料。
- 下游服务 `renal-hepatic-clearance/`、`acute-kidney-injury-renal-replacement-continuity/`、高血压和糖尿病风险建模。
- 不替代医生、肾脏科、药师、营养师、透析/移植团队或个体医疗建议。

## 维护规则

- 不写实验室解读、CKD 分期、饮食、补液、药物、透析、移植、检查排序或个体建议。
- 不把系统级 CKD 研究写成个人肾病管理工具。
- 新增变量必须区分筛查、分层、进展、保护治疗、转诊和替代治疗准备。
