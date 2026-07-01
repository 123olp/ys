# iron-deficiency-anemia-oxygen-carrying-continuity 目录说明

本目录维护铁缺乏、贫血、氧输送、疲劳、病因追踪和恢复可及资料。它关注贫血如何改变体力、认知速度和有效时间。

## 目录结构

```text
iron-deficiency-anemia-oxygen-carrying-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义铁缺乏贫血如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案化验、月经、胃肠症状、妊娠、饮食、用药或保险资料。
- 资料进入本域时必须保留贫血类型、铁状态、来源路径、阶段性风险、治疗可及和禁止用途。

## 上下游关系

- 上游来自 NHLBI、NIH ODS、血液学、营养、妇科、胃肠和慢病资料。
- 下游服务 `blood-oxygen-hemostasis/`、`menstrual-health-cycle-literacy-continuity/` 和消化连续性模型。
- 不替代血液科、营养、妇科、胃肠科、产科、药学、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、化验判读、补铁剂量、输血、胃肠检查、月经处理、妊娠或饮食建议。
- 不把贫血资料写成补充剂计划或失血来源判断。
- 新增资料必须区分铁缺乏、其他贫血、氧输送、疲劳、来源追踪和功能结果。
