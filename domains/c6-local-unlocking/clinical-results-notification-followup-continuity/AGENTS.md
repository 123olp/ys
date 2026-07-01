# clinical-results-notification-followup-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/clinical-results-notification-followup-continuity` |
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


## 职责

本目录承载临床结果通知、异常结果闭环、关键值升级、follow-up tracking 和诊断安全资料。

## 边界

- 只研究结果从系统产生到主体行动之间的通信和责任闭环。
- 不解释检查结果，不提供诊断、治疗、急救、加急或法律建议。
- 不保存结果数值、报告、影像、PHI、portal 凭证或联系方式。

## 结构

```text
clinical-results-notification-followup-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分实验室结果、影像报告、病理报告、筛查结果和诊断安全。
- 涉及个体结果解释或医疗行动的内容必须转回临床团队和官方入口。
