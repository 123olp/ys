# Fisheries Aquatic Food Systems Continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/fisheries-aquatic-food-systems-continuity` |
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


本目录承载渔业、水产养殖和水生食物系统研究，关注水生资源如何成为营养、收入和社区连续性的外部输入。

## 目录结构

```text
fisheries-aquatic-food-systems-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究捕捞渔业、水产养殖、内陆渔业、水产品营养、加工冷链、渔业治理和小规模渔业生计。
- 上游连接海洋生态、淡水水文和气候；下游连接营养、食品安全、冷链、贸易和社区收入。
- 不提供捕捞、养殖、船只作业、加工、投资、配额规避、非法捕捞、走私或标签造假建议。

## 维护规则

- 渔业资料必须标明物种、区域、生产方式、时间尺度和治理来源。
- 水产品营养和食品安全资料不得写成个体饮食或医疗建议。
- 涉及 IUU、执法、贸易和资源开采时，只保留公共治理材料，不输出可操作规避信息。
