# occupational-exposure-industrial-hygiene 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/occupational-exposure-industrial-hygiene` |
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


本目录维护职业暴露与工业卫生域。它是 Human Infra 的“工作环境暴露控制层”，负责工作如何在提供资源的同时保护身体、感官、呼吸和长期行动能力。

## 目录结构

```text
occupational-exposure-industrial-hygiene/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明职业化学、物理、生物、粉尘、噪声、热、辐射和皮肤暴露如何影响主体持续性。
- 本域只做公开工业卫生、职业暴露、控制层级、监管和风险治理资料整理。
- 不提供现场检测、PPE 选择、职业病诊断、工伤法律、事故处置或监管规避建议。

## 维护规则

- 新增材料必须区分暴露识别、暴露评估、工程控制、行政控制、PPE 和监管责任。
- 不把职业健康材料写成个人工伤、法律、雇佣或赔偿建议。
- 涉及危险作业时，只写原则、证据和责任边界，不写操作步骤。
