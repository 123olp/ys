# light-exposure-circadian-environment-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/light-exposure-circadian-environment-continuity` |
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


本目录维护光照暴露与昼夜节律环境连续性域。它是 Human Infra 的“节律同步层”，负责光环境如何影响睡眠、警觉性、情绪、代谢、恢复和有效时间。

## 目录结构

```text
light-exposure-circadian-environment-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明光照暴露、昼夜节律、夜间光污染、轮班照明和恢复时间如何支撑主体持续性。
- 本域只做公开光照、节律、睡眠、工作时间和环境设计资料整理。
- 不提供个体睡眠诊断、光疗处方、补剂/药物建议、灯具购买、照明施工、排班许可或驾驶/值班判断。

## 维护规则

- 新增材料必须区分自然光、夜间光、室内照明、屏幕光、轮班环境、极端环境和光污染。
- 不把照度、色温、睡眠分数或 AI 输出写成个体医疗、工作许可或寿命结论。
- 涉及照明产品、建筑、电气、劳动制度和临床光疗时，只写证据边界和系统变量。
