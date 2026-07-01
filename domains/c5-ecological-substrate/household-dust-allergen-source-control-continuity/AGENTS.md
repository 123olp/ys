# household-dust-allergen-source-control-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-dust-allergen-source-control-continuity` |
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


本目录承载家庭灰尘与室内过敏原源控制连续性研究域，关注环境负荷如何消耗睡眠、注意力和恢复能力。

## 目录结构

```text
household-dust-allergen-source-control-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义灰尘、尘螨、宠物皮屑、织物、清洁源控制、过敏负荷和家庭任务连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 EPA、CDC、NIH、公共卫生、住房和过敏/哮喘资料。
- 不写诊断、治疗、药物、宠物处置、杀虫操作、清洁产品推荐、深度清洁教程或法律建议。
- 新增指标必须注明口径：过敏原类型、房间/织物来源、清洁状态、湿度接口、症状负荷、任务负担或恢复结果。
- 涉及儿童、哮喘、过敏、害虫或租房问题时，必须保留医疗、害虫控制和住房责任边界。
