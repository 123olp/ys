# captions-relay-service-communication-access-continuity AGENTS

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/captions-relay-service-communication-access-continuity` |
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

- 维护字幕、中继服务与沟通访问连续性的研究边界、变量表、证据入口和禁止用途。
- 将字幕、实时转写、电话/视频中继、会议可访问性、准确性、延迟和隐私资料整理为 Source Card、机制链和模型变量。
- 与 `hearing-auditory-communication-continuity/`、`language-access-plain-communication/`、`healthcare-language-interpreter-effective-communication-continuity/` 保持边界清晰。

## 非目标

- 不提供法律合规判断、平台采购、字幕质量认证、翻译解释、手语服务安排、个人便利资格或诉讼策略。
- 不替代无障碍合规、听力学、法律、教育、医疗沟通、公共服务或平台安全专业判断。

## 上游

- `hearing-auditory-communication-continuity/`：听觉沟通总框架。
- `language-access-plain-communication/`：语言可达和清晰沟通。
- `digital-accessibility-assistive-design/`：数字可访问性和平台接口。

## 下游

- `healthcare-language-interpreter-effective-communication-continuity/`：医疗有效沟通。
- `court-language-access-interpreter-continuity/`：法律/法院沟通访问。
- `remote-hybrid-court-hearing-access-continuity/`：远程会议和程序参与。
