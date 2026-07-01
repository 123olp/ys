# periodontal-disease-systemic-inflammation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/periodontal-disease-systemic-inflammation-continuity` |
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


`domains/c6-local-unlocking/periodontal-disease-systemic-inflammation-continuity/` 保存牙周病、牙齿支持结构和慢性炎症交叉研究域。

## 目录结构

```text
periodontal-disease-systemic-inflammation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责牙周炎症、牙齿稳定性、缺牙风险、维护服务和全身交叉证据的资料整理。
- 本域可以整理糖尿病、吸烟、心血管风险叙事和牙周证据边界。
- 本域不提供牙周诊断、分期、探诊/影像解释、治疗、手术、抗生素或个体护理建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`chronic-disease-multimorbidity/`、`risk-reduction-preventive-care/`。
- 下游：`tooth-loss-prosthodontic-chewing-continuity/`、`dental-care-access-insurance-workforce-continuity/`。

## 维护规则

- 牙周与全身疾病资料必须标注证据等级，不得把相关性写成直接因果。
- 涉及治疗路径时只描述系统级服务连续性，不给个体方案。
- 新增文件或子目录时，同步更新本文件。
