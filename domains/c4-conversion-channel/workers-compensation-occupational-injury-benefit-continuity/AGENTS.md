# workers-compensation-occupational-injury-benefit-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/workers-compensation-occupational-injury-benefit-continuity` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


本目录承载工伤、职业病、伤害记录、工资替代和恢复权益连续性资料。它研究工作伤害发生后，制度如何把伤害事实转化为医疗、收入替代、康复和复工机会。

## 目录结构

```text
workers-compensation-occupational-injury-benefit-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分伤害记录、职业病记录、雇主报告、医疗给付、工资替代、复工、职业康复、争议和 OSHA recordkeeping。
- 本域不保存个人伤害、医疗、雇佣或索赔资料，不提供索赔、赔偿、诊断、复工、法律、保险或个人案件建议。

## 维护规则

- 引用资料优先来自 DOL OWCP、OSHA、州级 workers compensation 机构、职业伤害监测和工伤研究。
- 必须保留医学边界、法律边界、个人案件边界、报告义务、反报复、反欺诈和复工压力风险。
- 不把工伤补偿写成简单保险产品，也不输出任何伪造、隐瞒、欺诈或规避报告路径。
