# idiopathic-hypersomnia-excessive-sleepiness-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/idiopathic-hypersomnia-excessive-sleepiness-continuity` |
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


本目录维护特发性嗜睡、白天过度嗜睡、睡眠惯性和清醒启动困难资料。它关注“睡了仍无法清醒”如何压缩有效行动窗口。

## 目录结构

```text
idiopathic-hypersomnia-excessive-sleepiness-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义特发性嗜睡如何通过日间嗜睡、醒后困难、诊断不确定性和污名影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠、用药、驾驶、学校、工作或医疗资料。
- 资料进入本域时必须保留对象、排除诊断语境、功能损耗、支持接口和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`narcolepsy-daytime-sleepiness-continuity/` 和注意力/任务启动模型。
- 不替代睡眠医学、神经科、精神科、药学、驾驶安全、学校/雇主、保险、残障服务或个体医疗建议。

## 维护规则

- 不写个人诊断、睡眠检查解释、药物、剂量、作息、驾驶许可、便利申请或残障建议。
- 不把嗜睡体验写成治疗流程或自我诊断。
- 新增资料必须区分持续嗜睡、醒后困难、诊断不确定性、支持和安全暴露。
