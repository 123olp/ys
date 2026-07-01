# api-platform-dependency-runtime-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/api-platform-dependency-runtime-continuity` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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
