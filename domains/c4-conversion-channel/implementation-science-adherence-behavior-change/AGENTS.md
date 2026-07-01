# Implementation Science Adherence Behavior Change 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/implementation-science-adherence-behavior-change` |
| 所属层级 | `C4` - 可能性转换通道层 |
| 父级容器 | `domains/c4-conversion-channel` |
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


## 目录结构

```text
implementation-science-adherence-behavior-change/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义实施科学、依从性、行为改变、采用维护和现实效果边界。
- `AGENTS.md`：说明本目录的职责边界和维护规则。

## 边界

本目录只承载干预落地、行为摩擦和实施质量的研究语言。它不承载个人行为处方、心理治疗、临床依从性建议、组织监控系统或操控性行为设计。

## 维护规则

- 新增干预评估必须区分 efficacy、effectiveness、implementation 和 maintenance。
- 不允许把“技术存在”直接等同于“主体收益”。
- 所有行为改变内容必须保留自主性、退出权、资源约束和环境约束。
- 涉及组织场景时必须避免把 Human Infra 变成效率压榨工具。
