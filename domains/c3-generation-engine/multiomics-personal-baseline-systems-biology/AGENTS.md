# multiomics-personal-baseline-systems-biology 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/multiomics-personal-baseline-systems-biology` |
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


`domains/c3-generation-engine/multiomics-personal-baseline-systems-biology/` 保存多组学、个人基线和系统生物学状态建模资料。

## 目录结构

```text
multiomics-personal-baseline-systems-biology/
├── AGENTS.md
└── README.md
```

## 文件职责

- `README.md`：定义多组学个人基线在 Human Infra 生命路径建模中的数据底座位置。
- `AGENTS.md`：记录本目录职责、允许新增材料类型和安全边界。

## 职责边界

- 本域关注多层生物状态建模，不解释个体检测结果。
- 可以整理公开平台、队列、方法论文、数据质量问题和模型变量。
- 不保存个人可识别数据、原始基因组文件、医学诊断或个体风险承诺。

## 维护规则

- 新增资料必须标明数据层级、样本类型、代表性、隐私风险和可解释性边界。
- 任何因果表述必须区分相关、预测和可干预证据。
- 新增文件或子目录时同步更新本文件。
