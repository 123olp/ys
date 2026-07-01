# Personal Automation Integration Workflow Continuity

`personal-automation-integration-workflow-continuity` 研究个人自动化、低代码/无代码集成、脚本、触发器、动作、webhook、OAuth 授权、API 连接和工作流编排如何影响主体是否能把重复任务交给可靠工具链。

> 核心问题：自动化能降低重复成本，也会制造新的隐形依赖；触发器失效、权限过期或平台政策变化会让任务在无声中中断。

## 关注对象

- 触发器、动作、webhook、OAuth scopes、API token、低代码平台、脚本、定时任务、同步任务和错误通知。
- 个人自动化、家庭自动化、资料整理、账单/表单流程、研究资料流、任务分派和跨应用连接。
- 幂等、重试、日志、权限最小化、人工确认、失败恢复、平台退出和自动化债务。
- 隐私泄露、越权授权、无限循环、重复提交、平台锁定、限流、费用失控和无人监控自动化。

## Human Infra 链路

```text
个人自动化与工作流连续
  -> 重复任务、跨应用传递和低价值操作可被可靠编排
  -> 人工摩擦、遗忘、重复输入和流程断点下降
  -> 主体释放有效时间和注意力，并保留失败可见性与人工中止权
  -> 任务吞吐、恢复能力和长期项目维护能力增强
```

## 非目标

- 不提供绕过平台限制、规避计费、批量滥用、凭证窃取、自动化刷量、垃圾提交或安全攻击方法。
- 不替代平台工程、SRE、安全、法律、隐私、采购或合规审查。
- 不收集 API key、OAuth token、私有 webhook、自动化日志、账号数据或敏感工作流。

## Source Signals

- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- OAuth 2.0 RFC 6749: https://www.rfc-editor.org/rfc/rfc6749
- W3C Web of Things and automation-adjacent integration references.
- Platform public docs for webhook, status, rate limit and deprecation signals.

## 下一步

- 建立 `trigger -> authorization -> action -> idempotency -> logging -> human override -> recovery` 变量表。
- 区分个人自动化、家庭自动化、研究自动化、业务流程自动化和公共服务自动化。
- 与 `api-platform-dependency-runtime-continuity`、`cloud-service-exit-interoperability-continuity`、`notification-alert-routing-attention-continuity` 和 `ai-agency-safety` 建立边界。
