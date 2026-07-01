# multimorbidity-polypharmacy-care-coordination 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/multimorbidity-polypharmacy-care-coordination` |
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


本目录维护多病共存、多重用药与照护协调域。它是 Human Infra 的“复杂身体状态和治疗负担统一编排”层，负责多疾病、多药物、多专科之间的协调风险。

## 目录结构

```text
multimorbidity-polypharmacy-care-coordination/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明多病共存、多重用药、药物重整、治疗负担和跨专科照护如何影响主体持续性。
- 本域只做公开资料整理和模型变量维护。
- 不提供个体用药、停药、剂量、相互作用、诊断、检查、转诊或治疗优先级建议。

## 维护规则

- 新增资料必须区分群体证据、药物安全信号、临床流程和个体处方决策。
- 涉及药物时必须写明“不得替代医生、药师或紧急医疗服务”。
- 不把复杂照护协调简化为单一 App、单一指标或单一指南叠加。
