# acute-heart-failure-decompensation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/acute-heart-failure-decompensation-continuity` |
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


本目录维护急性心衰失代偿、肺水肿、低灌注、住院和出院交接资料。它是慢性心血管风险进入急性循环/呼吸/肾脏失衡的研究域。

## 目录结构

```text
acute-heart-failure-decompensation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义急性心衰失代偿如何改变住院、再入院、呼吸支持、肾损伤和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案体重、血压、氧饱和度、化验、影像、药物或设备数据。
- 资料进入本域时必须区分急性稳定、住院过程、出院交接、再入院和长期功能恢复。

## 上下游关系

- 上游来自 AHA/ACC/HFSA、NHLBI、CDC 和心衰质量改进资料。
- 下游服务 `cardiovascular-resilience/`、`mechanical-ventilation-respiratory-failure-continuity/` 和 `acute-kidney-injury-renal-replacement-continuity/`。
- 不替代医生、急诊、心内科、住院团队、康复团队或个体医疗建议。

## 维护规则

- 不写药物调整、利尿策略、氧疗、饮食、急诊分诊、住院或出院建议。
- 不把系统级心衰研究写成个案监测、预警或治疗工具。
- 新增变量必须区分容量、灌注、肾心交互、呼吸状态、交接和恢复负担。
