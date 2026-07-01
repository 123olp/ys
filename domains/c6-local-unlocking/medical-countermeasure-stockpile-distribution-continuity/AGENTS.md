# medical-countermeasure-stockpile-distribution-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/medical-countermeasure-stockpile-distribution-continuity` |
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


`domains/c6-local-unlocking/medical-countermeasure-stockpile-distribution-continuity/` 是 Human Infra 的医疗对策储备与分发连续性域，负责把暴发关键物资从库存转化为可达、合规、公平的风险控制输入。

## 目录结构

```text
medical-countermeasure-stockpile-distribution-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义战略储备、POD、医疗对策、PPE、冷链、物流、分配和公平可达的对象、链路、非目标和来源信号。
- 本域只整理公开医疗对策和供应分发资料。
- 药品选择、剂量、处方、囤货、库存位置、配送路径、资源抢占和监管规避不属于本域。

## 上下游关系

- 上游：`pharmaceutical-quality-supply-integrity/`、`public-procurement-contracting-capacity/`、`freight-logistics-port-cold-chain-continuity/` 和 `supply-chain-continuity/`。
- 下游：`healthcare-surge-triage-capacity-continuity/`、`vaccination-campaign-booster-delivery-continuity/`、`medicine-access-treatment-continuity/` 和 `mask-respirator-source-control-fit-access-continuity/`。

## 维护规则

- 新增资料必须说明它支持储备、POD、分发、冷链、分配公平、质量安全还是供应瓶颈分析。
- 不能输出处方治疗、个人囤货、库存位置、配送路径、设施安全弱点或规避分配内容。
