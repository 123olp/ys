# industrial-process-safety-management-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/industrial-process-safety-management-continuity` |
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


`domains/c6-local-unlocking/industrial-process-safety-management-continuity/` 是 Human Infra 的工业过程安全管理连续性域，负责把重大事故预防、维护、变更管理和组织学习建模为工人社区持续性基础设施。

## 目录结构

```text
industrial-process-safety-management-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 PSM、RMP、机械完整性、变更管理、事故学习和社区接口。
- 本域只整理公开制度、组织变量、事故预防框架和禁止用途。
- 工艺参数、设备操作、联锁绕过、企业合规、事故责任和监管规避不属于本域。

## 上下游关系

- 上游：`manufacturing-repair-capacity/`、`occupational-exposure-industrial-hygiene/`、`chemical-safety-poison-control-toxicology/`。
- 下游：`chemical-release-shelter-evacuation-continuity/`、`community-right-to-know-chemical-risk-disclosure-continuity/`、`risk-engineering/`。

## 维护规则

- 新增资料必须说明它支持预防、维护、变更、组织学习、工人安全还是社区风险边界。
- 不得写入危险工艺操作、事故制造、规避监管、法律结论或企业具体合规建议。
