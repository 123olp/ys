# apprenticeship-work-based-learning-continuity

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/apprenticeship-work-based-learning-continuity` |
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


本目录承载学徒制与工作场景学习连续性资料。它研究主体如何在真实任务环境中通过导师、工时、技能标准和行业证书积累可迁移能力。

## 目录结构

```text
apprenticeship-work-based-learning-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 说明本域对象、Human Infra 价值、边界、上下游和初始资料线索。
- 后续资料应区分注册学徒制、在岗训练、相关课堂教学、导师制、工时记录、工资进阶和结业证明。
- 本域不保存个人学徒记录，不判断个体项目选择，也不提供申请、劳动争议、法律、移民或职业个案建议。

## 维护规则

- 引用资料优先来自 Apprenticeship.gov、劳工部门、学徒制标准、职业教育和劳工保护资料。
- 必须保留项目质量、劳动保护、工资进阶、反歧视、记录可携带和证书边界。
- 不把工作中学习写成廉价劳动合理化、规避劳动法或快速拿证路径。
