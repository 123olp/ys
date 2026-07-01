# ai-agent-tool-permission-sandbox-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-agent-tool-permission-sandbox-continuity` |
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


本目录维护 AI agent 工具权限、沙箱和副作用控制资料。它是 AI 从文本输出进入真实行动前的运行控制层。

## 目录结构

```text
ai-agent-tool-permission-sandbox-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义工具权限、沙箱、人类审批、日志、回滚和中止机制如何影响主体持续性。
- 本目录只维护权限与副作用控制框架，不保存凭证、token、cookie、私有日志或组织内部配置。
- 资料进入本域时必须保留工具边界、权限粒度、可逆性、审计需求和禁止用途。

## 上下游关系

- 上游来自 OWASP LLM Top 10、NIST AI RMF、CISA、MITRE ATLAS 和 agent 工具治理资料。
- 下游服务 `personal-automation-integration-workflow-continuity/`、`human-ai-oversight-handoff-accountability-continuity/` 和 AI 工具运行策略。
- 不替代 `cybersecurity-resilience-critical-services/`；该域关注一般安全，本目录关注 AI agent 工具副作用。

## 维护规则

- 不记录权限绕过、沙箱逃逸、凭证提取、prompt injection payload 或自动化滥用方法。
- 不把自动化能力写成授权结论。
- 若新增工具契约影响工具链治理文档，必须同步更新索引。
