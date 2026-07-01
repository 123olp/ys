# obstetric-emergency-hemorrhage-hypertension-continuity 目录说明

<!-- domain-agent-contract:start -->
## 标准维护契约

| 字段 | 内容 |
| --- | --- |
| 物理路径 | `domains/c5-ecological-substrate/obstetric-emergency-hemorrhage-hypertension-continuity` |
| 所属层级 | `C5` - 可能性生态承载层 |
| 父级容器 | `domains/c5-ecological-substrate` |
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


本目录维护产科出血、妊娠/产后高血压急症、子痫和孕产妇严重并发症资料。它是妊娠、分娩和产后阶段的急性主体持续性研究域。

## 目录结构

```text
obstetric-emergency-hemorrhage-hypertension-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义产科急症如何改变孕产妇死亡、脑/肾损伤、家庭连续性和长期有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案妊娠状态、血压、出血量、胎儿信息、位置、家庭或法律资料。
- 资料进入本域时必须区分产前、分娩、产后、出血、高血压、转运、血液接口和 ICU 接口。

## 上下游关系

- 上游来自 ACOG、WHO、CDC 和孕产妇健康 public materials。
- 下游服务 `maternal-newborn-child-development/`、`transfusion-blood-management-hemorrhage-continuity/` 和 `hypertensive-crisis-end-organ-risk-continuity/`。
- 不替代医生、助产士、急诊、产科、ICU、公共卫生机构或个体医疗建议。

## 维护规则

- 不写症状判断、血压判断、出血判断、用药、分娩方式、医院选择、转运、产后恢复或母乳建议。
- 不把系统级产科急症研究写成个人 emergency plan 或临床决策工具。
- 新增变量必须区分出血、高血压/子痫、转运、团队能力、血液可得、产后随访和家庭连续性。
