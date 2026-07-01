# manufacturing-repair-capacity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/manufacturing-repair-capacity` |
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


本目录承载 Human Infra 中“制造、维修和维护能力”研究域。

## 结构

```text
manufacturing-repair-capacity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义制造维修能力如何影响主体持续性、关注对象、非目标、来源信号和下一步。
- 本目录只做公开资料、变量建模、质量边界和跨域接口，不放受管制制造、危险维修、破解或商业采购建议。

## 上下游关系

- 上游：`docs/reference/research-domain-atlas.md`、`supply-chain-continuity/`、`standards-metrology-quality-infrastructure/`。
- 下游：医疗设备、辅助技术、能源、通信、水卫生、应急恢复、产品安全和长期照护相关模型。

## 维护规则

- 公开结论必须回到官方制造、标准、质量、工程或产业资料来源。
- 不写武器、医疗器械、药品、危险设备、芯片或关键基础设施的制造/维修步骤。
- 涉及设备安全时，只做资料索引和边界说明，不替代工程或监管判断。
