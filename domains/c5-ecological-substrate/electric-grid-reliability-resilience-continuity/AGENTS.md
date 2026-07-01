# Electric Grid Reliability Resilience Continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/electric-grid-reliability-resilience-continuity` |
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


本目录承载电网可靠性、韧性和服务连续性研究，关注电力生命线如何支撑医疗、通信、水务、温控、冷链、支付和数字工具。

## 目录结构

```text
electric-grid-reliability-resilience-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究电网可靠性、资源充足性、输配电资产、停电恢复、关键负荷、备用能力和韧性投资。
- 上游连接燃料、材料、天气、网络安全、公共工程和监管；下游连接医疗、水务、通信、温控、支付、冷链、交通和 AI 工具。
- 不提供调度、控制系统、设施弱点、绕供、攻击、工程设计、施工、维修、交易、采购或监管规避建议。

## 维护规则

- 电网资料只使用公开、非敏感的政策、统计、标准、韧性框架和聚合研究材料。
- 不记录可用于攻击、规避、破坏或利用电力设施的细节。
- 涉及实时停电、灾害、设备故障或公用事业服务时，只链接官方公告，不做操作指挥。
