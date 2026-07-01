# Wildfire Landscape Fire Resilience

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/wildfire-landscape-fire-resilience` |
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


本目录承载野火、景观火灾和社区火灾韧性研究，关注复合火灾风险如何影响主体持续性。

## 目录结构

```text
wildfire-landscape-fire-resilience/
├── AGENTS.md
└── README.md
```

## 职责边界

- 研究野火风险、火灾天气、景观燃料、WUI、社区防火、烟雾暴露、疏散和恢复。
- 上游连接气候、土地、建筑和空气质量；下游连接住房、医疗、能源、通信、保险和灾后恢复。
- 不提供实时火场行动、灭火战术、疏散路线、纵火、规避指挥或保险索赔建议。

## 维护规则

- 野火资料必须区分长期风险治理、官方预警和实时应急行动。
- 不发布可支持纵火、扩大火势、规避救援或干扰指挥的信息。
- 涉及公众安全时，必须明确官方消防、应急和公共卫生机构优先。
