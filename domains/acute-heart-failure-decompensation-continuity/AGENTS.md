# acute-heart-failure-decompensation-continuity 目录说明

本目录维护急性心衰失代偿、肺水肿、低灌注、住院和出院交接资料。它是慢性心血管风险进入急性循环/呼吸/肾脏失衡的研究域。

## 目录结构

```text
acute-heart-failure-decompensation-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义急性心衰失代偿如何改变住院、再入院、呼吸支持、肾损伤和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案体重、血压、氧饱和度、化验、影像、药物或设备数据。
- 资料进入本域时必须区分急性稳定、住院过程、出院交接、再入院和长期功能恢复。

## 上下游关系

- 上游来自 AHA/ACC/HFSA、NHLBI、CDC 和心衰质量改进资料。
- 下游服务 `cardiovascular-resilience/`、`mechanical-ventilation-respiratory-failure-continuity/` 和 `acute-kidney-injury-renal-replacement-continuity/`。
- 不替代医生、急诊、心内科、住院团队、康复团队或个体医疗建议。

## 维护规则

- 不写药物调整、利尿策略、氧疗、饮食、急诊分诊、住院或出院建议。
- 不把系统级心衰研究写成个案监测、预警或治疗工具。
- 新增变量必须区分容量、灌注、肾心交互、呼吸状态、交接和恢复负担。
