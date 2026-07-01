# cardiac-arrhythmia-syncope-decompensation-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/cardiac-arrhythmia-syncope-decompensation-continuity` |
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


本目录维护心律失常、晕厥、传导异常和节律稳定资料。它是主体从正常行动突然进入脑灌注不足、跌倒、卒中或骤停风险的研究域。

## 目录结构

```text
cardiac-arrhythmia-syncope-decompensation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义心律和晕厥如何改变突发失能、跌倒、卒中、心衰、骤停和未来选择权。
- 本目录只维护系统级变量、来源和边界，不保存个案心电图、设备、症状、用药或位置数据。
- 资料进入本域时必须区分监测、风险识别、转诊、设备路径、栓塞风险和骤停前状态。

## 上下游关系

- 上游来自 AHA/ACC/HRS、NHLBI 和心律失常/晕厥 guideline materials。
- 下游服务 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `cardiac-arrest-cpr-defibrillation-continuity/`。
- 不替代医生、急诊、心内科、电生理、神经科或个体医疗建议。

## 维护规则

- 不写心电图判读、抗凝、用药、起搏器、ICD、消融、驾驶、运动或晕厥处理建议。
- 不把系统级节律连续性研究写成个人风险计算或治疗工具。
- 新增变量必须区分节律、传导、晕厥、栓塞、跌倒和骤停上游风险。
