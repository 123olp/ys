# insurance-underwriting-algorithmic-risk-scoring-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/insurance-underwriting-algorithmic-risk-scoring-continuity` |
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


本目录承载保险承保、算法评分和风险转移准入连续性资料。它研究保险模型、外部数据和自动化理赔如何影响主体获得风险池保护。

## 目录结构

```text
insurance-underwriting-algorithmic-risk-scoring-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应记录险种、数据来源、模型治理、消费者保护、监管责任和申诉边界。
- 本域不保存保险资料，不比较产品，不解释保费、理赔、拒保或个案法律责任。

## 维护规则

- 引用资料优先来自 NAIC、州保险监管机构、NIST、消费者保护和公开研究资料。
- 必须保留精算、监管、消费者保护、公平性和模型治理之间的边界。
- 不提供核保规避、理赔操作或保险购买建议。
