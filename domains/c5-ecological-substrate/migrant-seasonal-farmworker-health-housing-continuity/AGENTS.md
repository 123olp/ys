# migrant-seasonal-farmworker-health-housing-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/migrant-seasonal-farmworker-health-housing-continuity` |
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


本目录维护迁徙与季节性农业工人健康、住房和劳动连续性域。它是 Human Infra 的“季节性劳动-居住-服务链条”层，负责农业工作暴露、迁移、住房、交通、语言、劳动权利和医疗可达如何影响主体持续性。

## 目录结构

```text
migrant-seasonal-farmworker-health-housing-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明农业工人劳动、住房、交通、语言、职业暴露和医疗服务可达如何影响主体持续性。
- 本域只做公开农业工人健康、职业暴露、劳动权利、住房、迁移和家庭服务资料整理。
- 不提供个体医疗、移民、劳动纠纷、举报、工资追索、住房、交通、法律或现场处置建议。

## 维护规则

- 新增材料必须区分职业暴露、住房依赖、交通依赖、语言入口、劳动权利、医疗随访和家庭支持。
- 不把农业工人差异写成身份推断、风险定位、执法线索或商业开发机会。
- 涉及医疗、劳动、移民和住房服务时，只写结构性资料，不写个体操作建议。
