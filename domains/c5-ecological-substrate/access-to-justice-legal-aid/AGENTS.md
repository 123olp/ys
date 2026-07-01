# access-to-justice-legal-aid 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/access-to-justice-legal-aid` |
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


`access-to-justice-legal-aid/` 是 Human Infra 的司法可及与法律援助域，负责研究法律问题如何从主体持续性的截断风险转化为可理解、可代理、可申诉和可执行的救济路径。

## 目录结构

```text
access-to-justice-legal-aid/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义司法可及与法律援助域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做民事法律需求、法律援助、程序可达性、代理缺口、权利救济和制度恢复路径资料整理。
- 法律意见、案件策略、文书起草、诉讼建议、移民建议、规避监管和程序滥用不属于本域。

## 上下游关系

- 上游：`legal-identity-civil-registration/`、`health-literacy-navigation/`、`digital-inclusion-connectivity/`。
- 下游：`housing-built-environment-stability/`、`financial-resilience-access/`、`social-protection-benefits-delivery/`、`personal-safety-violence-prevention/`。

## 维护规则

- 新增资料必须说明它影响问题识别、法律信息、代理、费用、程序负担、语言可达、申诉还是执行。
- 禁止输出个体法律建议、诉讼策略、文书操作、监管规避、伪造材料或报复性行动建议。
