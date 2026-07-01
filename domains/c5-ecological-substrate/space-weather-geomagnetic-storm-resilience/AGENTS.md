# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/space-weather-geomagnetic-storm-resilience` |
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


## 职责

本目录维护空间天气、地磁暴和太阳活动对 Human Infra 的影响。重点是电网、卫星、通信、导航、时间同步和关键服务韧性。

## 文件

```text
space-weather-geomagnetic-storm-resilience/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/electric-grid-reliability-resilience-continuity/`
- `domains/c5-ecological-substrate/telecommunications-network-resilience-continuity/`
- `domains/c4-conversion-channel/geospatial-navigation-location-infrastructure/`
- `domains/c5-ecological-substrate/critical-infrastructure-lifeline-interdependency-resilience/`

## 下游

- 主体有效时间、求助能力、数据可用性和工具系统连续性。

## 边界

- 不提供实时空间天气操作建议。
- 不输出电网、卫星、航空、金融或导航系统的具体风险处置指令。
- 所有高风险结论必须回到 NOAA、NASA 或同等级权威来源。
