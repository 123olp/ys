# lipid-atherosclerosis-risk-management-continuity 目录说明

本目录维护血脂、动脉粥样硬化风险管理和 ASCVD 预防连续性资料。它是主体在心肌梗死、卒中和血管性失能之前的长期风险控制域。

## 目录结构

```text
lipid-atherosclerosis-risk-management-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义血脂检测、风险分层、预防性治疗证据、坚持和二级预防交接如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案血脂、家族史、用药、不良反应、影像或诊疗资料。
- 资料进入本域时必须保留风险模型边界、证据等级、可及性、坚持变量和禁止用途。

## 上下游关系

- 上游来自 USPSTF、CDC、NHLBI 和 ASCVD 风险管理资料。
- 下游服务 `cardiovascular-resilience/`、`acute-coronary-syndrome-reperfusion-continuity/` 和卒中风险建模。
- 不替代医生、药师、心内科、内分泌科或个体医疗建议。

## 维护规则

- 不写血脂解读、药物、剂量、补剂、饮食、运动、检查、风险计算或个体治疗建议。
- 不把系统级 ASCVD 预防研究写成个人用药或保险工具。
- 新增变量必须区分检测、风险分层、治疗可及、坚持、事件预防和二级预防阶段。
