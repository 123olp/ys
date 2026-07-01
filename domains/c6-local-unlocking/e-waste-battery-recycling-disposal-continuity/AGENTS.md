# e-waste-battery-recycling-disposal-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/e-waste-battery-recycling-disposal-continuity` |
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


本目录承载电子废弃物与电池回收处置连续性研究域，关注带电设备退役后如何避免火灾、毒性、数据和材料浪费风险。

## 目录结构

```text
e-waste-battery-recycling-disposal-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义电子废弃物、电池、设备退役、回收路径、数据残留和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CPSC、地方回收项目、制造商/零售 take-back 和消防安全资料。
- 不写电池拆解、刺穿、放电、改装、维修、数据擦除保证、危险运输或损坏电池处理步骤。
- 新增指标必须注明口径：设备类型、电池类型、退役状态、回收路径、火灾风险、隐私风险或材料循环结果。
- 涉及热失控、膨胀电池、医疗/辅助设备电池或灾后损坏设备时，必须保留消防和专业转介边界。
