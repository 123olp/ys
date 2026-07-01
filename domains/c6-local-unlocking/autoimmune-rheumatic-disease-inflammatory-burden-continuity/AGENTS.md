# autoimmune-rheumatic-disease-inflammatory-burden-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/autoimmune-rheumatic-disease-inflammatory-burden-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


本目录维护自身免疫风湿病、慢性炎症、免疫抑制、器官损害和照护连续性资料。它关注免疫系统失衡如何长期消耗行动能力和恢复能力。

## 目录结构

```text
autoimmune-rheumatic-disease-inflammatory-burden-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义自身免疫风湿病炎症负担如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、药物、感染、生育或保险资料。
- 资料进入本域时必须保留疾病类型、活动度、器官受累、药物风险、感染风险和禁止用途。

## 上下游关系

- 上游来自 NIAMS、CDC、风湿免疫、药物安全和慢病照护资料。
- 下游服务 `immune-maintenance/`、`multimorbidity-polypharmacy-care-coordination/` 和感染风险模型。
- 不替代风湿免疫科、药学、感染科、肾脏科、产科、残障、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、化验判读、免疫抑制用药、疫苗、妊娠、感染处理、检查周期或 flare 建议。
- 不把疾病活动证据写成个体治疗调整流程。
- 新增资料必须区分炎症负担、器官损害、治疗风险、感染风险、疲劳和功能结果。
