# anaphylaxis-allergic-emergency-continuity 目录说明

本目录维护过敏性休克、严重过敏、场所准备和急救转接资料。它是免疫反应突然关闭气道和循环的分钟级风险域。

## 目录结构

```text
anaphylaxis-allergic-emergency-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义过敏急症如何改变窒息、休克、死亡、活动边界和恢复连续性。
- 本目录只维护系统级变量、来源和边界，不保存个案过敏史、食物/药物、学校、工作地点、急救或医疗资料。
- 资料进入本域时必须区分触发物、识别、药物可及、场所计划、EMS 转接和过敏专科随访。

## 上下游关系

- 上游来自 WAO、NIAID、AAAAI 和公共卫生过敏资料。
- 下游服务 `immune-maintenance/`、`medical-id-allergy-critical-alert-continuity/` 和学校/工作场所连续性建模。
- 不替代医生、急诊、过敏专科、学校护士、雇主、EMS 或个体医疗建议。

## 维护规则

- 不写肾上腺素使用、剂量、急救步骤、过敏诊断、暴露挑战、脱敏或处方建议。
- 不把系统级过敏急症研究写成个人 action plan 或现场处理工具。
- 新增变量必须区分触发物、识别、药物可及、场所准备、转接和复发预防。
