# hypertension-detection-control-continuity 目录说明

本目录维护高血压检测、确认、长期控制和随访连续性资料。它是主体在卒中、心衰、肾衰和高血压危象之前的上游风险控制域。

## 目录结构

```text
hypertension-detection-control-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义高血压筛查、测量质量、确认、控制率和长期坚持如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血压、用药、病史、检查、设备或位置资料。
- 资料进入本域时必须保留筛查对象、测量条件、确认路径、随访责任、证据强度和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC、NHLBI 和高血压控制项目资料。
- 下游服务 `cardiovascular-resilience/`、`hypertensive-crisis-end-organ-risk-continuity/` 和肾脏风险建模。
- 不替代医生、护士、药师、急诊、远程监测服务或个体医疗建议。

## 维护规则

- 不写血压读数判断、降压药、剂量、家庭处理、设备选择、检查排序、急诊分诊或治疗建议。
- 不把系统级血压控制研究写成个人健康管理工具。
- 新增变量必须区分筛查、确认、控制、坚持、随访和靶器官预防阶段。
