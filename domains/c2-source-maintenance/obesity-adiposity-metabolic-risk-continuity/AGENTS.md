# obesity-adiposity-metabolic-risk-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c2-source-maintenance/obesity-adiposity-metabolic-risk-continuity` |
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


本目录维护肥胖、脂肪分布、代谢风险、服务可及和抗污名边界资料。它是主体在多系统慢病、行动负担和社会参与受限之前的上游风险控制域。

## 目录结构

```text
obesity-adiposity-metabolic-risk-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义肥胖/脂肪代谢风险、结构性环境、服务可及、长期坚持和污名风险如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案体重、照片、饮食、活动、用药、病史或行为数据。
- 资料进入本域时必须保留结构性因素、服务边界、长期结局、污名风险和禁止用途。

## 上下游关系

- 上游来自 CDC、USPSTF、WHO 和肥胖/代谢风险资料。
- 下游服务 `nutrition-metabolic-health/`、`physical-activity-mobility/`、糖尿病预防和心血管风险建模。
- 不替代医生、营养师、心理服务、运动专业人员、减重服务或个体医疗建议。

## 维护规则

- 不写 BMI/体脂解读、饮食、运动、药物、手术、补剂、餐单、热量或个体减重建议。
- 不产出羞辱、道德化、审美化、体型歧视或商业营销内容。
- 新增变量必须区分环境、服务、行为支持、污名、长期维持和复发风险。
