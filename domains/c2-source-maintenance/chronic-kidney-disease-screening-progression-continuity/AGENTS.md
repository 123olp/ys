# chronic-kidney-disease-screening-progression-continuity 目录说明

本目录维护慢性肾病筛查、进展风险、心肾代谢交互、保护治疗可及和透析前准备资料。它是主体在急性肾衰、心衰和长期肾替代治疗之前的上游储备域。

## 目录结构

```text
chronic-kidney-disease-screening-progression-continuity/
├── AGENTS.md
└── README.md
```

## 职责边界

- `README.md`：定义 CKD 观测、分层、进展延缓、转诊和替代治疗准备如何影响主体持续性。
- 本目录只维护系统级变量、来源和边界，不保存个案实验室、尿检、血压、糖尿病、用药、影像或诊疗资料。
- 资料进入本域时必须保留观测指标、进展阶段、转诊边界、治疗负担和禁止用途。

## 上下游关系

- 上游来自 KDIGO、NIDDK、NKF 和 CKD 进展管理资料。
- 下游服务 `renal-hepatic-clearance/`、`acute-kidney-injury-renal-replacement-continuity/`、高血压和糖尿病风险建模。
- 不替代医生、肾脏科、药师、营养师、透析/移植团队或个体医疗建议。

## 维护规则

- 不写实验室解读、CKD 分期、饮食、补液、药物、透析、移植、检查排序或个体建议。
- 不把系统级 CKD 研究写成个人肾病管理工具。
- 新增变量必须区分筛查、分层、进展、保护治疗、转诊和替代治疗准备。
