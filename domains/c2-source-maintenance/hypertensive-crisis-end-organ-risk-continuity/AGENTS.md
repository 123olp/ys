# hypertensive-crisis-end-organ-risk-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hypertensive-crisis-end-organ-risk-continuity` |
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


本目录维护高血压危象和急性靶器官风险资料。它是血管压力负荷进入脑、心、肾和主动脉急性损伤的研究域。

## 目录结构

```text
hypertensive-crisis-end-organ-risk-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义高血压危象如何改变卒中、心衰、AKI、主动脉事件和长期有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案血压、症状、化验、影像、药物或位置数据。
- 资料进入本域时必须区分测量、识别、靶器官评估、急性稳定和长期交接。

## 上下游关系

- 上游来自 AHA、CDC、NHLBI 和高血压 guideline materials。
- 下游服务 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/`。
- 不替代医生、急诊、心内科、肾内科、神经科或个体医疗建议。

## 维护规则

- 不写血压读数判断、降压药、剂量、家庭处理、急诊分诊、检查选择或预后建议。
- 不把系统级靶器官风险研究写成个人高血压危象判断工具。
- 新增变量必须区分慢性控制、急性危象、靶器官损伤和随访连续性。
