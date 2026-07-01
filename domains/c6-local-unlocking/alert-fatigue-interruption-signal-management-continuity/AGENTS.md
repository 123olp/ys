# alert-fatigue-interruption-signal-management-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/alert-fatigue-interruption-signal-management-continuity` |
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


本目录承载告警疲劳、通知疲劳、中断管理和信号优先级资料。它关注信号环境如何保护注意力，而不是告警配置或增长设计。

## 结构

```text
alert-fatigue-interruption-signal-management-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 alarm fatigue、alert fatigue、notification fatigue、interruption、signal prioritization 和 escalation routing。
- 必须记录假阳性/假阴性、响应负担、静默窗口、夜间打扰、责任转移和反注意力操控边界。
- 不保存通知记录、医疗告警、生产告警、值班记录、睡眠数据、位置、内部事件日志或个人行为数据。
