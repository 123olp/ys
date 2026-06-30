# hypertensive-crisis-end-organ-risk-continuity 目录说明

本目录维护高血压危象和急性靶器官风险资料。它是血管压力负荷进入脑、心、肾和主动脉急性损伤的研究域。

## 目录结构

```text
hypertensive-crisis-end-organ-risk-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义高血压危象如何改变卒中、心衰、AKI、主动脉事件和长期有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案血压、症状、化验、影像、药物或位置数据。
- 资料进入本域时必须区分测量、识别、靶器官评估、急性稳定和长期交接。

## 上下游关系

- 上游来自 AHA、CDC、NHLBI 和高血压 guideline materials。
- 下游服务 `cardiovascular-resilience/`、`cerebrovascular-stroke-brain-perfusion-resilience/` 和 `acute-kidney-injury-renal-replacement-continuity/`。
- 不替代医生、急诊、心内科、肾内科、神经科或个体医疗建议。

## 维护规则

- 不写血压读数判断、降压药、剂量、家庭处理、急诊分诊、检查选择或预后建议。
- 不把系统级靶器官风险研究写成个人高血压危象判断工具。
- 新增变量必须区分慢性控制、急性危象、靶器官损伤和随访连续性。
