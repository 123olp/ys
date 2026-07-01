# intensive-care-organ-support-delirium-continuity 目录说明

本目录维护 ICU 多器官支持、谵妄治理、恢复和 ICU 后综合征资料。它是危重病存活能否转化为有效主体持续性的研究域。

## 目录结构

```text
intensive-care-organ-support-delirium-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 ICU 支持、谵妄和恢复负担如何改变主体持续性。
- 本目录只维护系统级框架和证据边界，不保存 ICU 个案资料、设备参数、医嘱、家属记录或生命体征。
- 资料进入本域时必须保留 ICU 场景、器官支持类型、恢复结局、功能指标和禁止用途。

## 上下游关系

- 上游来自 SCCM、ICU Liberation、PADIS、危重病恢复和医院质量资料。
- 下游服务 `mechanical-ventilation-respiratory-failure-continuity/`、`ecmo-extracorporeal-life-support-continuity/`、`delirium-acute-cognitive-failure-prevention/` 和有效时间建模。
- 不替代 ICU 团队、医生、护士、呼吸治疗师、家属会议、伦理委员会或个人医疗建议。

## 维护规则

- 不写镇静、撤机、营养、感染控制、转院、预后或家属决策建议。
- 不把 ICU 质量改进资料写成个案治疗路径。
- 新增资料必须区分存活、认知恢复、身体恢复和家庭/社会恢复。
