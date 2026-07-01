# road-traffic-injury-prevention-safe-mobility 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/road-traffic-injury-prevention-safe-mobility` |
| 所属层级 | `C6` - 局部可能性解锁层 |
| 父级容器 | `domains/c6-local-unlocking` |
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


本目录维护道路交通伤害预防与安全移动域。它是 Human Infra 的“安全移动层”，负责道路系统如何支持出行而不把移动转化为死亡和失能风险。

## 目录结构

```text
road-traffic-injury-prevention-safe-mobility/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明道路交通伤害、安全系统、速度管理、车辆安全、交通数据和安全移动如何影响主体持续性。
- 本域只做公开道路安全、伤害预防、交通系统治理和安全移动资料整理。
- 不提供驾驶、路线、事故责任、保险、法律、车辆改装、危险驾驶、规避执法或急救建议。

## 维护规则

- 新增材料必须区分交通可达性、道路安全、车辆安全、执法、应急医疗和城市设计。
- 不把事故数据或交通安全资料写成个人路线、驾驶或法律建议。
- 涉及事故现场、执法或车辆技术时，只写系统治理，不写操作步骤。
