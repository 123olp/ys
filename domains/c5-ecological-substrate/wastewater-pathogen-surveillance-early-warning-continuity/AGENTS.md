# wastewater-pathogen-surveillance-early-warning-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/wastewater-pathogen-surveillance-early-warning-continuity` |
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


`domains/c5-ecological-substrate/wastewater-pathogen-surveillance-early-warning-continuity/` 是 Human Infra 的污水病原体监测与早期预警连续性域，负责把社区级污水信号建模为暴发预警基础设施。

## 目录结构

```text
wastewater-pathogen-surveillance-early-warning-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义污水病原体监测、趋势信号、早期预警、社区聚合、隐私边界和风险沟通的对象、链路、非目标和来源信号。
- 本域只整理公开公共卫生监测资料、变量模型和边界。
- 采样教程、设施定位、个体结果解释、社区点名、污名化、恐慌传播和水务设施操作不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/` 和 `water-wastewater-utility-service-continuity/`。
- 下游：`community-testing-screening-access-continuity/`、`school-workplace-outbreak-operations-continuity/`、`healthcare-surge-triage-capacity-continuity/` 和 `risk-engineering/`。

## 维护规则

- 新增资料必须说明它支持采样覆盖、趋势信号、早期预警、聚合隐私、公共卫生触发器还是风险沟通。
- 不能输出采样操作、设施定位、个体诊断、社区污名化、恐慌传播或规避监测内容。
