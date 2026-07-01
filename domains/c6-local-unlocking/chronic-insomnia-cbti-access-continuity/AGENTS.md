# chronic-insomnia-cbti-access-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/chronic-insomnia-cbti-access-continuity` |
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


本目录维护慢性失眠、CBT-I 可及性、睡眠行为治疗和长期恢复连续性资料。它关注恢复系统失败如何消耗有效时间、注意力和情绪稳定。

## 目录结构

```text
chronic-insomnia-cbti-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义慢性失眠和 CBT-I 可及如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠日志、精神健康、用药、工作或设备资料。
- 资料进入本域时必须保留诊断对象、干预类型、可及性、复发预防、证据边界和禁止用途。

## 上下游关系

- 上游来自 NIH/NHLBI、ACP、AASM 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`attention-executive-control/` 和精神健康功能模型。
- 不替代睡眠医学、心理治疗、精神科、药学、职业安全或个体医疗建议。

## 维护规则

- 不写个人 CBT-I 操作、睡眠限制计划、药物选择、停药建议、设备购买或危机处理。
- 不把行为治疗证据写成可自行执行的治疗流程。
- 新增资料必须区分慢性失眠、短期失眠、共病失眠、日间功能和治疗可及。
