# physical-activity-mobility 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/physical-activity-mobility` |
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


`domains/c6-local-unlocking/physical-activity-mobility/` 保存身体活动与移动能力研究域。它关注运动、久坐、心肺适能、力量和平衡如何支撑长期行动。

## 目录结构

```text
physical-activity-mobility/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责身体活动、久坐、心肺适能、力量、平衡和移动能力的研究整理。
- 本域可整理公共健康资料、功能指标和与慢病风险相关的模型变量。
- 本域不提供个体训练、康复、设备、药物或医疗建议。

## 维护规则

- 任何活动主张必须区分人群建议、临床处方、运动表现和康复治疗。
- 与康复、肌骨、心血管、睡眠、营养交叉时必须标注主拥有域。
- 新增文件或子目录时，同步更新本文件。
