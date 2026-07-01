# thyroid-disease-endocrine-function-continuity 目录说明

本目录维护甲状腺疾病、内分泌稳定、长期监测、症状归因和阶段性风险资料。它关注甲状腺轴如何影响能量、情绪、心血管、骨骼和认知速度。

## 目录结构

```text
thyroid-disease-endocrine-function-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义甲状腺疾病如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、影像、用药、妊娠、生育、心律或保险资料。
- 资料进入本域时必须保留疾病状态、监测边界、阶段性风险、过度诊疗风险和禁止用途。

## 上下游关系

- 上游来自 NIDDK、NCI、内分泌、肿瘤、产科和心血管资料。
- 下游服务 `endocrine-hormonal-regulation/`、`perimenopause-menopause-midlife-health-continuity/` 和心血管风险模型。
- 不替代内分泌科、产科、肿瘤、心血管、药学、保险或个体医疗建议。

## 维护规则

- 不写个人化验判读、结节分级、用药剂量、停药、补碘、妊娠、癌症筛查或治疗建议。
- 不把甲状腺资料写成症状自诊或用药调整流程。
- 新增资料必须区分功能异常、结构异常、监测、阶段风险、过度诊疗和功能结果。
