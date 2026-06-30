# Emergency Contact Next Of Kin Notification Continuity

Emergency Contact Next Of Kin Notification Continuity 研究 emergency contact、next of kin、照护者通知、身份确认和联系链如何在急救、灾害、住院、失能或死亡边界中维持主体与支持网络的连接。

> 核心问题：主体一旦无法表达，系统能否找到正确的人、以正确权限通知正确事实，决定医疗、照护、身份和后续恢复是否继续有人接住。

## 研究对象

- Emergency contact、next of kin、authorized contact、照护者、代理人和家庭通知链。
- 医院、EMS、学校、雇主、长期照护、灾害安置和公共机构中的联系人字段。
- 联系人信息更新、重复联系人、关系变化、隐私边界、误通知和通知失败。

## 先验链路

```text
主体在急救或失能场景中可能无法表达
  -> 医疗、灾害或机构系统需要外部联系人参与确认、照护、授权或后续安排
  -> 联系人记录若缺失、过期、错误或权限不清，支持网络无法及时进入
  -> 医疗信息、照护安排、身份确认、交通接回、财务和家庭责任产生断点
  -> 主体恢复、照护、尊严和未来选择权受到损害
  -> 因而紧急联系人与近亲通知链是主体持续性的急救社会接口
```

## 关键变量

- 联系人完整性、更新频率、关系类型、优先级和备用联系人。
- 通知触发条件、通知延迟、通知准确性、授权边界和记录一致性。
- 语言、听力、残障、跨境、无家可归、家庭暴力和隐私安全风险。

## 证据入口

- Ready.gov family emergency communication plan materials.
- MedlinePlus personal health records and emergency information materials.
- Hospital patient registration / emergency contact practices.
- Public safety, missing persons and next-of-kin notification policy materials.

## 非目标

- 本域不代写通知、寻找亲属、判断谁应被通知、处理家庭纠纷或提供法律建议。
- 不提供失踪寻人、执法协助、医院沟通、遗体认领、监护、继承或隐私投诉策略。
- 不收集真实姓名、电话、地址、病历号、定位、家庭关系、身份文件或其他敏感资料。

## 上下游

- 上游：`personal-health-record-emergency-summary-continuity/`、`digital-identity-security/`、`vital-records-life-event-continuity/`。
- 下游：`advance-care-planning-medical-decision-continuity/`、`healthcare-personal-representative-hipaa-access-continuity/`、`care-transitions-discharge-continuity/`。
