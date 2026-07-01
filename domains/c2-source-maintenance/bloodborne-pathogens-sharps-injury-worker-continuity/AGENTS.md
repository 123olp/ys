# bloodborne-pathogens-sharps-injury-worker-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/bloodborne-pathogens-sharps-injury-worker-continuity` |
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


本目录承载血源性病原体、针刺/锐器伤和照护工作者暴露连续性资料，只做研究域建模，不输出暴露处置、检测、PEP、用药、报告表填写或个案医疗/法律建议。

## 结构

```text
bloodborne-pathogens-sharps-injury-worker-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 定义 bloodborne pathogens、needlestick/sharps injury、exposure control、reporting、follow-up、confidentiality 和 stigma。
- 新增资料必须区分工程控制、安全器械、培训、疫苗语境、暴露报告、职业健康随访和隐私边界。
- 不保存暴露记录、检测结果、疫苗状态、患者资料、雇主记录、工伤资料、事故证据或其他 PHI/PII。

## 上下游

- 上游：`sterilization-disinfection-infection-control/`、`occupational-exposure-industrial-hygiene/`、`health-workforce-capacity/`。
- 下游：`workers-compensation-occupational-injury-benefit-continuity/`、`infectious-disease-outbreak-response` family domains、`mental-health-affective-stability/`。

## 维护规则

- 资料优先回到 OSHA、CDC/NIOSH、CDC healthcare infection control、职业健康和公开安全研究。
- 个案暴露、检测、PEP、工伤、隐私、复工或法律问题必须转回职业健康、医疗机构感染控制、雇主安全计划、OSHA/州监管、工伤或法律渠道。
