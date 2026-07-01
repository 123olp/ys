# chronic-liver-disease-masld-mash-continuity 目录说明

本目录维护 MASLD/MASH、慢性肝病、纤维化、肝硬化、肝癌风险和代谢共病资料。它关注隐匿肝病如何改变生命风险和有效时间。

## 目录结构

```text
chronic-liver-disease-masld-mash-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 MASLD/MASH 与慢性肝病如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、饮酒、体重、糖尿病、药物或保险资料。
- 资料进入本域时必须保留病程阶段、纤维化风险、代谢共病、肝癌风险、药物安全和禁止用途。

## 上下游关系

- 上游来自 NIDDK、CDC、肝病学、代谢健康和肿瘤预防资料。
- 下游服务 `renal-hepatic-clearance/`、`obesity-adiposity-metabolic-risk-continuity/` 和肝癌预防模型。
- 不替代肝病科、消化科、内分泌、营养、药学、肿瘤、保险或个体医疗建议。

## 维护规则

- 不写个人肝功能、影像、纤维化、饮酒、药物、减重、补充剂、筛查周期或治疗建议。
- 不把 MASLD/MASH 资料写成个人风险评分或监测计划。
- 新增资料必须区分脂肪变、炎症、纤维化、肝硬化、失代偿、肝癌风险和代谢共病。
