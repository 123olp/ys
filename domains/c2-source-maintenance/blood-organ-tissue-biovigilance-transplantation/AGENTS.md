# blood-organ-tissue-biovigilance-transplantation 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/blood-organ-tissue-biovigilance-transplantation` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


本目录维护血液、器官、组织、生物警戒与移植系统域。它是 Human Infra 中“外部生物材料可安全进入主体系统”的公共能力层。

## 目录结构

```text
blood-organ-tissue-biovigilance-transplantation/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明血液供应、器官移植、组织安全、追踪和生物警戒如何支撑主体持续性。
- 本域只做系统、监管、质量、安全、分配和风险治理资料整理。
- 不提供个体输血、移植、器官匹配、治疗、手术、非法获取或监管规避建议。

## 维护规则

- 所有材料必须区分公共系统能力、监管要求、临床证据和个体医疗决策。
- 涉及人体材料的内容必须保留同意、分配公平、追踪、不良事件和禁止交易边界。
- 不写任何可执行采集、保存、运输、处理或手术流程。
