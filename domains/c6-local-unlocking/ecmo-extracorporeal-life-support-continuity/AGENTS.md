# ecmo-extracorporeal-life-support-continuity 目录说明

本目录维护 ECMO/ECLS、体外生命支持和极端心肺衰竭桥接资料。它是短期保留主体未来选择权的高风险器官支持域。

## 目录结构

```text
ecmo-extracorporeal-life-support-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 ECMO 如何改变极端心肺衰竭中的存活窗口、并发症和退出条件。
- 本目录只维护来源、变量和安全边界，不保存个案参数、抗凝数据、病历、转运资料或费用资料。
- 资料进入本域时必须保留支持模式、中心能力、桥接目标、并发症、退出路径和禁止用途。

## 上下游关系

- 上游来自 ELSO、NIH、ICU、呼吸衰竭、循环支持和移植资料。
- 下游服务 `mechanical-ventilation-respiratory-failure-continuity/`、`intensive-care-organ-support-delirium-continuity/` 和高风险等待窗口建模。
- 不替代 ECMO 团队、ICU、心外/胸外/呼吸/麻醉团队、伦理委员会、转运中心或个人医疗建议。

## 维护规则

- 不写适应证、抗凝、泵机、转运、撤机、预后或中心选择建议。
- 不把 ECMO 描述成通用延寿或未来等待技术。
- 新增资料必须同时记录收益窗口和并发症/退出门槛。
