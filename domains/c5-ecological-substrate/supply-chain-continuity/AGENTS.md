# supply-chain-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/supply-chain-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


`domains/c5-ecological-substrate/supply-chain-continuity/` 保存供应链连续性研究域。它关注关键物资、服务和基础设施输入如何影响主体长期存在和行动。

## 目录结构

```text
supply-chain-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责关键物资、服务、基础设施、冗余、替代路径和恢复时间建模。
- 本域可整理药品、能源、食物、医疗设备、通信和物流连续性的高层风险资料。
- 本域不提供黑市采购、囤积恐慌、规避制度、供应链攻击或非法获取建议。

## 维护规则

- 任何供应链主张必须说明关键输入、依赖链、断裂点、替代方案和恢复路径。
- 涉及医疗、药品或关键基础设施时只写公共资料、风险边界和非操作性治理。
- 新增文件或子目录时，同步更新本文件。
