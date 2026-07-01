# wound-infection-cellulitis-sepsis-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/wound-infection-cellulitis-sepsis-continuity` |
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


`domains/c2-source-maintenance/wound-infection-cellulitis-sepsis-continuity/` 保存伤口感染、蜂窝织炎、软组织感染和脓毒症风险连续性资料。

## 职责

- 维护局部伤口感染到系统性风险之间的机制链路。
- 区分局部皮肤/软组织感染、慢性伤口感染和全身性脓毒症抢救域。
- 保留来源、证据等级、适用对象和禁止用途。

## 非目标

- 不提供诊断、抗生素、剂量、急诊判断、照片判断、培养解释或个体治疗建议。
- 不处理个人症状、图像、病历、检验结果或药物调整。

## 上游

- `skin-barrier-wound-healing/`
- `chronic-wound-venous-diabetic-pressure-ulcer-continuity/`
- `immune-maintenance/`

## 下游

- `sepsis-shock-early-recognition-resuscitation-continuity/`
- `antimicrobial-resilience/`
- `healthcare-access-continuity/`
