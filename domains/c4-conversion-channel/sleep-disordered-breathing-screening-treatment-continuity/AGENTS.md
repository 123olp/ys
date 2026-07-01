# sleep-disordered-breathing-screening-treatment-continuity 目录说明

本目录维护睡眠呼吸障碍、夜间低氧、诊断转介、治疗坚持和设备连续性资料。它是主体恢复系统、警觉性和心血管风险之间的交叉域。

## 目录结构

```text
sleep-disordered-breathing-screening-treatment-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义睡眠呼吸障碍如何通过低氧、疲劳、事故和心血管负荷影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案睡眠报告、血氧、病史、设备或驾驶资料。
- 资料进入本域时必须保留对象、诊断路径、治疗可及、坚持、随访和禁止用途。

## 上下游关系

- 上游来自 NHLBI、USPSTF、CDC 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`respiratory-oxygenation/` 和心血管风险模型。
- 不替代睡眠医学、呼吸科、牙科、职业安全、驾驶安全或个体医疗建议。

## 维护规则

- 不写个人诊断、睡眠报告判读、CPAP 参数、设备选择、治疗方案、驾驶限制或保险建议。
- 不把筛查不确定性写成普遍筛查推荐。
- 新增资料必须区分症状识别、诊断、治疗、坚持、设备维护和安全暴露阶段。
