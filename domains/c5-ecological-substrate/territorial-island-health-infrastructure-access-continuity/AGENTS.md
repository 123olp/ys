# territorial-island-health-infrastructure-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/territorial-island-health-infrastructure-access-continuity` |
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


本目录维护属地、岛屿与离岸地区健康基础设施可达连续性域。它是 Human Infra 的“离岸地理和制度边界”层，负责岛屿医疗、药品、电力、水、宽带、灾害、转诊和财政规则如何影响主体持续性。

## 目录结构

```text
territorial-island-health-infrastructure-access-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明属地和岛屿医疗基础设施、供应链、转诊、灾害恢复、公共卫生和财政规则如何影响主体持续性。
- 本域只做公开属地/岛屿健康基础设施、公共卫生、Medicaid/CHIP、供应链和灾害资料整理。
- 不提供个体医疗、保险、转诊、旅行、移居、撤离、救灾申请、物流、政治地位或法律建议。

## 维护规则

- 新增材料必须区分医疗容量、转诊供应链、能源水宽带、灾害恢复、公共卫生和财政规则。
- 不把岛屿社区写成地区污名、商业套利、实时资源判断或政治判断入口。
- 涉及灾害、医疗、保险和转诊服务时，只写结构性资料，不写个体操作建议。
