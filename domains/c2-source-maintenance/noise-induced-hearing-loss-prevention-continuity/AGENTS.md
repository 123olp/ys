# noise-induced-hearing-loss-prevention-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/noise-induced-hearing-loss-prevention-continuity` |
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

- 维护噪声性听损预防连续性的研究边界、变量表、证据入口和禁止用途。
- 将噪声暴露、听力保护、职业监测、耳鸣、沟通疲劳和工作安全资料整理为 Source Card、机制链和模型变量。
- 与 `hearing-auditory-communication-continuity/`、`noise-exposure-acoustic-environment-continuity/`、`occupational-exposure-industrial-hygiene/` 保持边界清晰。

## 非目标

- 不提供个人诊断、听力图解释、防护设备处方、职业合规判断、赔偿资格、法律索赔或工作许可建议。
- 不替代听力学、职业卫生、雇主听力保护计划、监管机构或法律专业服务。

## 上游

- `noise-exposure-acoustic-environment-continuity/`：声环境和噪声暴露总框架。
- `occupational-exposure-industrial-hygiene/`：职业暴露控制和监测。
- `hearing-auditory-communication-continuity/`：听觉沟通总框架。

## 下游

- `workplace-safety-operational-risk/`：职业安全和事故风险。
- `age-related-hearing-loss-hearing-aid-continuity/`：长期听损后的助听路径。
- `time-allocation-effective-time/`：听觉疲劳和沟通摩擦。
