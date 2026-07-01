# geriatric-long-term-care-oral-health-continuity 目录说明

`domains/geriatric-long-term-care-oral-health-continuity/` 保存老年口腔健康与长期照护连续性研究域。

## 目录结构

```text
geriatric-long-term-care-oral-health-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 本域负责老年口腔功能、义齿、口干、疼痛、吞咽、营养和照护工作流的资料整理。
- 本域可以整理长期照护和家庭照护场景中的口腔健康持续性。
- 本域不提供护理医嘱、义齿调整、药物更改、产品、吞咽训练或个体照护建议。

## 上下游关系

- 上游：`oral-health-continuity/`、`long-term-care-nursing-home-home-care-continuity/`、`frailty-sarcopenia-reserve/`。
- 下游：`tooth-loss-prosthodontic-chewing-continuity/`、`xerostomia-salivary-function-oral-medication-continuity/`、`swallowing-dysphagia-aspiration-nutrition/`。

## 维护规则

- 老年口腔资料必须区分家庭照护、机构照护、医疗牙科协作和个体医疗决策。
- 涉及护理流程时只整理系统级连续性，不写执行性医嘱。
- 新增文件或子目录时，同步更新本文件。
