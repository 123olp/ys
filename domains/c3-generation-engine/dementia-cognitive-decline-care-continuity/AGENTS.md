# dementia-cognitive-decline-care-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/dementia-cognitive-decline-care-continuity` |
| 所属层级 | `C3` - 可能性生成引擎层 |
| 父级容器 | `domains/c3-generation-engine` |
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


本目录维护痴呆、认知衰退与照护连续性域。它是 Human Infra 的“记忆判断逐步失稳时主体如何仍被保护”层，负责认知退行、照护支持、权利边界和可承受持续性。

## 目录结构

```text
dementia-cognitive-decline-care-continuity/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明痴呆、认知衰退、照护计划、照护者负担、安全风险、尊严和服务导航如何影响主体持续性。
- 本域只做公开认知衰退、照护连续性、照护者支持和服务系统资料整理。
- 不提供诊断、治疗、用药、法律财务、代理决策、监护、定位监控、约束或家庭个案建议。

## 维护规则

- 新增材料必须区分神经机制、认知功能、照护服务、照护者负担、权利保护和主体连续性。
- 不把认知衰退主体写成无权利对象、纯风险源或家庭负担。
- 涉及安全、定位、监控和约束时，只写伦理边界和公共框架，不写操作方案。
