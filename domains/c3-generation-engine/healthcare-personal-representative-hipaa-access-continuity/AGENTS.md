# healthcare-personal-representative-hipaa-access-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/healthcare-personal-representative-hipaa-access-continuity` |
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


本目录承载医疗个人代表、授权照护者和医疗信息访问连续性资料。它研究主体无法独自管理资料时，医疗信息如何在合法授权和隐私边界内跟随照护任务。

## 目录结构

```text
healthcare-personal-representative-hipaa-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分患者本人访问、personal representative、caregiver proxy access、机构披露和紧急例外。
- 本域不保存 PHI，不解释个案访问权，也不提供隐私投诉、表格填写或诉讼策略。

## 维护规则

- 引用资料优先来自 HHS OCR、ONC、CMS、医疗机构公开资料和隐私/互操作标准。
- 每条资料必须标注它支持的是访问权、隐私边界、代理角色还是机构义务。
- 不把“照护需要”写成越权访问或绕过同意的理由。
