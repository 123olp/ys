# measurement-feedback 目录说明

`domains/c4-conversion-channel/measurement-feedback/` 保存测量、预测与反馈研究域。它关注主体状态如何被观测、建模、反馈和纠偏。

## 目录结构

```text
measurement-feedback/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责生物标志物、状态测量、风险评分、可穿戴、多组学、预测模型和反馈闭环。
- 本域与 `docs/reference/life-path-prediction-model-contract.md` 对齐，但不替代模型治理文档。
- 本域不提供医学诊断、个体死亡日期、确定寿命预测或个体治疗建议。

## 维护规则

- 任何指标主张必须区分状态、风险、功能、替代终点和真实终点。
- 任何预测主张必须标注数据来源、适用人群、误差、偏差和禁止用途。
- 新增文件或子目录时，同步更新本文件。
