# personal-automation-integration-workflow-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/personal-automation-integration-workflow-continuity` |
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
