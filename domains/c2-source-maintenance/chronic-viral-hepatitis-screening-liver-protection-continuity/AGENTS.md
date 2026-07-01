# chronic-viral-hepatitis-screening-liver-protection-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/chronic-viral-hepatitis-screening-liver-protection-continuity` |
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


本目录维护慢性乙肝、丙肝筛查、确认、治疗连接、肝脏保护和肝癌风险监测资料。它是感染控制、肝脏清除和癌症预防之间的执行域。

## 目录结构

```text
chronic-viral-hepatitis-screening-liver-protection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义病毒性肝炎筛查和肝脏风险控制如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、病毒载量、影像、药物、暴露或身份资料。
- 资料进入本域时必须保留感染类型、筛查对象、确认路径、治疗连接、监测边界和禁止用途。

## 上下游关系

- 上游来自 CDC、USPSTF、肝病和公共卫生资料。
- 下游服务 `renal-hepatic-clearance/`、`chronic-infectious-disease-care-continuity/` 和肝癌风险建模。
- 不替代肝病专科、感染科、公共卫生、疫苗服务、药师或个体医疗建议。

## 维护规则

- 不写个人检测判读、抗病毒药物、剂量、疫苗建议、肝癌监测安排、家庭传播处理或治疗建议。
- 不收集或推断敏感感染、性行为、注射暴露、身份或保险资料。
- 新增资料必须区分筛查、确认、分期、治疗连接、随访、监测和预防接口。
