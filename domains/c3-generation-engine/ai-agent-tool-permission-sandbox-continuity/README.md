# AI Agent Tool Permission Sandbox Continuity

<!-- domain-standard:start -->
## 标准域信息

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-agent-tool-permission-sandbox-continuity` |
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


`ai-agent-tool-permission-sandbox-continuity/` 研究 AI agent 的工具调用、权限边界、沙箱、审批、人类确认、审计日志和中止机制，如何决定 AI 从“回答者”变成“行动者”后是否仍可控。

> 核心问题：AI 一旦能调用工具，就能改变文件、账户、数据、资金、基础设施和现实流程。主体增强的关键不是让 agent 更自由，而是让每个行动有权限、边界和可回滚性。

## 先验位置

```text
有效永生 / 主体持续性最大化
  -> 需要 AI agent 代理信息处理、自动化、工具编排和重复任务
  -> 工具调用把模型输出转化为真实副作用
  -> 权限过宽、沙箱不足、审批缺失和日志不可审查会把增强变成失控
  -> 因此 AI agent 工具权限与沙箱是 AI 行动能力的控制边界域
```

## 关注对象

- Tool permission、capability token、least privilege、sandbox、dry run、human approval、rollback 和 audit log。
- 文件、网络、浏览器、终端、数据库、支付、邮件、日历、代码仓库和第三方 API 的工具边界。
- Prompt injection 到 tool execution 的跨层风险、凭证隔离、输出验证、调用预算和中止条件。
- 与 `personal-automation-integration-workflow-continuity/` 的关系：个人自动化域关注日常工作流；本域关注 AI agent 的权限与副作用控制。
- 与 `ai-red-teaming-adversarial-testing-continuity/` 的边界：红队域关注测试发现；本域关注运行时权限设计。

## Human Infra 模型链路

```text
AI agent 工具权限与沙箱 T
  -> 改变权限粒度、工具边界、审批、日志、回滚和中止变量 X
  -> 改变 AI 行动系统的可控性、可审查性和副作用状态 S
  -> 改变越权、数据泄露、误操作、不可逆执行和自动化事故风险 λ(t)
  -> 影响主体有效时间、任务自动化收益、资源安全和未来选择权
```

## 非目标

- 不提供权限绕过、凭证提取、工具逃逸、沙箱逃逸、prompt injection payload 或自动化滥用方法。
- 不保存 API key、token、cookie、私有日志、账号资料或组织内部权限配置。
- 不把“agent 能做”写成“agent 应该做”，也不把自动化替代人工责任。

## Source Signals

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF Generative AI Profile: https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence-profile
- CISA AI resources: https://www.cisa.gov/ai
- MITRE ATLAS: https://atlas.mitre.org/

## 下一步

- 建立 Agent Tool Contract 字段：tool, permission, side effect, approval gate, sandbox, audit log, rollback, abort condition。
- 与 `human-ai-oversight-handoff-accountability-continuity/`、`ai-red-teaming-adversarial-testing-continuity/` 和 `personal-automation-integration-workflow-continuity/` 建立运行边界。
