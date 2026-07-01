# built-environment-accessibility-universal-design 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/built-environment-accessibility-universal-design` |
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


本目录维护建成环境无障碍与通用设计域。它是 Human Infra 的“空间可达性层”，负责建筑、公共空间和设施如何让不同能力状态的主体持续行动与参与。

## 目录结构

```text
built-environment-accessibility-universal-design/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明建成环境无障碍、通用设计、路径连续、标识和公共空间可达如何影响主体持续性。
- 本域只做公开无障碍标准、环境可达、通用设计和公共空间治理资料整理。
- 不提供建筑设计施工、验收、个案法律、合理便利、撤离路线或辅助设备建议。

## 维护规则

- 新增材料必须区分建筑空间、公共空间、交通节点、服务入口、消防安全和辅助技术接口。
- 不把 ADA/ABA 标准或案例写成合规法律意见。
- 涉及改造或施工时，只写原则、标准来源和边界，不写工程操作步骤。
