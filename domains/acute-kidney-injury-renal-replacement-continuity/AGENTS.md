# acute-kidney-injury-renal-replacement-continuity 目录说明

本目录维护急性肾损伤、肾脏替代治疗和内环境急性支持资料。它是代谢废物、容量、电解质和酸碱失控时的生命支持域。

## 目录结构

```text
acute-kidney-injury-renal-replacement-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 AKI 和肾脏替代治疗如何影响急性死亡、恢复能力和长期肾功能。
- 本目录只维护系统级资料和证据边界，不保存实验室、尿量、透析参数、病历、保险或设备日志。
- 资料进入本域时必须保留 AKI 阶段、支持方式、内环境变量、恢复结局和禁止用途。

## 上下游关系

- 上游来自 KDIGO、NKF、NIH、ICU、肾脏病和内环境稳态资料。
- 下游服务 `renal-hepatic-clearance/`、`fluid-electrolyte-acid-base-homeostasis/`、`intensive-care-organ-support-delirium-continuity/` 和恢复负担建模。
- 不替代肾脏科、ICU、透析中心、医生、营养师、保险计划或个人医疗建议。

## 维护规则

- 不写透析参数、适应证、饮食、补液、用药或实验室解读建议。
- 不把公开 AKI 资料写成个人肾病管理工具。
- 新增资料必须区分急性支持、长期清除功能和资源可达性。
