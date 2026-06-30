# ai-red-teaming-adversarial-testing-continuity 目录说明

本目录维护 AI 红队、安全测试和对抗性评估资料。它是 AI 系统发布前暴露失败模式、约束危险能力和验证缓解措施的治理层。

## 目录结构

```text
ai-red-teaming-adversarial-testing-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 红队、安全测试、滥用场景和缓解验证如何影响主体持续性。
- 本目录只维护测试框架、分类和治理边界，不保存攻击 payload、漏洞利用细节或可复用越狱语料。
- 资料进入本域时必须保留测试范围、授权状态、缓解状态和不可公开细节。

## 上下游关系

- 上游来自 NIST Dioptra、MITRE ATLAS、OWASP LLM Top 10、NIST AI RMF 和安全治理文献。
- 下游服务 `ai-agent-tool-permission-sandbox-continuity/`、`ai-incident-reporting-post-deployment-monitoring-continuity/` 和 release gate 设计。
- 不替代 `cybersecurity-resilience-critical-services/`；该域关注一般网络安全，本目录关注 AI 系统红队。

## 维护规则

- 不记录可操作攻击步骤、越狱样例、漏洞利用或防护绕过方法。
- 不把“已红队”写成“已安全”。
- 若新增风险分类影响安全边界文档，必须同步更新 `docs/reference/ethics-and-safety-boundaries.md`。
