# standards-metrology-quality-infrastructure 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/standards-metrology-quality-infrastructure` |
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


本目录承载标准、计量、校准、认证、质量基础设施和互操作规范如何支撑可信技术系统。

## 结构

```text
standards-metrology-quality-infrastructure/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只讨论标准计量和质量基础设施，不处理认证规避、检测报告伪造、设备改装或产品采购建议。
- 后续新增材料应优先是标准组织 Source Card、计量变量、质量基础设施案例和互操作边界。

## 上下游关系

- 上游：`research-infrastructure-open-science-translation/`、`measurement-feedback/`、`civic-data-open-government-transparency/`。
- 下游：`clinical-trials-regulatory-science-translation/`、`patient-data-interoperability/`、`supply-chain-continuity/`。
- 相邻域：`product-safety-recall-systems/`、`health-data-privacy-governance/`、`ai-agency-safety/`。

## 维护规则

- 不提供规避认证、伪造检测、绕过标准或规避质量审查策略。
- 不把标准号、认证标志或合格声明写成产品背书。
- 若新增标准表、计量模型或质量流程，必须同步维护本文件和相关索引。
