# Urban Planning Land Use Zoning Resilience

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/urban-planning-land-use-zoning-resilience` |
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


本目录承载城市规划、土地使用和空间治理研究，关注空间结构如何决定资源可达、风险暴露和有效时间。

## 目录结构

```text
urban-planning-land-use-zoning-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究城市规划、土地使用、分区、密度、混合功能、服务布局、公共空间、风险避让和空间公平。
- 上游连接法律制度、公共参与、灾害风险和基础设施投资；下游连接住房、交通、医疗、食物、教育、工作和社会连接。
- 不提供个案购房、选址、地产投资、审批、规划诉讼、政治游说、许可规避或项目操作建议。

## 维护规则

- 城市规划资料必须标明尺度：街区、城市、区域、国家或全球比较。
- 不把规划指标写成具体地产、开发、审批、法律或投资结论。
- 涉及分区、许可、住房开发和公共争议时，只保留公共研究材料和边界说明。
