# vision-eye-health-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/vision-eye-health-continuity` |
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

- 维护视觉与眼健康连续性的研究边界、变量表、证据入口和禁止用途。
- 将眼健康、低视力、视觉功能、任务参与和安全风险资料整理为 Source Card、机制链和模型变量。
- 与 `sensory-continuity/`、`assistive-technology-access/`、`rehabilitation-functioning/`、`built-environment-accessibility-universal-design/` 保持边界清晰。

## 非目标

- 不提供眼科诊断、验光处方、检查解释、治疗、用药、手术、设备选择或个体资格判断。
- 不替代眼科、验光、低视力康复、职业康复或无障碍专业服务。

## 上游

- `sensory-continuity/`：跨感官输入和反馈框架。
- `healthcare-access-continuity/`：眼科服务、筛查和转诊可及性。
- `assistive-technology-access/`：低视力工具和无障碍设备可及性。

## 下游

- `transportation-access-mobility/`：视觉与安全移动、出行能力。
- `learning-skill-acquisition/`：阅读和学习入口。
- `time-allocation-effective-time/`：视觉损失造成的任务摩擦和有效时间损耗。
