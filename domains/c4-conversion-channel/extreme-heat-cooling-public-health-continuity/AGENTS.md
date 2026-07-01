# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/extreme-heat-cooling-public-health-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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

本目录维护极端高温、制冷可及和公共卫生连续性对 Human Infra 的影响。重点是热健康、能源、住房、劳动、睡眠、城市热岛和公平风险。

## 文件

```text
extreme-heat-cooling-public-health-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c2-source-maintenance/thermal-homeostasis-resilience/`
- `domains/c5-ecological-substrate/energy-access-resilience/`
- `domains/c5-ecological-substrate/housing-built-environment-stability/`
- `domains/c6-local-unlocking/occupational-exposure-industrial-hygiene/`
- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`

## 下游

- 有效时间、睡眠恢复、工作安全、公共卫生应急和社区韧性。

## 边界

- 不输出个人急救、补水、药物调整、空调选择或工作许可建议。
- 不替代 CDC、NOAA、OSHA、地方公共卫生或职业安全机构。
- 所有材料只做域建模、证据整理和风险边界说明。
