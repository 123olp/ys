# weather-climate-observation-forecasting 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/weather-climate-observation-forecasting` |
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


本目录承载 Human Infra 中“天气气候观测与预报”研究域。

## 结构

```text
weather-climate-observation-forecasting/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义天气气候观测、预报和气候服务如何进入主体持续性模型。
- 本目录只做公开资料、变量、风险链路和来源治理，不放实时预报服务、灾害指挥或个体撤离建议。

## 上下游关系

- 上游：`docs/reference/research-domain-atlas.md`、`planetary-health-environment/`、`risk-engineering/`。
- 下游：`emergency-alerts-communications/`、`household-emergency-preparedness-resilience/`、`disaster-recovery-relief-continuity/`、`energy-access-resilience/`、`transportation-access-mobility/`。

## 维护规则

- 公开结论必须回到官方气象、气候、预警或科研数据来源。
- 不把模型预测写成确定事件，不输出个人安全承诺。
- 涉及实时危险天气时，只指向官方来源和安全边界，不给现场操作指令。
