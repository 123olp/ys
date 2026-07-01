# augmentative-alternative-communication-aac-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/augmentative-alternative-communication-aac-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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

- 维护 AAC、表达通道冗余、设备可达、伙伴训练和主体表达权的研究边界。
- 将 AAC 工具、服务入口、维护断点和环境集成整理为 Source Card。
- 与 `assistive-technology-access/`、`aphasia-language-access-recovery-continuity/` 和 `disability-services-independent-living/` 保持边界清晰。

## 非目标

- 不提供设备处方、访问方法选择、个体评估、训练计划、保险资格、学校服务或法律判断。
- 不替代言语语言治疗、辅助技术、教育、康复、保险或法律服务。

## 上游

- `speech-language-communication-continuity/`：言语语言沟通总框架。
- `assistive-technology-access/`：辅助技术可及。

## 下游

- `patient-advocacy-shared-decision-making/`：同意和偏好表达。
- `education-access-lifelong-learning/`：课堂和学习参与。
