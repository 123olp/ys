# noise-exposure-acoustic-environment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/noise-exposure-acoustic-environment-continuity` |
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


本目录维护噪声暴露与声环境连续性域。它是 Human Infra 的“声环境负荷层”，负责噪声如何影响睡眠、听觉、沟通、注意力、压力恢复和长期任务执行。

## 目录结构

```text
noise-exposure-acoustic-environment-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明噪声暴露、声环境、听力保护、恢复负荷和公共治理如何支撑主体持续性。
- 本域只做公开噪声、听力、工作环境、城市声环境和暴露控制资料整理。
- 不提供个体听力诊断、设备购买、隔音施工、工作场所合规判断、投诉策略或法律建议。

## 维护规则

- 新增材料必须区分环境噪声、职业噪声、交通噪声、娱乐噪声、听力损伤、睡眠影响和认知/心理负荷。
- 不把分贝读数、手机 App、穿戴设备或 AI 输出写成个体健康、安全、法律或合规结论。
- 涉及工作场所、学校、住房和交通时，只写系统变量和证据边界，不写个案处置方案。
