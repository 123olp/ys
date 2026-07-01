# sepsis-shock-early-recognition-resuscitation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/sepsis-shock-early-recognition-resuscitation-continuity` |
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


本目录维护脓毒症、感染性休克、早期识别和急性复苏资料。它是感染风险进入多器官失效和急性死亡边界的研究域。

## 目录结构

```text
sepsis-shock-early-recognition-resuscitation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义脓毒症和休克如何改变急性死亡、恢复能力和长期有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案实验室、培养、生命体征、药物或 ICU 资料。
- 资料进入本域时必须保留病程阶段、系统层级、时间窗、结局指标、证据强度和禁止用途。

## 上下游关系

- 上游来自 Surviving Sepsis Campaign、CDC、WHO、SCCM 和感染控制资料。
- 下游服务 `antimicrobial-resilience/`、`clinical-laboratory-diagnostic-quality/` 和 ICU 器官支持建模。
- 不替代医生、急诊、ICU、感染科、医院路径、公共卫生机构或个体医疗建议。

## 维护规则

- 不写抗生素、液体、升压药、源控制或 ICU 转诊建议。
- 不把系统性风险研究写成个人 triage 或治疗工具。
- 新增变量必须区分早识别、复苏、器官支持和恢复后负担。
