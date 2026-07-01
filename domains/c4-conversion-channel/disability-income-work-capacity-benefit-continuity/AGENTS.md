# disability-income-work-capacity-benefit-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/disability-income-work-capacity-benefit-continuity` |
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


本目录维护残障收入、工作能力与福利连续性的资料和边界。

## 文件结构

```text
disability-income-work-capacity-benefit-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 描述长期功能受限时，收入保障、医疗覆盖、复工激励和福利悬崖如何影响主体持续性。
- 本目录只做公开制度、研究框架和资料索引，不做个人福利、法律、医疗、税务、保险或申诉建议。
- 与社会保险记录、合理便利、工伤、社会保护和财务韧性域保持清晰分流。

## 维护规则

- 新增资料必须标明来源机构、辖区、适用对象和是否属于公共福利、私营保险或雇主福利。
- 不把公共残障福利与私营残障保险混写。
- 不记录可用于欺诈申领、隐瞒收入、伪造证据或规避审查的操作细节。
