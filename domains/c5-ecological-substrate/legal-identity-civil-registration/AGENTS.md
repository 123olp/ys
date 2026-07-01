# legal-identity-civil-registration 目录说明

`legal-identity-civil-registration/` 是 Human Infra 的法律身份与民事登记域，负责研究主体如何被制度承认为权利和服务对象。

## 目录结构

```text
legal-identity-civil-registration/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义法律身份与民事登记域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做法律身份、出生登记、民事登记、生命统计、身份覆盖和服务入口的资料整理。
- 个体法律、移民、身份申请、证件办理、资格判断、欺诈或规避方法不属于本域。

## 上下游关系

- 上游：`governance-rights/`、`resource-social-infra/` 和 `digital-identity-security/`。
- 下游：`healthcare-access-continuity/`、`financial-resilience-access/`、`emergency-preparedness-response/` 和公共服务接入。

## 维护规则

- 新增资料必须区分法律身份、民事登记、生命统计、数字身份和服务资格。
- 禁止输出证件办理、法律规避、身份欺诈或个体资格建议。
