# acute-coronary-syndrome-reperfusion-continuity 目录说明

本目录维护急性冠脉综合征、再灌注窗口和心肌损伤恢复资料。它是主体循环系统从急性缺血进入骤停、心衰或长期失能之前的时间关键域。

## 目录结构

```text
acute-coronary-syndrome-reperfusion-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 ACS 再灌注窗口如何影响死亡风险、心衰风险、行动能力和未来选择权。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、心电图、肌钙蛋白、用药、位置或急救资料。
- 资料进入本域时必须保留时间窗、系统层级、诊断链、恢复结局、证据强度和禁止用途。

## 上下游关系

- 上游来自 AHA/ACC、Professional Heart Daily、NHLBI 和胸痛/ACS 系统资料。
- 下游服务 `cardiovascular-resilience/`、`cardiac-arrest-cpr-defibrillation-continuity/` 和康复建模。
- 不替代医生、急诊、EMS、导管室、心内科、康复团队或个体医疗建议。

## 维护规则

- 不写胸痛处理、心电图判读、药物、PCI、溶栓、转运、医院选择或康复处方建议。
- 不把系统级再灌注研究写成个人分诊或治疗工具。
- 新增变量必须区分识别、诊断、转运、再灌注、并发症和恢复阶段。
