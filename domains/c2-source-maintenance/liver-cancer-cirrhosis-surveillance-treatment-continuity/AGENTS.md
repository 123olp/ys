# liver-cancer-cirrhosis-surveillance-treatment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/liver-cancer-cirrhosis-surveillance-treatment-continuity` |
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


本目录维护肝癌、肝硬化监测、病毒性肝炎/MASLD 上游、治疗可及、肝功能储备和支持照护连续性资料。它是癌症控制与肝脏基础设施交叉的器官特异域。

## 目录结构

```text
liver-cancer-cirrhosis-surveillance-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义肝癌、肝硬化监测、上游肝病控制和肝功能储备如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案肝病史、影像、AFP、病毒指标、肝功能、病理、饮酒史或治疗资料。
- 资料进入本域时必须保留上游肝病、监测对象、异常追踪、肝功能储备、治疗窗口和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和肝癌/肝病公开资料。
- 下游服务 `cancer-control/`、病毒性肝炎、MASLD/MASH、肝肾清除和严重疾病规划建模。
- 不替代医生、肝病科、肿瘤科、介入/移植团队、感染科、营养/戒酒服务、保险服务或个体医疗建议。

## 维护规则

- 不写个人超声/AFP 判读、监测频率、肝硬化分期、肝病治疗、抗病毒/代谢治疗、介入/移植、用药或个体建议。
- 不把系统级肝癌研究写成影像/标志物解释器、治疗推荐器、移植资格判断或商业检测推广。
- 新增变量必须区分上游肝病、监测覆盖、异常追踪、肝功能储备、治疗可及、失代偿风险和公平性。
