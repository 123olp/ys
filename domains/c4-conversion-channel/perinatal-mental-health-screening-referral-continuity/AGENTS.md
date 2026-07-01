# Perinatal Mental Health Screening Referral Continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c4-conversion-channel/perinatal-mental-health-screening-referral-continuity` |
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


本目录承载围产期心理健康筛查、转介、危机入口、同伴支持、保险语言文化安全、IPV/物质使用接口和 warm handoff 资料。它处理筛查转介连续性，不处理个体心理诊断或危机处置。

## 目录结构

```text
perinatal-mental-health-screening-referral-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 perinatal depression/anxiety screening、referral pathway、crisis boundary、IPV/substance-use interface、peer support、language/cultural safety 和 follow-up closure。
- 关注围产期心理风险是否能被发现、转接、跟进，而不被年龄、保险、污名或照护负担切断。
- 不提供诊断、量表解释、用药、危机干预、自伤判断、家庭暴力处置、儿童安全判断或心理治疗建议。

## 维护规则

- 新增资料优先引用 ACOG、HRSA、SAMHSA、CDC、NIH/NICHD 或公开母婴心理健康资料。
- 涉及自伤、他伤、精神病、家庭暴力、儿童安全和物质使用时必须保留危机与专业边界。
- 不把筛查工具或热线资料转化为个体风险评分或治疗建议。
