# household-ladder-step-stool-reach-task-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-ladder-step-stool-reach-task-continuity` |
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


本目录承载家庭梯凳、高处取物与维护任务连续性研究域，关注“够不到”的物理边界如何改变跌倒风险和维护执行。

## 目录结构

```text
household-ladder-step-stool-reach-task-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义梯子/梯凳、高处任务、跌倒风险、任务延迟和家庭维护连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 CPSC、CDC、NIA、消防、职业治疗和住房安全资料。
- 不写梯子操作教程、施工培训、产品推荐、现场评估、急救、职业合规豁免或法律建议。
- 新增指标必须注明口径：任务高度、访问方式、执行频率、主体状态、延迟后果、维护对象和风险边界。
- 涉及独居老人、平衡障碍、术后恢复、报警器维护和维修外包时，必须保留风险升级边界。
