# hearing-assistive-devices-alerting-access-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/hearing-assistive-devices-alerting-access-continuity` |
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

- 维护听觉辅助设备与警报接入连续性的研究边界、变量表、证据入口和禁止用途。
- 将提示系统、辅助听觉设备、电话/会议/课堂接入、灾害警报、维护互操作和公共服务可访问资料整理为 Source Card、机制链和模型变量。
- 与 `hearing-auditory-communication-continuity/`、`assistive-technology-access/`、`built-environment-accessibility-universal-design/` 保持边界清晰。

## 非目标

- 不提供设备处方、安装设计、产品推荐、合规判断、保险/ADA/学校/工作资格或个人安全系统建议。
- 不替代听力学、无障碍设计、消防安全、学校/雇主合理便利、公共服务机构或设备厂商支持。

## 上游

- `hearing-auditory-communication-continuity/`：听觉沟通总框架。
- `assistive-technology-access/`：辅助技术可及性和维护。
- `emergency-alert-warning-communication/`：警报和风险沟通。

## 下游

- `housing-built-environment-stability/`：居家警报和独立生活。
- `education-access-lifelong-learning/`：课堂沟通和辅助听觉系统。
- `healthcare-language-interpreter-effective-communication-continuity/`：医疗有效沟通。
