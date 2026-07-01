# dental-care-access-insurance-workforce-continuity 目录说明

`domains/dental-care-access-insurance-workforce-continuity/` 保存牙科服务可及性、保险支付和劳动力连续性研究域。

## 目录结构

```text
dental-care-access-insurance-workforce-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责牙科保险、费用、劳动力、地理分布、预约等待、语言可及性和转诊入口的资料整理。
- 本域可以比较不同服务结构如何影响龋病、牙痛、缺牙和预防连续性。
- 本域不提供个体保险资格、理赔、费用、牙医推荐、预约选择、项目申请或法律建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`health-literacy-navigation/`、`insurance-coverage-continuity/`。
- 下游：`dental-caries-prevention-restoration-continuity/`、`dental-pain-emergency-infection-continuity/`、`pediatric-oral-health-development-continuity/`。

## 维护规则

- 服务可及性资料必须区分政策、覆盖、劳动力、地理、语言和支付摩擦。
- 不允许写出个体资格判断、理赔路径承诺或服务推荐。
- 新增文件或子目录时，同步更新本文件。
