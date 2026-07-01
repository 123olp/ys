# emergency-alerts-communications 目录说明

本目录承载公共预警、应急通信、911/NG911、天气广播和第一响应通信如何进入主体持续性模型。

## 结构

```text
emergency-alerts-communications/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md` 是本域的边界、模型链路、非目标和来源入口。
- 本域只做非操作性资料整理和变量建模，不提供现场应急、调度、通信或警报发布指导。
- 后续资料必须区分官方系统说明、标准、统计、案例和传播性解释。

## 上下游关系

- 上游：`risk-engineering/`、`digital-inclusion-connectivity/`、`language-access-plain-communication/`。
- 下游：`emergency-preparedness-response/`、`disaster-recovery-relief-continuity/`、`personal-safety-violence-prevention/`。
- 相邻域：`public-service-design-accessibility/`、`transportation-access-mobility/`、`social-connection-relational-infra/`。

## 维护规则

- 不提供实时应急建议、路线、急救、无线电或警报发布操作。
- 不输出可用于伪造、干扰、冒充或滥用公共通信系统的信息。
- 若新增案例或指标，必须保留来源、时间、地区和适用边界。
