# caregiving-long-term-care 目录说明

`caregiving-long-term-care/` 是 Human Infra 的照护与长期照护域，负责研究主体失能、慢病、认知退行或生活支持需求出现后，照护网络是否能持续接住主体。

## 目录结构

```text
caregiving-long-term-care/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义照护与长期照护域的对象、先验位置、模型链路、非目标和来源信号。
- 本域只做照护系统、长期照护、照护者负担、照护连续性和尊严边界的资料整理。
- 个体护理计划、机构选择、保险福利、法律监护和医学处理不属于本域。

## 上下游关系

- 上游：`healthcare-access-continuity/`、`rehabilitation-functioning/`、`social-connection-relational-infra/`。
- 下游：`housing-built-environment-stability/`、`assistive-technology-access/`、`pain-suffering-control/` 和 `mental-health-affective-stability/`。

## 维护规则

- 新增资料必须标明它讨论的是照护需求、照护供给、照护者负担、长期照护质量还是照护转移。
- 禁止把照护资料改写成个体护理操作或机构选择建议。
