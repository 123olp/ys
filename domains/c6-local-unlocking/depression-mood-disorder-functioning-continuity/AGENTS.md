# depression-mood-disorder-functioning-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/depression-mood-disorder-functioning-continuity` |
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


本目录承载抑郁、心境低落、快感缺失和功能损害连续性资料。它关注心理状态如何改变主体有效时间和行动能力，而不是诊断、治疗或危机处置。

## 结构

```text
depression-mood-disorder-functioning-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分症状描述、诊断类别、功能结局、服务连续性、危机边界和反污名边界。
- 资料优先回到 WHO、NIMH、公共卫生资料、功能结局量表和系统性综述。
- 不保存量表分数、病历、心理咨询记录、用药记录、自伤信息、家庭个案或敏感身份资料。
