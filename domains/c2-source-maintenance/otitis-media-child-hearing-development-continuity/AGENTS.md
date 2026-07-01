# otitis-media-child-hearing-development-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/otitis-media-child-hearing-development-continuity` |
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

- 维护儿童中耳炎与听觉语言发展连续性的研究边界、变量表、证据入口和禁止用途。
- 将耳痛、反复感染、积液、暂时性听损、睡眠、语言发展和家庭照护资料整理为 Source Card、机制链和模型变量。
- 与 `newborn-hearing-screening-language-development-continuity/`、`hearing-auditory-communication-continuity/`、`antimicrobial-resilience/` 保持边界清晰。

## 非目标

- 不提供诊断、抗生素/滴耳液建议、鼓膜或听力检查解释、手术建议、返校判断或家长个体处置。
- 不替代儿科、耳鼻喉、听力学、学校健康、早期干预或抗菌药物管理服务。

## 上游

- `maternal-newborn-child-development/`：儿童发展和家庭照护背景。
- `hearing-auditory-communication-continuity/`：听觉沟通总框架。
- `healthcare-access-continuity/`：儿科和耳鼻喉服务可及性。

## 下游

- `speech-language-communication-continuity/`：语言发展和表达参与。
- `education-access-lifelong-learning/`：课堂参与和学习入口。
- `family-caregiver-respite-work-continuity/`：家庭照护时间和工作影响。
