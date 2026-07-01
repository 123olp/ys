# aspiration-pneumonia-airway-protection-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/aspiration-pneumonia-airway-protection-continuity` |
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


## 职责

- 维护误吸、口腔负荷、气道保护、肺部感染和照护流程交叉风险的研究边界。
- 将公开资料、指南和照护系统证据整理为 Source Card。
- 与 `oropharyngeal-dysphagia-swallow-safety-continuity/`、`respiratory-oxygenation/` 和 `oral-health-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、抗生素、氧疗、急救、口腔护理处方、吞咽动作或个体风险评级。
- 不替代急诊、呼吸、感染、言语语言治疗、牙科、护理或营养服务。

## 上游

- `swallowing-dysphagia-aspiration-nutrition/`：吞咽和误吸总框架。
- `oral-health-continuity/`：口腔负荷和入口健康。

## 下游

- `respiratory-oxygenation/`：呼吸氧合和肺部连续性。
- `sepsis-shock-early-recognition-resuscitation-continuity/`：严重感染风险边界。
