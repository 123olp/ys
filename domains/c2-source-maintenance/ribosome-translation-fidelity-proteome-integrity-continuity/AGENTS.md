# ribosome-translation-fidelity-proteome-integrity-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/ribosome-translation-fidelity-proteome-integrity-continuity` |
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


`domains/c2-source-maintenance/ribosome-translation-fidelity-proteome-integrity-continuity/` 保存核糖体、翻译控制和蛋白生成质量研究域。

## 目录结构

```text
ribosome-translation-fidelity-proteome-integrity-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责 ribosome、translation fidelity、protein synthesis、translation quality control 和 protein production error 的资料组织。
- 本域可整理神经退行、发育、生殖、再生、蛋白稳态和细胞衰老交叉资料。
- 本域不提供 mTOR/ISR 调节、药物、补剂、营养、检测解释、实验操作或临床建议。

## 维护规则

- 所有主张必须区分翻译速率、翻译保真度、错误蛋白生成、蛋白稳态压力和功能终点。
- 与 `proteostasis-autophagy/`、`ubiquitin-proteasome-protein-turnover-continuity/` 和 `rna-splicing-epitranscriptomic-maintenance-continuity/` 交叉时标注主机制。
- 新增文件或子目录时同步更新本文件。
