# ai-data-provenance-contamination-drift-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c3-generation-engine/ai-data-provenance-contamination-drift-continuity` |
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


本目录维护 AI 数据谱系、污染和漂移治理资料。它是 AI 模型可信性的数据地基层。

## 目录结构

```text
ai-data-provenance-contamination-drift-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AI 数据来源、污染、分布漂移和代表性如何影响主体持续性。
- 本目录只维护数据治理框架和边界，不保存私有数据集、受限全文、泄露数据或个人敏感数据。
- 资料进入本域时必须保留数据来源、版本、许可、污染检查、代表性和删除/退出约束。

## 上下游关系

- 上游来自 Datasheets for Datasets、NIST AI RMF、Data Provenance Initiative、OWASP LLM Top 10 和数据治理文献。
- 下游服务 `ai-evaluation-benchmark-validity-continuity/`、`synthetic-data-generation-validation-continuity/` 和模型发布审计。
- 不替代 `data-quality-missingness-representativeness/`；该域关注一般数据质量，本目录关注 AI 数据链路。

## 维护规则

- 不记录受限数据抓取、访问控制绕过、重新识别、数据造假或来源隐匿方法。
- 不把数据清洗写成事实净化。
- 若新增数据字段影响 Source Card 或模型卡契约，必须同步更新对应索引。
