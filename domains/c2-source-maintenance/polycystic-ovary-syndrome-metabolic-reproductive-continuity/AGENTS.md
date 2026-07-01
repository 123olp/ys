# Polycystic Ovary Syndrome Metabolic Reproductive Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/polycystic-ovary-syndrome-metabolic-reproductive-continuity` |
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


本目录承载 PCOS 作为内分泌、代谢、生殖、心理负担和未来选择权交叉域的资料。它只做研究域建模，不处理个体诊断、治疗或生育建议。

## 目录结构

```text
polycystic-ovary-syndrome-metabolic-reproductive-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料优先引用 NIH/NICHD、MedlinePlus、CDC、专业学会指南和系统综述。
- 记录 cycle irregularity、hyperandrogenism、metabolic risk、fertility planning、stigma、mental health 和 evidence boundary。
- 不写个人 PCOS 判读、药物、激素、促排、饮食、减重、补剂、皮肤处理或生育治疗建议。

## 上下游

- 上游：`endocrine-hormonal-regulation/`、`reproductive-fertility-continuity/`、`menstrual-health-cycle-literacy-continuity/`。
- 下游：`nutrition-metabolic-health/`、`prediabetes-diabetes-prevention-continuity/`、`mental-health-affective-stability/`。
