# prediabetes-diabetes-prevention-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/prediabetes-diabetes-prevention-continuity` |
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


本目录维护糖尿病前期筛查、2 型糖尿病预防和长期代谢风险转移资料。它是主体在糖尿病并发症和急性代谢危象之前的上游预防域。

## 目录结构

```text
prediabetes-diabetes-prevention-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义糖尿病前期筛查、预防项目、保留、行为支持和随访如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血糖、A1c、体重、饮食、活动、用药或病历资料。
- 资料进入本域时必须保留筛查对象、项目执行、可及性、保留率、长期结局和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC National DPP、NIDDK 和糖尿病预防资料。
- 下游服务 `nutrition-metabolic-health/`、`diabetes-insulin-glucose-monitoring-supplies-continuity/` 和急性代谢危象建模。
- 不替代医生、营养师、糖尿病教育者、项目教练或个体医疗建议。

## 维护规则

- 不写血糖/A1c 解读、饮食、运动、药物、补剂、减重、设备或个体预防建议。
- 不把系统级糖尿病预防研究写成个人干预计划。
- 新增变量必须区分筛查、转介、保留、行为支持、随访和并发症预防阶段。
