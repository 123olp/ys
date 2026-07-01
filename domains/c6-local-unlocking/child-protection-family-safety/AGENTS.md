# child-protection-family-safety 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/child-protection-family-safety` |
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


本目录维护儿童保护与家庭安全域。它是 Human Infra 的“未来主体能力形成不被虐待、忽视和家庭失稳截断”层，负责儿童保护、家庭支持和创伤知情服务如何影响主体持续性。

## 目录结构

```text
child-protection-family-safety/
├── AGENTS.md  # 本目录职责和维护规则
└── README.md  # 域定义、对象、边界和资料线索
```

## 职责边界

- `README.md` 说明儿童虐待、忽视、ACEs、儿童福利、家庭支持和创伤知情服务如何影响主体持续性。
- 本域只做公开儿童保护、儿童福利、预防、家庭支持和服务系统资料整理。
- 不提供个案报告、法律、监护、调查、取证、家庭冲突、儿童监控、规避报告或任何危害儿童的内容。

## 维护规则

- 新增材料必须区分儿童发展、家庭支持、虐待忽视预防、报告系统、儿童福利和制度伤害风险。
- 不写可用于伤害、诱导、定位、控制、剥削儿童或规避保护系统的信息。
- 涉及报告和调查时，只写公共框架、权利边界和证据来源，不写个案策略。
