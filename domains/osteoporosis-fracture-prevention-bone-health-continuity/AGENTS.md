# osteoporosis-fracture-prevention-bone-health-continuity 目录说明

本目录维护骨质疏松筛查、骨折风险、治疗坚持和骨折后功能恢复资料。它是主体在跌倒后长期失能、机构化和有效时间损失之前的结构性风险控制域。

## 目录结构

```text
osteoporosis-fracture-prevention-bone-health-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义骨质疏松筛查、骨折风险、治疗坚持、跌倒接口和骨折后恢复如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案骨密度、影像、跌倒史、骨折史、用药、体重或诊疗资料。
- 资料进入本域时必须保留筛查对象、损害收益权衡、行动结局、康复接口和禁止用途。

## 上下游关系

- 上游来自 USPSTF、NIH/NIAMS、BHOF 和骨健康资料。
- 下游服务 `musculoskeletal-integrity/`、`fall-risk-prevention-home-safety-continuity/` 和康复功能建模。
- 不替代医生、骨科、内分泌科、康复团队、物理治疗或个体医疗建议。

## 维护规则

- 不写骨密度解读、补剂、药物、运动、跌倒训练、影像、骨折处理、手术或个体建议。
- 不把系统级骨健康研究写成个人骨折风险工具。
- 新增变量必须区分筛查、风险识别、治疗可及、坚持、跌倒接口和骨折后恢复。
