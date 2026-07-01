# diabetic-hyperglycemic-hypoglycemic-crisis-continuity 目录说明

本目录维护 DKA、HHS、严重低血糖和糖尿病急性代谢危象资料。它是葡萄糖、胰岛素、水、电解质和意识状态同时失控的研究域。

## 目录结构

```text
diabetic-hyperglycemic-hypoglycemic-crisis-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义糖尿病急性危象如何改变意识、肾功能、住院、复发和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案血糖、酮体、电解质、胰岛素、设备、饮食或位置数据。
- 资料进入本域时必须区分日常供应、急性危象、急诊接入、恢复教育和复发预防。

## 上下游关系

- 上游来自 ADA、NIDDK、CDC 和糖尿病危象 consensus materials。
- 下游服务 `diabetes-insulin-glucose-monitoring-supplies-continuity/`、`endocrine-hormonal-regulation/` 和 `acute-kidney-injury-renal-replacement-continuity/`。
- 不替代医生、急诊、内分泌科、糖尿病教育团队或个体医疗建议。

## 维护规则

- 不写血糖判断、胰岛素剂量、泵/CGM 设置、补液、电解质、饮食、运动或急救建议。
- 不把系统级代谢危象研究写成个人危象判断或家庭处理工具。
- 新增变量必须区分 DKA、HHS、低血糖、监测断裂、供应断裂和恢复交接。
