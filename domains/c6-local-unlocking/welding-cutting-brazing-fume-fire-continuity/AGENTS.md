# welding-cutting-brazing-fume-fire-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/welding-cutting-brazing-fume-fire-continuity` |
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


本目录承载焊接切割钎焊、烟尘、热作业、火灾爆炸与工作者连续性资料，只做研究域建模和证据边界，不输出操作教程、通风设计、呼吸器/PPE、热作业许可、消防、合规、事故调查或法律建议。

## 结构

```text
welding-cutting-brazing-fume-fire-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义焊接、切割、钎焊、金属烟尘、热作业、火灾爆炸、气瓶和受限空间接口。
- 新增资料必须区分 welding、cutting、brazing、metal fume、hot work、fire/explosion、gas cylinder、ventilation evidence 和 incident reporting。
- 不保存现场照片、作业许可、通风参数、气瓶参数、PPE 参数、工伤材料、雇主记录、事故证据或可识别个人/企业资料。

## 上下游

- 上游：`occupational-exposure-industrial-hygiene/`、`confined-space-entry-atmospheric-hazard-continuity/`、`human-factors-ergonomics-task-system-continuity/`。
- 下游：`burn-injury-critical-care-rehabilitation-continuity/`、`asthma-copd-exacerbation-airway-continuity/`、`workers-compensation-occupational-injury-benefit-continuity/`。

## 维护规则

- 资料优先回到 OSHA、NIOSH、BLS/CFOI、工伤监测、职业呼吸健康和公开安全研究。
- 个案现场安全、职业暴露或伤害问题必须转回雇主安全计划、OSHA/州监管、专业安全人员、医疗/急救、工伤或法律渠道。
