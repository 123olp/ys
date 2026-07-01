# ai-agent-tool-permission-sandbox-continuity 目录说明

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
