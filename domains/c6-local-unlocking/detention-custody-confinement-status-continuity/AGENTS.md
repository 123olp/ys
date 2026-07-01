# detention-custody-confinement-status-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/detention-custody-confinement-status-continuity` |
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


`detention-custody-confinement-status-continuity/` 是 Human Infra 的拘押、羁押与监管状态连续性域，负责研究强制限制状态如何影响主体自由、通信、照护和恢复路径。

## 目录结构

```text
detention-custody-confinement-status-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义拘押、羁押与监管状态连续性域的对象、链路、非目标、来源信号和下一步。
- 本域只沉淀公开制度资料、变量表、服务断点和权利保护边界。

## 维护规则

- 新增资料必须说明它影响拘押状态、位置通知、通信、法律入口、医疗药物、家庭责任、释放转接还是监督机制。
- 优先使用 ICE、BOP、BJS、WHO prisons、CDC correctional health、司法监察和官方拘押标准资料。
- 禁止输出刑事案件、保释、假释、移民拘押、申诉、上诉、逃避监管、设施规避或法律建议。
- 禁止提供设施弱点、通信规避、违禁品、逃脱、隐藏身份、对抗执法、规避筛查或骚扰拘押人员信息。
