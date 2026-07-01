# myasthenia-gravis-neuromuscular-junction-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/myasthenia-gravis-neuromuscular-junction-continuity` |
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


本目录承载重症肌无力与神经肌肉接头连续性研究域，只做公开资料整理、机制建模和边界约束。

```text
myasthenia-gravis-neuromuscular-junction-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 MG、神经肌肉接头、波动性肌无力、呼吸/吞咽风险和主体持续性的关系。
- 本域上游依赖 `neuro-continuity/`、`immune-maintenance/`、`respiratory-oxygenation/` 和 `functioning-quality-of-life-outcomes/`。
- 下游服务急性风险边界、药物风险治理、工作适配和神经肌肉波动模型。

## 维护规则

- 只使用 NINDS、NIH、CDC、专业学会或同行评审资料作为来源信号。
- 不提供诊断、检查判读、用药、免疫治疗、手术、危象处理、活动许可或药物相互作用建议。
