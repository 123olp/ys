# newborn-hearing-screening-language-development-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/newborn-hearing-screening-language-development-continuity` |
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

- 维护新生儿听力筛查与语言发展连续性的研究边界、变量表、证据入口和禁止用途。
- 将筛查、诊断确认、早期干预、家庭服务、语言输入和发展终点整理为 Source Card、机制链和模型变量。
- 与 `maternal-newborn-child-development/`、`hearing-auditory-communication-continuity/`、`speech-language-communication-continuity/` 保持边界清晰。

## 非目标

- 不提供诊断、筛查结果解释、设备选择、干预方案、语言路线、预后、学校安排、福利资格或家庭个体决策。
- 不替代儿科、听力学、早期干预、言语语言治疗、公共卫生项目或家庭支持服务。

## 上游

- `maternal-newborn-child-development/`：新生儿和儿童发展总框架。
- `public-health-screening-prevention/`：筛查项目和转诊框架。
- `hearing-auditory-communication-continuity/`：听觉沟通总框架。

## 下游

- `speech-language-communication-continuity/`：语言表达与理解。
- `education-access-lifelong-learning/`：学校准备和学习入口。
- `family-caregiver-respite-work-continuity/`：家庭服务导航和照护负担。
