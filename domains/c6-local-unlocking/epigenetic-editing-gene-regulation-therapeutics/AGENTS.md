# epigenetic-editing-gene-regulation-therapeutics 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c6-local-unlocking/epigenetic-editing-gene-regulation-therapeutics` |
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


本目录维护表观遗传编辑和可编程基因调控资料。它是表达状态改写域，不是细胞重编程或序列编辑的替代目录。

## 目录结构

```text
epigenetic-editing-gene-regulation-therapeutics/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义表观编辑、表达调控、持久沉默/激活和状态改写如何影响 Human Infra。
- 本目录不保存编辑器构建方案、靶点设计、递送操作、人体实验方案或规避监管材料。
- 资料必须区分概念验证、动物实验、临床前治疗平台、人体试验和获批疗法。

## 上下游关系

- 上游来自表观基因组学、基因调控、CRISPR 工具、递送平台和安全评估。
- 下游服务疾病通路控制、细胞状态维护、衰老机制研究和长期安全审查。
- 不替代 `cellular-reprogramming/`；本目录聚焦特定表达程序和表观标记调控。

## 维护规则

- 不把表观编辑写成通用逆龄、细胞年轻化或永生技术。
- 不提供可执行编辑、递送或人体实验操作步骤。
- 新增案例必须标注靶点、组织、证据阶段、可逆性、脱靶和长期安全未知项。
