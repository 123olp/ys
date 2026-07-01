# mechanical-ventilation-respiratory-failure-continuity 目录说明

本目录维护急性呼吸衰竭、机械通气、氧合/通气支持和恢复资料。它是主体氧供失败时的设备生命支持域。

## 目录结构

```text
mechanical-ventilation-respiratory-failure-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义机械通气如何改变缺氧、脑损伤、ICU 病程和长期恢复。
- 本目录只维护系统级资料和证据边界，不保存设备参数、血气、影像、SpO2、病历或家庭医疗设备数据。
- 资料进入本域时必须保留失败类型、支持类型、并发症、撤机/恢复指标和禁止用途。

## 上下游关系

- 上游来自 ATS、SCCM、NIH、CDC、呼吸治疗和 ICU 质量资料。
- 下游服务 `respiratory-oxygenation/`、`intensive-care-organ-support-delirium-continuity/` 和急性死亡风险建模。
- 不替代医生、呼吸治疗师、ICU、急诊、设备供应商或个人医疗建议。

## 维护规则

- 不写呼吸机参数、氧流量、气道管理、撤机或居家设备操作建议。
- 不把公开指南摘要写成个案治疗路径。
- 新增资料必须区分生理机制、设备支持、并发症和恢复结局。
