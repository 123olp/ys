# api-platform-dependency-runtime-continuity 目录说明

本目录承载 API、平台依赖与运行时连续性研究域，关注第三方平台能力如何影响工具链和任务执行。

## 目录结构

```text
api-platform-dependency-runtime-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义第三方 API、SDK、限流、计费、版本废弃、SLA、降级和替代路径如何进入 Human Infra 主体持续性模型。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 NIST、CNCF/SRE 公开资料、平台状态页、API deprecation 文档和互操作治理资料。
- 不写绕过限制、规避计费、接口滥用、批量抓取、账号规避、SDK 破解或漏洞利用方法。
- 涉及 API 中断时只讨论公开状态、依赖变量、恢复模式和治理边界。
- 新增指标必须注明口径：依赖集中度、SLA、限流风险、版本废弃、替代路径、降级能力或恢复时间。
