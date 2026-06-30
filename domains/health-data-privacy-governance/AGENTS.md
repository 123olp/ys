# health-data-privacy-governance 目录说明

`domains/health-data-privacy-governance/` 是 Human Infra 的健康数据隐私治理域，负责把敏感健康、基因、行为、神经和服务使用数据的权利、安全和用途边界建模为主体持续性的信任条件。

## 目录结构

```text
health-data-privacy-governance/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义健康数据隐私治理的对象、链路、非目标和来源信号。
- 本域只做公开制度资料、治理变量、失败模式和伦理边界整理。
- 法律意见、合规认证、真实数据处理架构、去标识化保证、数据共享许可和安全攻击方法不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`digital-identity-security/` 和 `measurement-feedback/`。
- 下游：`patient-data-interoperability/`、`healthcare-access-continuity/`、`longevity-evidence/` 和 `synthetic-biology-biosecurity/`。

## 维护规则

- 新增资料必须说明它支持的是同意、撤回、隐私、安全、共享、受试者保护、基因数据治理还是信息阻断边界。
- 不能把治理资料写成法律结论、合规保证、数据处理建议或绕过隐私边界的方法。
