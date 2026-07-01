# alcohol-use-risk-reduction-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/alcohol-use-risk-reduction-continuity` |
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


本目录维护不健康饮酒筛查、简短干预、治疗转介、复发/伤害减少和社会功能影响资料。它是主体在肝病、癌症、事故、暴力、工作和家庭风险之前的上游风险控制域。

## 目录结构

```text
alcohol-use-risk-reduction-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义酒精风险筛查、简短干预、转介、治疗连续和伤害减少如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案饮酒史、戒断、家庭冲突、驾驶、法律或心理危机资料。
- 资料进入本域时必须保留公共健康层级、成瘾与污名边界、风险链和禁止用途。

## 上下游关系

- 上游来自 NIAAA、USPSTF、WHO 和酒精风险降低资料。
- 下游服务 `substance-exposure-control/`、`mental-health-affective-stability/`、`renal-hepatic-clearance/` 和安全风险建模。
- 不替代医生、成瘾治疗、心理服务、危机服务、法律服务或个体医疗建议。

## 维护规则

- 不写饮酒量判断、戒断处理、解酒、药物、排毒、家庭干预、驾驶或法律建议。
- 不生成饮酒技巧、规避检测、危险挑战、未成年人饮酒或自伤相关内容。
- 新增变量必须区分筛查、简短干预、转介、治疗连续、复发/伤害减少和社会功能。
