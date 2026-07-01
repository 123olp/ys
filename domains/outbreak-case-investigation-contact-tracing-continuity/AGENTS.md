# outbreak-case-investigation-contact-tracing-continuity 目录说明

`domains/outbreak-case-investigation-contact-tracing-continuity/` 是 Human Infra 的暴发病例调查与接触追踪连续性域，负责把病例到接触者的执行链建模为传播阻断和服务转介基础设施。

## 目录结构

```text
outbreak-case-investigation-contact-tracing-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义病例调查、接触追踪、暴露通知、隐私保护和转介支持的对象、链路、非目标和来源信号。
- 本域只整理公开公共卫生资料、变量模型、风险边界和禁止用途。
- 个体诊断、接触者识别、定位追踪、隐私侵害、污名化和规避公共卫生措施不属于本域。

## 上下游关系

- 上游：`immunization-public-health-surveillance/`、`public-health-laboratory-diagnostic-capacity/` 和 `health-data-privacy-governance/`。
- 下游：`isolation-quarantine-work-school-continuity/`、`community-testing-screening-access-continuity/`、`school-workplace-outbreak-operations-continuity/` 和 `social-connection-relational-infra/`。

## 维护规则

- 新增资料必须说明它支持病例调查、接触者通知、转介服务、隐私保护还是信任治理。
- 不能把追踪资料写成个体名单、定位工具、惩罚机制、传播规避或诊断治疗建议。
