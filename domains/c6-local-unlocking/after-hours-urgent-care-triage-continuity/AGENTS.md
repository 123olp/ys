# after-hours-urgent-care-triage-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/after-hours-urgent-care-triage-continuity` |
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

本目录承载非工作时间照护、urgent care、护士热线、tele-triage 和闭环回传连续性资料，关注常规诊所关闭后的服务断点。

## 边界

- 只整理公开资料、机制、变量、证据边界和研究问题。
- 不提供症状分诊、急救判断、urgent care 推荐、等待建议、诊断治疗或保险规避。
- 不保存症状、位置、保险、病历、通话、门户消息或个案健康资料。

## 结构

```text
after-hours-urgent-care-triage-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 after-hours access、urgent care、tele-triage、ED diversion 和 follow-up 回传。
- 任何疑似急症、症状判断或个体医疗问题必须回到急救服务或医疗专业人员。
