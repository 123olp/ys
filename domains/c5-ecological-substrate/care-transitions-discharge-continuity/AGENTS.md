# care-transitions-discharge-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/care-transitions-discharge-continuity` |
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


本目录维护照护转移与出院连续性域。它是 Human Infra 的“恢复路径交接不断线”层，负责医院、急诊、康复、居家和社区之间的断点治理。

## 目录结构

```text
care-transitions-discharge-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明出院计划、交接、用药重整、随访和再入院风险如何影响主体恢复窗口。
- 本域只做公开照护转移、出院连续性和患者安全资料整理。
- 不提供个体出院、急诊、复诊、用药、护理、机构选择、保险索赔或医疗纠纷建议。

## 维护规则

- 新增材料必须区分系统交接流程、患者教育、医疗责任和个体临床决策。
- 涉及出院、复诊、药物和警示症状时，必须保留专业服务和紧急服务边界。
- 不把再入院率或流程指标写成单一机构排名、个体预后或责任归因。
