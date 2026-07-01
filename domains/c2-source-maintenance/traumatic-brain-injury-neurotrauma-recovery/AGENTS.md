# traumatic-brain-injury-neurotrauma-recovery 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/traumatic-brain-injury-neurotrauma-recovery` |
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


本目录维护创伤性脑损伤、脑震荡和神经创伤恢复资料。它是外部冲击进入主体连续性的脑保护域。

## 目录结构

```text
traumatic-brain-injury-neurotrauma-recovery/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 TBI、脑震荡、重复头部冲击和恢复轨迹如何影响主体持续性。
- 本目录不保存急救处置、诊断、影像解释、返赛返工许可或康复处方。
- 资料必须区分公共健康信息、临床指南、职业/运动政策、长期后遗症和个体医疗判断。

## 上下游关系

- 上游来自创伤医学、神经病学、运动医学、交通安全、职业健康和军事医学。
- 下游服务风险工程、认知资源保护、心理稳定、睡眠恢复和功能康复。
- 不替代 `risk-engineering/`；本目录聚焦脑外伤后的神经连续性损失。

## 维护规则

- 不提供个体脑震荡诊断、治疗、影像解释或活动恢复许可。
- 不把症状清单、设备读数或自评量表写成个人恢复结论。
- 新增资料必须标注损伤类型、证据阶段、适用场景、长期风险和禁止用途。
