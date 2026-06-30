# patient-data-interoperability 目录说明

`domains/patient-data-interoperability/` 是 Human Infra 的患者数据互操作域，负责把健康记录访问、数据可携带、互操作标准和授权共享建模为连续照护的资料条件。

## 目录结构

```text
patient-data-interoperability/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义患者数据访问、互操作、可携带、授权共享和数据连续性的对象、链路、非目标和来源信号。
- 本域只做公开标准、政策资料、变量建模、证据边界和数据断点分析。
- 个人病历解释、医学判断、保险权益判断、账号破解、授权绕过和隐私规避不属于本域。

## 上下游关系

- 上游：`digital-identity-security/`、`governance-rights/` 和 `health-literacy-navigation/`。
- 下游：`healthcare-access-continuity/`、`medicine-access-treatment-continuity/`、`caregiving-long-term-care/` 和 `measurement-feedback/`。

## 维护规则

- 新增资料必须说明它支持的是访问、互操作、数据可携带、授权、语义一致性、数据质量还是隐私治理变量。
- 不能把互操作资料写成个体数据权利结论、医疗解释或第三方应用背书。
