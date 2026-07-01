# restless-legs-periodic-limb-movement-sleep-continuity 目录说明

本目录维护不宁腿综合征、周期性肢体运动、睡眠碎片和感觉-运动睡眠负担资料。它关注夜间不适和移动冲动如何损害恢复系统。

## 目录结构

```text
restless-legs-periodic-limb-movement-sleep-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 RLS / 周期性肢体运动如何通过睡眠碎片、日间损耗和家庭睡眠负担影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、睡眠、实验室、用药、伴侣或医疗资料。
- 资料进入本域时必须保留症状对象、共病语境、恢复影响、支持接口和禁止用途。

## 上下游关系

- 上游来自 MedlinePlus 和睡眠医学资料。
- 下游服务 `sleep-circadian-recovery/`、`peripheral-neuropathy-somatosensory-continuity/` 和家庭恢复模型。
- 不替代睡眠医学、神经科、药学、肾病/妊娠照护、精神健康、保险或个体医疗建议。

## 维护规则

- 不写个人诊断、铁指标解释、药物/补铁、剂量、停药、睡眠检查、设备或伴侣建议。
- 不把症状描述写成治疗流程。
- 新增资料必须区分感觉冲动、周期性运动、睡眠碎片、日间损害和共病/药物语境。
