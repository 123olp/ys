# prediabetes-diabetes-prevention-continuity 目录说明

本目录维护糖尿病前期筛查、2 型糖尿病预防和长期代谢风险转移资料。它是主体在糖尿病并发症和急性代谢危象之前的上游预防域。

## 目录结构

```text
prediabetes-diabetes-prevention-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义糖尿病前期筛查、预防项目、保留、行为支持和随访如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血糖、A1c、体重、饮食、活动、用药或病历资料。
- 资料进入本域时必须保留筛查对象、项目执行、可及性、保留率、长期结局和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC National DPP、NIDDK 和糖尿病预防资料。
- 下游服务 `nutrition-metabolic-health/`、`diabetes-insulin-glucose-monitoring-supplies-continuity/` 和急性代谢危象建模。
- 不替代医生、营养师、糖尿病教育者、项目教练或个体医疗建议。

## 维护规则

- 不写血糖/A1c 解读、饮食、运动、药物、补剂、减重、设备或个体预防建议。
- 不把系统级糖尿病预防研究写成个人干预计划。
- 新增变量必须区分筛查、转介、保留、行为支持、随访和并发症预防阶段。
