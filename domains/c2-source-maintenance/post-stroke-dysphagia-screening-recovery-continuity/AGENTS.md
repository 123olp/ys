# post-stroke-dysphagia-screening-recovery-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/post-stroke-dysphagia-screening-recovery-continuity` |
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

- 维护卒中后吞咽筛查、恢复、营养入口和误吸风险链的研究边界。
- 将卒中指南、吞咽资料、康复资料和照护流程整理为 Source Card。
- 与 `cerebrovascular-stroke-brain-perfusion-resilience/`、`oropharyngeal-dysphagia-swallow-safety-continuity/` 和 `aspiration-pneumonia-airway-protection-continuity/` 保持边界清晰。

## 非目标

- 不提供卒中急救、筛查操作、训练、饮食调整、转诊判断、影像/量表解释或个人预后。
- 不替代急诊、神经、言语语言治疗、康复、营养、护理或卒中团队。

## 上游

- `cerebrovascular-stroke-brain-perfusion-resilience/`：急性脑灌注事件。

## 下游

- `rehabilitation-functioning/`：功能恢复。
- `care-transitions-discharge-followup-continuity/`：出院和随访连续性。
