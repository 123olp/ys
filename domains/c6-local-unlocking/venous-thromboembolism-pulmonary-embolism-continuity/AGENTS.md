# venous-thromboembolism-pulmonary-embolism-continuity 目录说明

本目录维护 DVT、肺栓塞、抗凝连续性和复发预防资料。它是血液凝固、循环、呼吸和移动能力交界处的急性风险域。

## 目录结构

```text
venous-thromboembolism-pulmonary-embolism-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 VTE/PE 如何改变急性死亡、氧合、右心负荷、复发和行动能力。
- 本目录只维护系统级变量、来源和边界，不保存个案影像、凝血结果、用药、癌症史、妊娠状态或住院资料。
- 资料进入本域时必须区分风险场景、诊断路径、抗凝连续性、出血权衡、复发和长期功能。

## 上下游关系

- 上游来自 ESC、CDC、NHLBI 和血栓/肺栓塞 public materials。
- 下游服务 `blood-oxygen-hemostasis/`、`respiratory-oxygenation/` 和 `transfusion-blood-management-hemorrhage-continuity/`。
- 不替代医生、急诊、血液科、心肺团队、产科或个体医疗建议。

## 维护规则

- 不写血栓诊断、影像解读、D-dimer、抗凝、溶栓、滤器、旅行、术后或妊娠建议。
- 不把系统级 VTE/PE 研究写成个人风险评分或治疗工具。
- 新增变量必须区分血栓形成、栓塞、氧合、右心、抗凝、出血和复发。
