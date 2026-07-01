# genomic-stability-dna-repair 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/genomic-stability-dna-repair` |
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


`domains/c2-source-maintenance/genomic-stability-dna-repair/` 保存基因组稳定性与 DNA 修复研究域。它关注遗传信息完整性如何支撑长期细胞功能和癌症风险控制。

## 目录结构

```text
genomic-stability-dna-repair/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责 DNA 损伤、修复系统、突变负荷、复制压力和基因组不稳定的研究整理。
- 本域可整理机制综述、风险变量、证据层级和与癌症/衰老的关系。
- 本域不提供基因编辑、实验协议、检测解释、医疗诊断或治疗建议。

## 维护规则

- 任何主张必须区分机制证据、动物实验、人群证据和临床终点。
- 与癌症、细胞重编程、免疫和干细胞交叉时必须标注主拥有域。
- 新增文件或子目录时，同步更新本文件。
