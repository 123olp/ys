# energy-access-resilience 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/energy-access-resilience` |
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


`energy-access-resilience/` 是 Human Infra 的能源可及与韧性域，负责研究电力、清洁烹饪、温控、通信供能和医疗设备供电如何支撑主体持续性。

## 目录结构

```text
energy-access-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义能源可及与韧性域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做能源可及、可靠性、清洁烹饪、能源负担、停电和能源韧性资料整理。
- 个体电气施工、发电设备、燃料储存、账单申请、投资和危险接线不属于本域。

## 上下游关系

- 上游：`supply-chain-continuity/`、`planetary-health-environment/`、`financial-resilience-access/`。
- 下游：`housing-built-environment-stability/`、`thermal-homeostasis-resilience/`、`healthcare-access-continuity/` 和 `emergency-preparedness-response/`。

## 维护规则

- 新增资料必须说明它影响电力可及、可靠性、清洁烹饪、能源负担、停电、医疗供电还是通信供电。
- 禁止输出危险电气、燃料、采购、补贴申请或应急供电操作建议。
