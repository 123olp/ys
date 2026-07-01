# age-related-hearing-loss-hearing-aid-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/age-related-hearing-loss-hearing-aid-continuity` |
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

- 维护年龄相关听损与助听连续性的研究边界、变量表、证据入口和禁止用途。
- 将言语识别、助听器可及、验配维护、沟通疲劳和社会参与资料整理为 Source Card、机制链和模型变量。
- 与 `hearing-auditory-communication-continuity/`、`assistive-technology-access/`、`geriatric-care-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、听力图解释、助听器处方、设备调试、品牌/购买建议、认知判断或个体资格结论。
- 不替代听力学、耳鼻喉、验配、言语语言治疗、职业康复或公共服务无障碍专业服务。

## 上游

- `hearing-auditory-communication-continuity/`：听觉沟通总框架。
- `assistive-technology-access/`：辅助设备可及性、维护和适配。
- `aging-frailty-resilience/`：晚年功能、孤立和照护背景。

## 下游

- `social-connection-relational-infra/`：关系参与和孤立风险。
- `medical-interpreter-cultural-mediation/`：医疗沟通安全。
- `time-allocation-effective-time/`：沟通重复和疲劳成本。
