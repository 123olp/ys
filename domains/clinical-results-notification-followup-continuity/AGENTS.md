# clinical-results-notification-followup-continuity

## 职责

本目录承载临床结果通知、异常结果闭环、关键值升级、follow-up tracking 和诊断安全资料。

## 边界

- 只研究结果从系统产生到主体行动之间的通信和责任闭环。
- 不解释检查结果，不提供诊断、治疗、急救、加急或法律建议。
- 不保存结果数值、报告、影像、PHI、portal 凭证或联系方式。

## 结构

```text
clinical-results-notification-followup-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分实验室结果、影像报告、病理报告、筛查结果和诊断安全。
- 涉及个体结果解释或医疗行动的内容必须转回临床团队和官方入口。
