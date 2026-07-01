# pediatric-oral-health-development-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/pediatric-oral-health-development-continuity` |
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


`domains/c2-source-maintenance/pediatric-oral-health-development-continuity/` 保存儿童口腔健康与发育连续性研究域。

## 目录结构

```text
pediatric-oral-health-development-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责儿童龋病、牙痛、学校缺勤、家庭照护、营养和预防项目的资料整理。
- 本域可以描述儿童口腔健康如何影响能力形成、家庭时间和教育参与。
- 本域不提供儿童牙科诊断、发育判断、氟化物剂量、产品、镇静、治疗或急救建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`early-childhood-development-family-support-continuity/`、`school-attendance-education-continuity/`。
- 下游：`dental-caries-prevention-restoration-continuity/`、`dental-care-access-insurance-workforce-continuity/`。

## 维护规则

- 儿童口腔资料必须标注年龄范围、学校/家庭/社区场景和证据边界。
- 不允许写出替代儿牙评估或家长自行治疗的步骤。
- 新增文件或子目录时，同步更新本文件。
