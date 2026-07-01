# dental-pain-emergency-infection-continuity 目录说明

`domains/dental-pain-emergency-infection-continuity/` 保存牙痛、急性牙科事件和感染连续性研究域。

## 目录结构

```text
dental-pain-emergency-infection-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责牙痛、牙源性感染、急诊摩擦、睡眠缺勤和风险升级的资料整理。
- 本域可以描述系统级急诊使用、服务延迟和可预防口腔事件的持续性影响。
- 本域不提供分诊、用药、剂量、手术、排脓、拔牙、影像判读或个体急救建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`pain-suffering-control/`、`emergency-dispatch-911-triage-continuity/`。
- 下游：`dental-caries-prevention-restoration-continuity/`、`periodontal-disease-systemic-inflammation-continuity/`、`dental-care-access-insurance-workforce-continuity/`。

## 维护规则

- 急性事件资料必须区分公共教育、系统可及性和个体医疗建议。
- 不允许写出可能被用于自我处置感染或替代急诊评估的步骤。
- 新增文件或子目录时，同步更新本文件。
