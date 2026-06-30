# functioning-quality-of-life-outcomes 目录说明

`domains/functioning-quality-of-life-outcomes/` 是 Human Infra 的功能、生活质量与患者报告结局域，负责把“人是否真的更好”转化为可审查的功能、症状、参与和生活质量变量。

## 目录结构

```text
functioning-quality-of-life-outcomes/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义功能状态、生活质量、症状负担、患者报告结局和主体中心结果的对象、链路、非目标和来源信号。
- 本域只做结局语言、变量模型、证据边界和价值判断终点整理。
- 个体分数解释、诊断、残障资格、保险待遇、临床评估和量表替代专业判断不属于本域。

## 上下游关系

- 上游：`measurement-feedback/`、`rehabilitation-functioning/` 和 `pain-suffering-control/`。
- 下游：`health-economics-value-assessment/`、`healthcare-access-continuity/`、`caregiving-long-term-care/` 和 `longevity-evidence/`。

## 维护规则

- 新增资料必须说明它支持的是功能、生活质量、症状、患者报告、参与还是主体体验变量。
- 不能把结局测量写成个体诊断、单一排名、福利资格判断或主体价值替代品。
