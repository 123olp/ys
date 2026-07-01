# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/tsunami-warning-coastal-evacuation-continuity` |
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

本目录维护海啸预警、沿海撤离和灾后恢复对主体持续性的影响。重点是预警触达、撤离可达性、无障碍、沿海基础设施和恢复链条。

## 文件

```text
tsunami-warning-coastal-evacuation-continuity/
├── AGENTS.md
└── README.md
```

## 上游

- `domains/c5-ecological-substrate/emergency-alerts-communications/`
- `domains/c5-ecological-substrate/coastal-marine-resilience-blue-economy-continuity/`
- `domains/c5-ecological-substrate/transportation-access-mobility/`
- `domains/c5-ecological-substrate/disaster-recovery-relief-continuity/`

## 下游

- 沿海社区生命安全、撤离窗口、灾后服务恢复和长期空间规划。

## 边界

- 不输出实时预警、撤离路线、避难点或个人风险判断。
- 不替代 NOAA、地方应急管理或公共安全机构。
- 内容只做研究域建模、证据索引和禁止用途维护。
