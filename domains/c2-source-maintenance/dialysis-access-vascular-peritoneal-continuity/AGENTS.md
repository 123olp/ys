# dialysis-access-vascular-peritoneal-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/dialysis-access-vascular-peritoneal-continuity` |
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


`domains/c2-source-maintenance/dialysis-access-vascular-peritoneal-continuity/` 保存透析通路、血管通路和腹膜通路连续性研究资料。

## 职责

- 维护血管通路、腹膜通路、成熟失败、感染、血栓和治疗中断边界。
- 将通路作为肾脏替代治疗的核心接口写入主体持续性模型。
- 保留来源、证据等级、禁止用途和上下游关系。

## 非目标

- 不提供通路选择、穿刺、护理、抗凝、感染处理、手术、透析参数或个体医疗建议。
- 不处理个人透析记录、通路照片、血流量、实验室或保险资料。

## 上游

- `renal-hepatic-clearance/`
- `chronic-kidney-disease-screening-progression-continuity/`
- `acute-kidney-injury-renal-replacement-continuity/`

## 下游

- `home-dialysis-supply-self-management-continuity/`
- `pharmaceutical-quality-supply-integrity/`
- `healthcare-access-continuity/`
