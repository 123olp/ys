# pancreatic-cancer-high-risk-detection-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pancreatic-cancer-high-risk-detection-treatment-continuity` |
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


本目录维护胰腺癌高风险识别、症状/诊断延迟、治疗可及、营养/疼痛负担和照护连续性资料。它是癌症控制中高致死风险和支持照护负担最重的器官特异域之一。

## 目录结构

```text
pancreatic-cancer-high-risk-detection-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义胰腺癌高风险识别、诊断延迟、治疗、营养、疼痛和照护负担如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、影像、CA19-9、病理、遗传检测、体重、疼痛或治疗资料。
- 资料进入本域时必须保留高风险边界、诊断延迟、治疗可及、营养/疼痛负担、家庭照护和禁止用途。

## 上下游关系

- 上游来自 NCI、权威病种组织和胰腺癌公开资料。
- 下游服务 `cancer-control/`、营养、疼痛、严重疾病规划和家庭照护建模。
- 不替代医生、肿瘤科、胃肠/胰腺外科、遗传咨询、疼痛/营养团队、临床试验服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人高风险判定、症状诊断、影像/标志物解释、筛查、分期、治疗、疼痛/营养处理、临床试验选择或个体建议。
- 不把系统级胰腺癌研究写成风险计算器、影像/标志物解释器、治疗推荐器或商业检测推广。
- 新增变量必须区分高风险边界、诊断延迟、治疗可及、营养/疼痛、家庭照护和公平性。
