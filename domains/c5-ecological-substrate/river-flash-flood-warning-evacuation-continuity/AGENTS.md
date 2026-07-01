# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/river-flash-flood-warning-evacuation-continuity` |
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

本目录维护河流洪水、山洪、道路淹没、洪水预警、撤离避难和灾后返回对主体持续性的影响。重点是从官方警报到人类行动的执行链，不做实时路线或水文调度。

## 文件

```text
river-flash-flood-warning-evacuation-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/weather-climate-observation-forecasting/`
- `domains/c5-ecological-substrate/emergency-alerts-communications/`
- `domains/c5-ecological-substrate/water-resources-hydrology-flood-drought-management/`
- `domains/c5-ecological-substrate/household-emergency-preparedness-resilience/`

## 下游

- `domains/c5-ecological-substrate/disaster-recovery-relief-continuity/`
- `domains/c5-ecological-substrate/post-flood-mold-moisture-indoor-recovery-continuity/`
- `domains/c5-ecological-substrate/flood-insurance-nfip-claims-continuity/`

## 边界

- 不输出实时预警、行车路线、涉水判断、撤离点选择或房屋返回建议。
- 不替代 NWS/NOAA、FEMA、地方应急管理、水文、交通或公共安全机构。
- 内容只做研究域建模、资料索引、证据边界和禁止用途维护。
