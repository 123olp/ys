# allergic-atopic-disease-immunologic-burden-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/allergic-atopic-disease-immunologic-burden-continuity` |
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


本目录维护过敏性疾病、特应性皮炎、食物过敏、过敏原暴露、睡眠损害和生活参与资料。它关注长期免疫负担如何消耗恢复质量和有效时间。

## 目录结构

```text
allergic-atopic-disease-immunologic-burden-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义过敏/特应性疾病免疫负担如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案皮肤照片、过敏史、食物反应、用药、学校/工作或保险资料。
- 资料进入本域时必须保留疾病类型、过敏原暴露、睡眠/瘙痒、急性反应边界、参与支持和禁止用途。

## 上下游关系

- 上游来自 NIAID、NIAMS、CDC、过敏免疫、皮肤、学校健康和环境健康资料。
- 下游服务 `immune-maintenance/`、`skin-barrier-wound-healing/` 和急性过敏反应边界模型。
- 不替代过敏免疫科、皮肤科、急诊、营养、学校健康、药学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、皮疹判断、食物挑战、脱敏、药物、肾上腺素、急救、饮食或环境改造建议。
- 不把过敏资料写成个人过敏原清单或生活限制方案。
- 新增资料必须区分长期特应性负担、急性过敏反应、环境暴露、睡眠损害和参与结果。
