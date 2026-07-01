# pituitary-disorders-hormone-axis-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pituitary-disorders-hormone-axis-continuity` |
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


本目录维护垂体疾病、多激素轴调度、腺瘤、催乳素语境、视觉/头痛接口和长期监测资料。它关注垂体如何作为内分泌调度节点影响主体持续性。

## 目录结构

```text
pituitary-disorders-hormone-axis-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义垂体疾病如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、MRI/CT、视野、处方、病理、手术、妊娠、生育或保险资料。
- 资料进入本域时必须保留多轴调度、占位/视觉接口、长期监测、治疗后替代、复发风险和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus、内分泌、神经、眼科和垂体疾病资料。
- 下游服务 `endocrine-hormonal-regulation/`、`vision-eye-health-continuity/`、`neuro-continuity/` 和靶腺域。
- 不替代内分泌科、神经外科、眼科、放疗、药师、保险或个体医疗建议。

## 维护规则

- 不写个人 MRI/CT/视野/化验判读、垂体腺瘤判断、用药、手术、放疗、妊娠、生育或急救建议。
- 不把垂体资料写成多轴自诊、影像解释或治疗后监测流程。
- 新增资料必须区分激素分泌、激素缺乏、占位效应、视觉接口、长期替代和功能结果。
