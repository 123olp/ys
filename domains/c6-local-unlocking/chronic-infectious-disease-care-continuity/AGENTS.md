# chronic-infectious-disease-care-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chronic-infectious-disease-care-continuity` |
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


本目录维护慢性与长疗程传染病照护连续性域。它是 Human Infra 的“长期感染风险和公共卫生屏障不断线”层，负责 HIV、结核、病毒性肝炎等疾病如何影响主体持续性。

## 目录结构

```text
chronic-infectious-disease-care-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明慢性传染病检测、治疗连续性、药物可及、耐药、隐私、污名和公共卫生协同如何影响主体持续性。
- 本域只做公开 HIV、结核、病毒性肝炎、长期感染照护和公共卫生资料整理。
- 不提供检测诊断、用药治疗、PEP/PrEP、隔离、传播规避、追踪规避、实验室操作或个体风险判断。

## 维护规则

- 新增材料必须区分个体治疗连续性、公共卫生监测、耐药、隐私、去污名和群体风险屏障。
- 不把感染状态写成道德判断、身份标签、关系判断或排除理由。
- 涉及检测、接触服务、报告和病原体时，只写公共框架和边界，不写规避或操作步骤。
