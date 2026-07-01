# cushing-syndrome-hypercortisolism-metabolic-bone-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cushing-syndrome-hypercortisolism-metabolic-bone-continuity` |
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


本目录维护库欣综合征、高皮质醇、代谢、骨骼肌肉、情绪认知、感染风险和恢复连续性资料。它关注激素过量如何把多个系统同时推向长期负荷。

## 目录结构

```text
cushing-syndrome-hypercortisolism-metabolic-bone-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义库欣综合征如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、处方、照片、手术、病理、血压血糖、骨密度或保险资料。
- 资料进入本域时必须保留高皮质醇来源、代谢骨骼负担、恢复/复发、污名风险和禁止用途。

## 上下游关系

- 上游来自 NIDDK、MedlinePlus、内分泌、代谢、骨骼和心理健康资料。
- 下游服务 `endocrine-hormonal-regulation/`、`metabolic-energy-homeostasis/`、`musculoskeletal-integrity/` 和情绪认知模型。
- 不替代内分泌科、神经外科、肾上腺/垂体专科、药师、心理健康、保险或个体医疗建议。

## 维护规则

- 不写个人检查解释、病因定位、影像判读、用药、手术、放疗、激素调整、减重或骨骼治疗建议。
- 不把库欣资料写成外貌诊断、减肥路径、用药调整或术后管理方案。
- 新增资料必须区分病因语境、代谢负荷、骨骼肌肉影响、情绪认知影响、恢复/复发和功能结果。
