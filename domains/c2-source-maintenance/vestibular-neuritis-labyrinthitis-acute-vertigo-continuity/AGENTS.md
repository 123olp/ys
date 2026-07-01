# vestibular-neuritis-labyrinthitis-acute-vertigo-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vestibular-neuritis-labyrinthitis-acute-vertigo-continuity` |
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

- 维护急性前庭神经炎、迷路炎、急性眩晕、步态不稳和恢复窗口的研究边界。
- 将急性空间稳定失败、照护需求、工作中断和前庭补偿资料整理为 Source Card。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/` 保持急性危险信号边界清晰。

## 非目标

- 不提供诊断、卒中排除、眼震解释、药物、康复动作、急诊判断或个人风险分级。
- 不替代急诊、耳鼻喉、神经、前庭康复或物理治疗服务。

## 上游

- `vestibular-balance-spatial-orientation/`：前庭和平衡总框架。
- `emergency-preparedness-response/`：急性求助和安全响应。

## 下游

- `care-transitions-discharge-continuity/`：急性发作后的转接。
- `rehabilitation-functioning/`：恢复和功能重建。
