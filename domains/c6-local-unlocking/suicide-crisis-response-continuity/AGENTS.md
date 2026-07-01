# suicide-crisis-response-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/suicide-crisis-response-continuity` |
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


本目录维护自杀危机响应连续性域。它是 Human Infra 的“急性自毁风险不能清零未来选择权”层，负责危机入口、转介、随访和恢复支持如何影响主体持续性。

## 目录结构

```text
suicide-crisis-response-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明自杀预防、危机热线、移动危机响应、急诊衔接、随访和社区支持如何影响主体持续性。
- 本域只做公开危机响应系统、服务可达、连续照护和安全治理资料整理。
- 不提供危机个案处置、自伤/自杀方法、心理治疗、药物、家庭干预、安全计划或替代专业帮助的建议。

## 维护规则

- 新增材料必须区分长期心理健康、急性危机入口、移动响应、医疗衔接、随访和社区支持。
- 不写自伤或自杀方法、细节、工具、地点、规避发现或鼓励性内容。
- 涉及风险评估和监测时，只写系统边界和权利保护，不写自动化打分或个人判定。
