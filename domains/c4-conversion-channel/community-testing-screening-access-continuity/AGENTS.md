# community-testing-screening-access-continuity 目录说明

`domains/c4-conversion-channel/community-testing-screening-access-continuity/` 是 Human Infra 的社区检测与筛查可达连续性域，负责把检测入口、筛查项目和结果报告建模为暴发观测基础设施。

## 目录结构

```text
community-testing-screening-access-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义社区检测、筛查、居家检测、报告、转介、可达公平和不确定性的对象、链路、非目标和来源信号。
- 本域只整理公开检测系统资料和变量模型。
- 检测选择、采样操作、结果解释、诊断治疗、隔离建议和检测规避不属于本域。

## 上下游关系

- 上游：`public-health-laboratory-diagnostic-capacity/`、`immunization-public-health-surveillance/` 和 `clinical-laboratory-diagnostic-quality/`。
- 下游：`outbreak-case-investigation-contact-tracing-continuity/`、`isolation-quarantine-work-school-continuity/` 和 `school-workplace-outbreak-operations-continuity/`。

## 维护规则

- 新增资料必须说明它支持检测进入、筛查覆盖、报告接口、转介路径还是公平评估。
- 不能输出个体诊断、检测解释、采样教程、检测规避或报告操纵内容。
