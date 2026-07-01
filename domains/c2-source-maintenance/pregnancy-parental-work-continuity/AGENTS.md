# pregnancy-parental-work-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pregnancy-parental-work-continuity` |
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


本目录维护孕产育儿工作连续性的资料、机制链路和伦理边界。

## 文件结构

```text
pregnancy-parental-work-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 描述怀孕、分娩、泵奶、育儿和托育责任如何影响工作、收入、时间和未来选择权。
- 本目录只做公开制度、研究框架和资料索引，不做个人医疗、法律、HR、福利、托育选择或雇主合规建议。
- 与母婴健康、托育、岗位保护、工资替代和合理便利域保持交叉引用。

## 维护规则

- 新增资料必须区分反歧视、合理便利、哺乳支持、父母假、托育和工资替代。
- 不把任何特定国家/州/雇主制度写成普遍规则。
- 不写个人便利申请、法律投诉、医疗限制证明或雇主政策模板。
