# Critical Infrastructure Lifeline Interdependency Resilience

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/critical-infrastructure-lifeline-interdependency-resilience` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录承载关键基础设施生命线互依赖和级联故障研究，关注多部门基础设施如何共同支撑主体持续性。

## 目录结构

```text
critical-infrastructure-lifeline-interdependency-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究能源、水务、通信、交通、医疗、食品、金融、政府和应急系统之间的依赖关系、级联故障、恢复优先级和跨部门协调。
- 上游连接单部门基础设施域、应急管理、公共行政和风险工程；下游连接医疗、资源、移动、支付、身份、通信和救援连续性。
- 不提供敏感设施清单、漏洞、攻击路径、绕行策略、安保规避、实时指挥或内部恢复计划。

## 维护规则

- 只使用公开、聚合、制度层面的关键基础设施韧性材料。
- 不记录可用于攻击、破坏、操控恢复优先级或利用互依赖弱点的细节。
- 涉及真实事件时，只做公开资料索引和结构化学习，不做现场行动建议。
