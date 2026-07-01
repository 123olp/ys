# AGENTS.md

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/synthetic-biological-intelligence-organoid-computing-continuity` |
| 所属层级 | `C2` - 可能性源体维护层 |
| 父级容器 | `domains/c2-source-maintenance` |
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


## 目录结构

```text
synthetic-biological-intelligence-organoid-computing-continuity/
├── AGENTS.md
├── README.md
└── literature-review.md
```

## 职责边界

- `README.md` 定义 SBI/OI/BI、闭环体外神经系统和类器官计算如何进入 Human Infra 主体持续性模型。
- `literature-review.md` 承接 `sbi_oi_literature_review_draft.md` 的稳定化综述，保留概念谱系、证据层级、应用、伦理和待补材料。
- 本目录只承载研究域定位、变量、机制、证据边界、综述和非目标。
- 本目录不承载细胞培养、刺激协议、药物实验、神经操控、平台搭建或临床/动物实验建议。

## 维护规则

- 新增资料必须区分 closed-loop task performance、learning、sentience、agency、consciousness 和 moral status。
- 不把 DishBrain/Pong、OI、CL1、SBI 或类器官指标写成意识、人格连续性、mind upload 或主体迁移证据。
- 不把预印本、商业平台、单实验室结果和同行评议论文同等计权。
- 若未来新增 source cards，必须保留 claim、变量、机制、证据等级、边界、反证条件和伦理风险。
