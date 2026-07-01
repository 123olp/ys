# ART Clinic Success Rate Quality Reporting Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/art-clinic-success-rate-quality-reporting-continuity` |
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


本目录承载 ART 诊所成功率、NASS、质量报告、数据校验、报告口径和解释边界资料。它处理可比较信息和观测治理，不处理诊所推荐或个人预后。

## 目录结构

```text
art-clinic-success-rate-quality-reporting-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料优先引用 CDC ART Success Rates、NASS、NASS validation、NASS data access 和公开数据字典。
- 记录 denominator、outcome definition、clinic reporting、patient mix、validation、privacy 和 lag。
- 不输出个体成功率、诊所排名、商业推荐、广告文案或保险/法律建议。

## 上下游

- 上游：`assisted-reproductive-technology-ivf-cycle-continuity/`、`data-governance/`、`outcome-measurement-quality-of-life/`。
- 下游：`trustworthy-scientific-communication-peer-review/`、`model-cards-ai-audit-evaluation/`、`uncertainty-quantification-model-calibration/`。
