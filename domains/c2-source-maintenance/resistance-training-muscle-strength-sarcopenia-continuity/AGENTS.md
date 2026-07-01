# resistance-training-muscle-strength-sarcopenia-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/resistance-training-muscle-strength-sarcopenia-continuity` |
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


`domains/c2-source-maintenance/resistance-training-muscle-strength-sarcopenia-continuity/` 保存抗阻训练、肌力、肌少症、虚弱和功能独立资料。

## 目录结构

```text
resistance-training-muscle-strength-sarcopenia-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义肌力和抗阻训练在主体行动密度、失能预防和有效寿命模型中的位置。
- `AGENTS.md`：记录本目录职责、可新增资料和安全边界。

## 职责边界

- 本域研究肌力、功能测量、抗阻训练证据和风险边界，不提供训练处方。
- 可以新增功能指标、试验证据、指南来源、风险筛查边界和可及性资料。
- 不提供动作教学、重量安排、训练周期、伤病处理、康复处方或个体建议。

## 维护规则

- 新增训练证据必须标注人群、强度语境、终点、持续时间、安全事件和适用边界。
- 不把肌肉量或训练表现直接等同于寿命延长。
- 新增文件或子目录时同步更新本文件。
