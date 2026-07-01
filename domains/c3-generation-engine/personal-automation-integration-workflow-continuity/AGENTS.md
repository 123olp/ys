# personal-automation-integration-workflow-continuity 目录说明

本目录承载个人自动化、集成与工作流连续性研究域，关注跨应用自动化如何降低任务摩擦并保持可见、可控、可恢复。

## 目录结构

```text
personal-automation-integration-workflow-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义触发器、动作、webhook、OAuth、脚本、低代码集成、日志和人工中止如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 OpenAPI、OAuth、平台公开 webhook/status/deprecation 文档和可靠性工程资料。
- 不写绕过限制、规避计费、批量滥用、凭证窃取、刷量、垃圾提交或安全攻击方法。
- 涉及自动化方案时只讨论变量、失败模式、权限最小化、日志和人工覆盖边界。
- 新增指标必须注明口径：触发成功率、重复提交率、权限范围、失败可见性、人工中止、平台锁定或恢复时间。
