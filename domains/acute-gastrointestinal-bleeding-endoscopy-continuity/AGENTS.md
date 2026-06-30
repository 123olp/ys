# acute-gastrointestinal-bleeding-endoscopy-continuity 目录说明

本目录维护急性消化道出血、内镜可及、输血接口和复发预防资料。它是血液供应、消化道病变和急性休克风险交界的研究域。

## 目录结构

```text
acute-gastrointestinal-bleeding-endoscopy-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义急性 GI 出血如何改变血容量、贫血、休克、再出血和有效时间。
- 本目录只维护系统级变量、来源和边界，不保存个案症状、生命体征、血红蛋白、图片、用药、内镜或病历资料。
- 资料进入本域时必须区分识别、稳定、输血接口、内镜可及、抗凝背景和复发预防。

## 上下游关系

- 上游来自 ACG、NIDDK、AABB 和消化道出血 guideline/public materials。
- 下游服务 `transfusion-blood-management-hemorrhage-continuity/`、`blood-oxygen-hemostasis/` 和 `surgical-anesthesia-perioperative-safety/`。
- 不替代医生、急诊、消化科、内镜团队、输血医学或个体医疗建议。

## 维护规则

- 不写便血/呕血判断、停药、抗凝处理、输血、内镜、药物、饮食、急诊分诊或预后建议。
- 不把系统级出血服务链研究写成个人风险评分或治疗工具。
- 新增变量必须区分上消化道、下消化道、失血、休克、内镜、输血和再出血。
