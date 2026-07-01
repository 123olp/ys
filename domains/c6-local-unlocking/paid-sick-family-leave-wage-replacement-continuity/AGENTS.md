# paid-sick-family-leave-wage-replacement-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/paid-sick-family-leave-wage-replacement-continuity` |
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


本目录维护带薪病假、家庭假、医疗假和工资替代连续性的资料与边界。

## 文件结构

```text
paid-sick-family-leave-wage-replacement-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 描述短期无法工作时，工资替代如何防止健康/照护事件演变成财务和工作断裂。
- 本目录只做制度和机制研究，不做个人福利、工资、税务、保险或法律建议。
- 与岗位保护、残障收入、工伤和失业保险的边界必须明确分流。

## 维护规则

- 新增资料必须标明联邦、州、雇主计划、公共计划或私营保险来源。
- 不将“带薪休假存在”推导为“个人一定可获得”。
- 不记录或生成可用于欺诈申领、伪造证明或规避审查的操作细节。
