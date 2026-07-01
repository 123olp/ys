# advanced-nuclear-energy-safety-generation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/advanced-nuclear-energy-safety-generation-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护先进核能、安全监管与发电连续性资料。它把核能作为长期低碳可靠能源候选路径进行边界化研究。

## 目录结构

```text
advanced-nuclear-energy-safety-generation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义核能、先进反应堆、许可、安全、燃料和废物如何影响主体持续性。
- 本目录不保存核设施设计、核材料处理、安保信息、应急操作步骤、投资建议或选址建议。

## 上下游关系

- 上游来自 DOE、NRC、IAEA、OECD NEA 和公开核能监管资料。
- 下游服务能源连续性、数据中心、制造、医疗、城市韧性和低碳转型讨论。
- 不替代 `radiation-nuclear-safety-protection/`；该域关注辐射防护，本目录关注发电路径与监管约束。

## 维护规则

- 必须同时记录能源收益、安全约束、监管阶段、废物责任和尾部风险。
- 不把核能讨论写成工程方案、投资建议或安全保证。
