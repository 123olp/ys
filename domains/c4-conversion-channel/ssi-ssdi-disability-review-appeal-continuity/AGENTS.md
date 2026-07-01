# ssi-ssdi-disability-review-appeal-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/ssi-ssdi-disability-review-appeal-continuity` |
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


本目录维护 SSI/SSDI 残障收入、复审和申诉连续性域。它是 Human Infra 的失能后收入承认与支付维护层，不是残障申请、医学证明或法律策略入口。

## 目录结构

```text
ssi-ssdi-disability-review-appeal-continuity/
├── AGENTS.md
└── README.md
```

## 职责

- 记录 disability determination、appeals、CDR、work reporting、overpayment 和 payment continuity。
- 区分制度流程研究、医学诊断、法律代理、福利策略和个案申请。
- 维护 SSA 官方资料、证据边界、隐私限制和禁止用途。

## 维护规则

- 新增资料必须标明 SSI/SSDI/SSA 流程差异和来源。
- 不保存 SSN、医疗记录、收入资产、工作记录、案件号、SSA 账户或代表人资料。
- 不提供资格、诊断、工作能力、上诉、CDR 或 overpayment 个案建议。
