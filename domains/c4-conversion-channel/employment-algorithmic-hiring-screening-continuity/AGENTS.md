# employment-algorithmic-hiring-screening-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/employment-algorithmic-hiring-screening-continuity` |
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


本目录承载算法招聘与就业筛查连续性资料。它研究 AI 和自动化筛查如何影响工作入口、收入、保险、技能路径和反歧视边界。

## 目录结构

```text
employment-algorithmic-hiring-screening-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应记录筛查工具类型、评价变量、偏差风险、告知、人类复核、合理便利和审计边界。
- 本域不提供求职作弊、规避筛查、个案劳动法律意见、投诉策略或雇主合规方案。

## 维护规则

- 引用资料优先来自 EEOC、DOL、NIST、州劳动机构和可信研究资料。
- 必须区分算法治理、反歧视、合理便利、职业服务和个案法律行动。
- 不把招聘算法写成能力本质评价，也不提供操纵测评的方法。
