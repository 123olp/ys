# cancer-survivorship-late-effects-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/cancer-survivorship-late-effects-continuity` |
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


本目录维护癌症幸存者晚期效应、复发恐惧、二次肿瘤、器官毒性、疲劳、工作/保险和照护转接资料。它是癌症治疗后恢复、长期治理和未来选择权重建的跨癌种域。

## 目录结构

```text
cancer-survivorship-late-effects-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义癌症幸存者晚期效应、复发恐惧、长期随访和工作/保险连续性如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案治疗史、病理、随访、症状、工作、保险、财务或心理资料。
- 资料进入本域时必须保留晚期效应、复发恐惧、二次肿瘤、器官毒性、工作/保险、照护转接和禁止用途。

## 上下游关系

- 上游来自 NCI、CDC 和癌症幸存者公开资料。
- 下游服务所有器官特异癌症域、心理健康、劳动权益、社会保护和长期恢复建模。
- 不替代医生、肿瘤科、康复团队、心理服务、保险/法律服务、雇主证明或个体医疗建议。

## 维护规则

- 不写个人随访计划、复发判断、症状诊断、晚期效应诊断、用药、康复、保险/工作证明、预后或个体建议。
- 不把系统级癌症幸存者研究写成复发预测器、保险申诉、工作能力证明或商业康复推广。
- 新增变量必须区分晚期效应、复发恐惧、二次肿瘤、器官毒性、疲劳、工作/保险、照护转接和公平性。
