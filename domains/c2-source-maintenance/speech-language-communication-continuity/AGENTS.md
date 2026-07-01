# speech-language-communication-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/speech-language-communication-continuity` |
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

- 维护言语、语言、沟通参与和辅助沟通连续性的研究边界、证据入口、变量表和禁止用途。
- 将失语、构音障碍、言语运动障碍、沟通康复、共同决策和主体表达权资料整理为 Source Card。
- 与 `language-access-plain-communication/`、`medical-interpreter-cultural-mediation/`、`patient-advocacy-shared-decision-making/`、`assistive-technology-access/` 保持边界清晰。

## 非目标

- 不提供诊断、治疗训练、设备处方、个体康复计划、吞咽处置或临床资格判断。
- 不替代言语语言治疗、神经、康复、教育、心理或法律同意专业判断。

## 上游

- `neuro-continuity/`：神经、意识、记忆和主体身份连续性。
- `cerebrovascular-stroke-brain-perfusion-resilience/`：卒中后沟通断点。
- `traumatic-brain-injury-neurotrauma-recovery/`：TBI 后沟通和认知语言问题。

## 下游

- `patient-advocacy-shared-decision-making/`：偏好表达和共同决策。
- `social-connection-relational-infra/`：关系和社会参与。
- `public-service-design-accessibility/`：服务沟通入口与替代沟通支持。
