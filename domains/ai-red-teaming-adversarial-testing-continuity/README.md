# AI Red Teaming Adversarial Testing Continuity

`ai-red-teaming-adversarial-testing-continuity/` 研究 AI 红队、安全测试、对抗性评估、滥用场景枚举、失效触发和缓解验证，如何保护 Human Infra 不把脆弱 AI 系统当成主体增强基础设施。

> 核心问题：AI 能提高行动密度，也能在边界条件下放大错误、欺骗、越权和滥用。红队不是攻击教程，而是让系统在进入真实任务前暴露失败模式。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI 工具持续参与研究、判断、编排和行动
  -> 高能力 AI 会带来新的失效、滥用和对抗输入面
  -> 若这些失败模式未经红队和安全测试暴露，主体会在关键任务中被工具反噬
  -> 因此 AI 红队与对抗性测试是 AI 可信部署前的失败发现域
```

## 关注对象

- 红队范围、威胁建模、滥用场景、对抗测试、安全评测、缓解措施和回归验证。
- Prompt injection、工具越权、数据泄露、越狱、欺骗、过度服从、危险能力和社工风险的治理边界。
- 红队发现如何转化为修复、policy、eval、monitoring、incident response 和 release gate。
- 与 `ai-agent-tool-permission-sandbox-continuity/` 的边界：工具权限域关注运行时权限和沙箱；本域关注测试与发现。
- 与 `cybersecurity-resilience-critical-services/` 的关系：网络安全域关注关键服务防护；本域只处理 AI 系统红队方法与结果治理。

## Human Infra 模型链路

```text
AI 红队与对抗性测试 T
  -> 改变失效样本、滥用场景、危险能力信号和缓解验证变量 X
  -> 改变 AI 工具发布、授权、限制和监控状态 S
  -> 改变越权、泄露、误导、攻击面扩张和关键任务失败风险 λ(t)
  -> 影响主体安全、任务可靠性、协作信任和未来选择权
```

## 非目标

- 不提供 jailbreak、prompt injection payload、漏洞利用、绕过防护、模型盗取或攻击步骤。
- 不生成可操作的攻击 playbook、社工话术、恶意自动化或测试规避方法。
- 不把红队报告写成“系统安全证明”；红队只能发现有限失败面。

## Source Signals

- NIST Dioptra: https://pages.nist.gov/dioptra/
- NIST AI RMF Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence-profile
- MITRE ATLAS: https://atlas.mitre.org/
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- CISA AI resources: https://www.cisa.gov/ai

## 下一步

- 建立 Red Team Source Card 字段：scope, threat model, tested capability, failure class, mitigation, retest status, residual risk。
- 与 `ai-incident-reporting-post-deployment-monitoring-continuity/` 和 `ai-agent-tool-permission-sandbox-continuity/` 建立从测试到运行监控的闭环。
