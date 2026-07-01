# household-operating-map-handoff-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/household-operating-map-handoff-continuity` |
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


本目录承载家庭运行地图、隐性知识显性化和交接连续性研究域，关注家庭任务系统如何从单点记忆变成可代理、可恢复的协作结构。

## 目录结构

```text
household-operating-map-handoff-continuity/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义家庭运行地图、代理交接、隐私边界和主体连续性的关系。
- `AGENTS.md`：说明本目录职责、边界和维护规则。

## 维护规则

- 资料优先回到 Ready.gov、FEMA、家庭应急计划、照护交接、灾后恢复和隐私最小化资料。
- 不写家庭监控、定位追踪、门禁共享、个人资料模板、医疗处方、法律/遗产建议或个案照护计划。
- 新增指标必须注明口径：资料类别、访问对象、更新周期、撤权机制、敏感性和连续性后果。
- 不保存真实家庭运行地图、住址、联系人、门禁、药品、账户、资产或照护对象资料。
