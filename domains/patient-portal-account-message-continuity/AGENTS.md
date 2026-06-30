# patient-portal-account-message-continuity

## 职责

本目录承载 patient portal、账号入口、secure messaging、通知路由、proxy access 和患者可见医疗任务资料。

## 边界

- 只研究医疗门户作为主体可见性和通信基础设施。
- 不代写医生消息、门户请求、投诉、授权或账号恢复材料。
- 不保存 portal 凭证、验证码、MRN、member ID、PHI、代理授权或联系方式。

## 结构

```text
patient-portal-account-message-continuity/
├── AGENTS.md
└── README.md
```

## 维护规则

- 新增资料必须区分 patient portal、patient-facing API、proxy access、secure messaging 和普通数字身份。
- 涉及个体病历、门户账号、医疗沟通或隐私争议的内容必须转回官方渠道和专业人员。
