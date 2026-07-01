# mask-respirator-source-control-fit-access-continuity 目录说明

`domains/c6-local-unlocking/mask-respirator-source-control-fit-access-continuity/` 是 Human Infra 的口罩、呼吸防护与源头控制连续性域，负责把暴发期间的呼吸防护建模为空气传播风险控制层。

## 目录结构

```text
mask-respirator-source-control-fit-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义口罩、呼吸器、源头控制、适配、可得、工作学校接口和风险沟通的对象、链路、非目标和来源信号。
- 本域只整理公开防护治理资料、变量模型和边界。
- 产品推荐、佩戴教程、fit testing、职业合规、假冒认证、防护规避和医疗建议不属于本域。

## 上下游关系

- 上游：`air-quality-ventilation-exposure-control/`、`occupational-exposure-industrial-hygiene/` 和 `immunization-public-health-surveillance/`。
- 下游：`school-workplace-outbreak-operations-continuity/`、`healthcare-surge-triage-capacity-continuity/` 和 `household-emergency-preparedness-resilience/`。

## 维护规则

- 新增资料必须说明它支持源头控制、呼吸防护可得、适配、场所策略还是风险沟通。
- 不能输出个人防护操作、产品购买、认证伪造、fit testing 指令或规避策略。
