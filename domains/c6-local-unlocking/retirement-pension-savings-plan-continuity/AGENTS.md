# retirement-pension-savings-plan-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/retirement-pension-savings-plan-continuity` |
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


本目录承载退休计划、养老金和长期储蓄账户连续性资料。它研究工作期资源如何通过制度化账户和记录在劳动退出后继续支撑主体行动。

## 目录结构

```text
retirement-pension-savings-plan-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分 defined benefit、defined contribution、IRA、rollover、vesting、beneficiary、lost accounts、plan termination 和 pension guarantee。
- 本域不保存个人账户、资产、计划或受益人资料，不提供投资、税务、退休、养老金申诉、法律或理财建议。

## 维护规则

- 引用资料优先来自 DOL EBSA、PBGC、IRS、官方退休监管机构和退休安全研究。
- 必须保留投资建议边界、税务边界、受益人隐私、账户恢复、计划终止、费用透明和反欺诈边界。
- 不把退休账户连续性写成收益保证，也不输出任何隐藏资产、冒领、伪造文件或规避监管路径。
