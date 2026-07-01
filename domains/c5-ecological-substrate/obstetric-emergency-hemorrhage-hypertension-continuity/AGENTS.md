# obstetric-emergency-hemorrhage-hypertension-continuity 目录说明

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
