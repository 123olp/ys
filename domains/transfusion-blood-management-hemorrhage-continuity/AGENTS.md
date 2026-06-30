# transfusion-blood-management-hemorrhage-continuity 目录说明

本目录维护输血、患者血液管理、大出血、凝血支持和血液安全资料。它是出血性死亡边界的急性修复域。

## 目录结构

```text
transfusion-blood-management-hemorrhage-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义血液可得、输血安全和大出血管理如何影响主体持续性。
- 本目录只维护系统级资料和证据边界，不保存血型、输血记录、化验、病历、献血者或供应合同。
- 资料进入本域时必须保留出血场景、产品类型、库存/匹配、安全结局和禁止用途。

## 上下游关系

- 上游来自 AABB、WHO、CDC、血库、创伤、手术和患者血液管理资料。
- 下游服务 `blood-organ-tissue-biovigilance-transplantation/`、`trauma-system-hemorrhage-control-continuity/` 和围手术期安全建模。
- 不替代医生、血库、输血医学、创伤/手术/产科团队、献血机构或个人医疗建议。

## 维护规则

- 不写输血阈值、血型匹配、凝血处理、止血药或个案输血建议。
- 不把血液供应资料写成采购、库存调度或医院协议。
- 新增资料必须区分血液系统供给、个体输血决策和安全监测。
