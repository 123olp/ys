# autoimmune-rheumatic-disease-inflammatory-burden-continuity 目录说明

本目录维护自身免疫风湿病、慢性炎症、免疫抑制、器官损害和照护连续性资料。它关注免疫系统失衡如何长期消耗行动能力和恢复能力。

## 目录结构

```text
autoimmune-rheumatic-disease-inflammatory-burden-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义自身免疫风湿病炎症负担如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、药物、感染、生育或保险资料。
- 资料进入本域时必须保留疾病类型、活动度、器官受累、药物风险、感染风险和禁止用途。

## 上下游关系

- 上游来自 NIAMS、CDC、风湿免疫、药物安全和慢病照护资料。
- 下游服务 `immune-maintenance/`、`multimorbidity-polypharmacy-care-coordination/` 和感染风险模型。
- 不替代风湿免疫科、药学、感染科、肾脏科、产科、残障、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、化验判读、免疫抑制用药、疫苗、妊娠、感染处理、检查周期或 flare 建议。
- 不把疾病活动证据写成个体治疗调整流程。
- 新增资料必须区分炎症负担、器官损害、治疗风险、感染风险、疲劳和功能结果。
