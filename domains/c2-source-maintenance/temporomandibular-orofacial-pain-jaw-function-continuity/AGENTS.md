# temporomandibular-orofacial-pain-jaw-function-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/temporomandibular-orofacial-pain-jaw-function-continuity` |
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


`domains/c2-source-maintenance/temporomandibular-orofacial-pain-jaw-function-continuity/` 保存颞下颌关节障碍、口颌面痛和颌功能连续性研究域。

## 目录结构

```text
temporomandibular-orofacial-pain-jaw-function-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责 TMD、口颌面痛、开口咀嚼、言语、睡眠、压力和服务路径的资料整理。
- 本域可以描述颌面疼痛如何改变注意力、有效时间、沟通和工作能力。
- 本域不提供诊断、咬合判断、护牙套、练习、用药、影像、手术或个体治疗建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`pain-suffering-control/`、`sleep-circadian-recovery/`。
- 下游：`tooth-loss-prosthodontic-chewing-continuity/`、`speech-language-communication-continuity/`、`nutrition-metabolic-health/`。

## 维护规则

- 颌面疼痛资料必须区分疼痛机制、功能后果、心理压力、睡眠和服务路径。
- 不允许将资料转化为自我矫治、咬合调整、药物或器械建议。
- 新增文件或子目录时，同步更新本文件。
