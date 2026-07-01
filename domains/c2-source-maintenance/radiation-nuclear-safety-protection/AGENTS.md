# radiation-nuclear-safety-protection 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/radiation-nuclear-safety-protection` |
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


本目录维护辐射、核安全与防护域。它是 Human Infra 的“不可见高能暴露治理层”，负责辐射与核风险的非操作性资料、标准和边界。

## 目录结构

```text
radiation-nuclear-safety-protection/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明辐射防护、核安全、监测、应急和长期污染治理如何支撑主体持续性。
- 本域只做公开标准、监管、监测和治理资料整理。
- 不提供放射源、核材料、设施、去污、防护、撤离、医疗影像或放疗个体建议。

## 维护规则

- 新增材料必须明确区分医疗、职业、环境、设施、事故和空间辐射场景。
- 任何可能变成操作指南的内容必须降级为风险分类、官方边界或禁止用途。
- 不写可执行核安全绕过、设施目标、放射源获取或应急现场操作。
