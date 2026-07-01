# Childhood Immunization Schedule Record Continuity 目录说明

本目录承载儿童常规免疫排程接口、记录证明、提醒召回、学校托育记录、可及性和隐私边界资料。它处理公共卫生和记录连续性，不处理个体疫苗医学判断。

## 目录结构

```text
childhood-immunization-schedule-record-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- 记录 official schedule interface、immunization records、IIS、school/childcare proof、reminder/recall、missed-dose follow-up、consent 和 privacy boundary。
- 关注免疫信息如何在儿科、公共卫生、学校、托育和家庭之间保持连续。
- 不提供疫苗建议、排程解释、补种、禁忌、不良反应、豁免或个体医疗建议。

## 维护规则

- 新增资料优先引用 CDC、state immunization program、AAP、学校/托育官方资料和公共卫生资料。
- 疫苗信息高度易变，引用时必须指向官方当前资料，不在本仓库复制个体排程细节。
- 不把公共卫生资料转化为个人接种计划、豁免策略或风险判断。
