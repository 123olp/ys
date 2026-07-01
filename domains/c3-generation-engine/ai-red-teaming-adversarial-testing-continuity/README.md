# AI Red Teaming Adversarial Testing Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-red-teaming-adversarial-testing-continuity` |
| 分级 | `C3` - 可能性生成引擎层 |
| 控制轴 | 主体能力生成 |
| 分级理由 | 关键词显示该域主要增强认知、学习、工具、AI、技能或沟通能力。 |
| 复核状态 | `heuristic-v0.1` |

### Human Infra 追问

这个域如何放大主体生成新路径的能力，例如认知、学习、注意力、记忆、AI、工具和反馈复利？

```text
研究域对象
  -> 影响变量 / 中间机制
  -> 改变主体状态或外部条件
  -> 改变风险、能力、时间成本或可达性
  -> 改变有效寿命、有效时间或未来选择权
```

### 使用边界

- 本域是研究与建模单元，不是个体医疗、法律、金融、工程、教育或安全操作建议。
- 新增内容必须标明来源、适用对象、证据等级和不确定性；AI 总结不能作为事实源。
- 若内容会改变分级、目录位置或上下游关系，先更新 `domains/_possibility-space-control/classification.tsv`。
<!-- domain-standard:end -->

<!-- domain-research-skeleton:start -->
## 研究推进骨架

### 最小问题集

- 界定被放大的通用能力资源：智力、注意力、记忆、学习、判断、执行、反馈或工具使用。
- 说明任务链路：能力变化如何改变问题求解、行动质量、创造密度或学习轮次。
- 识别复利结构：能力增强、工具采用、协作网络、经验积累和自我升级如何互相强化。
- 记录依赖条件：AI、数据、界面、训练、外部工具、社会支持或反馈系统。
- 列出误用、过载、依赖、幻觉、注意力破坏、人格边界和安全风险。

### 变量接口

- 输入变量：本域直接处理的对象、资源、技术、环境、制度或状态。
- 中间机制：变量通过什么因果路径改变主体状态、系统状态或外部条件。
- 状态改变：身体、认知、能力、资源、风险暴露、可及性、时间成本或协作条件如何变化。
- 风险 / 成本函数：死亡风险、失能风险、工程风险、尾部风险、机会成本、维护成本或治理成本如何变化。
- 输出指标：有效寿命、健康寿命、有效时间、主观时间、相对时间、行动能力、恢复能力或未来选择权。

### 证据入口

- 官方 / 原始资料：监管文件、数据库、临床登记、标准、论文原文、项目白皮书或一手报告。
- 综述 / 指南 / 标准：系统综述、领域指南、技术标准、伦理规范和权威机构材料。
- 数据集 / 登记系统：可复核的数据表、代码、实验记录、登记号、版本和采集边界。
- 反例 / 失败案例：负结果、副作用、安全事故、不可复现结果、伦理争议和误用案例。

### 最小产出

- Source Signals：记录候选资料、来源、日期、主张和待核验点。
- Source Cards：提取 claim、变量、机制、证据类型、边界、反证条件和可迁移位置。
- Claim-Evidence Matrix：把每个稳定主张绑定到来源、证据等级、适用范围和不确定性。
- 变量表：列出输入变量、中间变量、状态变量、风险变量、输出指标和可观测代理指标。
- 上下游关系：说明本域依赖哪些更根本域，并向哪些转化、应用或基础设施域输出。
<!-- domain-research-skeleton:end -->

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
