# asthma-copd-exacerbation-airway-continuity 目录说明

本目录维护哮喘急性发作、COPD 急性加重和气道连续性资料。它是日常呼吸管理和机械通气之间的时间关键研究域。

## 目录结构

```text
asthma-copd-exacerbation-airway-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义气道急性加重如何改变缺氧、住院、呼吸支持、再入院和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、氧饱和度、肺功能、用药、设备或位置数据。
- 资料进入本域时必须区分触发物、药物可及、急诊接入、住院支持、呼吸支持和恢复交接。

## 上下游关系

- 上游来自 GINA、GOLD、NHLBI 和呼吸系统 public materials。
- 下游服务 `respiratory-oxygenation/`、`home-oxygen-respiratory-equipment-supply-continuity/` 和 `mechanical-ventilation-respiratory-failure-continuity/`。
- 不替代医生、急诊、呼吸科、药师、EMS 或个体医疗建议。

## 维护规则

- 不写吸入药、氧疗、雾化、激素、抗生素、峰流速、急诊分诊、设备设置或家庭处理建议。
- 不把系统级气道连续性研究写成个人哮喘/COPD action plan。
- 新增变量必须区分哮喘、COPD、触发物、药物可及、氧合、通气和康复。
