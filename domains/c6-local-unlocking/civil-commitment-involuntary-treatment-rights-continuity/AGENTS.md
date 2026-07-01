# civil-commitment-involuntary-treatment-rights-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/civil-commitment-involuntary-treatment-rights-continuity` |
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


`civil-commitment-involuntary-treatment-rights-continuity/` 是 Human Infra 的民事收治、非自愿治疗与权利连续性域，负责研究危机干预如何在保护安全时不切断主体自主性和恢复路径。

## 目录结构

```text
civil-commitment-involuntary-treatment-rights-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义民事收治、非自愿治疗与权利连续性域的对象、链路、非目标、来源信号和下一步。
- 本域只整理公开制度资料、权利边界、风险变量和恢复接口。

## 维护规则

- 新增资料必须说明它影响危机评估、收治、强制治疗、复查、最小限制、同意能力、残障权利、出院转接还是社区支持。
- 优先使用 SAMHSA、HHS OCR、DOJ Civil Rights、WHO、残障权利机构和官方危机服务资料。
- 禁止输出个人危机判断、收治标准、强制治疗、出院、申诉、医疗、用药或安全计划建议。
- 禁止指导规避危机服务、躲避评估、控制他人、强迫治疗、定位监控、制造证据或扩大污名。
