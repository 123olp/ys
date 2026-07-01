# elder-justice-adult-protective-services 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/elder-justice-adult-protective-services` |
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


本目录维护老年正义与成人保护服务域。它是 Human Infra 的“脆弱成年人不被虐待、忽视和剥削吞噬”层，负责 APS、Elder Justice、长期照护监察和保护服务如何影响主体持续性。

## 目录结构

```text
elder-justice-adult-protective-services/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明老年虐待、成人保护、财务剥削、照护忽视、机构虐待和权利保护如何影响主体持续性。
- 本域只做公开成人保护、老年正义、虐待预防、服务转介和系统治理资料整理。
- 不提供个案法律、报案取证、监护、财务安排、家庭冲突、定位监控、约束控制或照护计划建议。

## 维护规则

- 新增材料必须区分虐待、忽视、自我忽视、财务剥削、照护服务、权利保护和多机构协作。
- 不把保护服务写成控制成年人、剥夺同意或争夺财产的工具。
- 涉及报告和保护流程时，只写公共资料和边界，不写个案策略。
